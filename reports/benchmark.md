# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **810.6 ms**
- Average token reduction vs full source context: **14.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 434.3 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1354.0 | 755 | 0.0% |  |
| E10 | short_term | PASS | 0.5 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1392.4 | 1599 | 0.0% |  |
| E03 | long_term | PASS | 1431.5 | 1630 | 0.0% |  |
| E04 | episodic | PASS | 286.5 | 263 | 0.0% |  |
| E05 | episodic | PASS | 259.5 | 282 | 0.0% |  |
| E07 | mixed | PASS | 1642.6 | 485 | 14.2% |  |
| E11 | semantic | PASS | 260.5 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1854.9 | 1589 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> The user is working on the LOTUS-88 project, prioritizing Java and Spring Boot for backend examples.  The user prioritizes Java and Spring Boot and explicitly avoids using Python for backend development. Their project is LOTUS-88. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du `

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user is studying async/await and coroutines and is working on a personal project named ORCHID-27. They need to complete a benchmark report by Friday at 16:00. They are debugging async HTTP and encountered an issue related to connection churn, identified as the root cause of ASYNC-FIX-20. Increasing the timeout to 60 seconds was not effective. The user is investigating the connection pool, client lifecycle, and concurrency. A ClientSession with a concurrency of 20 was identified as a solution for connection churn. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  The user prefers Python for personal demos like ORCHID-27, but for `

### E03 - long_term

`<USER_SUMMARY> The user is studying async/await and coroutines and is working on a personal project named ORCHID-27. They need to complete a benchmark report by Friday at 16:00. They are debugging async HTTP and encountered an issue related to connection churn, identified as the root cause of ASYNC-FIX-20. Increasing the timeout to 60 seconds was not effective. The user is investigating the connection pool, client lifecycle, and concurrency. A ClientSession with a concurrency of 20 was identified as a solution for connection churn. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  The user prefers Python for personal demos like ORCHID-27, but for `

### E04 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + con`

### E05 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: `

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is studying async/await and coroutines and is working on a personal project named ORCHID-27. They need to complete a benchmark report by Friday at 16:00. They are debugging async HTTP and encountered an issue related to connection churn, identified as the root cause of ASYNC-FIX-20. Increasing the timeout to 60 seconds was not effective. The user is investigating the connection pool, client lifecycle, and concurrency. A ClientSession with a concurrency of 20 was identified as a solution for connection churn. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  The user prefers Python for personal demos like ORCHID-`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> The user is studying async/await and coroutines and is working on a personal project named ORCHID-27. They need to complete a benchmark report by Friday at 16:00. They are debugging async HTTP and encountered an issue related to connection churn, identified as the root cause of ASYNC-FIX-20. Increasing the timeout to 60 seconds was not effective. The user is investigating the connection pool, client lifecycle, and concurrency. A ClientSession with a concurrency of 20 was identified as a solution for connection churn. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  The user prefers Python for personal demos like ORCHID-27, but for `
