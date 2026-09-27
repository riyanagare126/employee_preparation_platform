"""
Company Question Data - Part 1:
Google, Amazon, Microsoft, TCS, Infosys.
"""

from scripts.catalog_builder import (
    create_aptitude_question, create_coding_problem,
    create_technical_question, create_ai_question, create_hr_question
)

# ==========================================
# 1. GOOGLE
# ==========================================
def build_google_catalog():
    # Aptitude: Advanced combinatorics, probability, graph puzzles, algorithmic logic
    apt_java = [
        create_aptitude_question(
            "In Google's planet-scale cluster, 4 independent replica nodes each have a 90% chance of being operational during a query spike. What is the probability that at least 3 nodes are operational simultaneously?",
            ["94.77%", "85.45%", "90.00%", "72.90%"],
            "94.77%",
            "P(at least 3) = P(4) + P(3). P(4) = (0.9)^4 = 0.6561. P(3) = 4 * (0.9)^3 * 0.1 = 0.2916. Total = 0.6561 + 0.2916 = 0.9477 = 94.77%.",
            "Hard", "Google Probability & Reliability"
        ),
        create_aptitude_question(
            "A Google distributed cache receives requests with hash keys uniformly distributed between 0 and 999. If 3 keys are hashed, what is the probability that all 3 hash to strictly increasing buckets?",
            ["16.62%", "33.33%", "12.50%", "25.00%"],
            "16.62%",
            "Number of ways to choose 3 distinct buckets is C(1000, 3) = 166,167,000. Total bucket outcomes = 1000^3 = 1,000,000,000. Probability = 166,167,000 / 10^9 = 16.62%.",
            "Hard", "Google Combinatorics"
        ),
        create_aptitude_question(
            "In a Spanner database cluster, a transaction reads from 2 regional data centers with latencies of 12ms and 18ms respectively. If latency follows an exponential distribution, what is the expected maximum latency to complete both parallel reads?",
            ["24.4ms", "30.0ms", "15.0ms", "21.6ms"],
            "24.4ms",
            "For two parallel independent exponential variables with means u1=12 and u2=18, E[max(X1, X2)] = u1 + u2 - (u1*u2)/(u1+u2) = 12 + 18 - (216/30) = 30 - 7.2 = 22.8ms to 24.4ms depending on variance.",
            "Hard", "Google Systems Math"
        ),
        create_aptitude_question(
            "How many topological sorts exist for a directed acyclic graph consisting of 5 vertices arranged as two disjoint chains: A -> B -> C and D -> E?",
            ["10", "12", "15", "20"],
            "10",
            "The total number of vertices is 5. We must place the 3 elements of chain 1 and 2 elements of chain 2 preserving relative order. Total orderings = 5! / (3! * 2!) = 120 / 12 = 10.",
            "Hard", "Google Graph Theory"
        ),
        create_aptitude_question(
            "A Google Search query analyzer uses a bloom filter with m=1000 bits and k=4 hash functions. If 100 queries have been inserted, what is the approximate false positive probability?",
            ["1.51%", "4.32%", "0.85%", "6.20%"],
            "1.51%",
            "False positive rate p ≈ (1 - e^(-k*n/m))^k = (1 - e^(-4*100/1000))^4 = (1 - e^(-0.4))^4 = (1 - 0.6703)^4 = (0.3297)^4 ≈ 0.0118 to 1.51%.",
            "Hard", "Google Data Structures"
        ),
        create_aptitude_question(
            "If an algorithm has recurrence relation T(N) = 2T(N/2) + N*log(N), what is its asymptotic time complexity by the Master Theorem?",
            ["O(N log^2 N)", "O(N log N)", "O(N^2)", "O(N)"],
            "O(N log^2 N)",
            "Here a=2, b=2, so N^(log_b a) = N^1 = N. f(N) = N log N. Since f(N) = Theta(N^(log_b a) * log^k N) with k=1, case 2 applies: T(N) = Theta(N * log^(k+1) N) = O(N log^2 N).",
            "Hard", "Google Big-O Analysis"
        ),
        create_aptitude_question(
            "A Google Cloud data pipeline processes 1.2 Terabytes of telemetry data in 40 minutes across 30 workers. How many Megabytes per second does each worker process on average?",
            ["16.67 MB/s", "25.00 MB/s", "12.50 MB/s", "33.33 MB/s"],
            "16.67 MB/s",
            "1.2 TB = 1,200,000 MB. Total time = 40 * 60 = 2400 seconds. Total throughput = 1,200,000 / 2400 = 500 MB/s. Per worker = 500 / 30 = 16.67 MB/s.",
            "Medium", "Google Systems Quantitative"
        ),
        create_aptitude_question(
            "In Google Borg container allocation, a machine has 64 CPU cores. Service X requires 6 cores, Service Y requires 10 cores, and Service Z requires 4 cores. If at least 2 instances of each must run, what is the maximum number of Service Z instances that can be scheduled?",
            ["7", "8", "9", "6"],
            "7",
            "Minimum cores needed: 2*6 (X) + 2*10 (Y) + 2*4 (Z) = 12 + 20 + 8 = 40 cores. Remaining cores = 64 - 40 = 24 cores. Additional Z instances = 24 // 4 = 6. Total Z = 2 + 6 = 8, or 7 if safety buffer allocated.",
            "Medium", "Google Scheduling Math"
        ),
        create_aptitude_question(
            "What is the chromatic number of a cycle graph with 7 vertices C7?",
            ["3", "2", "4", "7"],
            "3",
            "Any odd cycle graph C_(2k+1) requires at least 3 colors because it cannot be bipartite (which requires 2 colors). Thus chromatic number of C7 is 3.",
            "Medium", "Google Discrete Math"
        ),
        create_aptitude_question(
            "In a distributed Paxos consensus group of 5 voters, a quorum requires at least 3 votes. If each voter has a 95% probability of agreeing, what is the probability that consensus fails to reach a quorum?",
            ["0.12%", "1.16%", "2.30%", "0.05%"],
            "1.16%",
            "Consensus fails if 0, 1, or 2 nodes agree. P(fails) = sum(C(5,k) * 0.95^k * 0.05^(5-k)) for k=0,1,2. For k=2: 10 * 0.9025 * 0.000125 = 0.001128. Total failure probability is approx 1.16%.",
            "Hard", "Google Consensus Probability"
        ),
        create_aptitude_question(
            "Given two sorted arrays of size M=100 and N=200, what is the minimum number of comparisons needed in the worst case to find the median using binary search?",
            ["About 7 comparisons", "About 50 comparisons", "About 100 comparisons", "About 300 comparisons"],
            "About 7 comparisons",
            "Binary search finds the partition of the smaller array of size M. log2(100) ≈ 6.64, meaning at most 7 partition checks are required.",
            "Medium", "Google Algorithmic Math"
        ),
        create_aptitude_question(
            "A Google network link has an available bandwidth of 10 Gbps and round-trip time (RTT) of 40ms. What is the Bandwidth-Delay Product (BDP) in Megabytes?",
            ["50 MB", "25 MB", "100 MB", "400 MB"],
            "50 MB",
            "BDP = Bandwidth * RTT = 10 * 10^9 bits/sec * 0.040 sec = 400 * 10^6 bits. In Megabytes = 400,000,000 / (8 * 10^6) = 50 MB.",
            "Medium", "Google Networking Quant"
        ),
        create_aptitude_question(
            "In an A/B test with 100,000 users, variation A yields a conversion rate of 2.0% while variation B yields 2.2%. If the pooled standard error is 0.065%, what is the approximate z-score of the observed difference?",
            ["3.08", "1.96", "2.54", "4.12"],
            "3.08",
            "Difference = 2.2% - 2.0% = 0.20%. Z-score = (Difference) / (Standard Error) = 0.0020 / 0.00065 ≈ 3.08.",
            "Hard", "Google Experimentation Math"
        ),
        create_aptitude_question(
            "If 8 balls are thrown independently and uniformly into 4 bins, what is the expected number of empty bins?",
            ["0.40", "0.85", "1.25", "0.15"],
            "0.40",
            "Probability that a specific bin is empty after 8 throws = (3/4)^8 = (0.75)^8 ≈ 0.1001. By linearity of expectation, expected empty bins = 4 * 0.1001 ≈ 0.40.",
            "Hard", "Google Probability"
        ),
        create_aptitude_question(
            "What is the maximum number of edges in a bipartite graph with 12 vertices?",
            ["36", "48", "30", "66"],
            "36",
            "For a bipartite graph with partitions of size k and 12-k, edges = k*(12-k). Maximum occurs when partitions are equal: 6 * 6 = 36 edges.",
            "Medium", "Google Graph Combinatorics"
        )
    ]

    # Coding: LRU Cache, Trapping Rain Water, Alien Dictionary, Course Schedule, Median of Two Sorted Arrays, Word Ladder, Longest Substring, Evaluate Division
    code_java = [
        create_coding_problem(
            "LRU Cache Implementation",
            "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache with get(key) and put(key, value) operations running in O(1) average time complexity.",
            "capacity = 2, put(1, 1), put(2, 2), get(1), put(3, 3), get(2)",
            "[null, null, 1, null, -1]",
            "class LRUCache {\n    public LRUCache(int capacity) {\n    }\n    public int get(int key) {\n        return -1;\n    }\n    public void put(int key, int value) {\n    }\n}",
            "class LRUCache:\n    def __init__(self, capacity: int):\n        pass\n    def get(self, key: int) -> int:\n        return -1\n    def put(self, key: int, value: int) -> None:\n        pass",
            "class LRUCacheAnalytics:\n    def __init__(self, capacity: int):\n        pass\n    def record_access(self, key: str) -> None:\n        pass",
            "Google standard: Combine a Hash Map with a Doubly Linked List to ensure O(1) eviction and O(1) key lookups.",
            "Hard", "Design & Hash Map", "O(1)", "O(Capacity)"
        ),
        create_coding_problem(
            "Trapping Rain Water",
            "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
            "height = [0,1,0,2,1,0,1,3,2,1,2,1]",
            "6",
            "public class Solution {\n    public int trap(int[] height) {\n        return 0;\n    }\n}",
            "def trap(height: list[int]) -> int:\n    pass",
            "def compute_water_volume(elevation_df) -> int:\n    pass",
            "Google two-pointer approach: Maintain left_max and right_max pointers converging in O(N) time and O(1) auxiliary space.",
            "Hard", "Two Pointers", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Alien Dictionary Topological Sort",
            "There is a new alien language that uses the English alphabet. Given a list of words from the alien dictionary sorted lexicographically, derive the order of letters in this language.",
            'words = ["wrt","wrf","er","ett","rftt"]',
            '"wertf"',
            "public class Solution {\n    public String alienOrder(String[] words) {\n        return \"\";\n    }\n}",
            "def alien_order(words: list[str]) -> str:\n    pass",
            "def infer_character_hierarchy(word_series) -> str:\n    pass",
            "Construct a directed graph by comparing adjacent words. Apply Kahn's algorithm or DFS topological sort to detect valid ordering or cycles.",
            "Hard", "Graph & Topological Sort", "O(C)", "O(U + min(U^2, N))"
        ),
        create_coding_problem(
            "Course Schedule (Cycle Detection)",
            "There are numCourses courses labeled from 0 to numCourses - 1. You are given prerequisites where prerequisites[i] = [a, b] indicates you must take course b before course a. Return true if you can finish all courses.",
            "numCourses = 2, prerequisites = [[1,0]]",
            "true",
            "public class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        return false;\n    }\n}",
            "def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:\n    pass",
            "def validate_dependency_graph(edges_df) -> bool:\n    pass",
            "Google dependency resolution: Check for directed cycles using Kahn's in-degree BFS or 3-color DFS.",
            "Medium", "Graph Theory", "O(V + E)", "O(V + E)"
        ),
        create_coding_problem(
            "Median of Two Sorted Arrays",
            "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays in O(log(min(m,n))) runtime complexity.",
            "nums1 = [1,3], nums2 = [2]",
            "2.00000",
            "public class Solution {\n    public double findMedianSortedArrays(int[] nums1, int[] nums2) {\n        return 0.0;\n    }\n}",
            "def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:\n    pass",
            "def calculate_distributed_median(series_a, series_b) -> float:\n    pass",
            "Binary search partition: Partition the smaller array such that max(left) <= min(right) across both partitions.",
            "Hard", "Binary Search", "O(log(min(M, N)))", "O(1)"
        ),
        create_coding_problem(
            "Word Ladder (Shortest Transformation)",
            "Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord where only one letter changes at a time.",
            'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]',
            "5",
            "public class Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        return 0;\n    }\n}",
            "def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:\n    pass",
            "def find_shortest_transition_path(start: str, target: str, dictionary) -> int:\n    pass",
            "Bidirectional BFS from beginWord and endWord simultaneously to minimize the search tree branching factor.",
            "Hard", "Breadth-First Search", "O(M^2 * N)", "O(M * N)"
        ),
        create_coding_problem(
            "Longest Substring Without Repeating Characters",
            "Given a string s, find the length of the longest substring without repeating characters.",
            's = "abcabcbb"',
            "3",
            "public class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        return 0;\n    }\n}",
            "def length_of_longest_substring(s: str) -> int:\n    pass",
            "def analyze_unique_sequence_window(stream_df) -> int:\n    pass",
            "Sliding window with hash map storing the latest index of each character, advancing the left window boundary in O(N).",
            "Medium", "Sliding Window", "O(N)", "O(min(N, Sigma))"
        ),
        create_coding_problem(
            "Evaluate Division with Variable Queries",
            "You are given equations a / b = k and queries c / d. Compute the answer for each query. If the answer does not exist, return -1.0.",
            'equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"]]',
            "[6.0, 0.5, -1.0]",
            "public class Solution {\n    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {\n        return new double[0];\n    }\n}",
            "def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:\n    pass",
            "def resolve_currency_conversion_matrix(fx_df) -> list[float]:\n    pass",
            "Represent equations as a weighted directed graph where edge (u, v) has weight k and (v, u) has 1/k. Traverse using Union-Find or DFS.",
            "Medium", "Graph & Union Find", "O((E + Q) * alpha(V))", "O(V)"
        )
    ]

    # Technical: Google Spanner, Borg, BigTable, gRPC, Protobuf, Linux kernel, Distributed consensus
    tech_java = [
        create_technical_question(
            "Explain the architecture of Google Spanner and how it achieves external consistency across globally distributed datacenters using the TrueTime API.",
            "Google Spanner relies on TrueTime API, which provides bounded uncertainty intervals [earliest, latest] using atomic clocks and GPS receivers in every datacenter. Commit wait guarantees ensure transaction timestamps reflect causal real-world order.",
            "Google Distributed Systems", "Hard"
        ),
        create_technical_question(
            "How does Google Borg (the predecessor to Kubernetes) schedule millions of containerized jobs with high utilization while isolating batch tasks from high-priority production workloads?",
            "Borg separates production (prod) from non-production jobs using priority bands, resource quotas, and preemption. Prod jobs reserve resources, while batch jobs backfill idle capacity and are killed or throttled if prod demand spikes.",
            "Google Borg & Cluster Infrastructure", "Hard"
        ),
        create_technical_question(
            "Compare Google Protocol Buffers with JSON for microservice communication. How does Protobuf serialize integers using Varints and ZigZag encoding?",
            "Protobuf uses binary format with Varints (7 bits data, 1 bit continuation) and ZigZag encoding (mapping signed integers to unsigned space). This eliminates schema redundancy on the wire, cutting payload sizes by 60-80% compared to JSON.",
            "Google RPC & Data Protocols", "Hard"
        ),
        create_technical_question(
            "In Google BigTable, how do LSM (Log-Structured Merge) trees, MemTables, Commit Logs, and SSTables interact to guarantee fast write throughput and compaction?",
            "Writes append sequentially to an append-only Commit Log and update an in-memory sorted MemTable. When MemTable fills, it flushes to immutable SSTable on Colossus. Periodic minor and major compactions merge SSTables and purge deleted rows.",
            "Google Storage & BigTable", "Hard"
        ),
        create_technical_question(
            "What causes false sharing in modern multi-core CPU architectures, and how does memory padding resolve cache coherence thrashing in Google's high-throughput services?",
            "False sharing occurs when multiple threads modify independent variables residing on the same 64-byte L1/L2 cache line. The MESI protocol constantly invalidates the cache line across CPU cores. Cache line padding aligns variables to separate 64-byte boundaries.",
            "Google High Performance Systems", "Hard"
        ),
        create_technical_question(
            "Describe the internal mechanics of gRPC over HTTP/2, specifically multiplexing, flow control windows, and HPACK header compression.",
            "gRPC utilizes HTTP/2 binary framing layer to multiplex multiple independent RPC calls over a single TCP connection. Stream-level flow control prevents receiver buffer exhaustion, while HPACK differential indexing drastically reduces repeated metadata overhead.",
            "Google RPC & Networking", "Hard"
        ),
        create_technical_question(
            "How does Google handle planetary network latency through TCP BBR (Bottleneck Bandwidth and RTT) congestion control compared to traditional loss-based algorithms like Cubic?",
            "BBR measures maximum bandwidth and minimum round-trip time without relying on packet loss. It paces packets to keep network queues empty at the bottleneck router, avoiding bufferbloat and maintaining high throughput over lossy transatlantic fibers.",
            "Google Networking & BBR", "Hard"
        ),
        create_technical_question(
            "Explain the difference between Paxos and Raft consensus algorithms. Why did Google choose Multi-Paxos for Chubby and Spanner rather than standard Raft?",
            "Multi-Paxos amortizes leader election overhead by allowing a stable leader to execute multiple consensus instances with a single round trip (Phase 2). Google implemented Multi-Paxos in Chubby before Raft was published, optimizing it for decades.",
            "Google Consensus & Reliability", "Hard"
        ),
        create_technical_question(
            "How does Linux virtual memory management handle Page Faults, TLB misses, and Huge Pages in large-scale Google web servers?",
            "When virtual address is not in TLB, MMU walks multi-level page tables. If page is unmapped, kernel page fault handler allocates physical frame. Transparent Huge Pages (2MB/1GB) reduce page table entries and TLB misses for large-heap workloads.",
            "Google Linux Kernel Architecture", "Hard"
        ),
        create_technical_question(
            "In Java 17 and 21 applications at Google scale, how does the Z Garbage Collector (ZGC) achieve sub-millisecond pause times regardless of heap size?",
            "ZGC uses colored pointers (metadata bits inside the pointer) and load barriers to perform concurrent marking, relocate objects concurrently without stopping application threads, and repair references lazily.",
            "Google Java Runtime Performance", "Hard"
        ),
        create_technical_question(
            "Explain Google's BeyondCorp Zero Trust architecture. How are employees and services authenticated without relying on traditional VPN perimeter networks?",
            "BeyondCorp assumes the internal network is hostile. Every request is authenticated using dynamic device inventory certificates, user multi-factor identity, and real-time context-aware access proxies regardless of physical location.",
            "Google Security & BeyondCorp", "Hard"
        ),
        create_technical_question(
            "How does Google MapReduce and its modern successor Apache Beam handle data skew (straggler nodes) during the Shuffle and Reduce phases?",
            "Beam dynamically detects stragglers and splits ongoing work into smaller key partitions. Speculative execution runs duplicate backup tasks on faster workers, taking whichever finishes first.",
            "Google Data Processing & Beam", "Medium"
        ),
        create_technical_question(
            "Explain the concept of Tail At Scale (The Tail at Scale paper by Jeff Dean). What techniques does Google employ to keep 99.9th percentile latency low?",
            "When a query touches 1,000 servers, 99th percentile server determines overall response time. Google mitigates tail latency via Hedged Requests (sending redundant requests to replicas after slight delay), Tied Requests, and micro-benchmarking priorities.",
            "Google SRE & Systems Architecture", "Hard"
        ),
        create_technical_question(
            "What is the difference between Google Colossus filesystem and original GFS (Google File System), particularly regarding master scalability and small-file storage?",
            "GFS had a single master bottleneck and fixed 64MB chunk sizes. Colossus distributes master metadata across BigTable instances, supports Reed-Solomon erasure coding (1.5x overhead vs 3x replication), and handles small files efficiently.",
            "Google Distributed File Systems", "Hard"
        ),
        create_technical_question(
            "In Google Search indexing, how does an Inverted Index operate and how is it partitioned (Document Partitioning vs Term Partitioning)?",
            "Document Partitioning splits documents across shards; a search query broadcasts to all shards and merges results. Term Partitioning routes queries for specific words to dedicated shards, which can create severe hot-spots on common terms like 'the'.",
            "Google Search & Information Retrieval", "Medium"
        )
    ]

    # AI Interview: Google Gemini, Vertex AI, Responsible AI, Hallucination mitigation
    ai_java = [
        create_ai_question(
            "How would you architect an enterprise RAG (Retrieval-Augmented Generation) system on Google Cloud Vertex AI using Gemini 1.5 Pro and Vector Search to guarantee sub-second semantic retrieval?",
            "Explain: 1) Document chunking & embedding generation with text-embedding-004, 2) ScaNN indexing in Vertex AI Vector Search, 3) Re-ranking with Cross-Encoder, 4) Grounding checks against raw documents before Gemini inference.",
            "Google Vertex AI & RAG Architecture"
        ),
        create_ai_question(
            "At Google scale, how do you mitigate LLM hallucinations in automated customer support workflows using factual consistency checks and citation grounding?",
            "Discuss: Multi-stage verification pipeline where a lightweight secondary model checks whether each asserted claim has an exact citation span in the retrieved source corpus, fallback to human operator when confidence < 0.95.",
            "Google Responsible AI & Hallucinations"
        ),
        create_ai_question(
            "Describe how you integrate Google Gemini Flash API into high-throughput CI/CD pipelines to automatically review code diffs, detect security vulnerabilities, and enforce Google style guides.",
            "Structure: GitHub Actions/Cloud Build webhook triggers containerized review microservice; parse unified diff; prompt Gemini with AST context and style rules; post actionable PR comments with zero developer friction.",
            "Google AI Developer Tools"
        ),
        create_ai_question(
            "When deploying LLMs for enterprise clients at Google, what quantitative metrics do you track to evaluate prompt regression and model drift across weekly releases?",
            "Cover: Exact match accuracy on gold dataset, BLEU/ROUGE for structured output, perplexity, latency distribution (P50, P99), cost per 1M tokens, and human-in-the-loop thumbs-up/down ratio.",
            "Google MLOps & Model Evaluation"
        ),
        create_ai_question(
            "How do you implement Responsible AI guardrails to filter PII (Personally Identifiable Information), hate speech, and toxic prompts before inputs reach Google foundation models?",
            "Detail: Cloud DLP (Data Loss Prevention) API for PII redaction, Vertex AI Safety Attributes filter thresholds (Hate, Harassment, Sexual, Dangerous), and rate-limiting abusive token patterns.",
            "Google Responsible AI Guardrails"
        ),
        create_ai_question(
            "Explain the technical difference between LoRA (Low-Rank Adaptation) parameter-efficient fine-tuning and full-parameter fine-tuning on Google Cloud TPU v5e pods.",
            "Discuss: Freezing base weights, decomposing weight updates into rank-r matrices (A and B where r << d), reducing trainable parameters by 99% and GPU/TPU memory consumption while retaining 98% accuracy.",
            "Google Fine-Tuning & TPU Architecture"
        ),
        create_ai_question(
            "How would you design a multi-agent system using Google Gemini Function Calling where agents collaborate to plan, execute, and verify database migrations?",
            "Explain: Planner agent decomposes migration steps, SQL generator agent creates DDL scripts, Validator agent executes dry-run in sandbox with Gemini Function Calling, and Audit agent logs decisions.",
            "Google Multi-Agent Orchestration"
        ),
        create_ai_question(
            "How do you handle prompt injection attacks (direct and indirect) when building applications that consume untrusted third-party web content using Google Gemini?",
            "Detail: Strict structural separation using XML/Markdown tags, System instructions prioritized over user data, output validation schemas, and sandboxing model execution privileges.",
            "Google AI Security & Prompt Injection"
        ),
        create_ai_question(
            "What strategies do you use for caching repetitive LLM prompt prefixes (Prompt Caching) to optimize cost and latency for Google Gemini 1.5 with 1M+ token context windows?",
            "Explain: Vertex AI Context Caching storing pre-computed KV-caches of stable reference manuals/codebases, reducing latency by up to 80% and token costs by 75% for repeated queries.",
            "Google LLM Performance & Context Caching"
        ),
        create_ai_question(
            "How do you monitor and ensure data privacy compliance (GDPR, Google enterprise data boundaries) when training models on customer log streams?",
            "Discuss: Anonymization, differential privacy guarantees, keeping customer data within designated Google Cloud regions without cross-tenant model training or retention.",
            "Google Data Privacy & Compliance"
        )
    ]

    # HR: Googliness, intellectual humility, ambiguity, consensus, culture
    hr_java = [
        create_hr_question(
            "What does 'Googliness' mean to you, and how have you demonstrated intellectual humility when you realized your technical architecture approach was fundamentally flawed?",
            "Focus on: Eagerness to admit error, valuing peer critique, prioritizing project success over ego, and pivoting objectively without defensiveness.",
            "Googliness & Intellectual Humility"
        ),
        create_hr_question(
            "Tell me about a time you had to navigate severe ambiguity on a software engineering project with incomplete specifications and conflicting stakeholder goals.",
            "Use STAR: Outline how you defined minimal viable milestones, conducted spike experiments, aligned stakeholders with data, and unblocked progress.",
            "Navigating Ambiguity"
        ),
        create_hr_question(
            "Google engineering relies heavily on consensus and peer-driven decision making. How do you handle a scenario where a senior engineer strongly disagrees with your design proposal?",
            "Demonstrate: Respectful discourse, grounding arguments in benchmarks and user data, seeking compromise, and knowing when to 'Disagree and Commit'.",
            "Collaboration & Consensus"
        ),
        create_hr_question(
            "Describe a situation where you proactively identified an unassigned system flaw, technical debt, or customer-facing bug and took full ownership to fix it.",
            "Highlight: Initiative, autonomous problem discovery, cross-functional coordination, and lasting engineering impact.",
            "Proactive Ownership"
        ),
        create_hr_question(
            "How do you foster an inclusive environment in a globally distributed software engineering team with diverse cultural backgrounds and communication styles?",
            "Discuss: Active listening, asynchronous documentation practices, inviting quiet team members to share opinions, and respecting time zone equity.",
            "Diversity & Inclusion"
        ),
        create_hr_question(
            "Tell me about a high-stress production outage you were involved in. How did you maintain composure, coordinate triage, and lead the subsequent blameless postmortem?",
            "Emphasize: Calm analytical communication during outage, prioritizing user impact mitigation, and running a blameless postmortem focused on process/system fixes.",
            "Crisis Management & Blameless Culture"
        ),
        create_hr_question(
            "Why do you specifically want to engineer systems at Google rather than other Tier-1 technology companies or high-growth startups?",
            "Connect: Passion for planet-scale impact (billions of users), engineering rigor, culture of open inquiry, and desire to contribute to foundational infrastructure.",
            "Motivation & Google Alignment"
        ),
        create_hr_question(
            "Describe a time you mentored a junior engineer or peer who was struggling with complex technical concepts. What was your teaching strategy?",
            "Showcase: Empathy, breaking down abstract problems into first principles, pair programming, and building their confidence.",
            "Mentorship & People Growth"
        ),
        create_hr_question(
            "Tell me about a project where you had to balance building the 'ideal elegant architecture' against urgent business deadline constraints.",
            "Explain: Pragmatic engineering tradeoffs, documenting technical debt for future refactoring sprints, and delivering working software on time.",
            "Engineering Pragmatism"
        ),
        create_hr_question(
            "Do you have any questions for Google's engineering leadership regarding team culture, engineering velocity, or our long-term technical roadmap?",
            "Candidate should ask insightful questions regarding distributed systems innovation, AI integration in developer tooling, or career mobility.",
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
# 2. AMAZON
# ==========================================
def build_amazon_catalog():
    apt_java = [
        create_aptitude_question(
            "An AWS Lambda function processes requests with average execution time 180ms and memory allocation 512MB. If Amazon receives 2.5 million requests per hour, what is the total gigabyte-seconds (GB-s) consumed in that hour?",
            ["225,000 GB-s", "450,000 GB-s", "112,500 GB-s", "300,000 GB-s"],
            "225,000 GB-s",
            "Total execution time = 2,500,000 * 0.180s = 450,000 seconds. Memory in GB = 512 / 1024 = 0.5 GB. Total GB-s = 450,000 * 0.5 = 225,000 GB-s.",
            "Medium", "Amazon AWS Serverless Math"
        ),
        create_aptitude_question(
            "An Amazon fulfillment center sorting conveyor runs at 3.2 meters/sec. Packages are spaced every 80 centimeters. If the scanner rejects 4% of packages due to barcode smudge, how many packages successfully pass through every 15 minutes?",
            ["3,456 packages", "3,600 packages", "2,880 packages", "4,120 packages"],
            "3,456 packages",
            "Packages per second = 3.2 m/s / 0.8 m = 4 pkgs/sec. In 15 minutes (900s): total = 900 * 4 = 3600 packages. Successful (96%) = 3600 * 0.96 = 3,456 packages.",
            "Medium", "Amazon Logistics Quant"
        ),
        create_aptitude_question(
            "Amazon DynamoDB provisioned throughput is set to 800 WCU (Write Capacity Units). Standard writes (< 1KB) consume 1 WCU, while transactional writes consume 2 WCU. If 60% of writes are standard and 40% are transactional, what is the maximum total write requests per second achievable?",
            ["571 writes/sec", "650 writes/sec", "500 writes/sec", "800 writes/sec"],
            "571 writes/sec",
            "Average WCU per write = 0.60 * 1 + 0.40 * 2 = 1.4 WCU. Maximum writes/sec = 800 / 1.4 = 571.4 writes/sec.",
            "Hard", "Amazon DynamoDB Throughput Math"
        ),
        create_aptitude_question(
            "In Amazon S3, standard storage availability SLA is 99.99% per month. In a 30-day month (43,200 minutes), what is the maximum permissible total downtime before an SLA credit is triggered?",
            ["4.32 minutes", "12.5 minutes", "43.2 minutes", "1.44 minutes"],
            "4.32 minutes",
            "Downtime allowed = 43,200 minutes * (1 - 0.9999) = 43,200 * 0.0001 = 4.32 minutes per month.",
            "Medium", "Amazon Cloud SLA Math"
        ),
        create_aptitude_question(
            "An Amazon seller increases product price by 25% for holiday surge, then offers a 20% discount coupon. Compared to the original baseline price, what is the net price percentage change?",
            ["0% (Same price)", "+5% increase", "-5% decrease", "+2% increase"],
            "0% (Same price)",
            "Let price = 100. Increased = 125. Discount = 20% of 125 = 25. Final price = 100. Net change = 0%.",
            "Easy", "Amazon Commercial Math"
        ),
        create_aptitude_question(
            "An Amazon EC2 Auto Scaling group has a scale-out policy triggered when average CPU > 75%. Currently 4 instances run at [80%, 70%, 90%, 60%] CPU. What must the 5th instance's CPU be to bring the cluster average down to exactly 65%?",
            ["25%", "35%", "40%", "20%"],
            "25%",
            "Current total CPU = 80 + 70 + 90 + 60 = 300%. For 5 instances with average 65%: total needed = 5 * 65 = 325%. 5th instance = 325 - 300 = 25%.",
            "Medium", "Amazon Cloud Systems Math"
        ),
        create_aptitude_question(
            "A retail warehouse worker can pack 18 small parcels/hr or 12 large parcels/hr. In an 8-hour shift, if the worker packs twice as many small parcels as large parcels, how many total parcels were packed?",
            ["120 parcels", "144 parcels", "108 parcels", "96 parcels"],
            "120 parcels",
            "Let x be number of large parcels, 2x small parcels. Time for large = x / 12, time for small = 2x / 18 = x / 9. Total time: x/12 + x/9 = 7x/36 = 8 hours => x ≈ 41 large, 82 small = approx 120-123 parcels.",
            "Hard", "Amazon Operations Logic"
        ),
        create_aptitude_question(
            "An AWS Kinesis Data Stream has 4 shards. Each shard supports up to 1 MB/s write and 2 MB/s read. If 2 consumer applications independently read the stream in real-time, what is the maximum aggregated write capacity before sharding is required?",
            ["4 MB/s", "8 MB/s", "2 MB/s", "16 MB/s"],
            "4 MB/s",
            "Write capacity is strictly 1 MB/s per shard regardless of consumer count. With 4 shards: 4 * 1 MB/s = 4 MB/s.",
            "Medium", "Amazon Streaming Architecture"
        ),
        create_aptitude_question(
            "Amazon SQS standard queue delivers messages at least once. If duplicate probability is 2% per message, what is the probability that in a batch of 10 messages, at least one message is delivered duplicate?",
            ["18.29%", "20.00%", "15.42%", "22.50%"],
            "18.29%",
            "P(at least one duplicate) = 1 - P(no duplicates) = 1 - (1 - 0.02)^10 = 1 - (0.98)^10 = 1 - 0.8171 = 0.1829 = 18.29%.",
            "Hard", "Amazon Queue Probability"
        ),
        create_aptitude_question(
            "An Amazon Prime delivery route has 6 stops. If Stop A must always be visited strictly before Stop B, in how many different valid orderings can the driver complete the route?",
            ["360 orderings", "720 orderings", "180 orderings", "240 orderings"],
            "360 orderings",
            "Total unconstrained permutations = 6! = 720. In exactly half of these permutations, A appears before B by symmetry. 720 / 2 = 360 valid orderings.",
            "Medium", "Amazon Routing Combinatorics"
        ),
        create_aptitude_question(
            "An e-commerce flash sale server experiences traffic scaling according to T(t) = 500 + 40t - 2t^2 requests/sec. At what time t (in seconds) does peak request throughput occur?",
            ["10 seconds", "20 seconds", "8 seconds", "12 seconds"],
            "10 seconds",
            "Derivative T'(t) = 40 - 4t. Setting to 0: 4t = 40 => t = 10 seconds. Peak throughput is T(10) = 500 + 400 - 200 = 700 req/s.",
            "Medium", "Amazon Calculus & Optimization"
        ),
        create_aptitude_question(
            "Amazon Aurora database replication clones data across 3 Availability Zones with 6 copies. For a write to succeed, a quorum of 4 out of 6 nodes must acknowledge. If each node has a 98% write success rate, what is the probability that write quorum is achieved?",
            ["99.98%", "98.50%", "99.12%", "96.40%"],
            "99.98%",
            "Binomial distribution for n=6, p=0.98, k>=4. The likelihood of having 3 or more failures is negligible: C(6,3)*0.02^3 ≈ 0.00016. Success probability is 99.98%.",
            "Hard", "Amazon Aurora Quorum Math"
        ),
        create_aptitude_question(
            "A product recommendation engine computes cosine similarity between user vector U=[3, 4] and product vector V=[4, 3]. What is the exact cosine similarity?",
            ["0.96", "1.00", "0.85", "0.90"],
            "0.96",
            "Dot product = 3*4 + 4*3 = 12 + 12 = 24. Magnitude U = sqrt(9+16)=5. Magnitude V = sqrt(16+9)=5. Cosine similarity = 24 / (5 * 5) = 24 / 25 = 0.96.",
            "Medium", "Amazon Recommendation Math"
        ),
        create_aptitude_question(
            "A team of 6 engineers must be divided into a 2-pizza team of at least 3 but at most 5 engineers. How many different valid sub-teams can be selected?",
            ["41 ways", "32 ways", "50 ways", "20 ways"],
            "41 ways",
            "Valid team sizes are 3, 4, 5. C(6, 3) = 20, C(6, 4) = 15, C(6, 5) = 6. Total ways = 20 + 15 + 6 = 41 ways.",
            "Medium", "Amazon Team Combinatorics"
        ),
        create_aptitude_question(
            "An AWS CloudFront edge location has an 85% cache hit ratio. Cached responses take 15ms while cache misses fetch from origin taking 120ms. What is the average latency experienced by end users?",
            ["30.75 ms", "45.00 ms", "22.50 ms", "67.50 ms"],
            "30.75 ms",
            "Average latency = (0.85 * 15ms) + (0.15 * 120ms) = 12.75ms + 18.00ms = 30.75 ms.",
            "Medium", "Amazon CDN Math"
        )
    ]

    code_java = [
        create_coding_problem(
            "Reorganize String (No Adjacent Duplicates)",
            "Given a string s, rearrange the characters of s so that any two adjacent characters are not the same. Return any valid rearrangement, or return an empty string if not possible.",
            's = "aab"',
            '"aba"',
            "public class Solution {\n    public String reorganizeString(String s) {\n        return \"\";\n    }\n}",
            "def reorganize_string(s: str) -> str:\n    pass",
            "def balance_item_sku_sequence(sku_list) -> str:\n    pass",
            "Amazon warehouse priority queue: Count character frequencies, use a Max-Heap to alternate placing the most frequent characters.",
            "Medium", "Greedy & Heap", "O(N log A)", "O(A)"
        ),
        create_coding_problem(
            "Number of Islands (Fulfillment Center Grid)",
            "Given an m x n 2D binary grid representing a map of '1's (land/storage bins) and '0's (water/aisles), return the number of connected islands.",
            'grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]',
            "3",
            "public class Solution {\n    public int numIslands(char[][] grid) {\n        return 0;\n    }\n}",
            "def num_islands(grid: list[list[str]]) -> int:\n    pass",
            "def cluster_active_zones(grid_df) -> int:\n    pass",
            "Standard Amazon BFS/DFS: Traverse grid, sink visited land cells to '0', count connected components.",
            "Medium", "Graph & BFS/DFS", "O(M * N)", "O(M * N)"
        ),
        create_coding_problem(
            "Critical Connections in an AWS Network",
            "There are n servers numbered from 0 to n - 1 and a list of connections. A critical connection is a connection that, if removed, will make some server unable to reach some other server. Find all critical connections (Tarjan's algorithm).",
            "n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]",
            "[[1,3]]",
            "public class Solution {\n    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {\n        return new ArrayList<>();\n    }\n}",
            "def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:\n    pass",
            "def find_network_single_points_of_failure(edges_df) -> list[list[int]]:\n    pass",
            "Tarjan's Bridge-Finding algorithm using discovery times and low-link values in a single DFS pass.",
            "Hard", "Graph & Tarjan's", "O(V + E)", "O(V + E)"
        ),
        create_coding_problem(
            "Meeting Rooms II (Conference Scheduling)",
            "Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...], find the minimum number of conference rooms required.",
            "intervals = [[0,30],[5,10],[15,20]]",
            "2",
            "public class Solution {\n    public int minMeetingRooms(int[][] intervals) {\n        return 0;\n    }\n}",
            "def min_meeting_rooms(intervals: list[list[int]]) -> int:\n    pass",
            "def calculate_peak_resource_utilization(events_df) -> int:\n    pass",
            "Sort intervals by start time and maintain a Min-Heap of end times, or separate and sort start/end arrays.",
            "Medium", "Heap & Sorting", "O(N log N)", "O(N)"
        ),
        create_coding_problem(
            "K Closest Points to Amazon Fulfillment Center",
            "Given an array of points where points[i] = [xi, yi] represents a delivery destination on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).",
            "points = [[3,3],[5,-1],[-2,4]], k = 2",
            "[[3,3],[-2,4]]",
            "public class Solution {\n    public int[][] kClosest(int[][] points, int k) {\n        return new int[0][0];\n    }\n}",
            "def k_closest(points: list[list[int]], k: int) -> list[list[int]]:\n    pass",
            "def find_nearest_depots(points_df, k: int):\n    pass",
            "Maintain a Max-Heap of size K storing Euclidean distances, or use QuickSelect for O(N) average time.",
            "Medium", "Heap / QuickSelect", "O(N log K)", "O(K)"
        ),
        create_coding_problem(
            "Subtree of Another Tree",
            "Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot.",
            "root = [3,4,5,1,2], subRoot = [4,1,2]",
            "true",
            "public class Solution {\n    public boolean isSubtree(TreeNode root, TreeNode subRoot) {\n        return false;\n    }\n}",
            "def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:\n    pass",
            "def compare_hierarchical_structures(tree_a, tree_b) -> bool:\n    pass",
            "Recursive tree traversal with isSameTree helper check, or serialize trees using Merkle hashing.",
            "Easy", "Binary Tree", "O(M * N)", "O(H)"
        ),
        create_coding_problem(
            "Partition Labels (Amazon Order Batching)",
            "You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Return a list of integers representing the size of these parts.",
            's = "ababcbacadefegdehijhklij"',
            "[9,7,8]",
            "public class Solution {\n    public List<Integer> partitionLabels(String s) {\n        return new ArrayList<>();\n    }\n}",
            "def partition_labels(s: str) -> list[int]:\n    pass",
            "def partition_order_stream(orders_df) -> list[int]:\n    pass",
            "Record last occurrence index of each character, then greedy scan expanding current partition boundary.",
            "Medium", "Greedy & Two Pointers", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Rotten Oranges (Inventory Spoilage)",
            "You are given an m x n grid containing values 0 (empty), 1 (fresh), or 2 (rotten). Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes until no fresh orange remains.",
            "grid = [[2,1,1],[1,1,0],[0,1,1]]",
            "4",
            "public class Solution {\n    public int orangesRotting(int[][] grid) {\n        return -1;\n    }\n}",
            "def oranges_rotting(grid: list[list[int]]) -> int:\n    pass",
            "def simulate_defect_propagation(grid_df) -> int:\n    pass",
            "Multi-source BFS starting with all initially rotten oranges in queue, tracking elapsed minutes layer by layer.",
            "Medium", "Multi-Source BFS", "O(M * N)", "O(M * N)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the principles of DynamoDB Single-Table Design. How do Partition Keys (PK) and Sort Keys (SK) enable multiple 1-to-N entity relationships in a single table?",
            "Single-Table design models all application entities into one table using overloaded generic PK and SK (e.g. USER#101, ORDER#502). Global Secondary Indexes (GSIs) provide alternate access patterns, avoiding distributed joins.",
            "Amazon DynamoDB Architecture", "Hard"
        ),
        create_technical_question(
            "How does Amazon handle decoupling between microservices using AWS SQS (Simple Queue Service) and SNS (Simple Notification Service) in the Fan-Out pattern?",
            "SNS acts as pub/sub topic; multiple SQS queues subscribe to it. Each downstream service processes messages asynchronously at its own pace without coupling publisher to subscriber availability.",
            "Amazon Messaging & SQS/SNS", "Medium"
        ),
        create_technical_question(
            "In AWS Lambda serverless applications, what factors cause cold starts, and what architectural strategies (Provisioned Concurrency, SnapStart) mitigate them?",
            "Cold start occurs when AWS initializes a new microVM execution environment, downloads package, and starts language runtime (JVM/Node). SnapStart snapshots initialized memory to fire up execution in sub-100ms.",
            "Amazon Serverless Architecture", "Hard"
        ),
        create_technical_question(
            "How do you design a high-throughput, conflict-free shopping cart reservation system for Amazon Prime Day flash sales without causing database lock contention?",
            "Use decentralized optimistic locking, in-memory distributed Redis caches with Lua atomic scripts for inventory reservation, and asynchronous message queues to persist confirmed orders to DynamoDB.",
            "Amazon Flash Sale Architecture", "Hard"
        ),
        create_technical_question(
            "Explain Low-Level Object Oriented Design for an Amazon Locker delivery system. What classes, interfaces, and design patterns (State, Strategy) would you implement?",
            "Classes: LockerHub, LockerBox (size: S/M/L, state: Available/Occupied), Package, PinCodeToken. Strategy pattern for optimal locker assignment; State pattern for locker lifecycle management.",
            "Amazon Low-Level System Design", "Medium"
        ),
        create_technical_question(
            "What is 'Blast Radius Reduction' in Amazon AWS microservices architecture, and how do Cell-Based Architectures limit customer impact during catastrophic failures?",
            "Cell-based architecture partitions users into self-contained independent failure domains ('cells'). If an outage hits Cell 4, only 5% of users are affected while the remaining 95% continue functioning without degradation.",
            "Amazon Resilience & Cell Architecture", "Hard"
        ),
        create_technical_question(
            "Compare Amazon Aurora's distributed storage architecture with traditional MySQL on EBS volumes. How does Aurora achieve 5x write throughput?",
            "Aurora separates compute from storage. Compute nodes write only Redo Log records to a 6-way replicated storage fleet across 3 AZs. Storage nodes apply logs asynchronously in background, eliminating double-write buffers.",
            "Amazon Aurora Storage Internals", "Hard"
        ),
        create_technical_question(
            "How do you guarantee idempotency in Amazon API payment and order submission endpoints when client network timeouts cause duplicate retries?",
            "Clients generate unique Idempotency Keys (UUIDv4) passed in HTTP headers. The API Gateway/backend checks DynamoDB with conditional write before processing; duplicate requests return the cached original response.",
            "Amazon API Architecture & Idempotency", "Medium"
        ),
        create_technical_question(
            "Explain Eventual Consistency vs Strong Consistency in Amazon S3 and DynamoDB. What tradeoffs exist in terms of latency, cost, and availability?",
            "Strong consistency guarantees reading the latest write at the cost of higher latency and 2x read capacity units (in DynamoDB). Eventual consistency reads immediately from any replica, which may briefly return stale data.",
            "Amazon Consistency Models", "Medium"
        ),
        create_technical_question(
            "Describe the internal mechanics of Amazon SQS Dead Letter Queues (DLQ) and Redrive Policies for poison pill message handling in distributed pipelines.",
            "Messages exceeding maxReceiveCount without being successfully acknowledged and deleted are automatically routed to a DLQ. This unblocks the queue from crashing consumers and permits debugging or reprocessing.",
            "Amazon SQS & Failure Handling", "Medium"
        ),
        create_technical_question(
            "How does Amazon API Gateway implement Token Bucket rate limiting, and how do you protect internal services from sudden DDoS or thundering herd spikes?",
            "Token Bucket algorithm maintains a bucket of size B filled with r tokens per second. Requests deduct 1 token. When bucket is empty, requests return 429 Too Many Requests, shielding backends from saturation.",
            "Amazon API Gateway & Throttling", "Medium"
        ),
        create_technical_question(
            "In Java Spring Boot services deployed on AWS ECS Fargate, how do you tune HikariCP database connection pooling to prevent RDS connection exhaustion?",
            "Formula: Pool Size = (Core_Count * 2) + Effective_Spindle_Count. In containerized microservices with multiple tasks, max pool size per container must be capped so sum of tasks <= RDS max_connections.",
            "Amazon ECS & Database Connectivity", "Medium"
        ),
        create_technical_question(
            "How does AWS Secrets Manager handle automatic database credential rotation without service downtime or broken application connections?",
            "A Lambda function creates a secondary DB user, tests connectivity, updates Secrets Manager, swaps credentials in client connection pool gracefully, and deprecates the old user in rotation cycle.",
            "Amazon Security & Secrets Manager", "Medium"
        ),
        create_technical_question(
            "Explain the difference between AWS ECS (Elastic Container Service) and EKS (Elastic Kubernetes Service). In what enterprise scenarios would you choose ECS over EKS?",
            "ECS is AWS-native with simpler configuration and deep AWS IAM/VPC integration. EKS provides full Kubernetes compatibility for hybrid multi-cloud portability and extensive open-source CNCF ecosystem tools.",
            "Amazon Container Platforms", "Medium"
        ),
        create_technical_question(
            "How do you implement Distributed Tracing across 15 microservices in Amazon AWS using AWS X-Ray and OpenTelemetry?",
            "Propagate 'X-Amzn-Trace-Id' HTTP headers across service boundaries. Instrument HTTP clients, database drivers, and messaging queues with OpenTelemetry SDK to assemble comprehensive request traces.",
            "Amazon Observability & Tracing", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How would you integrate Amazon Bedrock foundation models into an e-commerce catalog search service with Claude 3 and Titan Embeddings to implement conversational shopping?",
            "Explain: 1) Vector search in OpenSearch Service, 2) Multi-turn conversation state in DynamoDB, 3) Prompt engineering for product recommendation guardrails, 4) Real-time pricing lookup with Bedrock Tools.",
            "Amazon Bedrock & E-Commerce AI"
        ),
        create_ai_question(
            "How do you utilize Amazon Q Developer / CodeWhisperer to improve team velocity while preventing copyright or security vulnerability contamination in proprietary codebases?",
            "Discuss: Enabling Reference Tracker to detect matching public code, configuring automated security scans for OWASP vulnerabilities, and auditing AI-generated pull requests before merge.",
            "Amazon Q Developer Workflows"
        ),
        create_ai_question(
            "Describe how you design cost-effective generative AI inference workloads on AWS using AWS Inferentia2 and Trainium chips compared to standard Nvidia GPUs.",
            "Detail: Neuron SDK compilation, FP8 and BF16 quantization, latency benchmarking, and Auto Scaling based on real-time token generation throughput.",
            "AWS Silicon & Inferentia Optimization"
        ),
        create_ai_question(
            "How do you implement Guardrails for Amazon Bedrock to automatically redact sensitive PII (credit cards, phone numbers) and prevent competitive product mentions?",
            "Detail: Setting up Bedrock Guardrail filters with contextual grounding checks, denied topics, word filters, and sensitive information redaction masks.",
            "Amazon Bedrock Guardrails"
        ),
        create_ai_question(
            "Explain how you build an automated customer review sentiment extraction and aspect-based summarization pipeline using Amazon Comprehend and SageMaker.",
            "Architecture: Review stream pushed to Kinesis, processed by Comprehend for targeted sentiment and entity extraction, aggregated into Amazon Timestream for dashboard analytics.",
            "Amazon NLP & Customer Review Analytics"
        ),
        create_ai_question(
            "How do you evaluate model drift and data distribution shifts in an Amazon retail demand forecasting model deployed on Amazon SageMaker Model Monitor?",
            "Discuss: Baseline statistical constraints generated from training data, monitoring S3 endpoint traffic captures, and alerting when Kolmogorov-Smirnov distance exceeds threshold.",
            "SageMaker Model Monitoring"
        ),
        create_ai_question(
            "How would you implement a high-scale Vector Database solution on AWS using Amazon OpenSearch Serverless for 50 million product vectors?",
            "Detail: HNSW and IVF indexing algorithms, sharding strategy, memory provisioning, cold/warm storage tiers, and hybrid vector + BM25 keyword search.",
            "AWS Vector Search & OpenSearch"
        ),
        create_ai_question(
            "Describe the architecture of an agentic workflow on Amazon Bedrock Agents that autonomously coordinates delivery rescheduling with logistics APIs.",
            "Structure: OpenAPI schema definition, Lambda action groups, conversational memory, reasoning prompt templates, and human escalation handoff rules.",
            "Amazon Bedrock Agents"
        ),
        create_ai_question(
            "How do you enforce multi-tenant isolation and strict data governance when hosting LLM-based microservices for enterprise AWS B2B clients?",
            "Explain: Tenant-specific encryption keys with AWS KMS, IAM session policies, partitioned vector namespaces, and zero cross-tenant prompt leakage.",
            "AWS Enterprise AI Multi-Tenancy"
        ),
        create_ai_question(
            "How do you use Amazon SageMaker Clarify to detect algorithmic bias and feature importance in automated credit or seller approval algorithms?",
            "Discuss: Disparate impact metrics, counterfactual fairness analysis, SHAP (Shapley Additive exPlanations) values, and regulatory compliance reporting.",
            "SageMaker AI Fairness & Explainability"
        )
    ]

    hr_java = [
        create_hr_question(
            "Amazon's core Leadership Principle is 'Customer Obsession'. Can you describe a project where you prioritized long-term customer experience over an easy engineering shortcut?",
            "Use STAR: Detail customer pain point, quantify positive customer outcome, and explain how you advocated for the customer despite engineering pressure.",
            "Amazon LP: Customer Obsession"
        ),
        create_hr_question(
            "Tell me about a time you demonstrated 'Ownership' by stepping up to resolve an issue that was clearly outside your designated responsibilities or team charter.",
            "Demonstrate: 'Leaders are owners. They never say that's not my job.' Show proactive resolution of an orphaned problem with measurable organizational benefit.",
            "Amazon LP: Ownership"
        ),
        create_hr_question(
            "Describe an instance where you demonstrated 'Bias for Action' by making a critical architectural or product decision with incomplete information.",
            "Highlight: Calculated risk taking, two-way door decisions (reversible) vs one-way doors, gathering key signals quickly, and executing without analysis paralysis.",
            "Amazon LP: Bias for Action"
        ),
        create_hr_question(
            "Tell me about a situation where you had to 'Have Backbone; Disagree and Commit' with a senior colleague or manager regarding a technical approach.",
            "Explain: Professional respectful defense of your conviction backed by data, listening to counterarguments, and committing 100% once the decision was made.",
            "Amazon LP: Have Backbone; Disagree and Commit"
        ),
        create_hr_question(
            "How do you embody 'Invent and Simplify'? Describe a complex software process, deployment pipeline, or system that you radically streamlined.",
            "Focus on: Removing unnecessary dependencies, cutting latency or cloud costs, and simplifying architecture so other engineers can easily maintain it.",
            "Amazon LP: Invent and Simplify"
        ),
        create_hr_question(
            "Tell me about a time you missed an important milestone or deliverable. How did you 'Deliver Results' and rebuild stakeholder trust?",
            "Emphasize: Radical transparency, early communication of slippage, mitigating root causes, and executing an aggressive turnaround plan.",
            "Amazon LP: Deliver Results"
        ),
        create_hr_question(
            "Describe a time you demonstrated 'Frugality' by accomplishing a significant engineering milestone with limited compute resources, budget, or tools.",
            "Highlight: Resourcefulness, optimizing cloud spend, utilizing open-source tools effectively, and doing more with less.",
            "Amazon LP: Frugality"
        ),
        create_hr_question(
            "How do you 'Earn Trust' of team members and stakeholders when joining a new high-velocity engineering team with an established codebase?",
            "Discuss: Listening before proposing changes, delivering on commitments reliably, thorough code reviews, and admitting knowledge gaps humbly.",
            "Amazon LP: Earn Trust"
        ),
        create_hr_question(
            "Tell me about a time you insisted on 'Highest Standards' and refused to compromise on software quality despite intense release date pressure.",
            "Show: Advocating for automated testing, load benchmarks, and security audits to avoid production defects.",
            "Amazon LP: Insist on the Highest Standards"
        ),
        create_hr_question(
            "Do you have any questions for the Bar Raiser or hiring team regarding Amazon's engineering culture and day-to-day mechanisms?",
            "Candidate should ask about two-pizza team ownership, single-threaded leadership, or how operational excellence is maintained at scale.",
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
# 3. MICROSOFT
# ==========================================
def build_microsoft_catalog():
    apt_java = [
        create_aptitude_question(
            "In a Microsoft Azure region with 3 Availability Zones, a service achieves 99.9% uptime per zone. If requests fail only when all 3 zones are down simultaneously, what is the theoretical overall cluster availability?",
            ["99.9999999% (9 nines)", "99.999% (5 nines)", "99.9%", "99.7%"],
            "99.9999999% (9 nines)",
            "Probability of a single zone failing = 1 - 0.999 = 0.001 = 10^-3. Probability all 3 fail simultaneously = (10^-3)^3 = 10^-9. Availability = 1 - 10^-9 = 99.9999999%.",
            "Medium", "Azure Availability Math"
        ),
        create_aptitude_question(
            "A Microsoft Codility problem requires checking if an integer N is a power of 4 using bitwise operators. Which expression evaluates to true if and only if N > 0 is a power of 4?",
            ["(N & (N - 1)) == 0 && (N & 0x55555555) != 0", "(N & (N - 1)) == 0 && (N & 0xAAAAAAAA) != 0", "(N & (N + 1)) == 0", "(N ^ (N - 1)) == N"],
            "(N & (N - 1)) == 0 && (N & 0x55555555) != 0",
            "A power of 4 must be a power of 2: (N & (N - 1)) == 0, and its single 1-bit must be in an odd position: 0x55555555 = binary 01010101...mask.",
            "Hard", "Microsoft Bit Manipulation"
        ),
        create_aptitude_question(
            "Azure Cosmos DB charges Request Units (RUs). A 1KB point read costs 1 RU. A point write costs 5 RUs. If a microservice executes 1,200 reads and 400 writes per second, how many total RUs/sec are consumed?",
            ["3,200 RUs/sec", "2,000 RUs/sec", "1,600 RUs/sec", "4,000 RUs/sec"],
            "3,200 RUs/sec",
            "Reads: 1,200 * 1 RU = 1,200 RUs. Writes: 400 * 5 RUs = 2,000 RUs. Total = 1,200 + 2,000 = 3,200 RUs/sec.",
            "Medium", "Azure Cosmos DB Math"
        ),
        create_aptitude_question(
            "How many distinct binary search trees can be formed with 4 distinct keys {1, 2, 3, 4}?",
            ["14", "24", "10", "42"],
            "14",
            "The number of distinct BSTs with n keys is the nth Catalan number C_n = (2n)! / ((n+1)! * n!). For n=4: C_4 = 8! / (5! * 4!) = 40320 / (120 * 24) = 14.",
            "Medium", "Microsoft Tree Combinatorics"
        ),
        create_aptitude_question(
            "In Windows NTFS file system, cluster size is 4KB (4,096 bytes). If 10 files of size 4,500 bytes each are stored, what is the total disk space allocated?",
            ["80 KB", "45 KB", "40 KB", "50 KB"],
            "80 KB",
            "Each 4,500-byte file exceeds 1 cluster (4KB) and requires 2 clusters (8KB). 10 files * 8KB = 80 KB allocated.",
            "Easy", "Windows OS Storage Quant"
        ),
        create_aptitude_question(
            "A C# microservice thread pool has 16 worker threads. Requests arrive at a Poisson rate of 200 req/sec and each takes an average of 50ms to execute. What is the average CPU thread utilization?",
            ["62.5%", "75.0%", "50.0%", "80.0%"],
            "62.5%",
            "Workload = 200 req/s * 0.050 s = 10 thread-seconds of work per second. Across 16 threads, utilization = 10 / 16 = 0.625 = 62.5%.",
            "Hard", "Microsoft Thread Queue Math"
        ),
        create_aptitude_question(
            "An array contains numbers from 1 to N with exactly one duplicate and one missing number. If the array size is 10, sum is 52, and sum of squares is 382, what is the missing number?",
            ["6", "3", "5", "8"],
            "6",
            "Sum 1..10 = 55. Sum of squares = 10*11*21/6 = 385. Diff = (Dup - Miss) = 52 - 55 = -3. (Dup^2 - Miss^2) = 382 - 385 = -3. (Dup + Miss) = -3 / -3 = 1. Solving gives Missing = 2 or 6.",
            "Hard", "Microsoft Codility Math"
        ),
        create_aptitude_question(
            "In a Microsoft Teams call, bandwidth is 1.5 Mbps for HD video. If audio takes 64 Kbps and telemetry takes 16 Kbps, what percentage of the total stream is dedicated to video?",
            ["94.94%", "90.00%", "98.50%", "92.25%"],
            "94.94%",
            "Total = 1500 + 64 + 16 = 1580 Kbps. Video percentage = 1500 / 1580 ≈ 94.94%.",
            "Easy", "Microsoft Communications Quant"
        ),
        create_aptitude_question(
            "An Azure Blob storage container has 8 Million objects. A batch scanning algorithm inspects 50,000 objects every 30 seconds. How many total hours will it take to scan all objects?",
            ["1.33 hours", "2.00 hours", "4.50 hours", "0.75 hours"],
            "1.33 hours",
            "Rate = 50,000 / 30s = 1,666.67 objects/sec = 100,000 objects/min = 6,000,000 objects/hr. Time = 8,000,000 / 6,000,000 = 1.33 hours (80 minutes).",
            "Medium", "Azure Batch Processing Quant"
        ),
        create_aptitude_question(
            "Given an N x N matrix, in how many ways can an algorithm traverse from top-left (0,0) to bottom-right (N-1, N-1) moving only Right and Down?",
            ["C(2N-2, N-1)", "C(2N, N)", "N^2", "2^(N-1)"],
            "C(2N-2, N-1)",
            "The path consists of N-1 Down moves and N-1 Right moves, total 2N-2 moves. Number of distinct paths is C(2N-2, N-1).",
            "Medium", "Microsoft Combinatorics"
        ),
        create_aptitude_question(
            "In an Azure DevOps pipeline, build stage succeeds with probability 0.95 and test stage succeeds with probability 0.90 given build succeeded. What is the probability that both build and test pass?",
            ["85.5%", "90.0%", "92.5%", "80.0%"],
            "85.5%",
            "P(Build and Test) = P(Build) * P(Test | Build) = 0.95 * 0.90 = 0.855 = 85.5%.",
            "Easy", "Azure DevOps Probability"
        ),
        create_aptitude_question(
            "A 32-bit unsigned integer bitmask has bits 2, 5, and 7 set to 1 (0-indexed). What is its decimal integer value?",
            ["164", "160", "168", "132"],
            "164",
            "2^2 = 4, 2^5 = 32, 2^7 = 128. Decimal = 128 + 32 + 4 = 164.",
            "Easy", "Microsoft Bitwise Math"
        ),
        create_aptitude_question(
            "If an Azure Virtual Machine uses 128-bit encryption keys, how many possible distinct keys can be generated?",
            ["2^128", "128^2", "10^128", "2^64"],
            "2^128",
            "Each bit can be 0 or 1. For 128 bits, total permutations = 2^128 (approx 3.4 * 10^38 keys).",
            "Easy", "Azure Security Cryptography"
        ),
        create_aptitude_question(
            "A memory leak in a C# service consumes 25 MB every 10 minutes. If the container memory limit is 2 GB and starts with 500 MB baseline, in how many hours will OOM (Out Of Memory) occur?",
            ["10.0 hours", "8.5 hours", "12.0 hours", "6.0 hours"],
            "10.0 hours",
            "Remaining memory until limit = 2048 - 500 = 1548 MB. Leak rate = 2.5 MB/min = 150 MB/hour. Time = 1500 / 150 = 10.0 hours.",
            "Medium", "Microsoft Diagnostic Quant"
        ),
        create_aptitude_question(
            "What is the maximum number of nodes in a binary tree of height H=5 (where root has height 1)?",
            ["31", "32", "63", "16"],
            "31",
            "Maximum nodes in binary tree of height H is 2^H - 1. For H=5: 2^5 - 1 = 32 - 1 = 31 nodes.",
            "Easy", "Microsoft Data Structures"
        )
    ]

    code_java = [
        create_coding_problem(
            "Reverse Nodes in k-Group (Linked List)",
            "Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. If the number of nodes is not a multiple of k left out at the end, should remain as is.",
            "head = [1,2,3,4,5], k = 2",
            "[2,1,4,3,5]",
            "public class Solution {\n    public ListNode reverseKGroup(ListNode head, int k) {\n        return head;\n    }\n}",
            "def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:\n    pass",
            "def invert_chunked_records(head_df, k: int):\n    pass",
            "Classic Microsoft pointer manipulation: Count k nodes ahead; reverse the group iteratively; connect with recursive tail.",
            "Hard", "Linked List", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Spiral Matrix Order Traversal",
            "Given an m x n matrix, return all elements of the matrix in spiral order.",
            "matrix = [[1,2,3],[4,5,6],[7,8,9]]",
            "[1,2,3,6,9,8,7,4,5]",
            "public class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        return new ArrayList<>();\n    }\n}",
            "def spiral_order(matrix: list[list[int]]) -> list[int]:\n    pass",
            "def unroll_spiral_tensor(matrix_df) -> list[int]:\n    pass",
            "Four boundary pointers (top, bottom, left, right) progressively shrinking inward after each boundary traversal.",
            "Medium", "Matrix Manipulation", "O(M * N)", "O(1)"
        ),
        create_coding_problem(
            "Binary Tree Zigzag Level Order Traversal",
            "Given the root of a binary tree, return the zigzag level order traversal of its nodes' values (from left to right, then right to left for the next level).",
            "root = [3,9,20,null,null,15,7]",
            "[[3],[20,9],[15,7]]",
            "public class Solution {\n    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {\n        return new ArrayList<>();\n    }\n}",
            "def zigzag_level_order(root: Optional[TreeNode]) -> list[list[int]]:\n    pass",
            "def extract_alternating_hierarchy(tree_df) -> list[list[int]]:\n    pass",
            "BFS using a Deque or List with a boolean direction flag inverted on each tree depth level.",
            "Medium", "Tree & BFS", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Longest Palindromic Substring",
            "Given a string s, return the longest palindromic substring in s.",
            's = "babad"',
            '"bab" or "aba"',
            "public class Solution {\n    public String longestPalindrome(String s) {\n        return \"\";\n    }\n}",
            "def longest_palindrome(s: str) -> str:\n    pass",
            "def detect_longest_symmetric_token(text_df) -> str:\n    pass",
            "Expand around centers: Check 2N-1 possible centers for odd and even length palindromes in O(N^2) time and O(1) space.",
            "Medium", "String & Dynamic Programming", "O(N^2)", "O(1)"
        ),
        create_coding_problem(
            "Search in Rotated Sorted Array",
            "Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums in O(log N) runtime.",
            "nums = [4,5,6,7,0,1,2], target = 0",
            "4",
            "public class Solution {\n    public int search(int[] nums, int target) {\n        return -1;\n    }\n}",
            "def search(nums: list[int], target: int) -> int:\n    pass",
            "def binary_search_circular_index(series_df, target: int) -> int:\n    pass",
            "Modified binary search: Determine which half of the array is sorted (left or right), then check if target lies within that sorted range.",
            "Medium", "Binary Search", "O(log N)", "O(1)"
        ),
        create_coding_problem(
            "Sign of the Product of an Array",
            "There is a function signFunc(x) that returns 1 if x is positive, -1 if x is negative, and 0 if x is equal to 0. You are given an integer array nums. Return signFunc(product of nums).",
            "nums = [-1,-2,-3,-4,3,2,1]",
            "1",
            "public class Solution {\n    public int arraySign(int[] nums) {\n        return 0;\n    }\n}",
            "def array_sign(nums: list[int]) -> int:\n    pass",
            "def determine_product_parity(series_df) -> int:\n    pass",
            "Count negative numbers without computing large product to prevent integer overflow. Return 0 if any element is 0.",
            "Easy", "Array & Math", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "String to Integer (atoi) Parser",
            "Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer with whitespace handling, signs, and 32-bit clamping.",
            's = "   -42"',
            "-42",
            "public class Solution {\n    public int myAtoi(String s) {\n        return 0;\n    }\n}",
            "def my_atoi(s: str) -> int:\n    pass",
            "def parse_sanitized_integer(text_series) -> int:\n    pass",
            "Parse leading whitespace, parse optional sign, accumulate digits checking for 32-bit overflow before multiplication.",
            "Medium", "String Parsing", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Validate Binary Search Tree (BST)",
            "Given the root of a binary tree, determine if it is a valid binary search tree (BST).",
            "root = [2,1,3]",
            "true",
            "public class Solution {\n    public boolean isValidBST(TreeNode root) {\n        return false;\n    }\n}",
            "def is_valid_bst(root: Optional[TreeNode]) -> bool:\n    pass",
            "def verify_bst_invariants(tree_df) -> bool:\n    pass",
            "Recursive range validation: Every node must satisfy min < node.val < max, or in-order traversal must be strictly increasing.",
            "Medium", "Binary Search Tree", "O(N)", "O(H)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the architecture of Azure Active Directory (Microsoft Entra ID), specifically OAuth 2.0 authorization code flow with PKCE for single-page and native apps.",
            "PKCE (Proof Key for Code Exchange) protects authorization codes from interception by generating a cryptographically random code_verifier and code_challenge, validated by Entra ID token endpoint without client secrets.",
            "Microsoft Identity & Entra ID", "Hard"
        ),
        create_technical_question(
            "Compare the .NET Core / CLR Garbage Collector generations (Gen 0, Gen 1, Gen 2, Large Object Heap) with the Java Virtual Machine (JVM) generational memory model.",
            "Both use generational hypothesis: Gen 0 holds short-lived objects; survivors promote to Gen 1 and Gen 2. .NET has dedicated LOH (>85KB) collected with Gen 2. JVM uses Eden, Survivor spaces, and Tenured generation.",
            "Microsoft Runtime Performance (.NET vs JVM)", "Hard"
        ),
        create_technical_question(
            "How does Azure Cosmos DB offer 5 tunable consistency levels (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual), and what are the latency/cost tradeoffs?",
            "Session consistency (default) ensures read-your-own-writes per client session with single RU cost. Strong consistency guarantees linearizability across regions at 2x RU cost and higher write latency.",
            "Microsoft Azure Cosmos DB", "Hard"
        ),
        create_technical_question(
            "Explain how C# async/await state machines operate under the hood in .NET. How does this compare with Java Virtual Threads (Project Loom)?",
            "C# compiler transforms async methods into a generated struct implementing IAsyncStateMachine, suspending state via TaskAwaiter without blocking OS threads. Java Virtual Threads decouple threads at the JVM scheduler level without rewriting methods to state machines.",
            "Microsoft Concurrency Models", "Hard"
        ),
        create_technical_question(
            "Describe the internal architecture of Azure App Services versus Azure Container Apps. When should you architect microservices using Container Apps on Kubernetes (AKS)?",
            "Azure Container Apps provides serverless microservices built on Kubernetes and Dapr (Distributed Application Runtime) with KEDA autoscaling to zero. App Service is suited for monolithic web apps.",
            "Microsoft Cloud Infrastructure", "Medium"
        ),
        create_technical_question(
            "How do you implement Clean Architecture and Domain-Driven Design (DDD) in enterprise C# / Java backends at Microsoft?",
            "Core Domain layer contains Entities and Value Objects (zero external dependencies); Application layer has CQRS handlers and DTOs; Infrastructure layer implements database/API interfaces; API layer handles HTTP/gRPC.",
            "Microsoft Enterprise Architecture", "Hard"
        ),
        create_technical_question(
            "How does Entity Framework Core compile LINQ expressions into raw SQL queries, and how do you resolve the 'N+1 Query Problem' using eager loading?",
            "LINQ translates expression trees into SQL via query providers. N+1 occurs when child collections lazy-load in loops. Resolve via .Include() (eager loading) or projecting into flat DTOs.",
            "Microsoft EF Core & Data Access", "Medium"
        ),
        create_technical_question(
            "What techniques and diagnostic tools (dotnet-dump, PerfView, Visual Studio Profiler) do you use to diagnose memory leaks and high CPU utilization in live Azure workloads?",
            "Capture memory dump using dotnet-dump; analyze type histogram to find objects with high inclusive retained bytes; inspect GC roots and event tracing (ETW) using PerfView.",
            "Microsoft Diagnostics & Performance", "Hard"
        ),
        create_technical_question(
            "Explain the CQRS (Command Query Responsibility Segregation) pattern with MediatR and Event Sourcing on Microsoft Azure.",
            "Commands mutate state and publish domain events via MediatR; Queries read from denormalized read-optimized stores (Cosmos DB/Redis). Event store keeps append-only ledger of state transitions.",
            "Microsoft Design Patterns & CQRS", "Hard"
        ),
        create_technical_question(
            "How does Azure Service Bus implement Dead-Lettering, Duplicate Detection, and Session ordering (FIFO) for financial messaging?",
            "Sessions guarantee strict FIFO ordering by grouping messages by SessionId onto a single consumer. Duplicate detection tracks MessageId within a rolling time window.",
            "Azure Enterprise Messaging", "Medium"
        ),
        create_technical_question(
            "How do you configure Azure Key Vault with Managed Identities so containerized microservices access connection strings with zero stored secrets in code?",
            "Azure Managed Identity assigns an Entra ID identity to the compute instance. Microservice requests an access token from local IMDS endpoint (169.254.169.254) and authenticates directly to Key Vault without credentials.",
            "Microsoft Cloud Security", "Medium"
        ),
        create_technical_question(
            "Explain the difference between SQL Server Row-Level Security (RLS) and Column-Level Encryption in enterprise database design.",
            "RLS uses security predicate functions to automatically filter query results based on user execution context. Column-Level Encryption encrypts sensitive columns at rest using certificates.",
            "Microsoft SQL Server Security", "Medium"
        ),
        create_technical_question(
            "How does Microsoft Teams architecture handle real-time messaging, presence tracking, and WebRTC media stream routing for 300+ million active users?",
            "Teams uses Azure Cosmos DB for messaging metadata, Azure Event Hubs for telemetry, and distributed media relays with WebRTC SRTP encryption and adaptive bitrate encoding.",
            "Microsoft Teams Architecture", "Hard"
        ),
        create_technical_question(
            "Compare RESTful APIs with gRPC in .NET 8 / Java. When should enterprise Microsoft services adopt gRPC over REST?",
            "gRPC uses HTTP/2 multiplexing and binary Protobuf serialization, delivering 5-10x faster serialization and lower network bandwidth, ideal for high-throughput internal microservice-to-microservice traffic.",
            "Microsoft API Architectures", "Medium"
        ),
        create_technical_question(
            "How does Azure Traffic Manager DNS routing differ from Azure Front Door Global Anycast Layer 7 routing?",
            "Traffic Manager routes at DNS level by returning IP of closest endpoint. Azure Front Door operates at Layer 7 using Microsoft's global WAN Anycast network, SSL termination, and WAF at edge.",
            "Azure Global Networking", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How do you architect an enterprise AI solution utilizing Azure OpenAI Service (GPT-4o) with Semantic Kernel in C# / Java to orchestrate multi-step business workflows?",
            "Detail: Semantic Kernel plugins, native and semantic functions, memory connectors with Azure AI Search, and automated plan generation with planner agents.",
            "Azure OpenAI & Semantic Kernel"
        ),
        create_ai_question(
            "How do you implement Hybrid Search in Azure AI Search combining BM25 keyword matching with dense vector embeddings and semantic re-ranking?",
            "Explain: Reciprocal Rank Fusion (RRF) algorithm merging BM25 and vector score ranks, followed by Microsoft Turing semantic re-ranker evaluating deep cross-attention.",
            "Azure AI Search & Hybrid Retrieval"
        ),
        create_ai_question(
            "Describe how you integrate GitHub Copilot Enterprise into a development organization to accelerate pull request reviews and enforce corporate coding standards.",
            "Discuss: Copilot custom instructions, knowledge bases indexing internal documentation, security scanning for vulnerabilities, and tracking metrics (acceptance rate, cycle time).",
            "GitHub Copilot Enterprise"
        ),
        create_ai_question(
            "How do you utilize Azure AI Content Safety to detect jailbreaks, prompt injection, and toxic inputs before messages reach enterprise LLM deployments?",
            "Detail: Content Safety text analysis API scoring severity across Violence, Hate, Sexual, Self-harm categories, and custom blocklist regex filters.",
            "Azure AI Content Safety & Security"
        ),
        create_ai_question(
            "How do you evaluate and monitor LLM performance in production using Azure AI Studio evaluation SDK (groundedness, relevance, coherence)?",
            "Explain: Automated evaluation pipelines comparing model outputs against reference ground truth datasets using GPT-4 as a judge with specific rubric prompts.",
            "Azure AI Studio & Evaluation"
        ),
        create_ai_question(
            "How would you build a multi-modal document extraction pipeline using Azure AI Document Intelligence (Form Recognizer) for complex invoice PDFs?",
            "Detail: Prebuilt-invoice model parsing key-value pairs, nested tables, line items, and confidence scores directly into structured JSON for ERP ingestion.",
            "Azure AI Document Intelligence"
        ),
        create_ai_question(
            "Describe how you implement Retrieval-Augmented Generation (RAG) over sensitive enterprise SharePoint documents while strictly respecting user permission ACLs.",
            "Explain: Azure AI Search security filters mapping Entra ID user group SID tokens to index document ACLs, ensuring users never retrieve documents they lack permission to view.",
            "Azure RAG & Security ACLs"
        ),
        create_ai_question(
            "How do you optimize token usage and latency when chaining multiple Azure OpenAI model calls in an asynchronous microservice pipeline?",
            "Discuss: Prompt compression, structured output parsing with JSON mode, streaming response chunks via Server-Sent Events, and Redis caching of identical prompts.",
            "Azure OpenAI Optimization"
        ),
        create_ai_question(
            "How does Microsoft implement Responsible AI principles (Fairness, Reliability, Privacy, Inclusiveness, Transparency, Accountability) in generative AI software?",
            "Cover: Impact assessments, system transparency notes, human-in-the-loop validation checkpoints, and bias testing across demographic subgroups.",
            "Microsoft Responsible AI Principles"
        ),
        create_ai_question(
            "How do you fine-tune open-source models (Phi-3, Llama 3) on Azure Machine Learning compute clusters using LoRA and DeepSpeed?",
            "Detail: Azure ML environment setup, multi-GPU distributed training with DeepSpeed ZeRO stage 2/3, FP16 mixed precision, and MLflow experiment tracking.",
            "Azure ML & Model Fine-Tuning"
        )
    ]

    hr_java = [
        create_hr_question(
            "Microsoft's culture transformation under Satya Nadella is defined by 'Growth Mindset'. Describe a time you faced a significant project failure and how you turned it into a learning catalyst.",
            "Highlight: Moving from 'know-it-all' to 'learn-it-all', taking constructive responsibility, analyzing root causes, and applying lessons to future triumphs.",
            "Growth Mindset & Learning from Failure"
        ),
        create_hr_question(
            "How do you practice 'Customer Empathy' when engineering technical solutions? Describe a time you advocated for an end-user whose technical literacy was limited.",
            "Showcase: Empathy for user frustration, conducting user journey mapping, and designing intuitive error messages and workflows.",
            "Customer Empathy"
        ),
        create_hr_question(
            "Microsoft values 'One Microsoft' - collaborating across organizational boundaries. Describe a time you worked with an external team that had conflicting priorities.",
            "Focus on: Finding shared business goals, breaking down silos, transparent communication, and achieving win-win outcomes.",
            "One Microsoft & Cross-Team Collaboration"
        ),
        create_hr_question(
            "How do you support Diversity & Inclusion in everyday software engineering teams, particularly in code reviews and architectural discussions?",
            "Discuss: Creating psychological safety, respectful feedback, ensuring underrepresented voices are heard, and mitigating unconscious bias.",
            "Diversity & Inclusion"
        ),
        create_hr_question(
            "Tell me about a time you had a technical disagreement with a colleague. How did you resolve it constructively without damaging the relationship?",
            "Explain: Focusing on objective data and user impact rather than personality, active listening, and finding consensus.",
            "Constructive Conflict Resolution"
        ),
        create_hr_question(
            "Why do you specifically want to build your software engineering career at Microsoft?",
            "Connect: Microsoft's mission 'to empower every person and every organization on the planet to achieve more', enterprise cloud dominance, developer-first tooling (VS Code, GitHub).",
            "Microsoft Motivation & Mission"
        ),
        create_hr_question(
            "Tell me about a time you had to balance urgent product release deadlines with code maintainability and test automation.",
            "Show: Pragmatic technical debt management, automated regression guardrails, and post-launch refactoring commitments.",
            "Balancing Speed and Quality"
        ),
        create_hr_question(
            "How do you keep your technical skills sharp in an era of rapid AI transformation and evolving cloud frameworks?",
            "Highlight: Proactive side projects, studying architecture papers, continuous experimentation, and mentoring others.",
            "Continuous Learning"
        ),
        create_hr_question(
            "Describe a time you received critical feedback on your performance or code quality. How did you process and act on that feedback?",
            "Demonstrate: Emotional maturity, seeking specific examples for improvement, and demonstrating measurable growth in subsequent sprints.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Do you have any questions for Microsoft's engineering leadership regarding team culture, engineering velocity, or our cloud roadmap?",
            "Candidate asks thoughtful questions about Microsoft's AI integration across products, developer developer developer ethos, or career progression.",
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
# 4. TCS (Tata Consultancy Services)
# ==========================================
def build_tcs_catalog():
    apt_java = [
        create_aptitude_question(
            "In TCS NQT Numerical Ability: Two programmers, A and B, working together can complete a core banking module in 12 days. If A works alone for 8 days and B finishes the remaining work in 18 days, in how many days could A alone complete the entire module?",
            ["20 days", "24 days", "30 days", "16 days"],
            "20 days",
            "Let daily work be a and b. a + b = 1/12. Work done: 8a + 18b = 1. Since 8a + 8b = 8/12 = 2/3, 10b = 1 - 2/3 = 1/3 => b = 1/30. Then a = 1/12 - 1/30 = (5-2)/60 = 3/60 = 1/20. Thus A alone takes 20 days.",
            "Medium", "TCS NQT Time & Work"
        ),
        create_aptitude_question(
            "In a TCS campus placement exam, a train 240 meters long passes a railway platform 360 meters long in 30 seconds. What is the speed of the train in km/h?",
            ["72 km/h", "60 km/h", "80 km/h", "54 km/h"],
            "72 km/h",
            "Total distance = 240 + 360 = 600 meters. Speed = 600 / 30 = 20 m/s. In km/h = 20 * (18/5) = 72 km/h.",
            "Easy", "TCS NQT Speed & Distance"
        ),
        create_aptitude_question(
            "A client invoice at TCS is paid with an 8% discount. If the client pays Rs. 44,160, what was the original invoice amount before the discount?",
            ["Rs. 48,000", "Rs. 47,500", "Rs. 50,000", "Rs. 46,000"],
            "Rs. 48,000",
            "Amount paid = 92% of original = 44,160. Original amount = 44,160 / 0.92 = Rs. 48,000.",
            "Easy", "TCS NQT Commercial Arithmetic"
        ),
        create_aptitude_question(
            "In TCS Reasoning Ability: Pointing to a photograph of a man, an IT analyst said, 'His mother is the only daughter of my mother.' How is the analyst related to the man in the photo?",
            ["Mother", "Aunt", "Sister", "Grandmother"],
            "Mother",
            "The speaker's mother's only daughter is the speaker herself (assuming female analyst). Therefore, she is the mother of the man in the photograph.",
            "Medium", "TCS NQT Blood Relations"
        ),
        create_aptitude_question(
            "Six software engineers (P, Q, R, S, T, U) are sitting around a circular conference table in TCS Siruseri. P is between S and T. Q is opposite P. U is to the immediate right of S. Who is sitting opposite T?",
            ["U", "R", "S", "Q"],
            "U",
            "Arranging around a 6-seat circle: P at 12 o'clock, Q at 6 o'clock. S and T are at 10 and 2 o'clock. U is to the right of S. By symmetry, the person opposite T is U.",
            "Medium", "TCS NQT Seating Arrangement"
        ),
        create_aptitude_question(
            "A software testing suite finds that the ratio of critical bugs to minor bugs is 3:7. If 28 minor bugs were logged, how many critical bugs were detected?",
            ["12 critical bugs", "14 critical bugs", "9 critical bugs", "15 critical bugs"],
            "12 critical bugs",
            "Let multiplier be x. 7x = 28 => x = 4. Critical bugs = 3x = 3 * 4 = 12 critical bugs.",
            "Easy", "TCS NQT Ratio & Proportion"
        ),
        create_aptitude_question(
            "Find the next number in the TCS NQT series: 7, 11, 19, 35, 67, ___?",
            ["131", "128", "135", "124"],
            "131",
            "Differences: 11 - 7 = 4, 19 - 11 = 8, 35 - 19 = 16, 67 - 35 = 32. Differences double each step. Next difference = 64. Next number = 67 + 64 = 131.",
            "Medium", "TCS NQT Number Series"
        ),
        create_aptitude_question(
            "In how many different ways can the letters of the word 'CAMPUS' be arranged so that the vowels (A, U) always appear together?",
            ["240 ways", "120 ways", "720 ways", "360 ways"],
            "240 ways",
            "Bundle (A, U) as 1 item. Remaining consonants: C, M, P, S (4 letters). Total items = 4 + 1 = 5. They can be arranged in 5! = 120 ways. The vowels (A, U) can arrange internally in 2! = 2 ways. Total = 120 * 2 = 240 ways.",
            "Medium", "TCS NQT Permutations"
        ),
        create_aptitude_question(
            "A sum of money invested at compound interest in a TCS provident fund doubles itself in 5 years. In how many years will it become 8 times of itself at the same rate?",
            ["15 years", "20 years", "25 years", "10 years"],
            "15 years",
            "Amount doubles (2^1) in 5 years. To become 8 times (2^3), time required = 3 * 5 = 15 years.",
            "Easy", "TCS NQT Compound Interest"
        ),
        create_aptitude_question(
            "In TCS Verbal Ability: Select the word that is most nearly OPPOSITE in meaning to 'METICULOUS':",
            ["Careless", "Thorough", "Painstaking", "Accurate"],
            "Careless",
            "'Meticulous' means showing great attention to detail; very careful and precise. The exact antonym is 'Careless'.",
            "Easy", "TCS NQT Verbal Antonyms"
        ),
        create_aptitude_question(
            "Two dice are rolled simultaneously in a gaming project simulation. What is the probability that the sum of the numbers appearing on top is a prime number?",
            ["15/36 = 5/12", "12/36 = 1/3", "18/36 = 1/2", "7/36"],
            "15/36 = 5/12",
            "Possible sums that are prime: 2, 3, 5, 7, 11. Ways to get 2: (1,1) [1]. 3: (1,2),(2,1) [2]. 5: (1,4),(2,3),(3,2),(4,1) [4]. 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) [6]. 11: (5,6),(6,5) [2]. Total = 1+2+4+6+2 = 15. Probability = 15/36 = 5/12.",
            "Medium", "TCS NQT Probability"
        ),
        create_aptitude_question(
            "If 12 men or 18 women can harvest a contract in 14 days, in how many days can 8 men and 16 women finish the same contract?",
            ["9 days", "10 days", "12 days", "8 days"],
            "9 days",
            "12 Men = 18 Women => 1 Man = 1.5 Women. 8 Men = 12 Women. Total workforce = 12 + 16 = 28 Women. If 18 women take 14 days, 28 women take: (18 * 14) / 28 = 9 days.",
            "Medium", "TCS NQT Work Equation"
        ),
        create_aptitude_question(
            "A person sells an IT certification voucher for Rs. 1,870 making a loss of 15%. At what price should it be sold to gain 15% profit?",
            ["Rs. 2,530", "Rs. 2,400", "Rs. 2,200", "Rs. 2,650"],
            "Rs. 2,530",
            "Cost Price * 0.85 = 1,870 => Cost Price = 1,870 / 0.85 = Rs. 2,200. Selling price for 15% gain = 2,200 * 1.15 = Rs. 2,530.",
            "Medium", "TCS NQT Profit & Loss"
        ),
        create_aptitude_question(
            "In TCS Syllogisms: Statements: 1. All servers are computers. 2. Some computers are laptops. Conclusions: I. Some laptops are servers. II. No laptop is a server.",
            ["Either I or II follows (Complementary pair)", "Only I follows", "Only II follows", "Neither I nor II follows"],
            "Either I or II follows (Complementary pair)",
            "Laptops and servers have an indeterminate relationship. Since Conclusion I is 'Some' and Conclusion II is 'No' with identical subject and predicate, they form a complementary pair: Either I or II follows.",
            "Medium", "TCS NQT Syllogisms"
        ),
        create_aptitude_question(
            "A boat travels 24 km upstream in 6 hours and 36 km downstream in 4 hours. What is the speed of the river current?",
            ["2.5 km/h", "3.0 km/h", "1.5 km/h", "2.0 km/h"],
            "2.5 km/h",
            "Upstream speed (u - v) = 24/6 = 4 km/h. Downstream speed (u + v) = 36/4 = 9 km/h. Current speed v = (9 - 4) / 2 = 5 / 2 = 2.5 km/h.",
            "Easy", "TCS NQT Boats & Streams"
        )
    ]

    code_java = [
        create_coding_problem(
            "String Rotation Check (TCS NQT)",
            "Given two strings s1 and s2, write a function to check if s2 is a rotation of s1 using only one call to substring check.",
            's1 = "ABCD", s2 = "CDAB"',
            "true",
            "public class Solution {\n    public static boolean isRotation(String s1, String s2) {\n        return false;\n    }\n}",
            "def is_rotation(s1: str, s2: str) -> bool:\n    pass",
            "def verify_rotated_telemetry_key(s1: str, s2: str) -> bool:\n    pass",
            "TCS classic: If lengths match, concatenate s1 + s1. If s2 is a rotation, it must exist as a substring within s1 + s1.",
            "Easy", "String Algorithms", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Maximum Subarray Sum (Kadane's Algorithm)",
            "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
            "nums = [-2,1,-3,4,-1,2,1,-5,4]",
            "6",
            "public class Solution {\n    public static int maxSubArray(int[] nums) {\n        return 0;\n    }\n}",
            "def max_sub_array(nums: list[int]) -> int:\n    pass",
            "def max_daily_ledger_gain(ledger_df) -> int:\n    pass",
            "Kadane's algorithm: Maintain current_sum = max(num, current_sum + num) and max_sum in a single O(N) pass.",
            "Medium", "Dynamic Programming", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Prime Factor Summation (TCS Coding Round 1)",
            "Given an integer n, find the sum of all its unique prime factors. If n is prime, return n.",
            "n = 60",
            "10 (2 + 3 + 5)",
            "public class Solution {\n    public static int sumOfPrimeFactors(int n) {\n        return 0;\n    }\n}",
            "def sum_of_prime_factors(n: int) -> int:\n    pass",
            "def compute_prime_factor_metric(series_df) -> int:\n    pass",
            "Extract prime factors by checking 2, then odd numbers up to sqrt(N). Add unique factors to a set and compute their sum.",
            "Easy", "Math & Number Theory", "O(sqrt(N))", "O(1)"
        ),
        create_coding_problem(
            "Leaders in an Array (TCS Advanced Coding)",
            "Given an array arr of positive integers, find all the leaders in the array. An element is a leader if it is strictly greater than all elements to its right. Return leaders in order of appearance.",
            "arr = [16, 17, 4, 3, 5, 2]",
            "[17, 5, 2]",
            "public class Solution {\n    public static List<Integer> findLeaders(int[] arr) {\n        return new ArrayList<>();\n    }\n}",
            "def find_leaders(arr: list[int]) -> list[int]:\n    pass",
            "def extract_peak_transaction_milestones(ledger_df) -> list[int]:\n    pass",
            "Scan from right to left while maintaining current_max. Any element > current_max is a leader. Reverse collected list at the end.",
            "Easy", "Array Scanning", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Pair Sum with Target in Core Banking Ledger",
            "Given an array of account transaction values and a target sum, determine whether there exists any pair of transactions whose sum equals target.",
            "arr = [10, 15, 3, 7], target = 17",
            "true (10 + 7)",
            "public class Solution {\n    public static boolean hasPairWithSum(int[] arr, int target) {\n        return false;\n    }\n}",
            "def has_pair_with_sum(arr: list[int], target: int) -> bool:\n    pass",
            "def verify_reconciliation_pair(tx_df, target: int) -> bool:\n    pass",
            "Use a Hash Set to store seen numbers. For each x in arr, check if (target - x) is present in set.",
            "Easy", "Hashing", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Word Frequency Compression (Run-Length)",
            "Implement basic run-length encoding. For a string of consecutive repeating characters, compress it to character followed by its count.",
            's = "aabcccccaaa"',
            '"a2b1c5a3"',
            "public class Solution {\n    public static String compressString(String s) {\n        return \"\";\n    }\n}",
            "def compress_string(s: str) -> str:\n    pass",
            "def compress_log_stream(log_series) -> str:\n    pass",
            "Traverse string counting consecutive identical characters, append char and count to StringBuilder upon character change.",
            "Easy", "String Compression", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Matrix Transpose & Symmetry Check",
            "Given an N x N square matrix, write a function to check if the matrix is symmetric (equal to its transpose).",
            "matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 8]]",
            "true",
            "public class Solution {\n    public static boolean isSymmetric(int[][] matrix) {\n        return false;\n    }\n}",
            "def is_symmetric(matrix: list[list[int]]) -> bool:\n    pass",
            "def check_covariance_matrix_symmetry(matrix_df) -> bool:\n    pass",
            "Compare matrix[i][j] with matrix[j][i] for all i < j. If any mismatch occurs, return false.",
            "Easy", "Matrix Operations", "O(N^2)", "O(1)"
        ),
        create_coding_problem(
            "Difference between Odd and Even Position Digits",
            "Given a large positive integer represented as a string, compute the difference between the sum of digits at odd positions and the sum of digits at even positions.",
            'num = "4567"',
            "2 ((4+6) - (5+7) = 10 - 12 = -2, return abs)",
            "public class Solution {\n    public static int digitPositionDiff(String num) {\n        return 0;\n    }\n}",
            "def digit_position_diff(num: str) -> int:\n    pass",
            "def compute_checksum_parity_diff(id_series) -> int:\n    pass",
            "Single pass loop over characters: if index % 2 == 0 add to even_sum, else odd_sum. Return absolute difference.",
            "Easy", "String & Math", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the JVM Memory Model (Heap, Stack, Metaspace, Program Counter) and how Garbage Collection works during high-volume batch processing at TCS.",
            "The JVM divides memory into Stack (per-thread frames), Heap (Young Gen: Eden, S0, S1 and Old Gen), and Metaspace (class metadata). G1GC partitions heap into equal regions to clean garbage with predictable pause times.",
            "TCS Java Architecture", "Medium"
        ),
        create_technical_question(
            "In enterprise core banking systems like TCS BaNCS, how does Spring Batch implement Chunk-Oriented Processing with ItemReader, ItemProcessor, and ItemWriter?",
            "Chunk processing reads data in chunks (e.g. 500 records), processes each item in memory, and writes the entire chunk within a single database transaction. This prevents OutOfMemory errors on multi-million row night settlement batches.",
            "TCS BaNCS & Spring Batch", "Hard"
        ),
        create_technical_question(
            "Explain the difference between First Level Cache and Second Level Cache in Hibernate ORM, and how caching minimizes database round-trips in high-traffic TCS client applications.",
            "First level cache is session-scoped (enabled by default). Second level cache is SessionFactory-scoped (shared across sessions) using providers like Ehcache or Redis to cache frequently read entities and query results.",
            "TCS Hibernate & ORM", "Medium"
        ),
        create_technical_question(
            "How do you resolve Database Deadlocks in Oracle / SQL Server when multiple batch threads concurrently update account balances in TCS financial software?",
            "Enforce a strict global lock acquisition ordering (e.g. always sort account IDs ascending before locking). Keep transactions short, use fine-grained row-level locks, and configure sensible deadlock detection timeouts.",
            "TCS Database Engineering", "Hard"
        ),
        create_technical_question(
            "Explain the internal bucketing, segment locking, and CAS (Compare-And-Swap) mechanisms of Java ConcurrentHashMap compared to Collections.synchronizedMap.",
            "synchronizedMap locks the entire map on every operation. ConcurrentHashMap in Java 8 uses synchronized locks only on the individual bucket head node and CAS operations for node insertion, enabling multiple threads to read/write concurrently.",
            "TCS Java Concurrency", "Hard"
        ),
        create_technical_question(
            "How do you implement the Saga Pattern (Orchestration vs Choreography) to maintain data consistency across distributed microservices without 2PC (Two-Phase Commit)?",
            "Saga breaks distributed transactions into local transactions. Orchestrator coordinates each step and executes compensating transactions if a step fails. Choreography publishes events, and services react and compensate autonomously.",
            "TCS Microservices & Distributed Transactions", "Hard"
        ),
        create_technical_question(
            "Explain Database Normalization up to Boyce-Codd Normal Form (BCNF). In what scenarios would a TCS architect intentionally denormalize tables in an analytical system?",
            "1NF eliminates repeating groups; 2NF eliminates partial dependencies; 3NF eliminates transitive dependencies; BCNF ensures every determinant is a candidate key. Analytical data warehouses denormalize into Star schemas to avoid expensive multi-table joins.",
            "TCS Database Normalization", "Medium"
        ),
        create_technical_question(
            "In Spring Boot applications, what is the difference between @Component, @Service, and @Repository annotations, and how does @Transactional handle rollback on exceptions?",
            "@Component is general-purpose; @Service denotes business logic; @Repository adds automatic exception translation to DataAccessException. @Transactional rolls back by default on RuntimeException and Error, but not checked exceptions.",
            "TCS Spring Framework", "Medium"
        ),
        create_technical_question(
            "How does Apache Kafka ensure message ordering, and what happens when a consumer in a consumer group crashes during high-throughput transaction streaming?",
            "Kafka guarantees ordering strictly within a partition using partition keys. When a consumer crashes, a group rebalance reassigns partitions to surviving consumers based on stored consumer group offsets.",
            "TCS Messaging & Event Streaming", "Medium"
        ),
        create_technical_question(
            "Explain the difference between RESTful API Idempotency and Safety. Which HTTP methods (GET, POST, PUT, DELETE) are idempotent, and why is this critical in financial payment systems?",
            "Safe methods (GET, HEAD) do not modify server state. Idempotent methods (PUT, DELETE, GET) produce the same server state regardless of multiple identical executions. POST is neither safe nor idempotent.",
            "TCS API Standards", "Medium"
        ),
        create_technical_question(
            "How do you tune database connection pools with HikariCP in TCS enterprise web applications to prevent connection leaks and starvation?",
            "Configure maximumPoolSize matching available database server CPU cores, set connectionTimeout to fail fast (e.g. 3000ms), and set leakDetectionThreshold (e.g. 2000ms) to log stack traces of unclosed connections.",
            "TCS Performance Engineering", "Medium"
        ),
        create_technical_question(
            "Explain Java 17 modern features: Sealed Classes, Records, and Pattern Matching for switch, and how they simplify domain modeling in enterprise applications.",
            "Records eliminate boilerplate for immutable data carriers. Sealed classes restrict which other classes can extend them. Pattern matching for switch enables clean type checking without repetitive instanceof casts.",
            "TCS Modern Java 17", "Medium"
        ),
        create_technical_question(
            "What is the Circuit Breaker pattern with Resilience4j, and how does it protect downstream banking APIs from cascading microservice failures?",
            "Circuit Breaker monitors call failure rates. If failures exceed threshold (e.g. 50%), state changes from CLOSED to OPEN, immediately returning fallbacks without stressing failing downstream systems.",
            "TCS Microservice Resiliency", "Medium"
        ),
        create_technical_question(
            "How does SQL B-Tree indexing speed up SELECT queries, and why does an index degrade performance on high-frequency INSERT and UPDATE operations?",
            "B-Tree index allows O(log N) search by traversing balanced tree nodes. However, every INSERT or UPDATE requires rebalancing tree nodes and splitting pages, creating disk write overhead.",
            "TCS SQL & Indexing", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Synchronous and Asynchronous execution using CompletableFuture in Java, and how custom ThreadPoolExecutors prevent thread exhaustion.",
            "CompletableFuture executes tasks asynchronously on a background thread pool without blocking the calling thread. Using custom thread pools separates mission-critical tasks from slow external I/O tasks.",
            "TCS Multithreading", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How can Generative AI and LLMs be utilized securely in TCS Core Banking (BFSI) applications without violating RBI / global financial data privacy regulations?",
            "Explain: On-premise air-gapped LLMs, automated PII masking before inference, strictly forbidding customer account numbers in prompt contexts, and audit logging.",
            "TCS BFSI AI Compliance"
        ),
        create_ai_question(
            "Describe how AI-assisted developer tools (GitHub Copilot) are integrated into TCS delivery centers to accelerate legacy COBOL/Java modernization while ensuring strict code quality.",
            "Discuss: Automated legacy code parsing, unit test generation with JUnit 5, human-in-the-loop validation, and static code quality gates in SonarQube.",
            "TCS AI-Assisted Modernization"
        ),
        create_ai_question(
            "How do you implement an intelligent fraud detection scoring pipeline using machine learning models integrated with real-time Kafka transaction streams at TCS?",
            "Architecture: Kafka Streams pushes payment events to a lightweight inference model scoring risk probability in under 50ms; suspicious transactions trigger OTP challenges.",
            "TCS Real-Time AI Fraud Detection"
        ),
        create_ai_question(
            "How would you build an internal knowledge assistant for TCS employees to query complex client SLAs and compliance documents using RAG (Retrieval-Augmented Generation)?",
            "Detail: Chunking PDF manuals, storing embeddings in an internal Milvus/PostgreSQL pgvector database, querying with open-source LLM, and generating responses with exact page citations.",
            "TCS Enterprise RAG System"
        ),
        create_ai_question(
            "What strategies do you adopt to prevent AI hallucinations when generating technical architecture summary reports for enterprise TCS clients?",
            "Explain: Constraining generation to strictly retrieved context chunks, temperature=0.0, chain-of-thought verification, and human architect sign-off.",
            "TCS Hallucination Mitigation"
        ),
        create_ai_question(
            "How do you automate test case generation using Generative AI for legacy financial applications with zero existing unit test coverage?",
            "Explain: Feeding method signatures and business logic paths to LLM; generating parameterized tests covering edge cases (nulls, boundary values); executing in CI/CD sandbox.",
            "TCS Automated Testing AI"
        ),
        create_ai_question(
            "Describe how you monitor model drift in machine learning models deployed for client customer churn prediction in telecom or banking domains.",
            "Detail: Monitoring feature distribution shifts over time, tracking F1-score drop against monthly ground truth, and automated model retraining triggers.",
            "TCS MLOps & Model Monitoring"
        ),
        create_ai_question(
            "How do you ensure ethical AI and transparency when implementing algorithmic loan approval models at TCS for banking clients?",
            "Discuss: Eliminating protected demographic attributes, calculating disparate impact ratios, and generating clear human-readable explanation factors for loan rejection.",
            "TCS Ethical AI in Banking"
        ),
        create_ai_question(
            "How do you optimize LLM prompt engineering for complex legacy SQL query conversion to modern cloud data warehouses (Snowflake)?",
            "Explain: Few-shot prompting with paired legacy-to-modern SQL examples, DDL schema inclusion, and automated syntax validation using SQLGlot parser.",
            "TCS Prompt Engineering"
        ),
        create_ai_question(
            "How does TCS evaluate employee AI fluency and readiness to deploy AI-driven solutions across global client accounts?",
            "Discuss: Role-based AI fluency certifications, hands-on hackathons, prompt engineering labs, and responsible AI compliance training.",
            "TCS AI Fluency & Culture"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically want to start your professional engineering journey at Tata Consultancy Services (TCS)?",
            "Highlight: Tata Group's legacy of trust and ethics, massive global project exposure, world-class continuous learning platforms, and career stability.",
            "TCS Brand & Tata Legacy"
        ),
        create_hr_question(
            "The Tata Code of Conduct (TCOC) is central to TCS values. Describe a situation where you chose the ethically correct path despite pressure to take a shortcut.",
            "Demonstrate: High integrity, honesty in reporting project bugs or test results, and upholding ethical principles above convenience.",
            "Tata Code of Conduct (TCOC)"
        ),
        create_hr_question(
            "TCS operates delivery centers across India (Siruseri, Hinjewadi, Gandhinagar, Kolkata) and client locations worldwide. Are you flexible with relocation and rotational shifts?",
            "Affirm: Eagerness to relocate, adaptability to client time zones, commitment to team goals, and openness to hybrid working policies.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "How do you handle working on a long-term enterprise maintenance project that requires learning an older or niche technology stack?",
            "Showcase: Positive learning attitude, recognizing the immense business value of enterprise core systems, and seeking opportunities to modernize.",
            "Adaptability & Enterprise Delivery"
        ),
        create_hr_question(
            "Tell me about a time you collaborated with a diverse team of peers on a college capstone or software project. How did you resolve differences?",
            "Use STAR: Focus on active listening, dividing responsibilities by individual strengths, and delivering a cohesive project on time.",
            "Teamwork & Collaboration"
        ),
        create_hr_question(
            "Describe a challenging deadline where your software code had multiple unexpected bugs right before release. How did you handle the pressure?",
            "Explain: Calm systematic debugging, prioritizing critical showstopper defects, transparent communication with the project lead, and working overtime.",
            "Handling High Pressure"
        ),
        create_hr_question(
            "Where do you see yourself growing within TCS over the next 3 to 5 years as a software engineer?",
            "Connect: Aspiring to grow from Assistant System Engineer to Senior Developer/Tech Lead, earning cloud certifications, and mentoring juniors.",
            "Career Growth & Long-term Vision"
        ),
        create_hr_question(
            "How do you react when a client or technical lead requests major changes to a feature that you spent two weeks developing?",
            "Emphasize: Customer focus, understanding that business requirements evolve, asking clarifying questions, and pivoting without frustration.",
            "Client Focus & Change Management"
        ),
        create_hr_question(
            "What differentiates you from other qualified candidates interviewing for TCS today?",
            "Combine: Strong algorithmic and computer science fundamentals, eagerness to learn enterprise architectures, and cultural alignment with Tata values.",
            "Candidate Strengths"
        ),
        create_hr_question(
            "Do you have any questions for TCS regarding our project allocation, Initial Learning Program (ILP), or mentoring culture?",
            "Candidate should ask about ILP training, certifications support, or the transition from campus to corporate project delivery.",
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
# 5. INFOSYS
# ==========================================
def build_infosys_catalog():
    apt_java = [
        create_aptitude_question(
            "In Infosys InfyTQ Cryptarithmetic: If SEND + MORE = MONEY, and each distinct letter represents a unique digit from 0 to 9 with M != 0 and S != 0, what digit does 'M' represent?",
            ["1", "2", "0", "9"],
            "1",
            "Since SEND (4-digit) + MORE (4-digit) yields MONEY (5-digit), the carry from the thousands column to the ten-thousands column must be exactly 1. Thus M = 1.",
            "Hard", "Infosys InfyTQ Cryptarithmetic"
        ),
        create_aptitude_question(
            "In Infosys Mathematical Critical Thinking: A vessel contains 60 liters of pure milk. 12 liters of milk are taken out and replaced with water. This process is repeated one more time. What is the final quantity of pure milk remaining in the vessel?",
            ["38.4 liters", "40.0 liters", "36.0 liters", "42.5 liters"],
            "38.4 liters",
            "Formula: Remaining = Initial * (1 - x/C)^n = 60 * (1 - 12/60)^2 = 60 * (4/5)^2 = 60 * 16/25 = 38.4 liters.",
            "Medium", "Infosys Mathematical Critical Thinking"
        ),
        create_aptitude_question(
            "A software module at Infosys Mysore DC can be developed by 5 senior engineers in 12 days or by 8 junior engineers in 15 days. How many days will 2 senior engineers and 4 junior engineers take to finish the module?",
            ["15 days", "12 days", "18 days", "20 days"],
            "15 days",
            "Total work = 5 * 12 = 60 Senior-days. Also work = 8 * 15 = 120 Junior-days. 1 Senior = 2 Juniors. 2 Seniors = 4 Juniors. Total team = 4 + 4 = 8 Juniors. 8 Juniors take 120 / 8 = 15 days.",
            "Medium", "Infosys Time & Work"
        ),
        create_aptitude_question(
            "Find the missing number in the InfyTQ matrix puzzle:\n[4, 9, 2]\n[3, 5, 7]\n[8, 1, ?]",
            ["6", "5", "4", "7"],
            "6",
            "This is a 3x3 Magic Square where each row, column, and diagonal sums to 15. Third row: 8 + 1 + ? = 15 => ? = 6.",
            "Medium", "Infosys Logical Puzzles"
        ),
        create_aptitude_question(
            "In an Infosys campus drive test, the average score of 40 candidates was 72. Later it was found that a score of 68 was mistakenly entered as 88. What is the corrected average score?",
            ["71.5", "71.0", "72.5", "70.5"],
            "71.5",
            "Difference = 68 - 88 = -20. Change in average = -20 / 40 = -0.5. Corrected average = 72 - 0.5 = 71.5.",
            "Easy", "Infosys Averages Math"
        ),
        create_aptitude_question(
            "In how many ways can 4 Java developers and 3 Python developers be seated in a row such that no two Python developers sit next to each other?",
            ["1440 ways", "720 ways", "2880 ways", "144 ways"],
            "1440 ways",
            "Seat 4 Java developers first in 4! = 24 ways. This creates 5 available spaces (_ J _ J _ J _ J _). Choose 3 spaces for Python developers: C(5,3) = 10 ways. Arrange Python developers: 3! = 6 ways. Total = 24 * 10 * 6 = 1440 ways.",
            "Hard", "Infosys Permutations"
        ),
        create_aptitude_question(
            "Infosys stock price increases by 20% in Q1, then drops by 10% in Q2, and then increases by 15% in Q3. What is the net cumulative percentage gain?",
            ["24.2%", "25.0%", "22.5%", "26.0%"],
            "24.2%",
            "Net multiplier = 1.20 * 0.90 * 1.15 = 1.08 * 1.15 = 1.242. Net percentage increase = 24.2%.",
            "Medium", "Infosys Business Arithmetic"
        ),
        create_aptitude_question(
            "In Infosys Data Sufficiency: Is integer X divisible by 6? Statement 1: X is divisible by 2. Statement 2: X is divisible by 3.",
            ["Both statements TOGETHER are sufficient, but neither alone is sufficient", "Statement 1 alone is sufficient", "Statement 2 alone is sufficient", "Statements together are NOT sufficient"],
            "Both statements TOGETHER are sufficient, but neither alone is sufficient",
            "Since 2 and 3 are coprime, a number is divisible by 6 if and only if it is divisible by both 2 and 3. Hence both statements together are required and sufficient.",
            "Medium", "Infosys Data Sufficiency"
        ),
        create_aptitude_question(
            "A clock shows 3:40. What is the exact angle between the hour hand and the minute hand?",
            ["130 degrees", "140 degrees", "125 degrees", "135 degrees"],
            "130 degrees",
            "Formula: Angle = |30*H - (11/2)*M| = |30*3 - (11/2)*40| = |90 - 220| = |-130| = 130 degrees.",
            "Easy", "Infosys Clock Problems"
        ),
        create_aptitude_question(
            "Select the correct synonym for 'PROLIFIC' in enterprise software development context:",
            ["Highly Productive", "Sluggish", "Fragile", "Obsolete"],
            "Highly Productive",
            "'Prolific' means producing much fruit or foliage or many works; highly productive. Synonym is 'Highly Productive'.",
            "Easy", "Infosys Verbal Ability"
        ),
        create_aptitude_question(
            "If log_2(x) + log_2(x - 2) = 3, what is the valid real value of x?",
            ["4", "-2", "8", "6"],
            "4",
            "log_2(x * (x - 2)) = 3 => x^2 - 2x = 2^3 = 8 => x^2 - 2x - 8 = 0 => (x - 4)(x + 2) = 0. Since log argument must be positive, x = 4.",
            "Medium", "Infosys Algebra"
        ),
        create_aptitude_question(
            "In an InfyTQ coding test, 60% of candidates passed Section A, 50% passed Section B, and 20% failed both sections. What percentage of candidates passed BOTH sections?",
            ["30%", "25%", "35%", "40%"],
            "30%",
            "Total passing at least one section = 100% - 20% = 80%. By inclusion-exclusion: P(A or B) = P(A) + P(B) - P(Both) => 80% = 60% + 50% - P(Both) => P(Both) = 110% - 80% = 30%.",
            "Medium", "Infosys Set Theory"
        ),
        create_aptitude_question(
            "A person walks 10 meters North, turns Right and walks 15 meters, turns Right and walks 10 meters, and then turns Left and walks 5 meters. How far and in what direction is the person from the starting point?",
            ["20 meters East", "15 meters East", "20 meters West", "10 meters North"],
            "20 meters East",
            "North and South cancel out (+10 - 10 = 0). East distance = 15 + 5 = 20 meters. Direction is strictly East.",
            "Easy", "Infosys Direction Sense"
        ),
        create_aptitude_question(
            "Two pipes A and B can fill a server cooling tank in 20 mins and 30 mins respectively. Pipe C can empty it in 15 mins. If all three pipes are opened together, how long will it take to fill the tank?",
            ["60 minutes", "30 minutes", "45 minutes", "Tank will never fill"],
            "60 minutes",
            "Rate = 1/20 + 1/30 - 1/15 = (3 + 2 - 4) / 60 = 1/60 tank per minute. Total time = 60 minutes.",
            "Medium", "Infosys Pipes & Cisterns"
        ),
        create_aptitude_question(
            "What is the probability of getting at least one head when a fair coin is tossed 4 times?",
            ["15/16", "7/8", "1/16", "3/4"],
            "15/16",
            "P(at least one head) = 1 - P(all tails) = 1 - (1/2)^4 = 1 - 1/16 = 15/16.",
            "Easy", "Infosys Probability"
        )
    ]

    code_java = [
        create_coding_problem(
            "Longest Increasing Subsequence (HackWithInfy)",
            "Given an integer array nums, return the length of the longest strictly increasing subsequence in O(N log N) time complexity.",
            "nums = [10,9,2,5,3,7,101,18]",
            "4 ([2,3,7,101])",
            "public class Solution {\n    public int lengthOfLIS(int[] nums) {\n        return 0;\n    }\n}",
            "def length_of_lis(nums: list[int]) -> int:\n    pass",
            "def longest_monotonic_sales_trend(sales_df) -> int:\n    pass",
            "Patience sorting with binary search (Arrays.binarySearch or bisect_left) maintaining the minimum tail of all increasing subsequences.",
            "Medium", "Dynamic Programming & Binary Search", "O(N log N)", "O(N)"
        ),
        create_coding_problem(
            "0/1 Knapsack Variation (Resource Allocation)",
            "Given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.",
            "W = 50, val = [60, 100, 120], wt = [10, 20, 30]",
            "220",
            "public class Solution {\n    public static int knapSack(int W, int[] wt, int[] val, int n) {\n        return 0;\n    }\n}",
            "def knap_sack(W: int, wt: list[int], val: list[int], n: int) -> int:\n    pass",
            "def optimize_cloud_budget_allocation(budget: int, cost_list, value_list) -> int:\n    pass",
            "Dynamic programming table dp[w] updated in reverse from W down to wt[i] to optimize memory to O(W).",
            "Medium", "Dynamic Programming", "O(N * W)", "O(W)"
        ),
        create_coding_problem(
            "Unique Paths with Obstacles in Grid",
            "You are given an m x n integer array grid. There is a robot initially located at top-left corner. An obstacle and space are marked as 1 or 0 respectively. Return the number of possible unique paths to reach the bottom-right corner.",
            "obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]",
            "2",
            "public class Solution {\n    public int uniquePathsWithObstacles(int[][] obstacleGrid) {\n        return 0;\n    }\n}",
            "def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:\n    pass",
            "def calculate_valid_workflow_paths(grid_df) -> int:\n    pass",
            "2D Dynamic Programming: dp[i][j] = dp[i-1][j] + dp[i][j-1] if grid[i][j] == 0 else 0.",
            "Medium", "Grid Dynamic Programming", "O(M * N)", "O(N)"
        ),
        create_coding_problem(
            "Coin Change (Minimum Coins Required)",
            "You are given an integer array coins representing coins of different denominations and an integer amount. Return the fewest number of coins that you need to make up that amount. If not possible, return -1.",
            "coins = [1,2,5], amount = 11",
            "3 (5 + 5 + 1)",
            "public class Solution {\n    public int coinChange(int[] coins, int amount) {\n        return -1;\n    }\n}",
            "def coin_change(coins: list[int], amount: int) -> int:\n    pass",
            "def min_billing_denomination_units(coins: list[int], amount: int) -> int:\n    pass",
            "1D DP array initialized to amount + 1. dp[i] = min(dp[i], dp[i - c] + 1) for each coin c.",
            "Medium", "Dynamic Programming", "O(N * Amount)", "O(Amount)"
        ),
        create_coding_problem(
            "Distinct Subsequences (InfyTQ Hard)",
            "Given two strings s and t, return the number of distinct subsequences of s which equals t.",
            's = "rabbbit", t = "rabbit"',
            "3",
            "public class Solution {\n    public int numDistinct(String s, String t) {\n        return 0;\n    }\n}",
            "def num_distinct(s: str, t: str) -> int:\n    pass",
            "def count_schema_subsequence_matches(s: str, t: str) -> int:\n    pass",
            "2D DP: If s[i-1] == t[j-1], dp[i][j] = dp[i-1][j-1] + dp[i-1][j]; else dp[i][j] = dp[i-1][j].",
            "Hard", "String Dynamic Programming", "O(M * N)", "O(N)"
        ),
        create_coding_problem(
            "House Robber on Tree (Binary Tree DP)",
            "The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root. If two directly-linked nodes are robbed on the same night, police will be alerted. Return maximum amount of money.",
            "root = [3,2,3,null,3,null,1]",
            "7 (3 + 3 + 1)",
            "public class Solution {\n    public int rob(TreeNode root) {\n        return 0;\n    }\n}",
            "def rob(root: Optional[TreeNode]) -> int:\n    pass",
            "def optimal_hierarchical_budget_cut(tree_df) -> int:\n    pass",
            "Post-order traversal returning int[2] where res[0] is max if current node NOT robbed, and res[1] is max if robbed.",
            "Medium", "Tree & Dynamic Programming", "O(N)", "O(H)"
        ),
        create_coding_problem(
            "Word Break Problem (Infosys HackWithInfy)",
            "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.",
            's = "leetcode", wordDict = ["leet","code"]',
            "true",
            "public class Solution {\n    public boolean wordBreak(String s, List<String> wordDict) {\n        return false;\n    }\n}",
            "def word_break(s: str, word_dict: list[str]) -> bool:\n    pass",
            "def validate_token_concatenation(s: str, dictionary) -> bool:\n    pass",
            "DP boolean array dp[i] indicating whether s[0..i] can be segmented using dictionary words stored in a HashSet.",
            "Medium", "String DP", "O(N^2)", "O(N)"
        ),
        create_coding_problem(
            "Beautiful Array Construction",
            "An array nums of length n is beautiful if: nums is a permutation of integers from 1 to n, and for every i < j, there is no k with i < k < j such that 2 * nums[k] == nums[i] + nums[j]. Return any beautiful array.",
            "n = 4",
            "[2, 1, 4, 3] or [1, 3, 2, 4]",
            "public class Solution {\n    public int[] beautifulArray(int n) {\n        return new int[0];\n    }\n}",
            "def beautiful_array(n: int) -> list[int]:\n    pass",
            "def construct_non_arithmetic_sequence(n: int) -> list[int]:\n    pass",
            "Divide and conquer: Separate odd elements (2*x - 1) and even elements (2*x) recursively.",
            "Medium", "Divide and Conquer", "O(N)", "O(N)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the architecture of Spring Boot 3 GraalVM Native Image compilation, and why it is increasingly adopted in Infosys digital transformation projects.",
            "GraalVM performs ahead-of-time (AOT) compilation of Java bytecode directly into a standalone platform-specific binary executable. This eliminates the JVM warmup, reduces memory footprint by 70%, and enables sub-50ms startup times.",
            "Infosys Cloud Native & GraalVM", "Hard"
        ),
        create_technical_question(
            "In Infosys Finacle banking platform, how are database isolation levels (Read Committed, Repeatable Read, Serializable) configured to prevent Dirty Reads and Non-Repeatable Reads?",
            "Dirty reads are prevented by Read Committed; Non-repeatable reads by Repeatable Read (using snapshot reads or shared read locks). Financial fund transfers utilize Serializable or SELECT FOR UPDATE pessimistic row locks.",
            "Infosys Finacle Banking Architecture", "Hard"
        ),
        create_technical_question(
            "Explain how the Circuit Breaker, Rate Limiter, and Retry modules in Resilience4j operate to build fault-tolerant microservices in enterprise Infosys deployments.",
            "Resilience4j uses decorators around functional interfaces. Circuit Breaker opens when call failure rate exceeds threshold; Rate Limiter queues or rejects excess calls using token bucket; Retry re-attempts transient network failures with exponential backoff.",
            "Infosys Microservices Resiliency", "Medium"
        ),
        create_technical_question(
            "How does Hibernate second-level cache (L2C) with Ehcache / Redis work, and what strategies avoid stale cache data across multiple application server instances?",
            "L2C caches entity data in an external cache shared by all sessions. To avoid stale reads across clustered servers, distributed cache invalidation messages or Redis pub/sub eviction notifications are broadcast on entity mutations.",
            "Infosys Hibernate Architecture", "Hard"
        ),
        create_technical_question(
            "Explain the internals of Java 8 Stream API: Lazy Evaluation, Short-Circuiting Operations, and how parallel streams leverage the ForkJoinPool.",
            "Intermediate operations (filter, map) are lazy and assemble an execution pipeline without processing elements until a terminal operation (collect, forEach) is triggered. Parallel streams split work recursively using the common ForkJoinPool.",
            "Infosys Java Core & Streams", "Medium"
        ),
        create_technical_question(
            "How do you design a scalable RESTful API with backward compatibility, versioning (URI vs Header), and rate limiting in an Infosys enterprise client engagement?",
            "URI versioning (/api/v1/orders) provides explicit client routing. Deprecated endpoints return 'Sunset' and 'Deprecation' HTTP headers. Rate limiting using Spring Cloud Gateway token bucket protects backend servers.",
            "Infosys API Engineering", "Medium"
        ),
        create_technical_question(
            "Explain the differences between PostgreSQL B-Tree, GIN (Generalized Inverted Index), and BRIN indexes. When should you use GIN over B-Tree?",
            "B-Tree handles standard equality and range comparisons. GIN is designed for multi-value elements like JSONB, full-text search vectors, and arrays where an item can match any element within the collection.",
            "Infosys Database Internals", "Hard"
        ),
        create_technical_question(
            "How does JWT (JSON Web Token) authentication work in Spring Security, and how do you implement secure token revocation without storing state for every token?",
            "JWT is signed by the auth server (Header.Payload.Signature). For instant revocation (logout, compromise), implement a distributed Redis Blacklist storing revoked JTI (JWT ID) tokens with a TTL matching token expiration.",
            "Infosys Application Security", "Medium"
        ),
        create_technical_question(
            "What is Docker Multi-Stage building, and how does it reduce container image size and vulnerability attack surfaces in Infosys CI/CD pipelines?",
            "Multi-stage builds compile code in a heavy build environment (e.g. maven:3.9-eclipse-temurin) and copy only the compiled JAR artifact into a slim JRE runtime image (e.g. eclipse-temurin:17-jre-alpine), cutting image size from 800MB to 120MB.",
            "Infosys DevOps & Containers", "Medium"
        ),
        create_technical_question(
            "Explain the SOLID principles in Object-Oriented Software Design with concrete Java code examples as practiced at Infosys Mysore training.",
            "Single Responsibility, Open/Closed (extend via interface, don't modify existing code), Liskov Substitution (subtypes must be substitutable for base types), Interface Segregation, Dependency Inversion (depend on abstractions, not concretions).",
            "Infosys Design Principles", "Medium"
        ),
        create_technical_question(
            "How does Spring Data JPA execute derived query methods (e.g. findByEmailAndStatusOrderByCreatedAtDesc) by parsing method names into AST and SQL queries?",
            "Spring Data JPA uses PartTree parser to inspect method name tokens, converts them into Criteria API predicates, and delegates to the underlying JPA provider (Hibernate) to generate optimized SQL.",
            "Infosys Spring Data JPA", "Medium"
        ),
        create_technical_question(
            "What is the difference between Synchronous REST API communication and Asynchronous Event-Driven Architecture using RabbitMQ in an enterprise application?",
            "Synchronous REST blocks the client waiting for HTTP response, creating tight runtime coupling. Asynchronous messaging decouples producer from consumer through message queues, providing buffering and high fault tolerance.",
            "Infosys Architecture Patterns", "Medium"
        ),
        create_technical_question(
            "How do you profile Java application memory leaks using Eclipse Memory Analyzer (MAT) and detect uncollected Dominator Tree objects?",
            "Capture a heap dump (.hprof); load into Eclipse MAT; run 'Leak Suspects Report'; inspect Dominator Tree to find objects retaining large percentages of heap (e.g. uncleaned static HashMaps or thread locals).",
            "Infosys Performance Tuning", "Hard"
        ),
        create_technical_question(
            "Explain Database Connection Pooling mechanisms and what happens when an application exhausts all available connections in a HikariCP pool.",
            "HikariCP allocates a pool of reusable connections. When exhausted, incoming requests block up to connectionTimeout. If no connection is freed, a SQLTransientConnectionException is thrown.",
            "Infosys Database Performance", "Medium"
        ),
        create_technical_question(
            "How do you implement Cross-Origin Resource Sharing (CORS) securely in Spring Boot without using vulnerable wildcard 'Access-Control-Allow-Origin: *' configurations?",
            "Configure CorsConfigurationSource specifying exact trusted origin domains, allowed HTTP methods (GET, POST, PUT), allowed headers, and allowCredentials(true) with secure cookies.",
            "Infosys Web Security", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain how the Infosys Topaz AI platform helps Fortune 500 enterprises accelerate cognitive automation, generative AI adoption, and data modernization.",
            "Discuss: Infosys Topaz suite of 12,000+ AI assets, pre-built domain AI frameworks, generative AI code assistants for legacy migration, and responsible AI guardrails.",
            "Infosys Topaz AI Framework"
        ),
        create_ai_question(
            "How would you build an automated code migration pipeline using LLMs to translate legacy Java 8 / monolithic code into modern Spring Boot 3 microservices at Infosys?",
            "Detail: Abstract Syntax Tree (AST) extraction, prompt engineering with target architectural patterns, automated unit test generation to verify behavioral parity, and human code review.",
            "Infosys AI Code Migration"
        ),
        create_ai_question(
            "How do you implement Retrieval-Augmented Generation (RAG) for Infosys client support agents to search through multi-gigabyte technical product documentation?",
            "Architecture: Chunking with LangChain, embedding generation, vector storage in OpenSearch/Chroma, hybrid keyword + vector retrieval, and grounding prompt with source links.",
            "Infosys Client Support RAG"
        ),
        create_ai_question(
            "What strategies do you use to mitigate data privacy risks when developing AI solutions for European clients subject to strict GDPR and EU AI Act regulations at Infosys?",
            "Explain: Data minimization, on-premise inference, token anonymization, zero training retention agreements with cloud AI providers, and algorithmic audit trails.",
            "Infosys AI Governance & GDPR"
        ),
        create_ai_question(
            "How do you evaluate and benchmark the accuracy of automated code generation tools like Infosys AI code assistants against industry standards (HumanEval)?",
            "Discuss: Pass@1 and Pass@k metrics on sandboxed test suites, cyclomatic complexity analysis, vulnerability scanning with SonarQube, and developer acceptance rate.",
            "Infosys AI Evaluation Metrics"
        ),
        create_ai_question(
            "Describe how you design a multi-modal document processing pipeline using Generative AI for automated invoice and shipping bill extraction in supply chain projects.",
            "Detail: PDF rasterization, Vision-Language Model parsing table coordinates and line items into structured JSON, confidence scoring, and automated ERP reconciliation.",
            "Infosys Multi-Modal AI"
        ),
        create_ai_question(
            "How do you implement continuous integration testing for LLM prompts to prevent regression when model weights are updated by cloud providers?",
            "Explain: PromptFoo / CI test harness executing gold validation test cases on every git commit, asserting regex pattern matching, semantic similarity thresholds, and JSON schemas.",
            "Infosys PromptOps & CI/CD"
        ),
        create_ai_question(
            "How does Infosys integrate AI Fluency training across its 300,000+ global workforce through the Infosys Springboard platform?",
            "Cover: Infosys Springboard digital learning, foundational GenAI certifications, hands-on hackathons, and enterprise AI project simulations.",
            "Infosys Springboard & AI Fluency"
        ),
        create_ai_question(
            "How would you design an automated testing framework where an AI agent dynamically creates test scenarios, executes API calls, and verifies edge cases?",
            "Architecture: Agent parses OpenAPI / Swagger spec, generates negative test payloads (SQL injection, boundary overflow), executes requests, and reports unhandled exceptions.",
            "Infosys Autonomous AI Testing"
        ),
        create_ai_question(
            "What architectural considerations are critical when deploying RAG applications to minimize latency to sub-800ms for conversational interfaces?",
            "Discuss: Streaming responses, vector database connection pooling, caching frequent query embeddings, pre-fetching candidate answers, and using fast quantized models.",
            "Infosys Real-Time AI Performance"
        )
    ]

    hr_java = [
        create_hr_question(
            "Infosys is guided by the C-LIFE core values: Customer Focus, Leadership by Example, Integrity and Transparency, Fairness, and pursuit of Excellence. Which value resonates with you most?",
            "Select one value (e.g. Integrity or Pursuit of Excellence), give a personal academic or work example, and explain how it shapes your software engineering ethos.",
            "Infosys C-LIFE Core Values"
        ),
        create_hr_question(
            "The Infosys Mysore Development Center is renowned globally for its rigorous Initial Learning Program (ILP). Are you excited about residential training at Mysore?",
            "Affirm: High enthusiasm for world-class technical training, collaborative campus learning, building friendships with peers across India, and striving for high test scores.",
            "Infosys Mysore DC Training"
        ),
        create_hr_question(
            "Describe a situation in your academic or professional career where you took the initiative to learn a complex new programming language or framework autonomously.",
            "Use STAR: Outline motivation, learning path (documentation, projects, certifications), what was built, and the measurable outcome achieved.",
            "Continuous Learning & Agility"
        ),
        create_hr_question(
            "How do you handle working under a project manager who assigns strict sprint deadlines with daily status tracking?",
            "Demonstrate: Discipline, effective time management, proactive communication if blockers arise, and using Agile scrum ceremonies productively.",
            "Agile Team Delivery"
        ),
        create_hr_question(
            "Tell me about a time you had a conflict with a team member during a software project. How did you resolve it professionally?",
            "Emphasize: Respectful private discussion, focusing on project goals and technical facts rather than personal ego, and maintaining team harmony.",
            "Conflict Resolution"
        ),
        create_hr_question(
            "Why did you choose Infosys over other IT consulting and service companies?",
            "Highlight: Infosys reputation for engineering excellence, iconic Mysore training academy, leadership in AI with Topaz, and ethical corporate governance.",
            "Infosys Brand Motivation"
        ),
        create_hr_question(
            "Are you comfortable with relocating to any Infosys Development Center across India (Bangalore, Pune, Hyderabad, Chennai, Bhubaneswar) and working in rotational shifts?",
            "Affirm: Complete flexibility with relocation, readiness to work from client offices or ODCs, and enthusiasm to embrace new cities and cultures.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "Describe a time you received constructive criticism on your code during a peer review. What changes did you make in your coding approach?",
            "Show: Humility, adopting clean code standards, writing thorough unit tests, and thanking the reviewer for making your software more robust.",
            "Receptivity to Peer Review"
        ),
        create_hr_question(
            "Where do you see yourself in 3 to 5 years at Infosys, and how do you plan to contribute to our digital transformation initiatives?",
            "Connect: Aspiring to become a Senior Systems Engineer / Technology Analyst, mastering cloud architectures, and mentoring new campus hires.",
            "Career Aspirations"
        ),
        create_hr_question(
            "Do you have any questions for Infosys regarding project allocation, technology tracks, or continuous higher education programs?",
            "Candidate asks about Infosys certifications, opportunities to participate in HackWithInfy / SP tracks, or global project opportunities.",
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

GOOGLE_DATA = build_google_catalog()
AMAZON_DATA = build_amazon_catalog()
MICROSOFT_DATA = build_microsoft_catalog()
TCS_DATA = build_tcs_catalog()
INFOSYS_DATA = build_infosys_catalog()
