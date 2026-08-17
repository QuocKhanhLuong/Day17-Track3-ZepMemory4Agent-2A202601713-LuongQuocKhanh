# Lab 17 Benchmark Report

- Implementation: `no_memory`
- Kind: `practice`
- Cases: **11**
- Passed: **2/11**
- Evidence hit rate: **18.2%**
- Average retrieval latency: **0.0 ms**
- Average token reduction vs full source context: **81.8%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | FAIL | 0.0 | 0 | 100.0% | missing=Idempotency-Key, max-3-retries, exponential-backoff |
| E09 | long_term | FAIL | 0.0 | 0 | 100.0% | missing=LOTUS-88, Java, Spring Boot |
| E10 | short_term | PASS | 0.2 | 195 | 0.0% |  |
| E02 | long_term | FAIL | 0.0 | 0 | 100.0% | missing=Python |
| E03 | long_term | FAIL | 0.0 | 0 | 100.0% | missing=benchmark report, 16:00 |
| E04 | episodic | FAIL | 0.0 | 0 | 100.0% | missing=ClientSession, concurrency=20, ASYNC-FIX-20 |
| E05 | episodic | FAIL | 0.0 | 0 | 100.0% | missing=connection churn, timeout threshold |
| E07 | mixed | FAIL | 0.0 | 0 | 100.0% | missing=Python, Idempotency-Key |
| E11 | semantic | FAIL | 0.0 | 0 | 100.0% | missing=connection pooling, CONN-POOL-FIRST |
| E08 | long_term | FAIL | 0.0 | 0 | 100.0% | missing=BLUEBIRD-42, TypeScript, NestJS |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

``

### E09 - long_term

``

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

``

### E03 - long_term

``

### E04 - episodic

``

### E05 - episodic

``

### E07 - mixed

``

### E11 - semantic

``

### E08 - long_term

``
