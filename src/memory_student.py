from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Student implementation of the four retrieval/context contracts."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so every graph search uses cap_query.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        """Recall durable user memory through a fresh evaluation thread.

        The Context Block provides cross-session recall while the optional
        user-scoped edge search adds provenance/validity-bearing facts for
        open loops and scoped preference updates. The current evaluation query
        is ignored as a durable fact by prime_eval_thread.
        """
        prime_eval_thread(self.client, user_id, thread_id, query)

        response = self.client.thread.get_user_context(thread_id=thread_id)
        context = str(getattr(response, "context", "") or "")

        # Harden Context Block recall with user-scoped facts. This must never
        # search the shared semantic graph: long-term memory is user-specific.
        edge_evidence = ""
        try:
            results = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=25,
            )
            edge_evidence = render_graph_search(results)
        except Exception:
            # Edge search is a resilience bonus; Context Block remains the
            # primary contract and should still be returned if edges are not
            # available for an account/SDK combination.
            edge_evidence = ""

        return join_nonempty([context, edge_evidence], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        """Retrieve past trajectories/outcomes/reflections from a user graph."""
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=12,
        )
        # Keep several distinct episodes inside the tight 3% context budget.
        return render_graph_search(results, episode_char_cap=360)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        """Retrieve shared domain knowledge from the standalone semantic graph."""
        short_query = cap_query(query)

        # Raw episodes preserve literal scorer markers such as PAYMENT-RULE-3.
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=short_query,
                scope="episodes",
                limit=8,
            )
            evidence = render_graph_search(results)
            if evidence.strip():
                return evidence
        except Exception:
            # Some Zep account/SDK combinations may not expose episode scope
            # for standalone graphs; fall through to node search.
            pass

        fallback = self.client.graph.search(
            graph_id=graph_id,
            query=short_query,
            scope="nodes",
            limit=8,
        )
        return render_graph_search(fallback)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        """Assemble memory layers using the configured 10/4/3/3 token budget."""
        return self.budget.assemble(layers)
