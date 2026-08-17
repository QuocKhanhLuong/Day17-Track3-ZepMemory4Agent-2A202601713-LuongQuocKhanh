# Lab 17 Submission Reflection

## Benchmark analysis

The student implementation passed **11/11 practice cases** with **100% memory hit rate**, **810.6 ms average latency**, and **14.19% average token reduction** versus full source context. No memory layer had a lower hit rate in the final run: short-term, long-term, episodic, semantic, and mixed retrieval all passed their assigned cases.

**E03** retrieved the most context at **1,630 tokens**. E07 required combining **long-term** and **semantic** memory: the merged context had to preserve the personal preference **Python** and shared knowledge marker **Idempotency-Key**. Under the 10/4/3/3 budget, E07 used 324 long-term tokens after trimming and 148 semantic tokens, while short-term and episodic were unused.

The average token reduction was **14.19%**. A no-memory baseline can show very high reduction simply because it retrieves almost nothing; that is not useful if required evidence is missing. Therefore reduction must be interpreted together with evidence hit rate.

## Reflection

For this benchmark, I consider **long-term memory** the most important layer because it covers cross-session preference, open loops, recency, and user isolation across E02, E03, E08, and E09. E08 is the key recency example: the newer project-specific constraint for **BLUEBIRD-42** (TypeScript + NestJS) must override Minh's general Python preference only within that project scope.

Zep Context Block provides managed cross-session memory and graph-backed retrieval with less custom orchestration. A Redis + Qdrant design gives more control over persistence, indexing, ranking, and deployment, but requires more application logic for schema, retrieval, consolidation, and lifecycle management.

To reduce memory poisoning and unauthorized background writes, durable writes should require explicit consent, policy/type allowlists, provenance, and scope validation; background processes must not grant themselves broader write permissions.

E10 shows why compaction must preserve durable constraints: **REVIEW-DEADLINE-1600**, Friday, 16:00 survives even when older raw turns are evicted. A pure buffer is not sustainable because token usage grows with conversation length.
