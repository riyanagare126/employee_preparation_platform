"""
AI Employee Preparation Platform - Master Interview Question Bank
Comprehensive Placement & Corporate Interview Questions categorized by difficulty:
- Levels: Easy (Low / Junior / Fundamentals), Medium (Mid-Level / Practical), Hard (High / Senior / Architecture)
- Topics: System Design, Database Indexing, Microservices, Security/Auth, Cloud/DevOps, Java, Python, Frontend, STAR Behavioral, Incident Management.
- Tailored for modern tech roles: Software Engineer, Full Stack, Backend, Frontend, Cloud/DevOps.
"""

MASTER_INTERVIEW_BANK = [
    # =========================================================================
    # 1. FOUNDATIONAL CORE TECHNICAL & OOP CONCEPTS (LOW / EASY DIFFICULTY)
    # =========================================================================
    {
        "id": "tech_found_001",
        "category": "Core Fundamentals",
        "difficulty": "Easy",
        "demand_tag": "⭐ Foundation",
        "question": "Explain the four fundamental pillars of Object-Oriented Programming (OOP) — Encapsulation, Abstraction, Inheritance, and Polymorphism — with real-world software examples.",
        "guidance": "Explain data hiding with private fields and getters/setters (Encapsulation), abstract classes/interfaces (Abstraction), code reuse through base classes (Inheritance), and method overriding/overloading (Polymorphism).",
        "roles": ["all", "software engineer", "backend", "full stack", "java", "python"]
    },
    {
        "id": "tech_found_002",
        "category": "Core Fundamentals",
        "difficulty": "Easy",
        "demand_tag": "⭐ Foundation",
        "question": "What is a RESTful API? Explain the standard HTTP methods (GET, POST, PUT, DELETE, PATCH) and key HTTP response status code families (2xx, 4xx, 5xx).",
        "guidance": "Explain stateless client-server communication, idempotent vs non-idempotent operations, GET/PUT/DELETE idempotency, and common status codes like 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, and 500 Internal Server Error.",
        "roles": ["all", "software engineer", "backend", "full stack", "frontend"]
    },
    {
        "id": "tech_found_003",
        "category": "Core Fundamentals",
        "difficulty": "Easy",
        "demand_tag": "⭐ Foundation",
        "question": "In Relational Databases (RDBMS), what are Primary Keys, Foreign Keys, and Unique Constraints? How do they ensure data integrity across relational tables?",
        "guidance": "Define unique record identification (Primary Key), relational linking and referential integrity (Foreign Key / ON DELETE CASCADE), and preventing duplicate column values (Unique Constraint).",
        "roles": ["all", "software engineer", "backend", "full stack", "data"]
    },
    {
        "id": "tech_found_004",
        "category": "Core Fundamentals",
        "difficulty": "Easy",
        "demand_tag": "⭐ Foundation",
        "question": "Explain Git version control workflow: What is the difference between Git Merge and Git Rebase? How do you resolve a merge conflict in a team setting?",
        "guidance": "Explain 3-way merge commit preserving true history vs linear history created by rebase, using `git status` and `git diff` during conflict resolution, and never rebasing shared public branches.",
        "roles": ["all", "software engineer", "frontend", "backend", "full stack"]
    },
    {
        "id": "sec_203",
        "category": "Security & APIs",
        "difficulty": "Easy",
        "demand_tag": "🔥 High Demand",
        "question": "What are SQL Injection and Cross-Site Scripting (XSS)? How do modern frameworks prevent these vulnerabilities automatically, and what manual precautions must developers take?",
        "guidance": "Discuss parameterized queries and prepared statements (ORM safeguards), input sanitization, output encoding, Content Security Policy (CSP) headers, and avoiding raw HTML rendering.",
        "roles": ["all", "software engineer", "full stack", "backend", "frontend"]
    },
    {
        "id": "tech_py_502",
        "category": "Technical (Python)",
        "difficulty": "Easy",
        "demand_tag": "🔥 High Demand",
        "question": "What are Python Generators and the 'yield' keyword? How do they enable streaming processing of massive gigabyte-scale datasets with minimal RAM consumption?",
        "guidance": "Discuss state persistence inside generator frames, iterator protocol (`__iter__`, `__next__`), lazy evaluation, and generator pipelines vs in-memory list allocations.",
        "roles": ["python", "software engineer", "data", "ai"]
    },
    {
        "id": "tech_fe_603",
        "category": "Technical (Frontend)",
        "difficulty": "Easy",
        "demand_tag": "🔥 High Demand",
        "question": "How do you optimize Core Web Vitals (Largest Contentful Paint - LCP, Interaction to Next Paint - INP, Cumulative Layout Shift - CLS) in a modern web application?",
        "guidance": "Discuss preloading hero images/fonts, code-splitting with dynamic imports, minimizing main thread blocking scripts, specifying explicit image width/height dimensions to prevent layout shift, and server-side rendering (SSR).",
        "roles": ["frontend", "web", "full stack"]
    },
    {
        "id": "beh_star_803",
        "category": "Behavioral (STAR)",
        "difficulty": "Easy",
        "demand_tag": "🔥 High Demand",
        "question": "Give an example of a project where you took leadership initiative to improve engineering productivity, developer tooling, or system reliability beyond your assigned tasks.",
        "guidance": "Highlight proactive ownership: automating repetitive deployment/testing steps, introducing API documentation generators, establishing team code quality guidelines, and measurable hours saved per week.",
        "roles": ["all"]
    },
    {
        "id": "beh_star_804",
        "category": "Behavioral (STAR)",
        "difficulty": "Easy",
        "demand_tag": "🔥 High Demand",
        "question": "Tell me about an instance where you pushed a code change to production that caused a bug or broken functionality. How did you take ownership and prevent it from recurring?",
        "guidance": "Demonstrate humble accountability: immediately alerted the team, initiated rapid rollback or hotfix, conducted a blameless post-mortem, and implemented an automated regression test in CI/CD so the issue could never recur.",
        "roles": ["all"]
    },
    {
        "id": "hr_align_901",
        "category": "HR & Company Alignment",
        "difficulty": "Easy",
        "demand_tag": "🔥 High Demand",
        "question": "Why do you want to work with our engineering team specifically, and how do you envision contributing to our technical roadmap over the next 2 years?",
        "guidance": "Connect company products and architectural challenges with your technical strengths, demonstrating concrete domain knowledge, continuous learning agility, and commitment to long-term impact.",
        "roles": ["all"]
    },

    # =========================================================================
    # 2. MID-LEVEL PRACTICAL ENGINEERING QUESTIONS (MEDIUM DIFFICULTY)
    # =========================================================================
    {
        "id": "sys_arch_102",
        "category": "System Design & Architecture",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "How does database indexing work under the hood (B-Trees vs Hash Indexes)? How do you identify slow queries and prevent the classic N+1 query problem?",
        "guidance": "Cover B-Tree structure, logarithmic search, composite index column ordering, EXPLAIN query plans, eager loading / JOIN FETCH in ORMs, and avoiding full table scans.",
        "roles": ["all", "backend", "software engineer", "full stack"]
    },
    {
        "id": "sec_201",
        "category": "Security & APIs",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Compare JWT (JSON Web Tokens) with traditional server-side Sessions. Where should JWTs be stored in the browser (HttpOnly Cookies vs LocalStorage), and how do you handle secure token refresh and revocation?",
        "guidance": "Highlight XSS risks with localStorage vs CSRF risks with cookies, SameSite=Strict/Lax flags, short-lived access tokens (15m) paired with rotating refresh tokens stored in secure HttpOnly cookies, and token blacklisting using Redis.",
        "roles": ["all", "software engineer", "backend", "full stack", "frontend"]
    },
    {
        "id": "sec_202",
        "category": "Security & APIs",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Explain the CORS (Cross-Origin Resource Sharing) mechanism. Why do browsers trigger Preflight OPTIONS requests, and how do you configure CORS securely in enterprise production APIs?",
        "guidance": "Cover origin definition (protocol + domain + port), simple vs non-simple HTTP requests, preflight OPTIONS headers (Access-Control-Allow-Origin, Methods, Headers), and never using wildcard '*' with credentials.",
        "roles": ["all", "frontend", "full stack", "backend"]
    },
    {
        "id": "devops_301",
        "category": "DevOps & Cloud",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "How do multi-stage Docker builds reduce container image size and improve security? What are the key best practices when writing production Dockerfiles?",
        "guidance": "Explain separating compilation tools from lightweight runtime images (e.g. Alpine/Distroless), non-root user execution, layer caching order, avoiding hardcoded secrets, and vulnerability scanning.",
        "roles": ["all", "software engineer", "backend", "full stack"]
    },
    {
        "id": "devops_302",
        "category": "DevOps & Cloud",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "In a Continuous Integration & Deployment (CI/CD) pipeline, what automated validation gates do you implement before merging pull requests and deploying to production?",
        "guidance": "Cover linting/code formatting, unit tests, integration test suites, automated security dependency scanning (SAST/DAST), code coverage thresholds, and automated staging smoke tests.",
        "roles": ["all", "software engineer", "full stack"]
    },
    {
        "id": "devops_303",
        "category": "DevOps & Cloud",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Compare Blue-Green Deployment with Canary Releases. How do these deployment strategies achieve zero downtime and minimize blast radius during software upgrades?",
        "guidance": "Explain routing traffic between two identical production environments (Blue/Green) vs routing small percentage (e.g. 5%) of live traffic to canary version, monitoring error rates, and automated instant rollback.",
        "roles": ["software engineer", "backend", "full stack"]
    },
    {
        "id": "tech_java_401",
        "category": "Technical (Java)",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "How does Spring Boot's @Transactional annotation work under the hood? Explain transaction propagation levels (REQUIRED, REQUIRES_NEW) and rollback rules.",
        "guidance": "Discuss Spring AOP proxies intercepting method calls, starting and committing transactions on PlatformTransactionManager, default rollback on Unchecked (RuntimeException) vs Checked exceptions, and self-invocation proxy bypass pitfalls.",
        "roles": ["java", "backend", "software engineer", "full stack"]
    },
    {
        "id": "tech_py_501",
        "category": "Technical (Python)",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Explain the difference between WSGI (Flask/Django) and ASGI (FastAPI) applications. How does Python's asyncio event loop handle non-blocking asynchronous requests concurrently?",
        "guidance": "Cover synchronous single request-per-thread model in WSGI vs asynchronous coroutines (`async`/`await`) in ASGI, single-threaded cooperative multitasking, and avoiding blocking calls in the event loop.",
        "roles": ["python", "backend", "software engineer", "full stack"]
    },
    {
        "id": "tech_py_503",
        "category": "Technical (Python)",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "How does Python handle memory management through Reference Counting and Generational Garbage Collection? How do you detect and resolve circular reference memory leaks?",
        "guidance": "Detail `ob_refcnt` tracking, automatic deallocation when count reaches 0, the `gc` module identifying isolated circular references in generations 0, 1, 2, and using `weakref` to prevent memory leaks.",
        "roles": ["python", "backend", "software engineer"]
    },
    {
        "id": "tech_fe_601",
        "category": "Technical (Frontend)",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Explain the JavaScript Event Loop, Call Stack, Microtask Queue (Promises, queueMicrotask), and Macrotask Queue (setTimeout, I/O, UI events). What is the exact execution order?",
        "guidance": "Detail single-threaded synchronous stack execution, draining the entire microtask queue before processing the next macrotask, render pipeline timing, and starvation avoidance.",
        "roles": ["frontend", "web", "full stack", "software engineer"]
    },
    {
        "id": "sit_prod_701",
        "category": "Production Scenarios",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Your production API response times suddenly spike from 50ms to 4000ms and users encounter HTTP 504 Gateway Timeouts. Walk me through your step-by-step incident response process.",
        "guidance": "Structure response: 1. Acknowledge and communicate status; 2. Check APM dashboard metrics (DB connection pool saturation, slow queries, memory/CPU); 3. Mitigate impact (traffic shedding, roll back recent deploy, restart pods); 4. Conduct root cause analysis; 5. Write a blameless post-mortem with preventive actions.",
        "roles": ["all", "software engineer", "backend", "full stack"]
    },
    {
        "id": "sit_prod_703",
        "category": "Production Scenarios",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "You discover a critical security vulnerability or data corruption bug in production code right before a major national holiday weekend. What is your action plan?",
        "guidance": "Explain threat isolation (disabling affected endpoint or putting behind maintenance flag), isolating corrupted records with backup rollback, preparing hotfix branch, automated staging verification, and transparent stakeholder communication.",
        "roles": ["all", "software engineer", "full stack"]
    },
    {
        "id": "beh_star_801",
        "category": "Behavioral (STAR)",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Describe a scenario where you faced a tight delivery deadline in an Agile sprint while simultaneously handling emerging technical debt or production support. How did you prioritize?",
        "guidance": "Structure with STAR: Situation (deadline + tech debt), Task (deliver critical value without compromising stability), Action (negotiated scope with PM, broke work into atomic PRs, added unit tests), Result (delivered on time, zero regression bugs).",
        "roles": ["all"]
    },
    {
        "id": "beh_star_802",
        "category": "Behavioral (STAR)",
        "difficulty": "Medium",
        "demand_tag": "🔥 High Demand",
        "question": "Tell me about a time you strongly disagreed with a senior engineer's architectural proposal or a teammate's pull request. How did you handle the conversation professionally?",
        "guidance": "Emphasize focusing on objective engineering data, benchmarks, trade-off matrices rather than personal opinions, scheduling a collaborative design review, and committing fully to the agreed consensus once decided.",
        "roles": ["all"]
    },

    # =========================================================================
    # 3. ADVANCED ARCHITECTURAL & HIGH-SCALE QUESTIONS (HARD / HIGH DIFFICULTY)
    # =========================================================================
    {
        "id": "sys_arch_101",
        "category": "System Design & Architecture",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "How do you decide between a Monolithic architecture and Microservices? When a monolith starts encountering performance bottlenecks, how do you systematically decouple it?",
        "guidance": "Explain domain boundaries (DDD), network latency tradeoffs, independent team velocity, database per service pattern, and using the Strangler Fig pattern for zero-downtime migration.",
        "roles": ["all", "software engineer", "backend", "full stack"]
    },
    {
        "id": "sys_arch_103",
        "category": "System Design & Architecture",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "How do you implement distributed caching with Redis? Explain Cache-Aside, Write-Through, and how you protect your system against Cache Stampede, Cache Penetration, and Cache Breakdown.",
        "guidance": "Discuss Cache-Aside pattern, TTL jitter/randomization, Bloom filters for non-existent keys, mutex locks for stampede protection, and hotkey replication.",
        "roles": ["all", "backend", "software engineer", "full stack"]
    },
    {
        "id": "sys_arch_104",
        "category": "System Design & Architecture",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "In an event-driven architecture using message brokers like Apache Kafka or RabbitMQ, how do you handle consumer group offsets, dead letter queues (DLQ), and idempotent message processing?",
        "guidance": "Explain publisher-subscriber model, partition keys, at-least-once vs exactly-once semantics, unique message deduplication keys in DB, and retry mechanisms with exponential backoff.",
        "roles": ["backend", "software engineer", "full stack"]
    },
    {
        "id": "sys_arch_105",
        "category": "System Design & Architecture",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "How do you design a high-throughput API Rate Limiter to protect downstream microservices from DDoS or traffic spikes? Compare Token Bucket and Leaky Bucket algorithms.",
        "guidance": "Detail Token Bucket algorithm with Redis atomic scripts (EVAL/Lua), distributed memory consumption, HTTP 429 Too Many Requests response headers (Retry-After), and IP vs user-tier rate limiting.",
        "roles": ["all", "backend", "software engineer", "full stack"]
    },
    {
        "id": "tech_java_402",
        "category": "Technical (Java)",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "Explain Java Memory Model (JMM), Garbage Collection generations (Eden, Survivor, Tenured), and how modern collectors like G1 and ZGC achieve low latency.",
        "guidance": "Detail heap partitioning, Young vs Old Gen, Minor vs Full GC, stop-the-world pauses, region-based concurrent marking in G1 GC, and colored pointers in ZGC.",
        "roles": ["java", "backend", "software engineer"]
    },
    {
        "id": "tech_java_403",
        "category": "Technical (Java)",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "What is the internal working of ConcurrentHashMap in Java 8+? Compare it with synchronizedMap and explain how it achieves high concurrent read/write throughput without global locking.",
        "guidance": "Explain node-level synchronized locking on head nodes, CAS (Compare-And-Swap) for inserts into empty buckets, volatile value reads for lock-free read operations, and treeifying bins under hash collision.",
        "roles": ["java", "backend", "software engineer"]
    },
    {
        "id": "tech_java_404",
        "category": "Technical (Java)",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "How do Java Virtual Threads (Project Loom in Java 21) change high-concurrency server architectures compared to traditional platform (OS-level) threads?",
        "guidance": "Explain OS kernel thread overhead (1MB stack) vs lightweight user-mode virtual threads (mounted on carrier threads), non-blocking carrier thread unmounting during blocking I/O, and writing synchronous-style code with massive scalability.",
        "roles": ["java", "backend", "software engineer"]
    },
    {
        "id": "tech_fe_602",
        "category": "Technical (Frontend)",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "What is React Reconciliation and the Virtual DOM diffing algorithm? How do React 18 Concurrent features (useTransition, useDeferredValue) keep user interfaces responsive during heavy state updates?",
        "guidance": "Cover heuristic O(n) diffing, element keys for list stability, fiber architecture interruptible rendering, prioritizing urgent user inputs (typing, clicking) over non-urgent background render passes.",
        "roles": ["frontend", "web", "full stack"]
    },
    {
        "id": "sit_prod_702",
        "category": "Production Scenarios",
        "difficulty": "Hard",
        "demand_tag": "🔥 High Demand",
        "question": "How do you investigate and resolve a Java or Python service that crashes with 'OutOfMemoryError: Java heap space' or OS OOM Killer every few days in production?",
        "guidance": "Explain enabling automated heap dumps on OOM (`-XX:+HeapDumpOnOutOfMemoryError`), analyzing dumps with Eclipse MAT / Py-Spy, identifying retained objects/unclosed streams/static collections, memory leak patch, and load test validation.",
        "roles": ["all", "software engineer", "backend"]
    }
]
