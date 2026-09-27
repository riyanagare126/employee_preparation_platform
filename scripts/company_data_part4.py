"""
Company Question Data - Part 4:
LTIMindtree, Persistent Systems, SAP, EY, PwC.
"""

from scripts.catalog_builder import (
    create_aptitude_question, create_coding_problem,
    create_technical_question, create_ai_question, create_hr_question
)

# ==========================================
# 16. LTIMINDTREE
# ==========================================
def build_ltimindtree_catalog():
    apt_java = [
        create_aptitude_question(
            "In LTIMindtree Quantitative: Two software partners A and B invest in a cloud consulting startup in the ratio 3:5. If partner A's share of annual profit is Rs. 45,000, what is the total profit earned by the startup?",
            ["Rs. 120,000", "Rs. 100,000", "Rs. 150,000", "Rs. 135,000"],
            "Rs. 120,000",
            "A's share is 3 / (3 + 5) = 3/8 of total profit. (3/8) * Total = 45,000 => Total = (45,000 * 8) / 3 = Rs. 120,000.",
            "Easy", "LTIMindtree Partnership Math"
        ),
        create_aptitude_question(
            "A web application's daily active user count increases from 25,000 to 40,000 over 3 months. What is the percentage growth in daily active users?",
            ["60.0%", "50.0%", "62.5%", "75.0%"],
            "60.0%",
            "Growth = ((40,000 - 25,000) / 25,000) * 100 = (15,000 / 25,000) * 100 = 60.0%.",
            "Easy", "LTIMindtree Percentage"
        ),
        create_aptitude_question(
            "In LTIMindtree Logical Reasoning: Find the missing term in the sequence: 8, 24, 12, 36, 18, 54, ___?",
            ["27", "36", "48", "72"],
            "27",
            "Alternating pattern: Multiply by 3, then divide by 2: 8*3=24, 24/2=12, 12*3=36, 36/2=18, 18*3=54. Next is 54 / 2 = 27.",
            "Easy", "LTIMindtree Number Series"
        ),
        create_aptitude_question(
            "A microservice processes 750 requests in 30 seconds. How many requests will it process in 4 minutes at the same steady rate?",
            ["6,000 requests", "5,000 requests", "7,500 requests", "4,500 requests"],
            "6,000 requests",
            "Rate = 750 / 30 = 25 requests/sec. 4 minutes = 240 seconds. Total requests = 240 * 25 = 6,000 requests.",
            "Easy", "LTIMindtree Rate Math"
        ),
        create_aptitude_question(
            "In LTIMindtree Verbal Ability: Choose the word that best completes the sentence: 'The engineering squad demonstrated remarkable ______ when pivoting their cloud architecture to meet the client's tight timeline.'",
            ["agility", "stagnation", "hesitance", "complacency"],
            "agility",
            "'Agility' denotes the ability to move quickly and easily or adapt swiftly to change in agile development.",
            "Easy", "LTIMindtree English Ability"
        ),
        create_aptitude_question(
            "In how many ways can 4 microservices be deployed across 4 Kubernetes availability zones such that each zone hosts exactly one microservice?",
            ["24 ways", "16 ways", "12 ways", "64 ways"],
            "24 ways",
            "Permutations of 4 items = 4! = 4 * 3 * 2 * 1 = 24 ways.",
            "Easy", "LTIMindtree Combinatorics"
        ),
        create_aptitude_question(
            "A merchant marks an enterprise router at Rs. 15,000 and sells it for Rs. 12,750. What is the discount percentage offered to the client?",
            ["15%", "12%", "18%", "20%"],
            "15%",
            "Discount amount = 15,000 - 12,750 = Rs. 2,250. Percentage = (2,250 / 15,000) * 100 = 15%.",
            "Easy", "LTIMindtree Profit & Loss"
        ),
        create_aptitude_question(
            "If in a digital cipher, 'CLOUD' is coded as 'DMPVE', how is 'NATIVE' coded in that same cipher?",
            ["OBJUWF", "OBKVXG", "NAUJWE", "OBITWF"],
            "OBJUWF",
            "Each letter is shifted by +1: N->O, A->B, T->U, I->J, V->W, E->F. Result is OBJUWF.",
            "Easy", "LTIMindtree Coding-Decoding"
        ),
        create_aptitude_question(
            "Two trains traveling in opposite directions at 45 km/h and 63 km/h cross each other in 10 seconds. What is the combined sum of their lengths?",
            ["300 meters", "250 meters", "360 meters", "280 meters"],
            "300 meters",
            "Relative speed = 45 + 63 = 108 km/h = 108 * (5/18) = 30 m/s. Sum of lengths = Speed * Time = 30 * 10 = 300 meters.",
            "Easy", "LTIMindtree Speed & Distance"
        ),
        create_aptitude_question(
            "What is the compound interest on Rs. 10,000 for 2 years at 8% per annum, compounded annually?",
            ["Rs. 1,664", "Rs. 1,600", "Rs. 1,728", "Rs. 1,580"],
            "Rs. 1,664",
            "Amount = 10,000 * (1.08)^2 = 10,000 * 1.1664 = Rs. 11,664. CI = 11,664 - 10,000 = Rs. 1,664.",
            "Easy", "LTIMindtree Compound Interest"
        ),
        create_aptitude_question(
            "In LTIMindtree Cause & Effect: Statement I: Cloud migration budgets increased by 40% across enterprise accounts. Statement II: Legacy datacenter hardware reached end-of-life status.",
            ["Statement II is the cause and Statement I is its effect", "Statement I is the cause and Statement II is its effect", "Both statements are independent causes", "Both statements are independent effects"],
            "Statement II is the cause and Statement I is its effect",
            "Datacenter hardware reaching end-of-life (II) forces enterprises to allocate higher budgets for cloud modernization (I).",
            "Medium", "LTIMindtree Cause & Effect"
        ),
        create_aptitude_question(
            "A person buys 5 enterprise software licenses for Rs. 2,000 each and sells 4 of them for Rs. 2,500 each. What is the net profit percentage earned so far?",
            ["0% (Break-even on cost)", "20%", "25%", "10%"],
            "0% (Break-even on cost)",
            "Total cost for 5 licenses = 5 * 2,000 = Rs. 10,000. Revenue from 4 licenses = 4 * 2,500 = Rs. 10,000. Net profit on total investment so far is 0% with 1 license left as pure profit.",
            "Easy", "LTIMindtree Commercial Math"
        ),
        create_aptitude_question(
            "A tank is filled by Pipe X in 25 minutes and by Pipe Y in 50 minutes. If both pipes operate together, in how many minutes will the tank be full?",
            ["16.67 minutes", "20.00 minutes", "15.00 minutes", "18.50 minutes"],
            "16.67 minutes",
            "Combined rate = 1/25 + 1/50 = 3/50 tank/min. Time = 50 / 3 = 16.67 minutes.",
            "Easy", "LTIMindtree Pipes & Cisterns"
        ),
        create_aptitude_question(
            "In a software development squad of 20 engineers, the average experience is 4.5 years. If the tech lead with 14 years of experience leaves, what is the new average experience?",
            ["4.0 years", "4.2 years", "3.8 years", "4.1 years"],
            "4.0 years",
            "Initial total = 20 * 4.5 = 90 years. New total = 90 - 14 = 76 years. New average = 76 / 19 = 4.0 years.",
            "Easy", "LTIMindtree Averages"
        ),
        create_aptitude_question(
            "What is the probability that a card drawn from a deck of 52 cards is a Spade or a Queen?",
            ["16/52 = 4/13", "17/52", "13/52 = 1/4", "15/52"],
            "16/52 = 4/13",
            "Spades = 13. Queens = 4. Queen of Spades is counted in both. Total favorable = 13 + 4 - 1 = 16. Probability = 16 / 52 = 4/13.",
            "Easy", "LTIMindtree Probability"
        )
    ]

    code_java = [
        create_coding_problem(
            "Sliding Window Maximum (LTIMindtree Coding)",
            "You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. Return the max sliding window in O(N) time.",
            "nums = [1,3,-1,-3,5,3,6,7], k = 3",
            "[3,3,5,5,6,7]",
            "public class Solution {\n    public int[] maxSlidingWindow(int[] nums, int k) {\n        return new int[0];\n    }\n}",
            "def max_sliding_window(nums: list[int], k: int) -> list[int]:\n    pass",
            "def compute_peak_traffic_window(traffic_df, k: int) -> list[int]:\n    pass",
            "Monotonic Deque: Store indices of elements in decreasing order. Evict indices outside current window and elements smaller than current num in O(N).",
            "Hard", "Monotonic Deque", "O(N)", "O(K)"
        ),
        create_coding_problem(
            "Smallest Missing Positive Integer",
            "Given an unsorted integer array nums, return the smallest positive integer that is not present in nums in O(N) time and O(1) auxiliary space.",
            "nums = [3,4,-1,1]",
            "2",
            "public class Solution {\n    public int firstMissingPositive(int[] nums) {\n        return 1;\n    }\n}",
            "def first_missing_positive(nums: list[int]) -> int:\n    pass",
            "def find_missing_subscriber_index(series_df) -> int:\n    pass",
            "Cycle sort / In-place bucket placement: Place each number x at index x-1 if 1 <= x <= n. Then scan to find first index where nums[i] != i + 1.",
            "Hard", "Array In-Place Sorting", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Subarray with Given XOR",
            "Given an array of integers A and an integer B, find the total number of contiguous subarrays having bitwise XOR of their elements equal to B in O(N) time.",
            "A = [4, 2, 2, 6, 4], B = 6",
            "4 (Subarrays: [4,2], [4,2,2,6,4], [2,2,6], [6])",
            "public class Solution {\n    public static int solve(int[] A, int B) {\n        return 0;\n    }\n}",
            "def solve(A: list[int], B: int) -> int:\n    pass",
            "def count_xor_telemetry_segments(stream_df, target_xor: int) -> int:\n    pass",
            "Prefix XOR and HashMap: Maintain running XOR xr; count occurrences of xr ^ B in HashMap storing prefix XOR frequencies.",
            "Medium", "Bit Manipulation & Hashing", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Container with Most Water",
            "Given n non-negative integers height where each represents a point at coordinate (i, height[i]), find two lines that together with the x-axis form a container that holds the most water.",
            "height = [1,8,6,2,5,4,8,3,7]",
            "49",
            "public class Solution {\n    public int maxArea(int[] height) {\n        return 0;\n    }\n}",
            "def max_area(height: list[int]) -> int:\n    pass",
            "def compute_max_buffer_capacity(levels_df) -> int:\n    pass",
            "Two pointers at array ends: Area = (right - left) * min(h[left], h[right]). Advance the pointer with the smaller height in O(N).",
            "Medium", "Two Pointers", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Find All Permutations of String",
            "Given a string s, return all unique permutations of the characters of the string in lexicographical order.",
            's = "ABC"',
            '["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]',
            "public class Solution {\n    public static List<String> findPermutation(String s) {\n        return new ArrayList<>();\n    }\n}",
            "def find_permutation(s: str) -> list[str]:\n    pass",
            "def generate_parameter_combinations(param_series):\n    pass",
            "Backtracking with a visited boolean array or sorting characters and swapping adjacent elements recursively.",
            "Medium", "Backtracking", "O(N! * N)", "O(N)"
        ),
        create_coding_problem(
            "Jump Game II (Minimum Hops)",
            "You are given an integer array nums where each element represents your maximum jump length. Return the minimum number of jumps to reach the last index.",
            "nums = [2,3,1,1,4]",
            "2",
            "public class Solution {\n    public int jump(int[] nums) {\n        return 0;\n    }\n}",
            "def jump(nums: list[int]) -> int:\n    pass",
            "def compute_min_routing_hops(network_df) -> int:\n    pass",
            "Greedy BFS: Maintain current_end and farthest_reach. When index reaches current_end, increment jumps and update current_end in O(N).",
            "Medium", "Greedy", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Minimum Size Subarray Sum",
            "Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If none, return 0.",
            "target = 7, nums = [2,3,1,2,4,3]",
            "2 ([4,3])",
            "public class Solution {\n    public int minSubArrayLen(int target, int[] nums) {\n        return 0;\n    }\n}",
            "def min_sub_array_len(target: int, nums: list[int]) -> int:\n    pass",
            "def find_minimal_transaction_window(tx_df, target: int) -> int:\n    pass",
            "Sliding window: Expand right pointer adding to sum. While sum >= target, update min_length and contract left pointer in O(N).",
            "Medium", "Sliding Window", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Next Permutation Lexicographical Order",
            "Given an array of integers nums, rearrange numbers into the lexicographically next greater permutation of numbers. If not possible, rearrange as the lowest possible order.",
            "nums = [1,2,3]",
            "[1,3,2]",
            "public class Solution {\n    public void nextPermutation(int[] nums) {\n    }\n}",
            "def next_permutation(nums: list[int]) -> None:\n    pass",
            "def advance_routing_permutation(route_df):\n    pass",
            "Find rightmost pivot nums[i] < nums[i+1]; find rightmost successor nums[j] > nums[i]; swap them; reverse suffix after i.",
            "Medium", "Array Two Pointers", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain Cloud-Native Modernization architecture at LTIMindtree: Transitioning legacy monolithic architectures to Spring Boot microservices on Kubernetes.",
            "Decompose monolith using Domain-Driven Design (DDD) bounded contexts; implement Strangler Fig pattern with API Gateway routing; externalize configurations; use containerized CI/CD pipelines.",
            "LTIMindtree Cloud Modernization", "Hard"
        ),
        create_technical_question(
            "How does Spring Cloud Gateway implement dynamic route predicates, filters, and rate limiting using Redis and Token Bucket algorithms?",
            "Spring Cloud Gateway runs on Netty non-blocking event loop. Route predicates match incoming path/headers; GatewayFilters inspect and modify requests; RequestRateLimiter queries Redis Lua script to enforce token bucket rates.",
            "LTIMindtree Spring Cloud Gateway", "Hard"
        ),
        create_technical_question(
            "Explain Reactive Programming with Spring WebFlux and Project Reactor: Mono vs Flux, Backpressure, and when WebFlux outperforms traditional Spring MVC.",
            "Mono emits 0 or 1 item; Flux emits 0 to N items. Backpressure allows consumers to signal how many items they can process, preventing buffer overflow. WebFlux outperforms MVC on high-concurrency streaming I/O with small memory footprint.",
            "LTIMindtree Spring WebFlux & Reactive", "Hard"
        ),
        create_technical_question(
            "How do you implement Distributed Tracing using OpenTelemetry and Zipkin across asynchronous microservices communicating via Apache Kafka?",
            "Inject W3C TraceContext headers into Kafka RecordHeaders on producer send; consumer extracts trace parent context and continues span, allowing Zipkin to visualize end-to-end transaction latency.",
            "LTIMindtree Distributed Tracing & OpenTelemetry", "Medium"
        ),
        create_technical_question(
            "Explain Resilience4j Microservices Patterns: Circuit Breaker, Retry, RateLimiter, and TimeLimiter in high-traffic retail banking services.",
            "Circuit Breaker prevents cascading failures by short-circuiting failing calls; Retry retries transient 503 errors; RateLimiter caps client request bursts; TimeLimiter aborts requests exceeding SLA timeout thresholds.",
            "LTIMindtree Microservice Resiliency", "Medium"
        ),
        create_technical_question(
            "How does Service Discovery operate with Netflix Eureka / HashiCorp Consul, and how do clients execute client-side load balancing with Spring Cloud LoadBalancer?",
            "Microservices register hostname and IP with Eureka server on startup and send periodic heartbeats. Client fetches registry cache and Spring Cloud LoadBalancer distributes requests round-robin.",
            "LTIMindtree Service Discovery", "Medium"
        ),
        create_technical_question(
            "Explain PostgreSQL Query Execution Analysis: Understanding EXPLAIN (ANALYZE, BUFFERS), Shared Buffer Cache hits, and Index-Only Scans.",
            "EXPLAIN ANALYZE executes query displaying actual node timings. BUFFERS reports shared hit/read blocks. An Index-Only Scan satisfies query directly from index pages without accessing the table heap.",
            "LTIMindtree PostgreSQL Tuning", "Medium"
        ),
        create_technical_question(
            "How does Apache Kafka manage Consumer Group Rebalancing, and how does the Cooperative Sticky Assignor eliminate stop-the-world partition rebalances?",
            "Traditional Eager Rebalance revoked all partitions from all consumers. Cooperative Sticky Assignor revokes only reassigned partitions in two phases, allowing surviving consumers to process uninterrupted.",
            "LTIMindtree Kafka Architecture", "Hard"
        ),
        create_technical_question(
            "Explain Java 17 features in enterprise backends: Records, Sealed Classes, and Pattern Matching for instanceof and switch.",
            "Records define transparent immutable data carriers with concise syntax. Sealed classes restrict inheritance to designated subclasses. Pattern matching simplifies type extraction and switch expressions.",
            "LTIMindtree Java 17 Features", "Easy"
        ),
        create_technical_question(
            "How do you configure Liquibase or Flyway for automated, version-controlled database schema migrations in CI/CD pipelines?",
            "Liquibase uses changelogs (XML/YAML/SQL) with changesets. It maintains a DATABASECHANGELOG table tracking applied checksums, executing unapplied scripts on application startup.",
            "LTIMindtree Database DevOps", "Medium"
        ),
        create_technical_question(
            "Explain the difference between SAGA Orchestration and SAGA Choreography in distributed transaction management across multi-cloud systems.",
            "Orchestration uses a central coordinator sending command messages to participants. Choreography relies on event publishing where each microservice reacts and publishes subsequent events.",
            "LTIMindtree Distributed Transactions", "Hard"
        ),
        create_technical_question(
            "How does Spring Batch manage JobRepository, JobExecution, StepExecution, and restartability for failed batch data processing jobs?",
            "JobRepository persists execution metadata in database tables. StepExecution tracks read/write/commit counts. If a step fails, Spring Batch restarts from the last committed chunk index.",
            "LTIMindtree Spring Batch", "Medium"
        ),
        create_technical_question(
            "Explain API Security best practices: OAuth 2.0 Resource Server configuration with Spring Security 6, JWT scope authorization, and mTLS.",
            "Spring Security validates JWT signatures against authorization server JWKS endpoint, mapping token scopes to GrantedAuthorities. mTLS adds certificate-based mutual verification at reverse proxy.",
            "LTIMindtree API Security", "Medium"
        ),
        create_technical_question(
            "What is Docker Multi-Stage Build and how does distroless base images (Google distroless) enhance container security in production?",
            "Multi-stage build compiles JAR in build container and copies binary into a distroless container containing only application and runtime dependencies (no package managers, no shell), eliminating attack vectors.",
            "LTIMindtree Container Security", "Medium"
        ),
        create_technical_question(
            "Explain Database Deadlock Resolution in high-volume e-commerce inventory booking systems.",
            "Enforce strict deterministic lock ordering (sort item IDs before acquiring locks); use pessimistic row locks (SELECT FOR UPDATE) with low lock timeouts; catch deadlocks and retry with exponential backoff.",
            "LTIMindtree Database Concurrency", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain how LTIMindtree Canvas.ai platform accelerates enterprise Generative AI adoption across application engineering and data operations.",
            "Discuss: Canvas.ai pre-built accelerators, GenAI-assisted code conversion, automated quality test suites, responsible AI guardrails, and enterprise RAG blueprints.",
            "LTIMindtree Canvas.ai Platform"
        ),
        create_ai_question(
            "How do you architect an enterprise RAG system combining semantic vector search with relational metadata filters using PostgreSQL pgvector?",
            "Architecture: Chunking enterprise docs, generating embeddings, indexing with HNSW in pgvector, executing combined SQL queries filtering on tenantId and Cosine distance.",
            "LTIMindtree pgvector RAG Architecture"
        ),
        create_ai_question(
            "Describe how AI-assisted automated code refactoring tools modernize legacy Java 8 codebases to Java 17/21 idioms at LTIMindtree.",
            "Detail: Parsing source code into AST, prompting specialized code LLMs to introduce records and pattern matching, running JaCoCo test suites to verify behavioral parity.",
            "LTIMindtree AI Code Modernization"
        ),
        create_ai_question(
            "How do you implement responsible AI guardrails to prevent PII leakage and prompt injection attacks in client conversational support portals?",
            "Explain: Dual-model guardrails, regex masks for sensitive credit/SSN patterns, system instruction primacy, and structured output schema verification.",
            "LTIMindtree Responsible AI Guardrails"
        ),
        create_ai_question(
            "How do you evaluate and benchmark LLM response accuracy in financial advisory applications using automated evaluation datasets?",
            "Discuss: Groundedness metrics, BLEU/ROUGE against golden reference answers, perplexity analysis, and human expert spot-check audits.",
            "LTIMindtree LLM Evaluation"
        ),
        create_ai_question(
            "Describe how Generative AI can assist in automated test case generation and synthetic test data creation for complex banking workflows.",
            "Detail: Parsing OpenAPI specs, generating boundary condition payloads, synthesizing compliant customer records without real PII, and running tests in sandbox.",
            "LTIMindtree Synthetic Data & Testing AI"
        ),
        create_ai_question(
            "How do you optimize LLM inference latency and token costs when deploying multi-tenant enterprise conversational search engines?",
            "Discuss: Prompt compression, caching common queries with Redis vector similarity, using quantized small language models (SLMs) for intent routing, and response streaming.",
            "LTIMindtree AI Cost Optimization"
        ),
        create_ai_question(
            "How do you design a multi-agent system where independent AI agents collaborate to triage, diagnose, and resolve IT infrastructure incidents?",
            "Structure: Ingestion agent categorizes alerts, Diagnostic agent queries log databases, Remediation agent drafts ansible scripts, and Verification agent tests health.",
            "LTIMindtree Multi-Agent AIOps"
        ),
        create_ai_question(
            "How does LTIMindtree ensure intellectual property protection and confidentiality when developers use generative AI coding assistants?",
            "Cover: Air-gapped corporate licenses, zero-code retention agreements with AI vendors, automated secret scanning, and mandatory human peer reviews.",
            "LTIMindtree AI IP Governance"
        ),
        create_ai_question(
            "How does LTIMindtree empower employees to build AI fluency through the Shaper learning platform and AI hackathons?",
            "Discuss: Role-based AI certification roadmaps, hands-on cloud sandbox labs, prompt engineering bootcamps, and client project simulations.",
            "LTIMindtree AI Talent Upskilling"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically choose LTIMindtree to build and accelerate your technology consulting career?",
            "Highlight: Combined strengths of L&T Infotech and Mindtree, leadership in cloud modernization, high-growth culture, and collaborative engineering teams.",
            "LTIMindtree Brand Motivation"
        ),
        create_hr_question(
            "LTIMindtree's culture emphasizes client-centricity, agility, and continuous learning. Describe a project where you demonstrated technical agility under changing requirements.",
            "Use STAR: Outline evolving project requirements, how you learned and adapted rapidly, and the positive delivery outcome for your stakeholders.",
            "Agility & Adaptability"
        ),
        create_hr_question(
            "LTIMindtree operates global delivery centers across India (Bangalore, Mumbai, Pune, Chennai, Hyderabad, Kolkata). Are you fully open to relocation and shift flexibility?",
            "Affirm: Complete willingness to relocate, readiness to support international client time zones, and adaptability to hybrid workplace practices.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "Tell me about a time you faced a difficult technical blocker during a critical sprint deadline. How did you handle the pressure?",
            "Showcase: Systematic root-cause debugging, transparent communication with leads, dividing problems into modular fixes, and hitting milestones.",
            "Delivering Under Pressure"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a conflicting technical opinion during software architecture discussions?",
            "Emphasize: Respectful dialogue, evaluating approaches based on performance benchmarks and project requirements, and aligning on consensus.",
            "Constructive Collaboration"
        ),
        create_hr_question(
            "Describe a time you received critical constructive feedback on your code quality or test coverage. What actions did you take to improve?",
            "Demonstrate: Professional humility, analyzing recommendations objectively, adopting clean code standards, and showing measurable improvement.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Where do you see yourself progressing at LTIMindtree over the next 3 to 5 years as an engineer?",
            "Connect: Growing from Software Engineer to Senior Software Engineer / Module Lead, mastering cloud native stacks, and mentoring junior engineers.",
            "Career Aspirations"
        ),
        create_hr_question(
            "Tell me about a time you took the initiative to learn an emerging technology stack (e.g. Reactive programming, Kafka, Cloud AI) without being asked.",
            "Highlight: Passion for technology, building prototypes, reading documentation, taking certifications, and sharing learnings with peers.",
            "Self-Driven Learning"
        ),
        create_hr_question(
            "Describe a situation where you had to explain a complex software defect or technical concept to a non-technical client or business manager.",
            "Show: Clear communication, avoiding jargon, using relatable analogies, and focusing on business outcomes and solutions.",
            "Communication Skills"
        ),
        create_hr_question(
            "Do you have any questions for LTIMindtree leadership regarding our cloud practices, project allocation, or employee development programs?",
            "Candidate asks thoughtful questions about LTIMindtree digital transformation practices, Canvas.ai innovation labs, or career progression tracks.",
            "Candidate Curiosity"
        )
    ]

    return {
        "aptitude": {"Java Developer": apt_java, "Python Developer": apt_java, "Data Analyst": apt_java},
        "coding": {"Java Developer": code_java, "Python Developer": code_java, "Data Analyst": code_java},
        "technical": {"Java Developer": tech_java, "Python Developer": tech_java, "Data Analyst": tech_java},
        "ai_interview": {"Java Developer": ai_java, "Python Developer": ai_java, "Data Analyst": ai_java},
        "hr": {"Java Developer": hr_java, "Python Developer": hr_java, "Data Analyst": hr_java}
    }


# ==========================================
# 17. PERSISTENT SYSTEMS
# ==========================================
def build_persistent_catalog():
    apt_java = [
        create_aptitude_question(
            "In Persistent Systems Engineering Drive: A binary tree of depth D has all leaves at depth D, and every internal node has exactly 2 children. If the tree has 16 leaves, what is the depth D (where root has depth 1)?",
            ["5", "4", "6", "16"],
            "5",
            "In a full binary tree, number of leaves = 2^(D-1). 2^(D-1) = 16 = 2^4 => D - 1 = 4 => D = 5.",
            "Medium", "Persistent Tree Data Structures"
        ),
        create_aptitude_question(
            "In a software product engineering team at Persistent, 5 developers write 10,000 lines of code in 8 days. How many lines of code can 8 developers write in 12 days at the same rate?",
            ["24,000 lines", "20,000 lines", "25,000 lines", "18,000 lines"],
            "24,000 lines",
            "Rate = 10,000 / (5 * 8) = 250 lines/developer-day. With 8 developers for 12 days: total = 8 * 12 * 250 = 24,000 lines.",
            "Medium", "Persistent Work Equation"
        ),
        create_aptitude_question(
            "Find the next number in the Persistent logical series: 4, 9, 25, 49, 121, 169, ___?",
            ["289", "225", "256", "361"],
            "289",
            "The sequence is squares of prime numbers: 2^2=4, 3^2=9, 5^2=25, 7^2=49, 11^2=121, 13^2=169. Next prime is 17; 17^2 = 289.",
            "Medium", "Persistent Number Series"
        ),
        create_aptitude_question(
            "A product license price increases by 25% and subsequently its sales volume drops by 20%. What is the net percentage change in total revenue?",
            ["0% (No change)", "+5% increase", "-5% decrease", "+2% increase"],
            "0% (No change)",
            "Revenue = Price * Volume. Net multiplier = (1 + 0.25) * (1 - 0.20) = 1.25 * 0.80 = 1.00. Net change = 0%.",
            "Easy", "Persistent Commercial Math"
        ),
        create_aptitude_question(
            "In how many ways can 5 software modules be scheduled in sequence if Module A must always execute strictly before Module B?",
            ["60 ways", "120 ways", "30 ways", "24 ways"],
            "60 ways",
            "Total permutations of 5 modules = 5! = 120. By symmetry, Module A appears before Module B in exactly half of all permutations: 120 / 2 = 60 ways.",
            "Easy", "Persistent Combinatorics"
        ),
        create_aptitude_question(
            "A train 180 meters long passes a signal pole in 9 seconds. What is the speed of the train in km/h?",
            ["72 km/h", "60 km/h", "80 km/h", "54 km/h"],
            "72 km/h",
            "Speed = Distance / Time = 180 / 9 = 20 m/s. In km/h = 20 * (18/5) = 72 km/h.",
            "Easy", "Persistent Speed & Time"
        ),
        create_aptitude_question(
            "In Persistent Verbal Ability: Choose the word that means 'existing or occurring everywhere at the same time in distributed computing':",
            ["Ubiquitous", "Ephemeral", "Ambiguous", "Anachronistic"],
            "Ubiquitous",
            "'Ubiquitous' means present, appearing, or found everywhere simultaneously.",
            "Easy", "Persistent Vocabulary"
        ),
        create_aptitude_question(
            "What is the sum of all interior angles of a regular hexagon?",
            ["720 degrees", "540 degrees", "1080 degrees", "360 degrees"],
            "720 degrees",
            "Formula: (n - 2) * 180 degrees. For a hexagon (n=6): (6 - 2) * 180 = 4 * 180 = 720 degrees.",
            "Easy", "Persistent Geometry"
        ),
        create_aptitude_question(
            "A test suite has 60 test cases. 45 passed on first run, 10 failed and were fixed, and 5 failed completely. What percentage of tests failed completely?",
            ["8.33%", "10.00%", "5.00%", "12.50%"],
            "8.33%",
            "Percentage = (5 / 60) * 100 = (1 / 12) * 100 = 8.33%.",
            "Easy", "Persistent Percentage"
        ),
        create_aptitude_question(
            "If log_10(x) = 2.5, what is the value of x in terms of powers of 10?",
            ["100 * sqrt(10)", "250", "1000", "500"],
            "100 * sqrt(10)",
            "x = 10^2.5 = 10^(2 + 0.5) = 10^2 * 10^0.5 = 100 * sqrt(10) ≈ 316.23.",
            "Easy", "Persistent Math"
        ),
        create_aptitude_question(
            "In Persistent Syllogisms: Statements: 1. All microservices are decoupled. 2. All decoupled systems are resilient. Conclusion: All microservices are resilient.",
            ["The conclusion follows logically", "The conclusion does not follow", "Data is inadequate", "None follows"],
            "The conclusion follows logically",
            "Microservices -> Decoupled -> Resilient. Transitive deduction validates that All microservices are resilient.",
            "Easy", "Persistent Syllogisms"
        ),
        create_aptitude_question(
            "A water reservoir has two inlet valves filling it in 10 and 15 hours. If both operate simultaneously, how many hours will it take to fill the reservoir?",
            ["6.0 hours", "7.5 hours", "5.0 hours", "8.0 hours"],
            "6.0 hours",
            "Combined rate = 1/10 + 1/15 = (3 + 2)/30 = 5/30 = 1/6. Total time = 6.0 hours.",
            "Easy", "Persistent Work Equation"
        ),
        create_aptitude_question(
            "What is the units digit of the product: 7^24 * 3^16?",
            ["1", "3", "7", "9"],
            "1",
            "Powers of 7 cycle in 7, 9, 3, 1 (24%4=0 -> 1). Powers of 3 cycle in 3, 9, 7, 1 (16%4=0 -> 1). Product units digit = 1 * 1 = 1.",
            "Medium", "Persistent Number Properties"
        ),
        create_aptitude_question(
            "A person walks 6 km West, turns Right and walks 8 km. How far is the person from the starting location?",
            ["10 km", "14 km", "12 km", "8 km"],
            "10 km",
            "Distance = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10 km.",
            "Easy", "Persistent Direction Sense"
        ),
        create_aptitude_question(
            "What is the probability of drawing two red face cards consecutively from a standard deck of 52 cards without replacement?",
            ["5/442", "6/52", "1/26", "3/221"],
            "5/442",
            "Red face cards: J, Q, K of Hearts and Diamonds = 6 cards. P(1st red face) = 6/52 = 3/26. P(2nd red face) = 5/51. Combined = (3/26) * (5/51) = (1/26) * (5/17) = 5 / 442.",
            "Medium", "Persistent Probability"
        )
    ]

    code_java = [
        create_coding_problem(
            "Implement Trie (Prefix Tree)",
            "A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement insert, search, and startsWith methods in O(L) time.",
            'insert("apple"), search("apple"), search("app"), startsWith("app")',
            "[null, true, false, true]",
            "public class Trie {\n    public Trie() {}\n    public void insert(String word) {}\n    public boolean search(String word) { return false; }\n    public boolean startsWith(String prefix) { return false; }\n}",
            "class Trie:\n    def __init__(self): pass\n    def insert(self, word: str) -> None: pass\n    def search(self, word: str) -> bool: return False\n    def starts_with(self, prefix: str) -> bool: return False",
            "class PrefixTreeIndex:\n    def __init__(self): pass\n    def index_token(self, token: str): pass",
            "Persistent product engineering standard: TrieNode with 26-child array and isEndOfWord boolean flag. O(L) runtime per operation.",
            "Medium", "Trie & Design", "O(L)", "O(Total Chars)"
        ),
        create_coding_problem(
            "Balanced Parentheses Check with Multiple Types",
            "Given a string s containing '(', ')', '{', '}', '[' and ']', determine if the input string is valid with matching brackets in proper order.",
            's = "{[()()]}"',
            "true",
            "public class Solution {\n    public boolean isValid(String s) {\n        return false;\n    }\n}",
            "def is_valid(s: str) -> bool:\n    pass",
            "def validate_json_token_enclosures(token_series) -> bool:\n    pass",
            "Stack tracking opening brackets; pop and assert matching bracket upon encounter of closing bracket; stack must be empty at end.",
            "Easy", "Stack", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Lowest Common Ancestor in Binary Tree",
            "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q in the tree in O(N) time.",
            "root = [3,5,1,6,2,0,8], p = 5, q = 1",
            "3",
            "public class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        return null;\n    }\n}",
            "def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:\n    pass",
            "def find_common_parent_module(tree_df, p: int, q: int):\n    pass",
            "Recursive post-order traversal: If root matches p or q, return root. Recurse left and right; if both return non-null, root is LCA.",
            "Medium", "Binary Tree", "O(N)", "O(H)"
        ),
        create_coding_problem(
            "Detect Loop in Linked List and Return Starting Node",
            "Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null in O(N) time and O(1) memory.",
            "head = [3,2,0,-4], pos = 1 (node with val 2)",
            "Node with value 2",
            "public class Solution {\n    public ListNode detectCycle(ListNode head) {\n        return null;\n    }\n}",
            "def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:\n    pass",
            "def find_dependency_cycle_origin(nodes_df):\n    pass",
            "Floyd's algorithm: Find meeting point of slow and fast pointers. Reset slow to head; advance both one step at a time until they meet at cycle start.",
            "Medium", "Linked List & Two Pointers", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Serialize and Deserialize Binary Tree",
            "Design an algorithm to serialize a binary tree to a string and deserialize that string back to the original tree structure.",
            "root = [1,2,3,null,null,4,5]",
            '"1,2,null,null,3,4,null,null,5,null,null"',
            "public class Codec {\n    public String serialize(TreeNode root) { return \"\"; }\n    public TreeNode deserialize(String data) { return null; }\n}",
            "class Codec:\n    def serialize(self, root: TreeNode) -> str: return \"\"\n    def deserialize(self, data: str) -> TreeNode: return None",
            "class TreeSerializer:\n    def serialize(self, root): return \"\"",
            "Pre-order DFS traversal with '#' or 'null' delimiters for missing children, rebuilding tree using Queue/iterator during deserialization.",
            "Hard", "Tree & Design", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Graph Breadth First Search (BFS) Traversal",
            "Given a directed graph with V vertices and an adjacency list, return the Breadth First Traversal of the graph starting from vertex 0.",
            "V = 5, adj = [[1,2,3],[0],[4],[0],[2]]",
            "[0, 1, 2, 3, 4]",
            "public class Solution {\n    public ArrayList<Integer> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {\n        return new ArrayList<>();\n    }\n}",
            "def bfs_of_graph(V: int, adj: list[list[int]]) -> list[int]:\n    pass",
            "def traverse_module_dependency_graph(adj_df) -> list[int]:\n    pass",
            "Standard BFS queue traversal with visited boolean array preventing cycles in O(V + E) time.",
            "Easy", "Graph & BFS", "O(V + E)", "O(V)"
        ),
        create_coding_problem(
            "Postfix Expression Evaluation using Stack",
            "Evaluate the value of an arithmetic expression in Reverse Polish Notation (Postfix). Valid operators are +, -, *, and /.",
            'tokens = ["2","1","+","3","*"]',
            "9 ((2 + 1) * 3)",
            "public class Solution {\n    public int evalRPN(String[] tokens) {\n        return 0;\n    }\n}",
            "def eval_rpn(tokens: list[str]) -> int:\n    pass",
            "def evaluate_postfix_metrics(tokens_series) -> int:\n    pass",
            "Push operands onto Stack. When encountering an operator, pop two operands, evaluate, and push result back onto Stack.",
            "Medium", "Stack & Math", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Flatten a Multilevel Doubly Linked List",
            "You are given a doubly linked list where each node has a next, prev, and child pointer. Flatten the list so that all nodes appear in a single-level doubly linked list.",
            "1---2---3---4\n        |\n        7---8",
            "1-2-3-7-8-4",
            "public class Solution {\n    public Node flatten(Node head) {\n        return head;\n    }\n}",
            "def flatten(head: Optional[Node]) -> Optional[Node]:\n    pass",
            "def flatten_hierarchical_structure(head_df):\n    pass",
            "Iterative traversal with Stack storing next nodes when encountering a child pointer, splicing child list in-line.",
            "Medium", "Doubly Linked List", "O(N)", "O(N)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain Domain-Driven Design (DDD) fundamentals: Ubiquitous Language, Bounded Contexts, Aggregates, and Domain Events in software product engineering at Persistent.",
            "Bounded context defines explicit boundaries where a domain model applies. Aggregates are clusters of domain entities and value objects treated as a single data mutation unit with an Aggregate Root.",
            "Persistent Systems DDD Architecture", "Hard"
        ),
        create_technical_question(
            "What is Clean Architecture (Robert C. Martin), and how do Dependency Inversion and the Dependency Rule protect domain entities from framework changes?",
            "Inner circles represent domain policies; outer circles represent mechanisms (UI, DB, Web). The Dependency Rule dictates that source code dependencies must point inward only toward higher-level policies.",
            "Persistent Clean Architecture", "Hard"
        ),
        create_technical_question(
            "Explain Test-Driven Development (TDD): Red-Green-Refactor cycle, Unit Tests vs Integration Tests, and why writing tests first improves modular design.",
            "Write a failing test (Red); write minimal code to pass (Green); refactor for clean code and performance (Refactor). TDD forces developers to design testable, decoupled interfaces before implementation.",
            "Persistent TDD & Software Craftsmanship", "Medium"
        ),
        create_technical_question(
            "How do you implement API Contract Testing using Pact to verify consumer-provider expectations without deploying full microservice test environments?",
            "Consumer tests define expected request/response pairs exported to Pact JSON files. Provider CI runs tests replaying consumer requests against real controllers, validating adherence.",
            "Persistent API Contract Testing", "Medium"
        ),
        create_technical_question(
            "Explain Java Concurrency: ExecutorService, ThreadPoolExecutor, and the Work-Stealing ForkJoinPool in high-throughput enterprise backends.",
            "ThreadPoolExecutor manages fixed worker threads over a blocking queue. ForkJoinPool uses work-stealing where idle threads steal subtasks from busy threads' deques, maximizing multi-core CPU utilization.",
            "Persistent Concurrency & Thread Pools", "Medium"
        ),
        create_technical_question(
            "What are Design Patterns in Software Product Engineering: Factory Method vs Abstract Factory, and Strategy vs State Pattern?",
            "Factory Method defines an interface for creating an object; Abstract Factory creates families of related objects. Strategy pattern encapsulates swappable algorithms; State pattern allows an object to alter its behavior when internal state changes.",
            "Persistent Design Patterns", "Medium"
        ),
        create_technical_question(
            "How does Liquibase manage automated database schema changesets, pre-conditions, and rollback tags in continuous deployment pipelines?",
            "Changesets define incremental schema mutations (XML/YAML/SQL). Pre-conditions verify table states before execution; rollback tags define undo SQL to safely reverse schema changes if builds fail.",
            "Persistent Database DevOps", "Medium"
        ),
        create_technical_question(
            "Explain Microservices Observability: The Three Pillars (Metrics with Micrometer, Distributed Tracing with OpenTelemetry, Centralized Logging with OpenSearch).",
            "Metrics capture numeric aggregates (CPU, request rates); Traces track request lifecycle across service boundaries; Logs record discrete application events. OpenTelemetry unifies instrumentation across all three.",
            "Persistent Observability Architecture", "Medium"
        ),
        create_technical_question(
            "How do you diagnose and fix Garbage Collection pause time spikes in Java backends using GC logs (-Xlog:gc*) and G1GC tuning parameters?",
            "Inspect GC logs for long 'Pause Young' or 'Full GC' events. Tune -XX:MaxGCPauseMillis, increase -XX:G1ReservePercent to avoid evacuation failures, and eliminate unnecessary short-lived object allocations.",
            "Persistent JVM Tuning", "Hard"
        ),
        create_technical_question(
            "Explain the difference between Optimistic Locking (@Version) and Pessimistic Locking in JPA/Hibernate enterprise applications.",
            "Optimistic locking verifies a version column on commit, throwing OptimisticLockException if conflict occurs (ideal for read-heavy). Pessimistic locking acquires row-level locks in database (SELECT FOR UPDATE) preventing concurrency.",
            "Persistent Data Access & Locking", "Medium"
        ),
        create_technical_question(
            "What is Static Code Analysis with SonarQube, and how do Cyclomatic Complexity and Cognitive Complexity differ in evaluating code maintainability?",
            "Cyclomatic complexity counts independent linear code execution paths (decision points). Cognitive complexity measures how difficult the control flow is for a human developer to read and understand.",
            "Persistent Code Quality & Metrics", "Easy"
        ),
        create_technical_question(
            "Explain how Docker multi-stage builds and non-root user execution comply with CIS Docker Security Benchmarks.",
            "Multi-stage build compiles JAR in heavy SDK and copies binary to minimal runtime JRE container. Creating a dedicated non-root user (USER appuser) prevents container breakout attacks from obtaining host root access.",
            "Persistent Container Security", "Medium"
        ),
        create_technical_question(
            "How do you design an Idempotent Consumer in Kafka microservices when network retries cause duplicate message delivery?",
            "Maintain an idempotent processed_messages table in database. When consuming a message, insert messageId inside the same database transaction as the business logic; duplicate messageIds trigger duplicate key exception and are skipped.",
            "Persistent Event-Driven Architecture", "Hard"
        ),
        create_technical_question(
            "Explain the difference between Monolithic, SOA, and Microservices architectures regarding service coupling, deployment autonomy, and database ownership.",
            "Monoliths share single codebase and database. SOA shares enterprise service buses and canonical data models. Microservices enforce strict bounded contexts with decentralized data management and independent deployment.",
            "Persistent Systems Architecture", "Medium"
        ),
        create_technical_question(
            "How do you implement secure REST API rate limiting using the Token Bucket algorithm with Redis in distributed environments?",
            "A Redis Lua script atomically executes token bucket logic: compute elapsed time since last refill, add tokens up to capacity, deduct requested tokens, and return allow/reject without race conditions.",
            "Persistent Distributed Rate Limiting", "Hard"
        )
    ]

    ai_java = [
        create_ai_question(
            "How does Persistent Systems integrate Generative AI across the Software Product Engineering lifecycle (from product requirements to automated deployment)?",
            "Discuss: AI-assisted user story generation, automated architecture diagram synthesis, code completion with security guardrails, test case synthesis, and automated documentation.",
            "Persistent Software Product Engineering AI"
        ),
        create_ai_question(
            "Explain how you design an enterprise RAG system with multi-modal document search across PDFs, technical blueprints, and CAD files using vector embeddings.",
            "Architecture: Multi-modal embedding models (e.g. CLIP/ColPali), vector database indexing, hybrid semantic + keyword search, and rendering visual grounded citations.",
            "Persistent Multi-Modal RAG"
        ),
        create_ai_question(
            "How do you implement continuous verification of AI-generated code commits in CI/CD pipelines to prevent security vulnerabilities and technical debt?",
            "Detail: Static analysis scanning with SonarQube, secret scanning with GitGuardian, dynamic dependency vulnerability checks with Snyk, and automated unit test assertions.",
            "Persistent AI Code Quality Gates"
        ),
        create_ai_question(
            "What strategies do you use for fine-tuning open source Small Language Models (SLMs) like Microsoft Phi-3 or Llama 3 for specialized API schema code generation?",
            "Discuss: Preparing domain-specific prompt-completion instruction datasets, LoRA parameter-efficient fine-tuning, evaluating BLEU and syntax validation scores, and exporting quantized models.",
            "Persistent SLM Fine-Tuning"
        ),
        create_ai_question(
            "How do you prevent data leakage and enforce strict corporate IP boundaries when integrating LLMs into proprietary enterprise software products?",
            "Cover: On-premise air-gapped model hosting, enterprise zero-retention API contracts, automated PII token redaction, and audit logging of all prompt exchanges.",
            "Persistent AI IP & Security"
        ),
        create_ai_question(
            "Describe how Generative AI can assist in automated test case generation and edge case synthesis for legacy enterprise software products.",
            "Detail: Extracting code execution paths, prompting LLMs to generate JUnit parameterized tests targeting edge cases (nulls, boundary limits), and measuring branch coverage.",
            "Persistent AI Automated Testing"
        ),
        create_ai_question(
            "How do you evaluate and monitor LLM prompt performance in production to detect model drift and hallucination across monthly software releases?",
            "Discuss: Golden dataset regression benchmarking, tracking groundedness metrics, human-in-the-loop evaluation dashboards, and alerting on accuracy drops.",
            "Persistent MLOps & LLM Monitoring"
        ),
        create_ai_question(
            "How do you optimize LLM API latency to achieve sub-500ms response times in interactive developer coding environments?",
            "Explain: Semantic prompt caching with Redis vector search, speculative decoding, prompt compression, and streaming token responses via Server-Sent Events.",
            "Persistent Real-Time AI Performance"
        ),
        create_ai_question(
            "How does Persistent Systems ensure responsible AI governance and algorithmic explainability in healthcare and life sciences product engineering?",
            "Cover: Algorithmic bias audits, demographic parity metrics, SHAP feature importance reporting, and adherence to FDA digital health software validation standards.",
            "Persistent Responsible AI in Healthcare"
        ),
        create_ai_question(
            "Describe how you design a multi-agent workflow using LangGraph where autonomous agents collaborate on software bug triage and automated patch generation.",
            "Structure: Triage agent reproduces bug from logs, Architect agent isolates root-cause file, Coder agent generates patch, and Tester agent runs regression tests.",
            "Persistent Multi-Agent Software Engineering"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically choose Persistent Systems to build your software product engineering career?",
            "Highlight: Persistent's focus on software product engineering, deep technical craftsmanship culture, partnership with global tech leaders, and focus on innovation.",
            "Persistent Brand Motivation"
        ),
        create_hr_question(
            "Persistent values 'Code Craftsmanship' and high engineering standards. Describe a project where you refused to take an easy shortcut and built a clean, maintainable architecture instead.",
            "Use STAR: Outline the pressure to take a shortcut, the clean architectural principles you implemented (TDD, clean code, design patterns), and the long-term maintainability benefits.",
            "Code Craftsmanship & Engineering Rigor"
        ),
        create_hr_question(
            "Persistent operates technology centers in Pune, Goa, Nagpur, Bangalore, Hyderabad, and client locations worldwide. Are you fully flexible with relocation and project assignments?",
            "Affirm: Complete willingness to relocate, readiness to support global product engineering schedules, and enthusiasm for collaborating with international teams.",
            "Relocation & Project Flexibility"
        ),
        create_hr_question(
            "Tell me about a time you worked on a complex software feature under an aggressive sprint deadline. How did you manage your time and ensure zero production defects?",
            "Showcase: Disciplined task prioritization, automated unit testing to prevent regression, transparent communication with leads, and delivering on time.",
            "Delivering Under Pressure"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a strong, conflicting technical opinion on software design or framework selection?",
            "Emphasize: Respectful listening, evaluating options based on data, benchmarks, and project requirements, and working together toward consensus.",
            "Constructive Collaboration"
        ),
        create_hr_question(
            "Describe a situation where you received constructive feedback on your code during a peer review. What steps did you take to implement the improvements?",
            "Demonstrate: Professional humility, analyzing recommendations objectively, adopting clean coding practices, and showing visible growth.",
            "Receptivity to Peer Review"
        ),
        create_hr_question(
            "Where do you see yourself progressing at Persistent Systems over the next 3 to 5 years as a product engineer?",
            "Connect: Growing from Software Engineer to Senior Software Engineer / Technical Lead, mastering cloud native and distributed architectures, and mentoring new hires.",
            "Career Aspirations"
        ),
        create_hr_question(
            "Tell me about a time you took the initiative to learn a new programming language, framework, or tool to solve an unassigned technical challenge.",
            "Highlight: Curiosity, self-driven learning, reading documentation, building prototypes, and sharing knowledge with teammates.",
            "Curiosity & Continuous Learning"
        ),
        create_hr_question(
            "Describe a time you discovered a critical bug or vulnerability in your code that had gone unnoticed. How did you handle taking ownership?",
            "Show: Immediate accountability, transparent communication with the team lead, isolating root causes, fixing the defect, and adding regression tests.",
            "Accountability & Integrity"
        ),
        create_hr_question(
            "Do you have any questions for Persistent Systems leadership regarding our product engineering practices, onboarding, or corporate culture?",
            "Candidate asks about Persistent product engineering centers of excellence, open source contributions, or career development programs.",
            "Candidate Curiosity"
        )
    ]

    return {
        "aptitude": {"Java Developer": apt_java, "Python Developer": apt_java, "Data Analyst": apt_java},
        "coding": {"Java Developer": code_java, "Python Developer": code_java, "Data Analyst": code_java},
        "technical": {"Java Developer": tech_java, "Python Developer": tech_java, "Data Analyst": tech_java},
        "ai_interview": {"Java Developer": ai_java, "Python Developer": ai_java, "Data Analyst": ai_java},
        "hr": {"Java Developer": hr_java, "Python Developer": hr_java, "Data Analyst": hr_java}
    }


# ==========================================
# 18. SAP
# ==========================================
def build_sap_catalog():
    apt_java = [
        create_aptitude_question(
            "In SAP Labs In-Memory Computing Math: A column-store database compresses 400 GB of enterprise ERP data with an average compression ratio of 4:1. How much RAM is required to hold this compressed dataset in SAP HANA memory?",
            ["100 GB", "80 GB", "160 GB", "200 GB"],
            "100 GB",
            "Compression ratio 4:1 means compressed size = 400 GB / 4 = 100 GB of RAM required.",
            "Easy", "SAP HANA Memory Math"
        ),
        create_aptitude_question(
            "In an SAP enterprise inventory system, warehouse stock of 1,200 parts decreases by 25% in month 1 and the remaining stock decreases by another 20% in month 2. How many parts remain in stock?",
            ["720 parts", "660 parts", "800 parts", "750 parts"],
            "720 parts",
            "Month 1 remaining = 1,200 * 0.75 = 900 parts. Month 2 remaining = 900 * 0.80 = 720 parts.",
            "Easy", "SAP Inventory Percentage"
        ),
        create_aptitude_question(
            "Find the next number in the SAP analytical sequence: 1, 4, 9, 16, 25, 36, ___?",
            ["49", "48", "64", "50"],
            "49",
            "Sequence of perfect squares: 1^2, 2^2, 3^2, 4^2, 5^2, 6^2. Next term = 7^2 = 49.",
            "Easy", "SAP Number Series"
        ),
        create_aptitude_question(
            "An enterprise SAP BTP cloud microservice executes 1,500 transactions/minute. How many transactions does it execute in an 8-hour enterprise work shift?",
            ["720,000 transactions", "600,000 transactions", "800,000 transactions", "900,000 transactions"],
            "720,000 transactions",
            "Transactions per hour = 1,500 * 60 = 90,000. In 8 hours = 90,000 * 8 = 720,000 transactions.",
            "Easy", "SAP Systems Rate Math"
        ),
        create_aptitude_question(
            "In SAP Deductive Reasoning: All ERP modules are business software. Some business software is cloud-native. Which conclusion follows definitively?",
            ["None follows definitively", "All cloud-native software is an ERP module", "Some ERP modules are cloud-native", "No cloud-native software is an ERP module"],
            "None follows definitively",
            "The middle term 'business software' is undistributed in both premises, meaning no definite connection can be proven between ERP modules and cloud-native software.",
            "Medium", "SAP Deductive Logic"
        ),
        create_aptitude_question(
            "In how many ways can 4 enterprise modules (Finance, HR, Supply Chain, CRM) be scheduled for sequential cloud migration?",
            ["24 ways", "12 ways", "16 ways", "48 ways"],
            "24 ways",
            "Permutations of 4 items = 4! = 4 * 3 * 2 * 1 = 24 ways.",
            "Easy", "SAP Combinatorics"
        ),
        create_aptitude_question(
            "A corporate client purchases an SAP S/4HANA software subscription for Rs. 500,000 with a 12% enterprise discount and an additional 5% prompt-payment incentive. What is the final price paid?",
            ["Rs. 418,000", "Rs. 415,000", "Rs. 420,000", "Rs. 430,000"],
            "Rs. 418,000",
            "After 12% discount: 500,000 * 0.88 = Rs. 440,000. After additional 5%: 440,000 * 0.95 = Rs. 418,000.",
            "Medium", "SAP Commercial Math"
        ),
        create_aptitude_question(
            "A server room backup generator has enough fuel to run 6 servers for 18 hours. How many hours will the fuel last if 9 servers run at the same power consumption rate?",
            ["12 hours", "10 hours", "15 hours", "14 hours"],
            "12 hours",
            "Total server-hours of fuel = 6 * 18 = 108 server-hours. Running 9 servers: hours = 108 / 9 = 12 hours.",
            "Easy", "SAP Work Equation"
        ),
        create_aptitude_question(
            "In SAP Verbal Ability: Choose the antonym for 'HAPHAZARD' in software quality engineering context:",
            ["Systematic", "Random", "Arbitrary", "Careless"],
            "Systematic",
            "'Haphazard' means lacking any obvious principle of organization. The direct antonym is 'Systematic'.",
            "Easy", "SAP English Ability"
        ),
        create_aptitude_question(
            "If an in-memory database query touches 8 parallel CPU cores and completes in 250ms, what was the total CPU time consumed in seconds?",
            ["2.0 seconds", "1.5 seconds", "2.5 seconds", "0.25 seconds"],
            "2.0 seconds",
            "Total CPU time = 8 cores * 0.250 seconds = 2.0 CPU-seconds.",
            "Easy", "SAP Performance Math"
        ),
        create_aptitude_question(
            "A train traveling at 72 km/h crosses an SAP campus gate in 12 seconds. What is the length of the train?",
            ["240 meters", "200 meters", "250 meters", "300 meters"],
            "240 meters",
            "Speed = 72 * (5/18) = 20 m/s. Length = Speed * Time = 20 * 12 = 240 meters.",
            "Easy", "SAP Speed & Distance"
        ),
        create_aptitude_question(
            "A manufacturing line produces 500 parts per hour with a 2% defect rate. In an 8-hour production run, how many non-defective parts are produced?",
            ["3,920 parts", "4,000 parts", "3,840 parts", "3,900 parts"],
            "3,920 parts",
            "Total parts = 500 * 8 = 4,000. Defective parts = 2% of 4,000 = 80 parts. Non-defective = 4,000 - 80 = 3,920 parts.",
            "Easy", "SAP Production Arithmetic"
        ),
        create_aptitude_question(
            "What is the compound interest on Rs. 20,000 for 2 years at 5% per annum, compounded annually?",
            ["Rs. 2,050", "Rs. 2,000", "Rs. 2,100", "Rs. 1,950"],
            "Rs. 2,050",
            "Amount = 20,000 * (1.05)^2 = 20,000 * 1.1025 = Rs. 22,050. CI = 22,050 - 20,000 = Rs. 2,050.",
            "Easy", "SAP Financial Math"
        ),
        create_aptitude_question(
            "In SAP Direction Sense: An logistics truck moves 15 km North, turns Right and moves 20 km. What is the shortest distance from the depot origin?",
            ["25 km", "30 km", "35 km", "22 km"],
            "25 km",
            "By Pythagorean theorem: Distance = sqrt(15^2 + 20^2) = sqrt(225 + 400) = sqrt(625) = 25 km.",
            "Easy", "SAP Geometry & Distance"
        ),
        create_aptitude_question(
            "What is the probability of selecting a red ball from a bin containing 8 red, 6 blue, and 6 green supply parts?",
            ["8/20 = 2/5", "6/20 = 3/10", "1/2", "1/4"],
            "8/20 = 2/5",
            "Total parts = 8 + 6 + 6 = 20. Probability = 8 / 20 = 2/5 = 40%.",
            "Easy", "SAP Probability"
        )
    ]

    code_java = [
        create_coding_problem(
            "Range Sum Query 2D (Immutable Matrix)",
            "Given a 2D matrix matrix, handle multiple queries of the sum of elements inside a rectangle defined by its upper-left and lower-right corners in O(1) query time.",
            "matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]], sumRegion(2,1,4,3)",
            "8",
            "public class NumMatrix {\n    public NumMatrix(int[][] matrix) {}\n    public int sumRegion(int row1, int col1, int row2, int col2) {\n        return 0;\n    }\n}",
            "class NumMatrix:\n    def __init__(self, matrix: list[list[int]]): pass\n    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int: return 0",
            "class MatrixRegionalLedger:\n    def __init__(self, matrix_df): pass\n    def query_revenue_box(self, r1: int, c1: int, r2: int, c2: int) -> int: return 0",
            "SAP HANA in-memory standard: 2D Prefix Sums table precomputed in O(M*N); each submatrix query resolves in O(1) via inclusion-exclusion formula.",
            "Medium", "2D Prefix Sum & Design", "O(1) query", "O(M * N)"
        ),
        create_coding_problem(
            "In-Memory Column Store Scan with Predicate Filter",
            "Given a columnar table represented as an integer array of record IDs and a parallel array of transaction amounts, return all record IDs where amount is between minVal and maxVal.",
            "ids = [101, 102, 103, 104], amounts = [450, 1200, 800, 150], minVal = 400, maxVal = 1000",
            "[101, 103]",
            "public class Solution {\n    public static List<Integer> columnScan(int[] ids, int[] amounts, int minVal, int maxVal) {\n        return new ArrayList<>();\n    }\n}",
            "def column_scan(ids: list[int], amounts: list[int], min_val: int, max_val: int) -> list[int]:\n    pass",
            "def filter_columnar_erp_records(ids_df, min_val: int, max_val: int) -> list[int]:\n    pass",
            "Vectorized linear scan iterating contiguous amounts array, matching predicates and collecting corresponding IDs in O(N).",
            "Easy", "Columnar Scan & Arrays", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Top K Frequent Financial Accounts (SAP BTP)",
            "Given an integer array nums representing ERP account transactions and an integer k, return the k most frequent account IDs in O(N log K) time.",
            "nums = [1,1,1,2,2,3], k = 2",
            "[1,2]",
            "public class Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        return new int[0];\n    }\n}",
            "def top_k_frequent(nums: list[int], k: int) -> list[int]:\n    pass",
            "def extract_high_volume_ledgers(ledger_df, k: int):\n    pass",
            "Count frequencies using HashMap; maintain a Min-Heap of size K comparing entry values, or use Bucket Sort.",
            "Medium", "Heap / Bucket Sort", "O(N log K)", "O(N)"
        ),
        create_coding_problem(
            "Matrix Block Sum (Convolution Filter)",
            "Given an m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for: i - k <= r <= i + k, j - k <= c <= j + k.",
            "mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1",
            "[[12,21,16],[27,45,33],[24,39,28]]",
            "public class Solution {\n    public int[][] matrixBlockSum(int[][] mat, int k) {\n        return new int[0][0];\n    }\n}",
            "def matrix_block_sum(mat: list[list[int]], k: int) -> list[list[int]]:\n    pass",
            "def compute_localized_smoothing_grid(grid_df, k: int):\n    pass",
            "Compute 2D Prefix Sums table; compute block sum for each cell in O(1) using precalculated boundary values.",
            "Medium", "2D Prefix Sum", "O(M * N)", "O(M * N)"
        ),
        create_coding_problem(
            "Longest Substring with At Most K Distinct Characters",
            "Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.",
            's = "eceba", k = 2',
            '3 ("ece")',
            "public class Solution {\n    public int lengthOfLongestSubstringKDistinct(String s, int k) {\n        return 0;\n    }\n}",
            "def length_of_longest_substring_k_distinct(s: str, k: int) -> int:\n    pass",
            "def max_window_with_distinct_tokens(text_df, k: int) -> int:\n    pass",
            "Sliding window maintaining character frequency map. While map.size() > k, contract left window boundary in O(N).",
            "Medium", "Sliding Window & Hash Map", "O(N)", "O(K)"
        ),
        create_coding_problem(
            "Merge Intervals in Business Scheduling",
            "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals.",
            "intervals = [[1,3],[2,6],[8,10],[15,18]]",
            "[[1,6],[8,10],[15,18]]",
            "public class Solution {\n    public int[][] merge(int[][] intervals) {\n        return new int[0][0];\n    }\n}",
            "def merge(intervals: list[list[int]]) -> list[list[int]]:\n    pass",
            "def consolidate_business_calendar_blocks(cal_df):\n    pass",
            "Sort intervals by start time; iterate through comparing current interval start with previous interval end.",
            "Medium", "Intervals & Sorting", "O(N log N)", "O(N)"
        ),
        create_coding_problem(
            "Find Median from Continuous Data Stream",
            "The median is the middle value in an ordered integer list. Design a data structure that supports addNum(num) and findMedian() from a continuous stream in O(log N) insert and O(1) lookup.",
            "addNum(1), addNum(2), findMedian(), addNum(3), findMedian()",
            "[null, null, 1.5, null, 2.0]",
            "public class MedianFinder {\n    public MedianFinder() {}\n    public void addNum(int num) {}\n    public double findMedian() { return 0.0; }\n}",
            "class MedianFinder:\n    def __init__(self): pass\n    def add_num(self, num: int) -> None: pass\n    def find_median(self) -> float: return 0.0",
            "class StreamingFinancialMedian:\n    def add_tick(self, val: float): pass",
            "Two Heaps: Max-Heap for lower half, Min-Heap for upper half. Balance heap sizes so difference <= 1.",
            "Hard", "Two Heaps Design", "O(log N) add, O(1) query", "O(N)"
        ),
        create_coding_problem(
            "Partition Equal Subset Sum in ERP Balancing",
            "Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.",
            "nums = [1,5,11,5]",
            "true (Subsets: [1, 5, 5] and [11])",
            "public class Solution {\n    public boolean canPartition(int[] nums) {\n        return false;\n    }\n}",
            "def can_partition(nums: list[int]) -> bool:\n    pass",
            "def verify_dual_ledger_balance(nums_df) -> bool:\n    pass",
            "0/1 Knapsack DP: If total sum is odd, return false. Find if subset exists with sum = total / 2 in O(N * Sum).",
            "Medium", "Dynamic Programming", "O(N * Target)", "O(Target)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the architecture of SAP HANA In-Memory Database: Column-Store vs Row-Store memory layouts, Delta Merge operations, and compression algorithms (Dictionary, Run-Length).",
            "HANA stores data in RAM in columnar format for lightning-fast SIMD scans. Writes append to a write-optimized in-memory Delta Store. Periodic Delta Merge operations merge delta records into the main compressed column store without blocking readers.",
            "SAP HANA In-Memory Architecture", "Hard"
        ),
        create_technical_question(
            "What is SAP Business Technology Platform (BTP), and how does the Cloud Foundry and Kyma (Kubernetes) runtime environment host enterprise microservices?",
            "SAP BTP is the enterprise integration and extension platform. Cloud Foundry provides managed polyglot runtimes (Java, Node.js). Kyma provides containerized microservices built on Kubernetes with native SAP Event Mesh integration.",
            "SAP BTP Architecture", "Hard"
        ),
        create_technical_question(
            "Explain SAP Core Data Services (CDS) views and how they implement code-to-data pushdown to execute calculations directly within SAP HANA rather than in application layers.",
            "CDS defines semantic data models and business views directly at the database layer. Complex joins, aggregations, and business logic push down to execute at in-memory database speed, returning only final results to application servers.",
            "SAP Core Data Services (CDS)", "Hard"
        ),
        create_technical_question(
            "What is the SAP Clean Core paradigm in SAP S/4HANA Cloud, and how do Side-by-Side Extensibility on SAP BTP and Key-User Extensibility enforce clean-core principles?",
            "Clean Core strictly separates custom client code from core ERP code. Rather than modifying standard SAP ABAP tables, extensions run side-by-side on SAP BTP communicating via standardized OData REST APIs.",
            "SAP S/4HANA Clean Core Paradigm", "Hard"
        ),
        create_technical_question(
            "Explain OData (Open Data Protocol) RESTful APIs in SAP systems: Entity Sets, Navigation Properties, $expand, $filter, and $select query options.",
            "OData is an OASIS standard for building REST APIs. $select restricts returned columns; $filter filters rows on server side; $expand traverses navigation properties in a single round-trip without multiple queries.",
            "SAP OData Protocol", "Medium"
        ),
        create_technical_question(
            "How does SAP Event Mesh enable asynchronous, decoupled communication between SAP S/4HANA ERP and external cloud applications?",
            "Business events (e.g. SalesOrderCreated) publish to SAP Event Mesh topics. External cloud applications subscribe via standard protocols (MQTT, AMQP, REST Webhooks) without polling the ERP database.",
            "SAP Event Mesh & Messaging", "Medium"
        ),
        create_technical_question(
            "Explain Java Concurrency: The Java Memory Model (JMM), ThreadPoolExecutor tuning, and CompletableFuture chaining in high-throughput enterprise batch jobs.",
            "JMM enforces memory visibility and instruction reordering constraints. ThreadPoolExecutor scales worker threads with bounded queues to avoid memory exhaustion during peak ERP month-end batch runs.",
            "SAP Enterprise Java Concurrency", "Medium"
        ),
        create_technical_question(
            "What is Multi-Tenancy architecture in SAP Cloud applications, and how is tenant data isolation enforced (Separate Database vs Shared Database with Tenant Discriminator Column)?",
            "Shared database with tenant-id column provides cost-effective scaling; Spring Security and JPA filters automatically inject 'WHERE tenant_id = ?' on all queries to strictly prevent cross-tenant data leakage.",
            "SAP Cloud Multi-Tenancy", "Hard"
        ),
        create_technical_question(
            "How does SAP Cloud SDK for Java streamline communication with SAP S/4HANA systems by providing typed client libraries and automated destination resolution?",
            "SAP Cloud SDK encapsulates SAP Destination Service lookups, handles OAuth2 token exchanges, automatically serializes/deserializes OData entities, and provides built-in circuit breakers with Resilience4j.",
            "SAP Cloud SDK for Java", "Medium"
        ),
        create_technical_question(
            "Explain High Availability and Disaster Recovery (HA/DR) for SAP HANA: HANA System Replication (HSR) modes (Synchronous, Asynchronous, Full Sync).",
            "HSR replicates data from primary to secondary HANA node. Synchronous mode waits for secondary to write to log buffer before commit; Asynchronous mode commits on primary immediately; Full Sync pauses primary if secondary disconnects.",
            "SAP HANA High Availability & HSR", "Hard"
        ),
        create_technical_question(
            "What is the difference between Synchronous RFC (sRFC), Asynchronous RFC (aRFC), and Transactional RFC (tRFC) in enterprise SAP integration?",
            "sRFC blocks until the remote function completes. aRFC returns control immediately without waiting. tRFC executes the function exactly once in transactional context using unique transaction IDs (TID).",
            "SAP Enterprise RFC Integration", "Medium"
        ),
        create_technical_question(
            "How do you implement Spring Boot Microservices on SAP BTP using the SAP Cloud Application Programming Model (CAP)?",
            "CAP provides a framework using CDS for data modeling and service definition, automatically generating OData endpoints and integrating with SAP HANA and SAP BTP authentication services.",
            "SAP Cloud Application Programming (CAP)", "Medium"
        ),
        create_technical_question(
            "Explain the difference between First Level Cache and Second Level Cache in JPA/Hibernate enterprise implementations.",
            "First level cache is bound to the EntityManager/Session scope. Second level cache is shared across the entire application using Redis or Ehcache, caching entities and queries to minimize database I/O.",
            "SAP JPA & Hibernate Caching", "Easy"
        ),
        create_technical_question(
            "What are SQL Stored Procedures and Triggers, and why does SAP HANA encourage calculation logic in calculation views rather than procedural triggers?",
            "HANA is optimized for parallel columnar vector operations. Procedural row-by-row triggers disrupt vectorization and force execution in the slower procedural engine, destroying in-memory performance.",
            "SAP HANA Calculation Views", "Medium"
        ),
        create_technical_question(
            "How do you configure Continuous Delivery in enterprise SAP software engineering using project 'Piper' and Jenkins / GitHub Actions pipelines?",
            "Project Piper provides ready-to-use pipeline stages for SAP technologies (linting, automated unit tests, SonarQube quality gates, transport management system integration, and zero-downtime deployment to BTP).",
            "SAP DevOps & Project Piper", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain SAP Joule AI copilot and how it integrates with SAP S/4HANA, SAP BTP, and SuccessFactors to deliver enterprise contextual generative AI.",
            "Discuss: Joule copilot embedded across business workflows, understanding ERP business context, generating natural language answers grounded in enterprise data, and automating business tasks.",
            "SAP Joule AI Copilot"
        ),
        create_ai_question(
            "How does SAP Business AI enforce strict data privacy, enterprise context augmentation, and zero training on customer proprietary ERP data?",
            "Explain: Enterprise AI agreements with LLM providers guaranteeing data is never retained or used for foundation model training, role-based access control, and audit trails.",
            "SAP Business AI Data Privacy"
        ),
        create_ai_question(
            "How do you architect an enterprise RAG system using SAP HANA Cloud Vector Engine to perform semantic search across millions of ERP supplier contracts?",
            "Detail: Storing dense embeddings in REAL_VECTOR columns, executing Cosine distance queries using HNSW indexing alongside relational SQL joins, and prompt grounding.",
            "SAP HANA Cloud Vector Engine RAG"
        ),
        create_ai_question(
            "Describe how Generative AI can automate the creation of SAP CDS views and OData service definitions from business requirement specifications.",
            "Detail: Prompting specialized code models with domain entity relationships, generating syntactically valid CDS DDL definitions, and validating schemas with CAP compiler.",
            "SAP AI Automated CDS Modeling"
        ),
        create_ai_question(
            "What techniques ensure zero hallucinations when using LLMs for generating automated corporate financial summaries from SAP S/4HANA balance sheets?",
            "Discuss: Strict prompt grounding to retrieved balance sheet line items, temperature=0, deterministic cross-validation against financial ledgers, and human controller sign-off.",
            "SAP Hallucination Prevention in Finance"
        ),
        create_ai_question(
            "How do you design an AI-powered automated accounts payable invoice matching engine using SAP AI Core and computer vision OCR?",
            "Architecture: Document information extraction model parses invoice PDFs, extracts supplier, tax, and line items, matches against purchase orders in S/4HANA, and routes discrepancies.",
            "SAP AI Core Document Extraction"
        ),
        create_ai_question(
            "How does SAP evaluate and audit algorithmic bias in automated human resources candidate screening within SAP SuccessFactors?",
            "Cover: Auditing hiring recommendation models across demographic groups, tracking disparate impact ratios, removing protected characteristics, and human HR review checkpoints.",
            "SAP Responsible AI in HCM"
        ),
        create_ai_question(
            "Describe how you optimize LLM API costs and latency when deploying conversational customer support features in SAP Commerce Cloud.",
            "Explain: Semantic caching of frequent customer inquiries, using small quantized language models for intent routing, and streaming responses to web clients.",
            "SAP Commerce Cloud AI Optimization"
        ),
        create_ai_question(
            "How do you implement continuous integration testing for AI-enabled enterprise workflows deployed on SAP AI Launchpad and AI Core?",
            "Detail: Automated pipeline testing model endpoints against validation test datasets, checking inference latency SLAs, and logging performance metrics in AI Launchpad.",
            "SAP AI Core & MLOps"
        ),
        create_ai_question(
            "How does SAP educate software engineering teams on Responsible AI and Generative AI principles across global SAP Labs development centers?",
            "Discuss: SAP AI ethics policy training, mandatory responsible AI reviews for product releases, hands-on SAP BTP AI hackathons, and internal developer certifications.",
            "SAP AI Education & Ethics"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically choose SAP Labs to launch and advance your software engineering career?",
            "Highlight: SAP's global dominance in enterprise application software (running 87% of the world's commerce), engineering rigor in in-memory computing, and human-centric workplace culture.",
            "SAP Brand Motivation"
        ),
        create_hr_question(
            "SAP software manages mission-critical global business workflows where software bugs can disrupt international supply chains. How do you approach software quality and craftsmanship?",
            "Emphasize: Zero compromise on automated testing, clean modular design, understanding long-term enterprise maintainability, and taking pride in resilient code.",
            "Software Craftsmanship & Enterprise Quality"
        ),
        create_hr_question(
            "SAP Labs operates world-class engineering campuses in Bangalore, Pune, Gurgaon, and Walldorf (Germany). Are you fully flexible with relocation and global project collaboration?",
            "Affirm: Complete willingness to relocate, enthusiasm to collaborate with colleagues across Germany, the US, and India, and adaptability to hybrid working models.",
            "Relocation & Global Collaboration"
        ),
        create_hr_question(
            "Tell me about a time you worked on a complex academic or professional software project under tight deadlines. How did you organize your priorities?",
            "Use STAR: Outline task decomposition, focusing on high-impact core features first, communicating transparently with leads, and delivering on schedule.",
            "Delivering Under Deadlines"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a different technical perspective during architecture design meetings?",
            "Showcase: Empathy, listening to understand their viewpoint, evaluating technical tradeoffs objectively with benchmarks, and building team consensus.",
            "Team Collaboration & Empathy"
        ),
        create_hr_question(
            "Describe a time you received critical constructive feedback on a software module or code submission. How did you act on that feedback?",
            "Demonstrate: Professional humility, analyzing recommendations constructively, adopting clean coding practices, and showing measurable improvement.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Where do you see yourself progressing at SAP over the next 3 to 5 years as an engineer?",
            "Connect: Growing from Associate Developer to Developer / Senior Developer, mastering SAP BTP and in-memory cloud architectures, and mentoring new campus hires.",
            "Career Aspirations"
        ),
        create_hr_question(
            "Tell me about a time you demonstrated curiosity by learning an advanced software concept or technology autonomously.",
            "Highlight: Self-starter mindset, reading technical papers, building prototypes, taking online certifications, and sharing learnings with peers.",
            "Continuous Learning & Curiosity"
        ),
        create_hr_question(
            "Describe a situation where you noticed an unassigned bug or defect in a system. How did you demonstrate personal initiative to resolve it?",
            "Show: Taking ownership, creating a reproduction test case, fixing the root cause, and adding automated tests to ensure lasting software reliability.",
            "Personal Initiative & Ownership"
        ),
        create_hr_question(
            "Do you have any questions for SAP Labs leadership regarding our cloud transformation, developer community, or research initiatives?",
            "Candidate asks thoughtful questions about SAP HANA innovation roadmap, open source contributions, or career mobility across SAP Labs.",
            "Candidate Curiosity"
        )
    ]

    return {
        "aptitude": {"Java Developer": apt_java, "Python Developer": apt_java, "Data Analyst": apt_java},
        "coding": {"Java Developer": code_java, "Python Developer": code_java, "Data Analyst": code_java},
        "technical": {"Java Developer": tech_java, "Python Developer": tech_java, "Data Analyst": tech_java},
        "ai_interview": {"Java Developer": ai_java, "Python Developer": ai_java, "Data Analyst": ai_java},
        "hr": {"Java Developer": hr_java, "Python Developer": hr_java, "Data Analyst": hr_java}
    }


# ==========================================
# 19. EY (Ernst & Young)
# ==========================================
def build_ey_catalog():
    apt_java = [
        create_aptitude_question(
            "In EY GDS Tech Quantitative: A corporate tax client has a gross taxable income of $750,000. The corporate tax rate is 20% on the first $500,000 and 25% on the remaining income. What is the total corporate tax payable?",
            ["$162,500", "$150,000", "$175,000", "$187,500"],
            "$162,500",
            "Tax on first $500,000 = 20% of 500,000 = $100,000. Remaining income = $250,000. Tax on remaining = 25% of 250,000 = $62,500. Total = $100,000 + $62,500 = $162,500.",
            "Easy", "EY Tax Math"
        ),
        create_aptitude_question(
            "In an EY financial audit sample, an auditor examines 450 corporate invoices and finds discrepancies in 18 invoices. What is the discrepancy rate percentage?",
            ["4.0%", "4.5%", "3.5%", "5.0%"],
            "4.0%",
            "Discrepancy rate = (18 / 450) * 100 = (2 / 50) * 100 = 4.0%.",
            "Easy", "EY Audit Statistics"
        ),
        create_aptitude_question(
            "Find the next number in the financial consulting sequence: 12, 25, 52, 107, ___?",
            ["218", "214", "220", "216"],
            "218",
            "Pattern: Each term is (previous * 2) + 1, +2, +3: 12*2+1=25, 25*2+2=52, 52*2+3=107. Next is 107*2 + 4 = 214 + 4 = 218.",
            "Easy", "EY Number Series"
        ),
        create_aptitude_question(
            "An enterprise cloud project budget of $360,000 is shared among 3 delivery teams in the ratio 4:5:3. What is the budget allocation for the team with the largest share?",
            ["$150,000", "$120,000", "$160,000", "$180,000"],
            "$150,000",
            "Total ratio parts = 4 + 5 + 3 = 12. Largest share (5 parts) = (5 / 12) * $360,000 = 5 * $30,000 = $150,000.",
            "Easy", "EY Proportional Math"
        ),
        create_aptitude_question(
            "In EY Verbal Ability: Select the word that means 'strict adherence to an ethical code or moral principles in business consulting':",
            ["Integrity", "Ambiguity", "Expediency", "Duplicity"],
            "Integrity",
            "'Integrity' is the quality of being honest and having strong moral principles; moral uprightness.",
            "Easy", "EY Professional Vocabulary"
        ),
        create_aptitude_question(
            "A software product depreciates in accounting value by 20% each year on diminishing balance. If purchased for $100,000, what is its book value at the end of 2 years?",
            ["$64,000", "$60,000", "$70,000", "$65,000"],
            "$64,000",
            "Year 1 value = 100,000 * 0.80 = $80,000. Year 2 value = 80,000 * 0.80 = $64,000.",
            "Easy", "EY Asset Depreciation Math"
        ),
        create_aptitude_question(
            "In how many ways can an EY audit team of 4 consultants be selected from a pool of 8 qualified professionals?",
            ["70 ways", "56 ways", "120 ways", "84 ways"],
            "70 ways",
            "Combinations: C(8,4) = (8 * 7 * 6 * 5) / (4 * 3 * 2 * 1) = 70 ways.",
            "Easy", "EY Combinatorics"
        ),
        create_aptitude_question(
            "A consulting consultant drives 120 km at 60 km/h and another 120 km at 40 km/h. What is the average speed for the entire journey?",
            ["48 km/h", "50 km/h", "45 km/h", "52 km/h"],
            "48 km/h",
            "Total distance = 240 km. Total time = 120/60 + 120/40 = 2 + 3 = 5 hours. Average speed = 240 / 5 = 48 km/h.",
            "Easy", "EY Speed & Time"
        ),
        create_aptitude_question(
            "In EY Syllogisms: Statements: 1. All financial statements are audited. 2. All audited documents are compliant. Conclusion: All financial statements are compliant.",
            ["The conclusion follows logically", "The conclusion does not follow", "Data is insufficient", "None follows"],
            "The conclusion follows logically",
            "Transitive deduction: Financial statements -> Audited -> Compliant. Therefore, All financial statements are compliant follows unconditionally.",
            "Easy", "EY Deductive Logic"
        ),
        create_aptitude_question(
            "A sum of money invested at simple interest yields $1,200 interest in 3 years at 5% per annum. What was the principal invested?",
            ["$8,000", "$6,000", "$7,500", "$10,000"],
            "$8,000",
            "SI = (P * R * T)/100 => 1,200 = (P * 5 * 3)/100 = 15P / 100 => P = (1,200 * 100) / 15 = $8,000.",
            "Easy", "EY Financial Interest Math"
        ),
        create_aptitude_question(
            "In an analytical test, 65% of candidates passed Section A, 70% passed Section B, and 15% failed both. What percentage of candidates passed BOTH sections?",
            ["50%", "45%", "55%", "60%"],
            "50%",
            "Total passed at least one = 100% - 15% = 85%. P(Both) = P(A) + P(B) - P(At least one) = 65% + 70% - 85% = 135% - 85% = 50%.",
            "Medium", "EY Set Theory"
        ),
        create_aptitude_question(
            "If an automated ETL process takes 45 minutes to process 90,000 records, what is the processing throughput in records per second?",
            ["33.33 records/sec", "25.00 records/sec", "50.00 records/sec", "20.00 records/sec"],
            "33.33 records/sec",
            "Time in seconds = 45 * 60 = 2,700 seconds. Throughput = 90,000 / 2,700 = 33.33 records/sec.",
            "Easy", "EY Systems Rate Math"
        ),
        create_aptitude_question(
            "In EY Direction Logic: An auditor walks 20 meters North, turns Right and walks 30 meters, turns Right and walks 20 meters. How far is the auditor from the starting point?",
            ["30 meters East", "20 meters East", "30 meters West", "50 meters North"],
            "30 meters East",
            "North and South cancel out (+20 - 20 = 0). Position is 30 meters directly East.",
            "Easy", "EY Direction Sense"
        ),
        create_aptitude_question(
            "What is the probability of selecting an odd number from the first 25 natural numbers (1 to 25)?",
            ["13/25", "12/25", "1/2", "14/25"],
            "13/25",
            "Odd numbers: 1, 3, 5, ..., 25 (13 numbers). Total numbers = 25. Probability = 13/25 = 52%.",
            "Easy", "EY Probability"
        ),
        create_aptitude_question(
            "A team of 6 analysts finishes an assurance report in 8 days. How many analysts are needed to finish the same report in 4 days?",
            ["12 analysts", "10 analysts", "8 analysts", "14 analysts"],
            "12 analysts",
            "Work = 6 * 8 = 48 analyst-days. Analysts needed for 4 days = 48 / 4 = 12 analysts.",
            "Easy", "EY Work Equation"
        )
    ]

    code_java = [
        create_coding_problem(
            "Financial Ledger Reconciliation (EY GDS Tech)",
            "Given two arrays of transactions ledgerA and ledgerB, return the symmetric difference: transaction amounts that exist in ledgerA or ledgerB but not in both.",
            "ledgerA = [100, 250, 400], ledgerB = [250, 300, 400]",
            "[100, 300]",
            "public class Solution {\n    public static List<Integer> reconcileLedgers(int[] a, int[] b) {\n        return new ArrayList<>();\n    }\n}",
            "def reconcile_ledgers(a: list[int], b: list[int]) -> list[int]:\n    pass",
            "def reconcile_audit_ledger_streams(stream_a, stream_b) -> list[int]:\n    pass",
            "Count frequencies using HashMaps; collect elements where count in A != count in B, or set symmetric difference in O(N+M).",
            "Easy", "Hash Table & Hashing", "O(N + M)", "O(N + M)"
        ),
        create_coding_problem(
            "Cleanse and Standardize Tax IDs",
            "Given an array of raw tax ID strings containing erratic formatting (hyphens, spaces, lowercase characters), clean and standardize each tax ID to uppercase alphanumeric without separators.",
            'rawIds = ["us-98-765-4321", " CA 123 456 ", "gb_999a"]',
            '["US987654321", "CA123456", "GB999A"]',
            "public class Solution {\n    public static List<String> cleanTaxIds(List<String> rawIds) {\n        return new ArrayList<>();\n    }\n}",
            "def clean_tax_ids(raw_ids: list[str]) -> list[str]:\n    pass",
            "def sanitize_corporate_tax_identifiers(id_series) -> list[str]:\n    pass",
            "Use regex replaceAll('[^a-zA-Z0-9]', '') and toUpperCase() on each string in O(Total Chars).",
            "Easy", "String Sanitization", "O(N * L)", "O(N * L)"
        ),
        create_coding_problem(
            "Sliding Window Financial Anomaly Detection",
            "Given a stream of daily transaction amounts and a threshold multiplier, flag any transaction that is greater than 3 times the rolling average of the previous k days.",
            "k = 3, stream = [100, 100, 100, 400]",
            "Index 3 (400 > 3 * 100)",
            "public class Solution {\n    public static List<Integer> detectAnomalies(int[] stream, int k) {\n        return new ArrayList<>();\n    }\n}",
            "def detect_anomalies(stream: list[int], k: int) -> list[int]:\n    pass",
            "def flag_outlier_audit_transactions(tx_df, k: int) -> list[int]:\n    pass",
            "Sliding window queue maintaining running sum of previous k elements; compare current element with 3 * (running_sum / k) in O(N).",
            "Medium", "Sliding Window & Queue", "O(N)", "O(K)"
        ),
        create_coding_problem(
            "Validate Credit Card Number (LUHN Algorithm)",
            "Given a string representing a credit card number, return true if the number is valid according to the Luhn checksum algorithm.",
            'card = "79927398713"',
            "true",
            "public class Solution {\n    public static boolean checkLuhn(String card) {\n        return false;\n    }\n}",
            "def check_luhn(card: str) -> bool:\n    pass",
            "def validate_card_checksum(card_series) -> bool:\n    pass",
            "Traverse digits from right to left; double every second digit; subtract 9 if > 9; sum all digits; valid if sum % 10 == 0.",
            "Easy", "Math & Luhn Algorithm", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Group Transactions by Vendor Category",
            "Given an array of transaction strings in the format 'Vendor:Category:Amount', aggregate and return the total spent per unique category.",
            'txs = ["Amazon:Cloud:500", "Azure:Cloud:700", "Staples:Office:100"]',
            '{"Cloud": 1200, "Office": 100}',
            "public class Solution {\n    public static Map<String, Integer> groupByCategory(List<String> txs) {\n        return new HashMap<>();\n    }\n}",
            "def group_by_category(txs: list[str]) -> dict[str, int]:\n    pass",
            "def aggregate_vendor_expenditures(spend_df) -> dict[str, int]:\n    pass",
            "Split string by ':'; accumulate amounts into a HashMap<String, Integer> in O(N).",
            "Easy", "Hash Map & Aggregation", "O(N)", "O(K)"
        ),
        create_coding_problem(
            "Reconcile Invoices with Rounding Tolerances",
            "Given expected payments and received payments, determine if each payment matches the expected amount within an allowable rounding tolerance of 0.05.",
            "expected = 100.00, received = 100.04",
            "true (|100.00 - 100.04| = 0.04 <= 0.05)",
            "public class Solution {\n    public static boolean isWithinTolerance(double exp, double recv, double tol) {\n        return false;\n    }\n}",
            "def is_within_tolerance(exp: float, recv: float, tol: float = 0.05) -> bool:\n    pass",
            "def verify_ledger_rounding_variance(ledger_df) -> bool:\n    pass",
            "Check Math.abs(exp - recv) <= tol with precision rounding.",
            "Easy", "Math & Precision", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "Detect Circular Transactions in Auditing (Graph Cycle)",
            "In forensic auditing, transactions between accounts can form circular wash trades (e.g. Account A -> B -> C -> A). Given V accounts and transaction edges, detect if any circular wash trade exists.",
            "V = 3, edges = [[0, 1], [1, 2], [2, 0]]",
            "true (Circular transaction loop detected)",
            "public class Solution {\n    public static boolean hasCircularTrade(int V, int[][] edges) {\n        return false;\n    }\n}",
            "def has_circular_trade(V: int, edges: list[list[int]]) -> bool:\n    pass",
            "def detect_wash_trading_cycle(trades_df) -> bool:\n    pass",
            "Cycle detection in directed graph using DFS with recursion stack or Kahn's topological sort in O(V + E).",
            "Medium", "Graph & Cycle Detection", "O(V + E)", "O(V)"
        ),
        create_coding_problem(
            "Calculate Compound Tax Brackets",
            "Given an annual taxable income and tax bracket thresholds with corresponding progressive rates, calculate the total progressive tax payable.",
            "income = 80000, brackets = [[0, 50000, 0.10], [50000, 100000, 0.20]]",
            "11000 (50000*0.10 + 30000*0.20 = 5000 + 6000)",
            "public class Solution {\n    public static double computeTax(double income, double[][] brackets) {\n        return 0.0;\n    }\n}",
            "def compute_tax(income: float, brackets: list[list[float]]) -> float:\n    pass",
            "def calculate_tiered_tax_obligation(income_df) -> float:\n    pass",
            "Iterate brackets; calculate taxable portion in current bracket; multiply by rate; accumulate in O(B).",
            "Easy", "Math & Progressive Brackets", "O(B)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "In EY regulatory audit and tax technology architectures, how do you enforce Database Transparent Data Encryption (TDE) and secure key rotation using Azure Key Vault / AWS KMS?",
            "TDE encrypts database files, logs, and backups at rest using AES-256 with a Database Encryption Key (DEK). The DEK is protected by a Customer Managed Key (CMK) in HSM/Key Vault, rotated annually with automated re-wrapping.",
            "EY Data Encryption & TDE", "Hard"
        ),
        create_technical_question(
            "How do you implement Automated ETL Pipeline Quality Gates and data validation checks (Great Expectations) to catch accounting ledger errors before data warehouse ingestion?",
            "Pre-ingestion quality gates assert constraints: non-null transaction IDs, debit/credit balance reconciliation, valid ISO currency codes, and referential integrity against master charts of accounts.",
            "EY ETL Architecture & Data Quality", "Hard"
        ),
        create_technical_question(
            "Explain SQL Window Functions in financial reporting: LEAD(), LAG(), and SUM() OVER (PARTITION BY account_id ORDER BY tx_date) for calculating running balances.",
            "LAG() accesses prior row values; LEAD() accesses subsequent row values without self-joins. SUM() OVER with ORDER BY calculates running cumulative balance per account across time partitions.",
            "EY SQL Analytical Functions", "Medium"
        ),
        create_technical_question(
            "How does Role-Based Access Control (RBAC) and Least Privilege enforcement protect confidential client audit workpapers in multi-tenant cloud portals?",
            "Users receive minimal permissions necessary for their assigned engagements. Token claims verify engagement-specific access; audit logs track every read, export, and modification with immutable timestamps.",
            "EY Enterprise Security & Access Control", "Medium"
        ),
        create_technical_question(
            "Explain the OWASP Top 10 Web Application Security risks (SQL Injection, Broken Authentication, Broken Access Control) and their practical mitigations in enterprise backends.",
            "Use PreparedStatements against SQLi; enforce MFA and secure cookie flags (HttpOnly, Secure, SameSite) for auth; validate object-level access permissions (IDOR prevention) on every endpoint.",
            "EY Web Application Security (OWASP)", "Medium"
        ),
        create_technical_question(
            "What is the difference between Immutable Audit Logging and standard application logging? How do cryptographic hashes guarantee tamper-evident audit trails?",
            "Standard logs can be overwritten or truncated by administrators. Immutable audit logging stores logs in WORM (Write Once, Read Many) storage with SHA-256 block hashing where altering any record invalidates the cryptographic chain.",
            "EY Tamper-Evident Audit Logging", "Hard"
        ),
        create_technical_question(
            "Explain Data Lakehouse architectures (Databricks Delta Lake, Snowflake) and how ACID transaction guarantees allow concurrent audit queries and data ingestion.",
            "Delta Lake maintains a transaction log (_delta_log) enabling ACID transactions, time-travel queries to inspect historical data state as of a past audit date, and schema enforcement.",
            "EY Data Lakehouse & Delta Lake", "Hard"
        ),
        create_technical_question(
            "How do you configure Mutual TLS (mTLS) and API Gateway authentication to securely transmit sensitive corporate tax documents between banking clients and EY services?",
            "Both client and API gateway exchange and verify X.509 certificates during TLS handshake; the API gateway extracts client certificate metadata and validates against approved client CA registries.",
            "EY Secure API Transport & mTLS", "Medium"
        ),
        create_technical_question(
            "What techniques are used for Data Anonymization and Pseudonymization (k-anonymity, differential privacy) when testing advisory software with production client data?",
            "Pseudonymization replaces identifiers with synthetic keys. k-anonymity generalizes attributes so each record is indistinguishable from at least k-1 others. Differential privacy adds controlled noise.",
            "EY Data Privacy & Compliance", "Hard"
        ),
        create_technical_question(
            "Explain Disaster Recovery RTO (Recovery Time Objective) and RTO planning for cloud-based financial assurance platforms.",
            "RTO specifies acceptable downtime; RPO specifies maximum allowable data loss duration. For financial assurance, geo-redundant database backups and automated Infrastructure-as-Code achieve RTO < 1 hr, RPO < 5 mins.",
            "EY Business Continuity Planning", "Medium"
        ),
        create_technical_question(
            "How do Python libraries (Pandas, PyArrow, Polars) accelerate big data tax calculation and audit reconciliation compared to row-by-row iteration?",
            "Vectorized operations in Pandas/Polars compile operations to C-level SIMD instructions, processing contiguous memory arrays 50-100x faster than Python for-loops while eliminating memory overhead.",
            "EY Big Data & Python Analytics", "Medium"
        ),
        create_technical_question(
            "What are Database Isolation Levels and how does Snapshot Isolation prevent Non-Repeatable Reads without acquiring read locks in PostgreSQL?",
            "Snapshot isolation reads data from a transaction snapshot taken at query start using MVCC. Writers modify separate row versions, allowing long audit queries to run without blocking concurrent financial writes.",
            "EY PostgreSQL & MVCC", "Medium"
        ),
        create_technical_question(
            "How do you implement centralized Security Information and Event Management (SIEM) integration using Splunk / Azure Sentinel for real-time security alerting?",
            "Forward syslog and container events via fluentbit/Logstash to Sentinel/Splunk. Configure KQL / SPL detection rules alerting on multiple failed logins followed by administrative privilege escalations.",
            "EY SIEM & Security Monitoring", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Restful Web Services and GraphQL in enterprise client reporting portals.",
            "REST returns fixed endpoint data schemas. GraphQL allows client dashboards to query exact required fields and nested entities in a single HTTP request, eliminating over-fetching on mobile audit tablets.",
            "EY Modern API Architecture", "Easy"
        ),
        create_technical_question(
            "How does Docker containerization with non-root user execution protect cloud audit platforms from container breakout vulnerabilities?",
            "Running containers as non-root (USER 1001) prevents exploited container processes from inheriting root capabilities (CAP_SYS_ADMIN), neutralizing privilege escalation attacks against the host Linux kernel.",
            "EY Container Security", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain how EY Canvas and EY Fabric utilize Artificial Intelligence and automated data ingestion to streamline global financial assurance audits.",
            "Discuss: EY Canvas cloud audit platform connecting global teams, AI-assisted document parsing, automated journal entry testing, and anomaly detection in financial ledgers.",
            "EY Canvas & AI Audit Innovation"
        ),
        create_ai_question(
            "How do you architect an automated invoice and tax document processing pipeline using Generative AI and OCR for EY client tax technology services?",
            "Detail: Computer vision parsing layout, prompt engineering extracting tax IDs and line items into JSON, validation against ERP tax rules, and exception routing for tax specialists.",
            "EY Intelligent Document AI"
        ),
        create_ai_question(
            "How do you implement Retrieval-Augmented Generation (RAG) over global tax treaties and regulatory audit codes with strict citation grounding?",
            "Architecture: Chunking international tax treaty PDFs, vector embedding in Azure AI Search, hybrid keyword + semantic search, and enforcing exact paragraph citations.",
            "EY Tax Regulatory RAG"
        ),
        create_ai_question(
            "What strategies ensure zero hallucinations when using LLMs for generating automated audit finding memos and client compliance risk summaries?",
            "Discuss: Constraining generation to strictly retrieved audit workpaper chunks, temperature=0.0, deterministic fact verification, and mandatory senior auditor sign-off.",
            "EY Hallucination Prevention in Auditing"
        ),
        create_ai_question(
            "How do you design a real-time corporate tax fraud anomaly detection model using unsupervised machine learning (Isolation Forests, Autoencoders)?",
            "Detail: Feature engineering on invoice amounts, supplier frequency, and round-number payments; scoring anomaly probability; flagging suspicious transactions for forensic audit.",
            "EY AI Forensic Tax Anomaly Detection"
        ),
        create_ai_question(
            "How does EY evaluate AI ethics, bias, and regulatory compliance under the EU AI Act for algorithmic models deployed across client organizations?",
            "Cover: High-risk AI categorization, bias testing across demographic subgroups, model transparency documentation, and establishing human-in-the-loop governance.",
            "EY AI Ethics & EU AI Act"
        ),
        create_ai_question(
            "Describe how Generative AI assists forensic accountants in detecting circular wash trading and corporate bribery schemes from email communication and ledger logs.",
            "Detail: NLP sentiment and keyword analysis on email communications correlated with sudden offshore wire transfers and shell company invoice records.",
            "EY Forensic AI & Fraud Investigation"
        ),
        create_ai_question(
            "How do you ensure data confidentiality and multi-tenant security when hosting LLM-based advisory solutions for competing Fortune 500 clients?",
            "Explain: Isolated tenant databases, dedicated customer-managed encryption keys, air-gapped model inference, and strict zero data retention agreements.",
            "EY Multi-Tenant AI Security"
        ),
        create_ai_question(
            "How do you evaluate and monitor the accuracy and drift of automated document classification models across multi-year audit engagements?",
            "Discuss: Tracking classification precision/recall against sampled manual auditor verifications, monitoring data drift with PSI, and retraining pipelines annually.",
            "EY MLOps & Model Governance"
        ),
        create_ai_question(
            "How does EY upskill employees in Artificial Intelligence through the EY Badges and EY Tech MBA learning initiatives?",
            "Discuss: EY Badges digital credentials in AI, Data, and Cloud; hands-on hackathons; prompt engineering bootcamps; and the fully-accredited EY Tech MBA program.",
            "EY AI Upskilling & Badges"
        )
    ]

    hr_java = [
        create_hr_question(
            "EY's global purpose is 'Building a better working world'. How do your personal professional principles align with this mission?",
            "Provide a concrete academic or project example demonstrating integrity, building trust with peers or stakeholders, and making a positive impact on your community.",
            "EY Purpose: Building a Better Working World"
        ),
        create_hr_question(
            "Why do you specifically choose EY GDS (Global Delivery Services) to begin and accelerate your technology consulting career?",
            "Highlight: EY's global prestige, premier assurance and tax consulting practice, multidisciplinary project exposure, and world-class continuous learning programs.",
            "EY Brand Motivation"
        ),
        create_hr_question(
            "EY operates major technology and delivery centers across India (Bangalore, Gurgaon, Hyderabad, Chennai, Kolkata, Kochi, Pune). Are you fully flexible with relocation?",
            "Affirm: Complete willingness to relocate, readiness to support global team time zones, and enthusiasm for collaborating across diverse international offices.",
            "Relocation & Project Flexibility"
        ),
        create_hr_question(
            "Auditing and consulting engagements often experience intense busy seasons with strict compliance deadlines. How do you maintain composure and high code quality under pressure?",
            "Use STAR: Outline disciplined time management, prioritizing critical deliverables, open communication with leads, and maintaining high software quality standards.",
            "Delivering Under Busy Seasons"
        ),
        create_hr_question(
            "Describe a situation where you discovered an ethical dilemma, data discrepancy, or software flaw in a project. How did you handle reporting it?",
            "Emphasize: Uncompromising integrity, honest communication with the project lead, never hiding flaws, and presenting constructive solutions.",
            "Professional Integrity & Ethics"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a different background or communication style in a global delivery team?",
            "Showcase: Empathy, active listening, respecting different cultural perspectives, and working collaboratively toward common project goals.",
            "Global Collaboration & Inclusion"
        ),
        create_hr_question(
            "Tell me about a time you received constructive criticism on your project work. What actions did you take to elevate your performance?",
            "Demonstrate: Professional humility, analyzing feedback objectively, seeking mentoring, and showing measurable improvement in subsequent sprints.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Where do you see yourself progressing at EY over the next 3 to 5 years as an engineer?",
            "Connect: Growing from Associate / Software Engineer to Senior Software Engineer / Consultant, earning EY Badges, mastering cloud architectures, and mentoring juniors.",
            "Career Aspirations & Growth"
        ),
        create_hr_question(
            "Describe a time you demonstrated exceptional curiosity by learning a new programming language or framework to solve a challenging problem.",
            "Highlight: Self-driven learning, reading technical documentation, building prototypes, taking certifications, and sharing learnings with teammates.",
            "Curiosity & Continuous Learning"
        ),
        create_hr_question(
            "Do you have any questions for EY leadership regarding our technology practices, EY Badges program, or corporate culture?",
            "Candidate asks about EY Canvas innovation, EY Badges curriculum, or opportunities to contribute to global client transformation projects.",
            "Candidate Curiosity"
        )
    ]

    return {
        "aptitude": {"Java Developer": apt_java, "Python Developer": apt_java, "Data Analyst": apt_java},
        "coding": {"Java Developer": code_java, "Python Developer": code_java, "Data Analyst": code_java},
        "technical": {"Java Developer": tech_java, "Python Developer": tech_java, "Data Analyst": tech_java},
        "ai_interview": {"Java Developer": ai_java, "Python Developer": ai_java, "Data Analyst": ai_java},
        "hr": {"Java Developer": hr_java, "Python Developer": hr_java, "Data Analyst": hr_java}
    }


# ==========================================
# 20. PWC (PricewaterhouseCoopers)
# ==========================================
def build_pwc_catalog():
    apt_java = [
        create_aptitude_question(
            "In PwC Acceleration Centers Quantitative: A private equity portfolio investment of $2.4 Million appreciates at a compound annual growth rate (CAGR) of 10% for 2 years. What is the total portfolio value at the end of 2 years?",
            ["$2.904 Million", "$2.880 Million", "$3.000 Million", "$2.750 Million"],
            "$2.904 Million",
            "Value = Principal * (1 + r)^n = 2.4M * (1.10)^2 = 2.4M * 1.21 = $2.904 Million.",
            "Easy", "PwC Financial CAGR Math"
        ),
        create_aptitude_question(
            "A consulting team at PwC analyses client invoices. If 12 consultants can review 720 invoices in 6 days, how many invoices can 8 consultants review in 5 days at the same pace?",
            ["400 invoices", "360 invoices", "480 invoices", "420 invoices"],
            "400 invoices",
            "Review rate = 720 / (12 * 6) = 10 invoices/consultant-day. 8 consultants for 5 days: total = 8 * 5 * 10 = 400 invoices.",
            "Easy", "PwC Work & Productivity"
        ),
        create_aptitude_question(
            "Find the next number in the PwC business forecasting sequence: 15, 31, 63, 127, ___?",
            ["255", "250", "254", "260"],
            "255",
            "Pattern: Each term is (previous * 2) + 1: 15*2+1=31, 31*2+1=63, 63*2+1=127. Next is 127*2+1 = 255.",
            "Easy", "PwC Number Series"
        ),
        create_aptitude_question(
            "A corporate client purchases an enterprise advisory subscription for $80,000 with an 8% early sign-up discount and a 5% volume rebate. What is the final net price?",
            ["$69,920", "$70,000", "$72,000", "$68,500"],
            "$69,920",
            "After 8% discount: 80,000 * 0.92 = $73,600. After additional 5%: 73,600 * 0.95 = $69,920.",
            "Medium", "PwC Commercial Math"
        ),
        create_aptitude_question(
            "In PwC Logical Sequence: Five financial filings (A, B, C, D, E) are submitted in sequence. B is submitted after A but before C. D is submitted before A. E is submitted after C. Which filing was submitted third?",
            ["B", "A", "C", "D"],
            "B",
            "Ordering: D is before A; A is before B; B is before C; C is before E. Sequence: D -> A -> B -> C -> E. Third filing is B.",
            "Easy", "PwC Sequence Logic"
        ),
        create_aptitude_question(
            "In how many ways can 5 advisory project deliverables be allocated among 5 senior managers with exactly one deliverable per manager?",
            ["120 ways", "60 ways", "24 ways", "720 ways"],
            "120 ways",
            "Permutations of 5 items = 5! = 5 * 4 * 3 * 2 * 1 = 120 ways.",
            "Easy", "PwC Combinatorics"
        ),
        create_aptitude_question(
            "A corporate merger saves $180,000 in operational costs in year 1 and $240,000 in year 2. What is the percentage increase in savings from year 1 to year 2?",
            ["33.33%", "25.00%", "40.00%", "30.00%"],
            "33.33%",
            "Increase = (240,000 - 180,000) / 180,000 = 60,000 / 180,000 = 1/3 = 33.33%.",
            "Easy", "PwC Percentage"
        ),
        create_aptitude_question(
            "In PwC Verbal Ability: Choose the word that best completes the sentence: 'The financial advisory report was praised for its ______ analysis and rigorous audit backing.'",
            ["meticulous", "cursory", "superficial", "equivocal"],
            "meticulous",
            "'Meticulous' means showing great attention to detail; very careful and precise, fitting financial audit standards.",
            "Easy", "PwC English Ability"
        ),
        create_aptitude_question(
            "A software server rack consumes 3.5 kWh of power every hour. How many kilowatt-hours does it consume in a continuous 30-day billing cycle (720 hours)?",
            ["2,520 kWh", "2,400 kWh", "2,600 kWh", "2,800 kWh"],
            "2,520 kWh",
            "Total = 3.5 * 720 = 2,520 kWh.",
            "Easy", "PwC Utility & Cost Math"
        ),
        create_aptitude_question(
            "Two corporate offices are 360 km apart. Two courier vehicles start towards each other simultaneously at 50 km/h and 70 km/h. How many hours will they take to meet?",
            ["3.0 hours", "3.5 hours", "4.0 hours", "2.5 hours"],
            "3.0 hours",
            "Relative speed = 50 + 70 = 120 km/h. Time = Distance / Speed = 360 / 120 = 3.0 hours.",
            "Easy", "PwC Speed & Distance"
        ),
        create_aptitude_question(
            "What is the compound interest on a corporate deposit of $50,000 for 2 years at 6% per annum, compounded annually?",
            ["$6,180", "$6,000", "$6,250", "$5,800"],
            "$6,180",
            "Amount = 50,000 * (1.06)^2 = 50,000 * 1.1236 = $56,180. CI = 56,180 - 50,000 = $6,180.",
            "Easy", "PwC Financial Math"
        ),
        create_aptitude_question(
            "In a financial sample of 120 audited transactions, the ratio of domestic to international transactions is 5:3. How many international transactions were audited?",
            ["45", "75", "40", "50"],
            "45",
            "Total ratio parts = 5 + 3 = 8. International share = (3 / 8) * 120 = 3 * 15 = 45 transactions.",
            "Easy", "PwC Ratio & Proportion"
        ),
        create_aptitude_question(
            "In PwC Deductive Logic: Statements: 1. All assets have value. 2. Some values are volatile. Conclusion: Some assets have volatile value.",
            ["The conclusion does not follow definitively", "The conclusion follows definitively", "Data is insufficient", "None follows"],
            "The conclusion does not follow definitively",
            "The middle term 'value' is undistributed; some values being volatile does not guarantee that those volatile values belong to assets.",
            "Medium", "PwC Deductive Logic"
        ),
        create_aptitude_question(
            "An enterprise server hard drive of size 2 Terabytes is 85% full. How many Gigabytes of free disk space remain?",
            ["300 GB", "250 GB", "350 GB", "200 GB"],
            "300 GB",
            "2 TB = 2,000 GB. Free space = 15% of 2,000 GB = 0.15 * 2,000 = 300 GB.",
            "Easy", "PwC Storage Math"
        ),
        create_aptitude_question(
            "What is the probability of rolling a sum of 8 with two fair six-sided dice?",
            ["5/36", "6/36", "4/36", "7/36"],
            "5/36",
            "Pairs summing to 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5 pairs. Total outcomes = 36. Probability = 5/36.",
            "Easy", "PwC Probability"
        )
    ]

    code_java = [
        create_coding_problem(
            "Calculate Rolling 30-Day Revenue (PwC Acceleration Centers)",
            "Given a stream of daily revenue figures and an integer window k=30, calculate the rolling sum of revenue for every day starting from day k in O(N) time.",
            "k = 3, revenue = [10, 20, 30, 40, 50]",
            "[60, 90, 120] (60=10+20+30, 90=20+30+40, 120=30+40+50)",
            "public class Solution {\n    public static List<Integer> rollingSum(int[] revenue, int k) {\n        return new ArrayList<>();\n    }\n}",
            "def rolling_sum(revenue: list[int], k: int) -> list[int]:\n    pass",
            "def compute_30_day_revenue_trail(rev_series, k: int = 30) -> list[int]:\n    pass",
            "Sliding window of length k: Add next day's revenue, subtract evicted oldest day's revenue in O(1) per step.",
            "Easy", "Sliding Window", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Filter Audited vs Unaudited Entities",
            "Given an array of entity records in format 'EntityID:AuditStatus', return all EntityIDs where AuditStatus is 'PENDING' in sorted order.",
            'records = ["E101:COMPLETED", "E102:PENDING", "E103:PENDING", "E104:COMPLETED"]',
            '["E102", "E103"]',
            "public class Solution {\n    public static List<String> filterPending(List<String> records) {\n        return new ArrayList<>();\n    }\n}",
            "def filter_pending(records: list[str]) -> list[str]:\n    pass",
            "def filter_unaudited_corporate_filings(filings_df) -> list[str]:\n    pass",
            "Parse each record splitting on ':'; filter records matching 'PENDING'; sort resulting IDs in O(N log N).",
            "Easy", "String Parsing & Filtering", "O(N log N)", "O(N)"
        ),
        create_coding_problem(
            "Find Longest Gap Between Fiscal Filings",
            "Given a sorted array of positive integers representing days of fiscal filings throughout the year, return the maximum gap (in days) between any two consecutive filings.",
            "filings = [10, 45, 120, 300]",
            "180 (300 - 120)",
            "public class Solution {\n    public static int maxGap(int[] filings) {\n        return 0;\n    }\n}",
            "def max_gap(filings: list[int]) -> int:\n    pass",
            "def compute_max_filing_dormancy(dates_series) -> int:\n    pass",
            "Single pass comparing filings[i] - filings[i-1]; maintain and return max_difference in O(N).",
            "Easy", "Array Scanning", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Matrix Asset Depreciation Table",
            "Given an array of asset purchase values and a annual depreciation rate r, compute the depreciated asset values for each asset over years 1 to Y in an M x Y matrix.",
            "values = [10000, 20000], r = 0.10, Y = 2",
            "[[9000.0, 8100.0], [18000.0, 16200.0]]",
            "public class Solution {\n    public static double[][] computeDepreciation(double[] values, double r, int Y) {\n        return new double[0][0];\n    }\n}",
            "def compute_depreciation(values: list[float], r: float, Y: int) -> list[list[float]]:\n    pass",
            "def generate_asset_amortization_schedule(assets_df, r: float, Y: int):\n    pass",
            "Nested loop: For each asset, multiply by (1 - r) iteratively across Y years in O(M * Y).",
            "Easy", "Matrix & Finance", "O(M * Y)", "O(M * Y)"
        ),
        create_coding_problem(
            "String Fuzzy Match for Client Entity Names",
            "Given two company names, return the Levenshtein edit distance: the minimum number of single-character edits (insertions, deletions, or substitutions) required to change name1 into name2.",
            'name1 = "Pricewaterhouse", name2 = "Pricewaterhuose"',
            "2 (Transposition/substitutions)",
            "public class Solution {\n    public int minDistance(String word1, String word2) {\n        return 0;\n    }\n}",
            "def min_distance(word1: str, word2: str) -> int:\n    pass",
            "def compute_entity_name_similarity(name_a: str, name_b: str) -> int:\n    pass",
            "2D Dynamic Programming (Edit Distance): dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (w1[i] == w2[j] ? 0 : 1)).",
            "Medium", "Dynamic Programming & Strings", "O(M * N)", "O(M * N)"
        ),
        create_coding_problem(
            "Normalize Currency Code Exchange Table",
            "Given an array of exchange rates in format 'USD:EUR:0.92', return the direct conversion rate between any requested base and target currency using a graph BFS.",
            'rates = ["USD:EUR:0.92", "EUR:GBP:0.85"], base = "USD", target = "GBP"',
            "0.782 (0.92 * 0.85)",
            "public class Solution {\n    public static double convertCurrency(List<String> rates, String base, String target) {\n        return -1.0;\n    }\n}",
            "def convert_currency(rates: list[str], base: str, target: str) -> float:\n    pass",
            "def resolve_fx_arbitrage_rate(fx_df, base: str, target: str) -> float:\n    pass",
            "Build directed weighted graph where edge (A, B) has rate r and (B, A) has 1/r; find path with BFS multiplying weights.",
            "Medium", "Graph & BFS", "O(V + E)", "O(V)"
        ),
        create_coding_problem(
            "Detect Sudden Spikes in Expense Stream",
            "Given an array of daily expense records, return the indices of all days where the expense is at least double the average of all preceding days (minimum 3 preceding days).",
            "expenses = [100, 100, 100, 250, 100]",
            "[3] (Day 3 expense 250 >= 2 * 100)",
            "public class Solution {\n    public static List<Integer> detectSpikes(int[] expenses) {\n        return new ArrayList<>();\n    }\n}",
            "def detect_spikes(expenses: list[int]) -> list[int]:\n    pass",
            "def flag_budget_overrun_anomalies(expense_series) -> list[int]:\n    pass",
            "Maintain running sum and count; for i >= 3, compare expense[i] with 2 * (running_sum / i) in O(N).",
            "Easy", "Array & Running Average", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Minimum Coins for Exact Change with Transaction Fee",
            "Given coin denominations coins, target amount, and a flat transaction fee, return the minimum number of coins to form target or -1 if impossible.",
            "coins = [1, 2, 5], amount = 11",
            "3 (5 + 5 + 1)",
            "public class Solution {\n    public int coinChange(int[] coins, int amount) {\n        return -1;\n    }\n}",
            "def coin_change(coins: list[int], amount: int) -> int:\n    pass",
            "def optimize_settlement_units(coins: list[int], amount: int) -> int:\n    pass",
            "1D DP array initialized to amount + 1. dp[i] = min(dp[i], dp[i - c] + 1) for each coin c.",
            "Medium", "Dynamic Programming", "O(N * Amount)", "O(Amount)"
        )
    ]

    tech_java = [
        create_technical_question(
            "In PwC Acceleration Centers, how do you architect enterprise Financial Risk Analytics data pipelines handling terabytes of client transactional data?",
            "Data pipelines ingest raw transaction logs via Apache Kafka; transform and aggregate using Apache Spark on cloud clusters; write to a Snowflake/Databricks lakehouse with automated schema validation and encryption.",
            "PwC Financial Risk Architecture", "Hard"
        ),
        create_technical_question(
            "Explain Data Lineage and Governance in modern data warehouses (Snowflake, BigQuery). How do metadata graphs satisfy regulatory BCBS 239 risk data aggregation standards?",
            "Data lineage tracks the end-to-end lifecycle of financial data from source ERPs through transformations to executive dashboards, proving provenance, transformation accuracy, and regulatory auditability.",
            "PwC Data Lineage & BCBS 239", "Hard"
        ),
        create_technical_question(
            "How do you implement FinOps (Cloud Financial Management) principles to optimize cloud computing costs across multi-account AWS and Azure enterprise deployments?",
            "Tag resources with cost-center metadata; identify idle and unattached EBS/disk volumes; purchase Reserved Instances and Savings Plans for baseline workloads; scale dev/test environments to zero off-hours.",
            "PwC FinOps & Cloud Cost Optimization", "Medium"
        ),
        create_technical_question(
            "Explain Secure File Transfer Protocol (SFTP) and AS2 (Applicability Statement 2) integration architectures for exchanging sensitive financial and tax files.",
            "AS2 provides point-to-point secure file transmission over HTTP/S with digital certificates for encryption, digital signatures for non-repudiation, and Message Disposition Notifications (MDN) as receipts.",
            "PwC Secure File Transfer & AS2", "Medium"
        ),
        create_technical_question(
            "What is Relational Data Modeling for complex financial accounting systems: General Ledger (GL), Subledger, and Chart of Accounts (COA) entity relationships?",
            "Chart of Accounts defines hierarchical account structures. General Ledger stores double-entry journal lines (debit/credit balancing). Subledgers maintain granular vendor/customer transactional details linked via foreign keys.",
            "PwC Accounting Data Modeling", "Medium"
        ),
        create_technical_question(
            "How do you optimize SQL query execution on multi-million row transactional tables using clustered vs non-clustered indexes and table partitioning?",
            "Clustered index physically sorts table rows on disk (ideal for date/primary key ranges). Non-clustered indexes provide B-Tree lookup pointers. Partitioning by fiscal quarter isolates scans to relevant timeframes.",
            "PwC SQL Optimization", "Medium"
        ),
        create_technical_question(
            "Explain Database Integrity Constraints: Primary Key, Foreign Key with ON DELETE CASCADE vs RESTRICT, and CHECK constraints in financial schema design.",
            "Primary keys enforce entity uniqueness; Foreign keys enforce referential integrity. In financial ledgers, ON DELETE RESTRICT is mandatory to prevent accidental deletion of parent accounts with posted transactions.",
            "PwC Database Integrity", "Easy"
        ),
        create_technical_question(
            "What are the Five Dimensions of the PwC Professional leadership framework, and how do they apply to software engineering delivery (Whole Leadership, Business Acumen, etc.)?",
            "Whole Leadership (leading self and others), Business Acumen (aligning code with business impact), Technical and Digital (engineering excellence), Global and Inclusive (collaborating across borders), Relationships (building trust).",
            "PwC Professional Framework", "Medium"
        ),
        create_technical_question(
            "How do you implement API Security Vulnerability Assessments (OWASP API Security Top 10: BOLA, Broken Authentication, Excessive Data Exposure)?",
            "BOLA (Broken Object Level Authorization) is mitigated by validating that the authenticated user owns the requested record ID on every API call. Strip sensitive internal fields before serializing DTO responses.",
            "PwC API Security & OWASP", "Medium"
        ),
        create_technical_question(
            "Explain Zero Trust Architecture in consulting client environments: Micro-segmentation, identity-aware proxies, and continuous device health verification.",
            "Never trust, always verify. Every request is authenticated and authorized based on user identity, device posture, and context, regardless of whether the request originates from within the corporate office network.",
            "PwC Zero Trust Security", "Medium"
        ),
        create_technical_question(
            "How does Apache Kafka event streaming power real-time fraud alert notifications across distributed banking client integrations?",
            "Transaction events publish to Kafka topics; real-time streaming analytics engines (Flink/Spark Streaming) evaluate fraud rules against sliding time-windows and push immediate alerts to messaging queues.",
            "PwC Real-Time Fraud Streaming", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Symmetric Encryption (AES-GCM) and Asymmetric Encryption (RSA-4096) in financial file exchange.",
            "Symmetric encryption uses one shared secret key for high-speed bulk data encryption. Asymmetric encryption uses public/private key pairs for secure key exchange, digital signatures, and identity verification.",
            "PwC Cryptography & Encryption", "Easy"
        ),
        create_technical_question(
            "What are Docker Container Security best practices: Minimizing image layers, scanning for CVEs with Trivy, and enforcing read-only filesystems?",
            "Multi-stage Docker builds reduce attack surfaces; Trivy scans image packages for known CVEs; running containers with read-only root filesystems prevents malware from downloading and executing scripts.",
            "PwC Container Security", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Synchronous and Asynchronous REST API designs for long-running financial simulation calculations.",
            "Synchronous calls time out on long tasks. Asynchronous API returns 202 Accepted with a Location header (task status URL); client polls or receives a webhook callback when simulation completes.",
            "PwC Asynchronous API Architecture", "Medium"
        ),
        create_technical_question(
            "How do you design an automated regression testing framework for financial calculations using JUnit 5, AssertJ, and parameterized test suites?",
            "Create golden test datasets with known financial outputs; execute parameterized tests verifying calculations to four decimal places; assert that boundary cases (zero, negative, overflow) throw expected exceptions.",
            "PwC Automated Testing & Quality", "Easy"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain how the PwC AI Factory and 'The New Equation' strategy leverage Generative AI to transform financial audit, tax compliance, and advisory services.",
            "Discuss: The New Equation strategy building trust and delivering sustained outcomes, PwC's $1B AI investment, partnership with OpenAI and Microsoft, and automated compliance tools.",
            "PwC AI Factory & The New Equation"
        ),
        create_ai_question(
            "How do you architect an enterprise RAG application using Azure OpenAI for forensic financial analysts to query thousands of confidential client audit workpapers?",
            "Architecture: Chunking financial documents with table-aware parsers, dense vector embeddings in Azure AI Search, hybrid search with semantic re-ranking, and strict citation grounding.",
            "PwC Audit & Forensic RAG"
        ),
        create_ai_question(
            "Describe how Generative AI models are utilized to automate complex commercial contract review and extract financial liability clauses during M&A due diligence.",
            "Detail: PDF OCR extraction, prompting specialized LLMs with legal tax rubrics, structured extraction of indemnities and warranties into tabular summaries, and attorney sign-off.",
            "PwC M&A Contract Review AI"
        ),
        create_ai_question(
            "What techniques ensure zero hallucinations when using LLMs for generating automated executive financial risk briefing reports at PwC?",
            "Discuss: Grounding prompts strictly in verified financial ledgers, temperature=0, structured JSON output schemas, deterministic calculations, and partner sign-off.",
            "PwC Hallucination Mitigation"
        ),
        create_ai_question(
            "How do you establish a Responsible AI Auditing Framework to certify that client AI algorithms are fair, explainable, and compliant with global regulations?",
            "Cover: Testing for demographic parity, calculating disparate impact ratios, evaluating SHAP feature importance for explainability, and verifying data provenance.",
            "PwC Responsible AI Framework"
        ),
        create_ai_question(
            "How do you design a real-time corporate expense anomaly detection model using unsupervised machine learning to detect kickbacks and bribery?",
            "Detail: Graph analysis connecting employee expense reports with vendor bank accounts, anomaly scoring using isolation forests, and automated flagging for forensic auditors.",
            "PwC Forensic Anomaly AI"
        ),
        create_ai_question(
            "How do you ensure data confidentiality and prevent corporate IP contamination when developers utilize AI coding assistants in PwC Acceleration Centers?",
            "Explain: Dedicated enterprise licenses with zero model training agreements, automated secret scanning in pre-commit hooks, and air-gapped corporate development environments.",
            "PwC Developer AI Policy & Security"
        ),
        create_ai_question(
            "Describe how you fine-tune open source models (e.g. Llama 3, Mistral) on specialized accounting and tax terminology using Parameter-Efficient Fine-Tuning (PEFT/LoRA).",
            "Detail: Curating domain instruction datasets, freezing base weights, training low-rank adapter matrices on GPU clusters, and evaluating accuracy on tax benchmark exams.",
            "PwC Model Fine-Tuning & Tax AI"
        ),
        create_ai_question(
            "How do you evaluate and monitor the accuracy and drift of automated document classification models across multi-year assurance engagements?",
            "Discuss: Tracking classification precision/recall against sampled manual auditor verifications, monitoring data drift with PSI, and retraining pipelines annually.",
            "PwC MLOps & Model Governance"
        ),
        create_ai_question(
            "How does PwC empower employees to build AI fluency across all business lines through the Digital Lab and AI upskilling initiatives?",
            "Discuss: PwC Digital Lab asset marketplace, hands-on generative AI bootcamps, prompt engineering certifications, and client project innovation challenges.",
            "PwC AI Upskilling & Culture"
        )
    ]

    hr_java = [
        create_hr_question(
            "PwC's global strategy is 'The New Equation'—helping clients build trust and deliver sustained outcomes. How do your personal professional values align with this mission?",
            "Provide a personal example showcasing building trust with team members or stakeholders, acting with integrity, and delivering high-quality, sustained results.",
            "PwC The New Equation & Trust"
        ),
        create_hr_question(
            "Why do you specifically choose PwC Acceleration Centers to begin and advance your software engineering and technology consulting career?",
            "Highlight: PwC's prestigious Big 4 brand, multidisciplinary exposure across Fortune 500 financial and cloud transformations, and focus on human-led, tech-powered innovation.",
            "PwC Brand Motivation"
        ),
        create_hr_question(
            "PwC operates major Acceleration Centers across India (Bangalore, Kolkata, Hyderabad, Mumbai, Gurgaon). Are you fully flexible with relocation and global project hours?",
            "Affirm: Complete willingness to relocate, readiness to support global project time zones, and adaptability to hybrid workplace practices.",
            "Relocation & Global Collaboration"
        ),
        create_hr_question(
            "The PwC Professional framework emphasizes 'Whole Leadership'. Tell me about a time you took personal leadership on a software project without being formally assigned as lead.",
            "Use STAR: Outline taking initiative, organizing tasks, unblocking team members, communicating with stakeholders, and delivering a successful outcome.",
            "PwC Dimension: Whole Leadership"
        ),
        create_hr_question(
            "Tell me about a challenging project deadline where you faced conflicting priorities and tight delivery schedules. How did you manage your workload?",
            "Showcase: Structured prioritization, transparent communication with managers, focusing on high-impact deliverables, and maintaining high software quality.",
            "Delivering Under Deadlines"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a different background or communication style in an international consulting squad?",
            "Emphasize: Empathy, active listening, respecting different cultural perspectives, and fostering an inclusive and supportive team environment.",
            "PwC Dimension: Global and Inclusive"
        ),
        create_hr_question(
            "Describe a time you received constructive feedback on your code or analytical report. What specific steps did you take to elevate your performance standard?",
            "Demonstrate: Professional humility, analyzing feedback objectively, seeking mentoring, and showing measurable improvement in subsequent sprints.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Where do you see yourself progressing at PwC over the next 3 to 5 years as an engineer?",
            "Connect: Growing from Associate to Senior Associate / Manager, mastering enterprise cloud architectures, and mentoring new campus joiners.",
            "Career Aspirations & Growth"
        ),
        create_hr_question(
            "Describe a time you discovered an ethical issue or data discrepancy in your project right before delivery. How did you handle reporting it?",
            "Show: Uncompromising integrity, honest communication with the lead, never hiding defects, and presenting constructive solutions.",
            "Ethics & Professional Integrity"
        ),
        create_hr_question(
            "Do you have any questions for PwC leadership regarding our Acceleration Centers, project allocation, or employee development programs?",
            "Candidate asks thoughtful questions about PwC AI Factory initiatives, Digital Lab assets, or career mobility across advisory practices.",
            "Candidate Curiosity"
        )
    ]

    return {
        "aptitude": {"Java Developer": apt_java, "Python Developer": apt_java, "Data Analyst": apt_java},
        "coding": {"Java Developer": code_java, "Python Developer": code_java, "Data Analyst": code_java},
        "technical": {"Java Developer": tech_java, "Python Developer": tech_java, "Data Analyst": tech_java},
        "ai_interview": {"Java Developer": ai_java, "Python Developer": ai_java, "Data Analyst": ai_java},
        "hr": {"Java Developer": hr_java, "Python Developer": hr_java, "Data Analyst": hr_java}
    }

LTIMINDTREE_DATA = build_ltimindtree_catalog()
PERSISTENT_DATA = build_persistent_catalog()
SAP_DATA = build_sap_catalog()
EY_DATA = build_ey_catalog()
PWC_DATA = build_pwc_catalog()
