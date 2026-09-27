"""
Company Question Data - Part 3:
Oracle, IBM, Red Hat, HCLTech, Tech Mahindra.
"""

from scripts.catalog_builder import (
    create_aptitude_question, create_coding_problem,
    create_technical_question, create_ai_question, create_hr_question
)

# ==========================================
# 11. ORACLE
# ==========================================
def build_oracle_catalog():
    apt_java = [
        create_aptitude_question(
            "In Oracle Computer Science Core: A database disk block size is 8KB (8,192 bytes). If a table row has average size of 200 bytes with 192 bytes block header, how many maximum complete rows fit in a single block without row migration?",
            ["40 rows", "41 rows", "39 rows", "42 rows"],
            "40 rows",
            "Usable block space = 8,192 - 192 = 8,000 bytes. Rows per block = 8,000 // 200 = 40 complete rows.",
            "Medium", "Oracle Database Block Math"
        ),
        create_aptitude_question(
            "Oracle Boolean Algebra: Which of the following Boolean expressions is logically equivalent to (A + B)' using De Morgan's Laws?",
            ["A' * B'", "A' + B'", "(A * B)'", "A + B'"],
            "A' * B'",
            "By De Morgan's Law of duality: the complement of a logical sum (OR) is the product (AND) of the complements: (A + B)' = A' * B'.",
            "Easy", "Oracle Boolean Algebra"
        ),
        create_aptitude_question(
            "An Oracle Cloud Infrastructure (OCI) Block Volume delivers 60 IOPS per GB up to a maximum of 25,000 IOPS. What is the minimum volume size in GB required to achieve peak 25,000 IOPS?",
            ["417 GB", "500 GB", "350 GB", "450 GB"],
            "417 GB",
            "Size = Required IOPS / IOPS per GB = 25,000 / 60 ≈ 416.67 GB. Rounding up = 417 GB.",
            "Medium", "Oracle OCI Storage Math"
        ),
        create_aptitude_question(
            "In a B+ Tree index of order m=4, what is the maximum number of keys that can be stored in a leaf node?",
            ["3 keys", "4 keys", "2 keys", "5 keys"],
            "3 keys",
            "A B+ tree node of order m can have at most m children and therefore at most m - 1 keys. For order m=4: 4 - 1 = 3 keys.",
            "Medium", "Oracle B+ Tree Data Structures"
        ),
        create_aptitude_question(
            "Convert the hexadecimal value 0x2FA to its equivalent decimal integer value:",
            ["762", "750", "770", "760"],
            "762",
            "0x2FA = (2 * 16^2) + (15 * 16^1) + (10 * 16^0) = (2 * 256) + (15 * 16) + 10 = 512 + 240 + 10 = 762.",
            "Easy", "Oracle Number Base Conversion"
        ),
        create_aptitude_question(
            "An Oracle database buffer cache has a 96% cache hit ratio. In-memory cache reads take 0.2ms, while disk reads take 5.0ms. What is the average memory access time (AMAT)?",
            ["0.392 ms", "0.500 ms", "0.200 ms", "1.250 ms"],
            "0.392 ms",
            "AMAT = (Hit Ratio * Hit Time) + ((1 - Hit Ratio) * Miss Penalty) = (0.96 * 0.2ms) + (0.04 * 5.0ms) = 0.192ms + 0.200ms = 0.392 ms.",
            "Hard", "Oracle Buffer Cache Performance"
        ),
        create_aptitude_question(
            "In how many ways can 6 Oracle database server racks be assigned to 3 Availability Domains such that each domain gets exactly 2 racks?",
            ["90 ways", "180 ways", "45 ways", "60 ways"],
            "90 ways",
            "Choose 2 for AD1: C(6,2) = 15. Choose 2 for AD2: C(4,2) = 6. Remaining 2 for AD3: C(2,2) = 1. Total = 15 * 6 * 1 = 90 ways.",
            "Medium", "Oracle Combinatorics"
        ),
        create_aptitude_question(
            "A software process executes on a CPU with a 3.0 GHz clock rate. If an instruction requires 6 clock cycles, what is its execution time in nanoseconds?",
            ["2.0 nanoseconds", "3.0 nanoseconds", "1.5 nanoseconds", "0.5 nanoseconds"],
            "2.0 nanoseconds",
            "Clock period T = 1 / (3.0 * 10^9) = (1/3) nanosecond. Time = 6 cycles * (1/3) ns = 2.0 nanoseconds.",
            "Easy", "Oracle Computer Architecture"
        ),
        create_aptitude_question(
            "In relational algebra, if Relation R has 50 tuples and Relation S has 30 tuples, what is the exact number of tuples in the Cartesian Product (R x S)?",
            ["1,500 tuples", "80 tuples", "20 tuples", "3,000 tuples"],
            "1,500 tuples",
            "The Cartesian Product R x S pairs every tuple of R with every tuple of S. Total tuples = 50 * 30 = 1,500 tuples.",
            "Easy", "Oracle Relational Algebra"
        ),
        create_aptitude_question(
            "An Oracle table stores employee salaries with mean $80,000 and standard deviation $10,000. By Chebyshev's inequality, what minimum percentage of salaries must lie between $60,000 and $100,000?",
            ["75%", "89%", "50%", "95%"],
            "75%",
            "Range is [mean - 2*sigma, mean + 2*sigma], so k = 2. By Chebyshev's theorem, P(|X - mu| < k*sigma) >= 1 - 1/k^2 = 1 - 1/4 = 3/4 = 75%.",
            "Hard", "Oracle Statistical Math"
        ),
        create_aptitude_question(
            "If an Oracle redo log buffer is 16 MB and writes flush to disk every 3 seconds or whenever 1 MB of logs accumulates, what is the maximum possible unflushed log volume?",
            ["1 MB", "16 MB", "3 MB", "0.5 MB"],
            "1 MB",
            "Because the threshold specifies flushing whenever 1 MB accumulates or 3 seconds elapse, log volume cannot exceed 1 MB under continuous high write workloads.",
            "Medium", "Oracle Database Architecture Quant"
        ),
        create_aptitude_question(
            "Two dice are thrown in an algorithmic simulation. What is the probability that the sum is strictly greater than 9?",
            ["6/36 = 1/6", "10/36 = 5/18", "4/36 = 1/9", "8/36 = 2/9"],
            "6/36 = 1/6",
            "Sums > 9 are 10, 11, 12. Sum 10: (4,6),(5,5),(6,4) [3]. Sum 11: (5,6),(6,5) [2]. Sum 12: (6,6) [1]. Total = 3 + 2 + 1 = 6. Probability = 6/36 = 1/6.",
            "Easy", "Oracle Probability"
        ),
        create_aptitude_question(
            "In how many ways can the letters of the word 'ORACLE' be arranged so that the vowels (O, A, E) never appear all together?",
            ["576 ways", "720 ways", "144 ways", "600 ways"],
            "576 ways",
            "Total arrangements = 6! = 720. Arrangements where vowels are together: bundle (O,A,E) with R,C,L (4 items total). 4! * 3! = 24 * 6 = 144. Vowels NOT together = 720 - 144 = 576 ways.",
            "Medium", "Oracle Combinatorics"
        ),
        create_aptitude_question(
            "An algorithm has time complexity recurrence T(N) = 4T(N/2) + N. What is the Big-O complexity by the Master Theorem?",
            ["O(N^2)", "O(N log N)", "O(N^3)", "O(N)"],
            "O(N^2)",
            "a=4, b=2. N^(log_b a) = N^(log_2 4) = N^2. Since f(N) = N is polynomial smaller than N^2 (Case 1), T(N) = Theta(N^2).",
            "Medium", "Oracle Big-O Complexity"
        ),
        create_aptitude_question(
            "A database backup job transmits 450 GB over a 1 Gbps dedicated OCI FastConnect link. Assuming 80% effective link utilization, how many minutes will the transfer take?",
            ["60 minutes", "45 minutes", "75 minutes", "50 minutes"],
            "60 minutes",
            "450 GB = 450 * 8 = 3600 Gigabits. Effective speed = 0.8 Gbps = 48 Gigabits/minute. Time = 3600 / (0.8 * 60) = 3600 / 48 = 75 minutes.",
            "Medium", "Oracle Network Quant"
        )
    ]

    code_java = [
        create_coding_problem(
            "Binary Search Tree Insertion and Search (Oracle DB Engine)",
            "Implement a Binary Search Tree (BST) with insert(val) and search(val) operations. Return the node if val exists, otherwise return null.",
            "insert(4), insert(2), insert(7), insert(1), insert(3), search(2)",
            "Subtree rooted at node with val 2 ([2, 1, 3])",
            "public class Solution {\n    public TreeNode insertIntoBST(TreeNode root, int val) {\n        return null;\n    }\n    public TreeNode searchBST(TreeNode root, int val) {\n        return null;\n    }\n}",
            "def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:\n    pass\ndef search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:\n    pass",
            "def index_lookup_bst(root, key: int):\n    pass",
            "Oracle standard: Compare value with current node; recursively route left if smaller, right if larger in O(H) time.",
            "Easy", "Binary Search Tree", "O(H)", "O(H)"
        ),
        create_coding_problem(
            "Reverse a Doubly Linked List",
            "Given the head of a doubly linked list, reverse the list so that the previous and next pointers of all nodes are swapped.",
            "head = [1 <-> 2 <-> 3 <-> 4]",
            "[4 <-> 3 <-> 2 <-> 1]",
            "public class Solution {\n    public Node reverseDLL(Node head) {\n        return null;\n    }\n}",
            "def reverse_dll(head: Optional[Node]) -> Optional[Node]:\n    pass",
            "def invert_bidirectional_journal_index(head_df):\n    pass",
            "Traverse doubly linked list, swapping prev and next pointers on every node in O(N) time and O(1) space.",
            "Easy", "Doubly Linked List", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Implement Queue using Two Stacks",
            "Implement a first-in, first-out (FIFO) queue using only two stacks supporting push, pop, peek, and empty operations with amortized O(1) time complexity.",
            "push(1), push(2), peek(), pop(), empty()",
            "[null, null, 1, 1, false]",
            "public class MyQueue {\n    public void push(int x) {}\n    public int pop() { return 0; }\n    public int peek() { return 0; }\n    public boolean empty() { return false; }\n}",
            "class MyQueue:\n    def push(self, x: int) -> None: pass\n    def pop(self) -> int: return 0\n    def peek() -> int: return 0\n    def empty(self) -> bool: return False",
            "class FIFOAuditBuffer:\n    def push(self, x: int): pass\n    def pop(self) -> int: return 0",
            "Use input_stack for pushing; when popping/peeking, if output_stack is empty, pop all items from input_stack to output_stack.",
            "Easy", "Stack & Queue Design", "Amortized O(1)", "O(N)"
        ),
        create_coding_problem(
            "Find Kth Smallest Element in BST",
            "Given the root of a binary search tree and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.",
            "root = [3,1,4,null,2], k = 1",
            "1",
            "public class Solution {\n    public int kthSmallest(TreeNode root, int k) {\n        return 0;\n    }\n}",
            "def kth_smallest(root: Optional[TreeNode], k: int) -> int:\n    pass",
            "def query_ranked_index_entry(tree_df, k: int) -> int:\n    pass",
            "Iterative or recursive in-order traversal (Left -> Node -> Right) visits elements in strictly sorted order; return kth element.",
            "Medium", "BST & In-Order Traversal", "O(H + K)", "O(H)"
        ),
        create_coding_problem(
            "Detect Cycle in Directed Graph (Lock Wait-For Graph)",
            "Given a directed graph representing database lock wait-for dependencies with V vertices and E edges, determine if the graph contains a cycle (deadlock).",
            "V = 4, edges = [[0, 1], [1, 2], [2, 3], [3, 1]]",
            "true (Cycle: 1 -> 2 -> 3 -> 1)",
            "public class Solution {\n    public boolean isCyclic(int V, ArrayList<ArrayList<Integer>> adj) {\n        return false;\n    }\n}",
            "def is_cyclic(V: int, adj: list[list[int]]) -> bool:\n    pass",
            "def detect_deadlock_cycle(dependencies_df) -> bool:\n    pass",
            "3-Color DFS (White=Unvisited, Gray=Visiting/Recursion Stack, Black=Visited). Cycle detected if edge touches Gray node.",
            "Medium", "Graph & Cycle Detection", "O(V + E)", "O(V)"
        ),
        create_coding_problem(
            "Merge K Sorted Lists (External Merge Sort)",
            "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
            "lists = [[1,4,5],[1,3,4],[2,6]]",
            "[1,1,2,3,4,4,5,6]",
            "public class Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        return null;\n    }\n}",
            "def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:\n    pass",
            "def merge_sorted_transaction_shards(shards_df):\n    pass",
            "Min-Heap of size K storing the current head node of each list; extract minimum and advance pointer in O(N log K) time.",
            "Hard", "Heap & Linked List", "O(N log K)", "O(K)"
        ),
        create_coding_problem(
            "In-Order Successor in BST",
            "Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If no successor exists, return null.",
            "root = [2,1,3], p = 1",
            "Node with value 2",
            "public class Solution {\n    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {\n        return null;\n    }\n}",
            "def inorder_successor(root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:\n    pass",
            "def get_next_indexed_key(tree_df, key: int):\n    pass",
            "If p has a right child, successor is minimum of right subtree. Otherwise, traverse from root tracking last node where we turned left.",
            "Medium", "Binary Search Tree", "O(H)", "O(1)"
        ),
        create_coding_problem(
            "Next Greater Element using Monotonic Stack",
            "Given an integer array nums, find the next greater element for each element. The next greater element of a number x is the first greater number to its right.",
            "nums = [4, 5, 2, 25]",
            "[5, 25, 25, -1]",
            "public class Solution {\n    public int[] nextGreaterElement(int[] nums) {\n        return new int[0];\n    }\n}",
            "def next_greater_element(nums: list[int]) -> list[int]:\n    pass",
            "def locate_next_higher_transaction_spike(series_df) -> list[int]:\n    pass",
            "Monotonic decreasing Stack: Traverse from right to left popping elements <= current num. Stack top is next greater.",
            "Medium", "Monotonic Stack", "O(N)", "O(N)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the Oracle Database System Global Area (SGA) memory architecture: Database Buffer Cache, Shared Pool (Library Cache, Data Dictionary), and Redo Log Buffer.",
            "SGA is shared memory allocated when Oracle instance starts. Buffer Cache caches data blocks; Shared Pool parses and caches SQL execution plans; Redo Log Buffer records all database changes before flushing to disk via LGWR.",
            "Oracle SGA Architecture", "Hard"
        ),
        create_technical_question(
            "How does Multi-Version Concurrency Control (MVCC) in Oracle Database use Undo Tablespaces to guarantee Non-Blocking Consistent Reads (Statement-Level Read Consistency)?",
            "When a query starts at System Change Number (SCN) T, it reads committed data at SCN T. If another transaction modifies and commits blocks after T, Oracle rebuilds prior block images using Undo records, preventing readers from blocking writers.",
            "Oracle MVCC & Undo Tablespace", "Hard"
        ),
        create_technical_question(
            "Compare B-Tree Indexes with Bitmap Indexes in Oracle Database. Why are Bitmap Indexes disastrous for high-concurrency OLTP applications?",
            "B-Tree indexes store row IDs per key (ideal for high cardinality). Bitmap indexes store bit vectors per key value (ideal for low cardinality read-only data warehousing). Updating a bitmap index locks the entire bitmap segment, freezing concurrent OLTP updates.",
            "Oracle B-Tree vs Bitmap Indexes", "Hard"
        ),
        create_technical_question(
            "Explain SQL Execution Plans in Oracle: Cost-Based Optimizer (CBO), EXPLAIN PLAN, and why an outdated DBMS_STATS histogram causes full table scans.",
            "CBO evaluates cardinality, CPU, and I/O costs across access paths. Stale statistics deceive CBO into underestimating index scan selectivity or overestimating table size, choosing suboptimal full table scans.",
            "Oracle Cost-Based Optimizer (CBO)", "Hard"
        ),
        create_technical_question(
            "What causes the classic Oracle error 'ORA-01555: snapshot too old', and how do UNDO_RETENTION and properly sized undo tablespaces eliminate it?",
            "ORA-01555 occurs when a long-running query requires older undo data to reconstruct a read-consistent block, but the undo block was already overwritten. Increase UNDO_RETENTION and enable undo tablespace autoextend.",
            "Oracle Diagnostics & ORA-01555", "Hard"
        ),
        create_technical_question(
            "Explain Oracle Real Application Clusters (RAC) and how Cache Fusion synchronizes in-memory database blocks across multiple cluster nodes over private interconnects.",
            "RAC runs multiple database instances accessing one shared storage. Cache Fusion transfers dirty database blocks from one instance's SGA to another's via high-speed InfiniBand/RDMA interconnect without writing to disk first.",
            "Oracle RAC & Cache Fusion", "Hard"
        ),
        create_technical_question(
            "How does Oracle Active Data Guard provide high availability and disaster recovery with real-time query offloading to physical standby databases?",
            "Primary database streams redo logs in real-time to standby. Active Data Guard applies redo logs continuously while keeping the standby database open read-only for reporting queries and backups.",
            "Oracle Active Data Guard", "Medium"
        ),
        create_technical_question(
            "Explain Oracle Table Partitioning strategies: Range, Hash, List, and Composite (Range-Hash). How does Partition Pruning boost query performance?",
            "Partition pruning allows CBO to scan only relevant partitions (e.g. sales_2024_q1) matching query WHERE predicates, skipping gigabytes of unneeded partitions.",
            "Oracle Partitioning & Performance", "Medium"
        ),
        create_technical_question(
            "How do Autonomous Transactions (PRAGMA AUTONOMOUS_TRANSACTION) operate in PL/SQL stored procedures, and what are their valid use cases?",
            "Autonomous transactions execute and commit or roll back independently of the main calling transaction, commonly used for writing persistent audit and error logs even when main transaction fails.",
            "Oracle PL/SQL & Concurrency", "Medium"
        ),
        create_technical_question(
            "Explain Database Connection Pooling with Oracle Universal Connection Pool (UCP) and Fast Connection Failover (FCF) integration with Oracle RAC.",
            "UCP maintains pre-allocated connections. FCF receives Oracle Notification Service (ONS) events when a RAC node fails, transparently severing severed connections and rerouting traffic to surviving nodes.",
            "Oracle UCP & High Availability", "Medium"
        ),
        create_technical_question(
            "What is the difference between TRUNCATE and DELETE statements in Oracle SQL regarding Redo generation, Rollback capability, and High Water Mark (HWM)?",
            "DELETE is DML; generates redo/undo per row; can be rolled back; does not lower High Water Mark. TRUNCATE is DDL; deallocates extents; generates minimal redo; resets HWM to zero; cannot be rolled back.",
            "Oracle SQL Fundamentals", "Easy"
        ),
        create_technical_question(
            "How does Oracle Cloud Infrastructure (OCI) Virtual Cloud Network (VCN) security differ between Security Lists and Network Security Groups (NSGs)?",
            "Security Lists apply ingress/egress firewall rules at the subnet level. Network Security Groups apply granular firewall rules directly to specific virtual network interface cards (VNICs) across subnets.",
            "Oracle OCI Cloud Networking", "Medium"
        ),
        create_technical_question(
            "Explain Java Concurrency: The Java Memory Model (JMM), 'happens-before' guarantee, and the volatile keyword semantics in high-concurrency systems.",
            "volatile guarantees memory visibility (reads bypass CPU L1/L2 cache directly to main memory) and prevents compiler instruction reordering. Synchronized blocks establish happens-before relationships.",
            "Oracle Java Concurrency & JMM", "Hard"
        ),
        create_technical_question(
            "How do Oracle Database In-Memory column stores accelerate real-time analytics on transactional databases without modifying application SQL?",
            "Dual-format architecture: Tables exist simultaneously in traditional row format for transactional OLTP and an in-memory SIMD-vectorized columnar format for blazing-fast aggregations.",
            "Oracle Database In-Memory", "Hard"
        ),
        create_technical_question(
            "Explain the difference between Hard Parsing and Soft Parsing in the Oracle Shared Pool, and why bind variables (:bind_var) are mandatory for OLTP scalability.",
            "Hard parse checks syntax, semantics, and runs CBO optimization (costly CPU). Soft parse reuses an existing execution plan from Library Cache. Bind variables ensure queries share identical plans.",
            "Oracle SQL Optimization & Shared Pool", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain Oracle Database 23ai AI Vector Search and how it integrates vector embeddings directly alongside relational tables for native enterprise RAG.",
            "Discuss: Storing dense vectors in VECTOR data types, running HNSW and IVF vector distance indexes (Cosine, Euclidean), and joining vectors with relational SQL filters in a single query.",
            "Oracle Database 23ai Vector Search"
        ),
        create_ai_question(
            "How does Oracle Cloud Infrastructure (OCI) Generative AI service deploy Cohere and Meta Llama foundation models on dedicated AI GPU clusters?",
            "Detail: Dedicated AI clusters isolating customer compute, fine-tuning with T-Few and LoRA, enterprise data privacy guarantees, and private endpoint integration.",
            "OCI Generative AI Architecture"
        ),
        create_ai_question(
            "How do you implement an enterprise AI assistant using Oracle Digital Assistant (ODA) with LLM orchestration for automated ERP supplier inquiries?",
            "Architecture: ODA intent routing, conversational skill dialogs, calling OCI Generative AI for natural language comprehension, and querying Oracle ERP Cloud via REST APIs.",
            "Oracle Digital Assistant (ODA)"
        ),
        create_ai_question(
            "Describe how Oracle Autonomous Database uses machine learning internally for automated indexing, tuning, and self-patching without DBA intervention.",
            "Explain: Ongoing query workload capture, ML candidate index evaluation in shadow tables, automated verification of performance gains, and continuous background tuning.",
            "Oracle Autonomous Database ML"
        ),
        create_ai_question(
            "How do you prevent data contamination and enforce data residency when fine-tuning LLMs with proprietary Oracle database transaction records?",
            "Discuss: OCI isolated tenancy boundaries, encryption with customer-managed keys (Vault), training on synthetic de-identified replicas, and zero external network egress.",
            "Oracle AI Data Residency & Security"
        ),
        create_ai_question(
            "Explain how Select AI in Oracle Database 23ai translates natural language questions directly into optimized SQL queries against live schemas.",
            "Detail: Select AI integration with OpenAI / OCI GenAI, sending DDL metadata prompts, generating syntactically valid Oracle SQL, and executing with user privileges.",
            "Oracle 23ai Select AI"
        ),
        create_ai_question(
            "How do you optimize vector distance computation across 100 million vector embeddings using OCI GPU acceleration and HNSW index parameters?",
            "Discuss: Tuning M (number of bidirectional links) and efConstruction in HNSW indexes, SIMD hardware acceleration, and partitioning vector spaces across nodes.",
            "OCI Vector Search Optimization"
        ),
        create_ai_question(
            "Describe how Oracle Cloud Guard and Security Zones automatically detect and remediate AI pipeline misconfigurations and exposed storage buckets.",
            "Explain: Real-time configuration audits, Security Zone recipes prohibiting public IPs and unencrypted storage, and automatic responder scripts fixing security drifts.",
            "Oracle Cloud Guard & AI Security"
        ),
        create_ai_question(
            "How do you evaluate and benchmark query latency when performing hybrid search combining BM25 full-text indexing and dense vector embeddings in Oracle 23ai?",
            "Discuss: P50 and P99 latency comparisons, Reciprocal Rank Fusion (RRF) score merging, and measuring recall against reference ground truth datasets.",
            "Oracle Hybrid AI Search Evaluation"
        ),
        create_ai_question(
            "How does Oracle ensure responsible AI governance, explainability, and bias mitigation across automated enterprise HCM (Human Capital Management) models?",
            "Cover: Oracle Machine Learning explainability features, partial dependence plots, feature importance scoring, and compliance with equal employment standards.",
            "Oracle Responsible AI in HCM"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically choose Oracle to build your engineering career in enterprise systems and cloud infrastructure?",
            "Highlight: Oracle's database market dominance, cutting-edge OCI engineering innovations, mission-critical enterprise footprint, and culture of technical depth.",
            "Oracle Brand Motivation"
        ),
        create_hr_question(
            "Oracle software powers the world's most critical financial and healthcare systems where downtime is intolerable. How do you approach technical accountability and precision?",
            "Emphasize: Zero compromise on testing, meticulous code verification, understanding production blast radius, and taking full ownership of your deliverables.",
            "Engineering Precision & Accountability"
        ),
        create_hr_question(
            "Tell me about a time you faced a critical production defect or severe project failure under high-pressure conditions. How did you react?",
            "Use STAR: Outline calm analytical triage, prioritizing customer mitigation, communicating transparently with leads, and executing a lasting fix.",
            "Resilience Under Pressure"
        ),
        create_hr_question(
            "Oracle engineering teams value deep first-principles technical debate. Describe a time you defended a technical architecture decision with hard benchmark data.",
            "Focus on: Backing arguments with metrics (latency, memory consumption, CPU utilization), respecting counter-arguments, and driving objective decisions.",
            "Technical Conviction & Data-Driven Debate"
        ),
        create_hr_question(
            "Oracle operates major engineering campuses in Bangalore, Hyderabad, Pune, and Silicon Valley. Are you fully flexible with relocation and global project collaboration?",
            "Affirm: Eagerness to relocate, adaptability to working with teams across North America and Europe, and enthusiasm for enterprise software development.",
            "Relocation & Global Collaboration"
        ),
        create_hr_question(
            "How do you handle working on an intricate, multi-million-line legacy codebase with minimal documentation?",
            "Showcase: Systematic code reading, writing diagnostic tests, tracing execution with debuggers, and documenting findings to help teammates.",
            "Mastering Complex Codebases"
        ),
        create_hr_question(
            "Describe a time you collaborated with a challenging teammate who had rigid viewpoints on software design. How did you build a productive partnership?",
            "Demonstrate: Active listening, focusing on shared project goals, separating code from personal ego, and establishing mutual respect.",
            "Teamwork & Conflict Resolution"
        ),
        create_hr_question(
            "Where do you see yourself contributing at Oracle over the next 3 to 5 years as an engineer?",
            "Connect: Growing from Software Engineer to Senior Member of Technical Staff (SMTS), mastering cloud and database internals, and leading architectural components.",
            "Career Growth & Vision"
        ),
        create_hr_question(
            "Tell me about a time you had to balance urgent feature delivery with refactoring accumulated technical debt.",
            "Explain: Communicating debt risks to product managers, allocating 20% of sprint time for refactoring, and improving automated test coverage.",
            "Technical Debt Management"
        ),
        create_hr_question(
            "Do you have any questions for Oracle's engineering leadership regarding team culture, OCI innovation, or our database roadmap?",
            "Candidate asks insightful questions about Oracle Database 23ai development, OCI hyperscale expansion, or engineering mentorship.",
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
# 12. IBM
# ==========================================
def build_ibm_catalog():
    apt_java = [
        create_aptitude_question(
            "In an IBM cloud cluster, 6 bare-metal servers deploy 120 container pods in 4 hours. How many pods can 9 servers deploy in 6 hours at the same deployment velocity?",
            ["270 pods", "240 pods", "300 pods", "210 pods"],
            "270 pods",
            "Rate = 120 / (6 * 4) = 5 pods/server-hour. With 9 servers for 6 hours: total = 9 * 6 * 5 = 270 pods.",
            "Medium", "IBM Cloud Systems Math"
        ),
        create_aptitude_question(
            "IBM Cognitive Ability: Find the missing number in the grid puzzle:\n[6, 18, 54]\n[4, 12, 36]\n[7, 21, ?]",
            ["63", "49", "56", "70"],
            "63",
            "Each row multiplies by 3: 7 * 3 = 21, 21 * 3 = 63.",
            "Easy", "IBM Number Series"
        ),
        create_aptitude_question(
            "An enterprise IBM watsonx client commits to a $180,000 annual contract with a 15% discount for upfront payment and an additional 2% early-bird incentive. What is the final contract payment?",
            ["$149,940", "$150,000", "$152,400", "$148,500"],
            "$149,940",
            "After 15% discount: 180,000 * 0.85 = $153,000. After additional 2% incentive: 153,000 * 0.98 = $149,940.",
            "Medium", "IBM Commercial Math"
        ),
        create_aptitude_question(
            "In how many ways can 4 OpenShift worker nodes and 3 control plane nodes be assigned to 7 available server racks?",
            ["35 ways", "70 ways", "140 ways", "210 ways"],
            "35 ways",
            "Number of ways to choose 3 racks out of 7 for control plane nodes = C(7,3) = (7*6*5)/(3*2*1) = 35 ways (the rest receive worker nodes).",
            "Easy", "IBM Infrastructure Combinatorics"
        ),
        create_aptitude_question(
            "A hybrid cloud link operates with a packet drop rate of 1 in 200 packets. In a transmission of 1,000 packets, what is the expected number of dropped packets?",
            ["5 packets", "10 packets", "2 packets", "20 packets"],
            "5 packets",
            "Expected dropped packets = 1,000 * (1 / 200) = 5 packets.",
            "Easy", "IBM Networking Probability"
        ),
        create_aptitude_question(
            "Find the next term in the IBM deductive sequence: Z26, X24, V22, T20, ___?",
            ["R18", "S19", "Q17", "P16"],
            "R18",
            "Letters step backward by 2: Z, X, V, T -> R. Numbers decrease by 2: 26, 24, 22, 20 -> 18. Term is R18.",
            "Easy", "IBM Alphanumeric Series"
        ),
        create_aptitude_question(
            "An IBM MQ message queue buffer of size 500 MB is 40% full. If incoming messages arrive at 5 MB/s while consumer processes at 3 MB/s, in how many minutes will the buffer overflow?",
            ["2.5 minutes", "3.0 minutes", "4.0 minutes", "1.5 minutes"],
            "2.5 minutes",
            "Remaining buffer capacity = 60% of 500 MB = 300 MB. Net accumulation rate = 5 - 3 = 2 MB/s. Time = 300 / 2 = 150 seconds = 2.5 minutes.",
            "Medium", "IBM Queue Mechanics"
        ),
        create_aptitude_question(
            "Two automated CI test suites run concurrently. Suite A finishes in 25 minutes, Suite B in 35 minutes. If both start together, how many minutes will elapsed before both suites are finished?",
            ["35 minutes", "60 minutes", "30 minutes", "25 minutes"],
            "35 minutes",
            "Running concurrently, total elapsed time is determined by the longer running suite: max(25, 35) = 35 minutes.",
            "Easy", "IBM Systems Logic"
        ),
        create_aptitude_question(
            "In an IBM mainframe telemetry audit, 75% of systems run z/OS, 40% run Linux on Z, and 20% run both. What percentage of systems run NEITHER operating system?",
            ["5%", "10%", "15%", "0%"],
            "5%",
            "Total running at least one = 75% + 40% - 20% = 95%. Percentage running neither = 100% - 95% = 5%.",
            "Medium", "IBM Set Theory"
        ),
        create_aptitude_question(
            "Select the correct antonym for 'HETEROGENEOUS' in system architecture context:",
            ["Homogeneous", "Distributed", "Asymmetric", "Fragmented"],
            "Homogeneous",
            "'Heterogeneous' refers to systems consisting of diverse, dissimilar elements. The direct antonym is 'Homogeneous' (of the same kind).",
            "Easy", "IBM Verbal Ability"
        ),
        create_aptitude_question(
            "A server cluster running 8 virtual machines experiences an average latency of 45ms. If two new high-performance VMs are added with 15ms latency each, what is the new average cluster latency?",
            ["39.0 ms", "40.0 ms", "35.0 ms", "42.0 ms"],
            "39.0 ms",
            "Total latency for 8 VMs = 8 * 45 = 360ms. Total for 10 VMs = 360 + 15 + 15 = 390ms. New average = 390 / 10 = 39.0 ms.",
            "Easy", "IBM Averages"
        ),
        create_aptitude_question(
            "If an encryption key permutation has 7! possible states, how many total states does that represent?",
            ["5,040 states", "720 states", "2,520 states", "10,080 states"],
            "5,040 states",
            "7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5,040 states.",
            "Easy", "IBM Cryptography Math"
        ),
        create_aptitude_question(
            "In IBM Deductive Reasoning: All hybrid cloud architectures are flexible. Some flexible systems are open-source. Which conclusion is definitively true?",
            ["None of the conclusions is definitively true", "All open-source systems are hybrid cloud", "Some hybrid cloud architectures are open-source", "No open-source system is hybrid cloud"],
            "None of the conclusions is definitively true",
            "The middle term 'flexible' is undistributed in both premises; therefore no categorical relationship can be deduced between hybrid cloud and open-source.",
            "Medium", "IBM Deductive Logic"
        ),
        create_aptitude_question(
            "A data pipeline script extracts 4,500 records in 15 seconds. At this constant throughput, how many records can it extract in 2 minutes?",
            ["36,000 records", "30,000 records", "45,000 records", "24,000 records"],
            "36,000 records",
            "Rate = 4,500 / 15 = 300 records/sec. In 2 minutes (120 seconds): total = 120 * 300 = 36,000 records.",
            "Easy", "IBM Rate Math"
        ),
        create_aptitude_question(
            "In how many ways can 3 distinct database backup files be stored across 5 cloud storage buckets if each bucket can hold at most one file?",
            ["60 ways", "120 ways", "15 ways", "20 ways"],
            "60 ways",
            "Permutations of 5 buckets taken 3 at a time: P(5,3) = 5 * 4 * 3 = 60 ways.",
            "Easy", "IBM Permutations"
        )
    ]

    code_java = [
        create_coding_problem(
            "Longest Common Subsequence (IBM Cognitive & Coding)",
            "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
            'text1 = "abcde", text2 = "ace"',
            "3 (Subsequence: \"ace\")",
            "public class Solution {\n    public int longestCommonSubsequence(String text1, String text2) {\n        return 0;\n    }\n}",
            "def longest_common_subsequence(text1: str, text2: str) -> int:\n    pass",
            "def align_historical_transaction_tokens(seq_a, seq_b) -> int:\n    pass",
            "2D Dynamic Programming: If chars match, dp[i][j] = dp[i-1][j-1] + 1; else dp[i][j] = max(dp[i-1][j], dp[i][j-1]).",
            "Medium", "Dynamic Programming", "O(M * N)", "O(M * N)"
        ),
        create_coding_problem(
            "Word Search in 2D Grid (Backtracking)",
            "Given an m x n grid of characters board and a string word, return true if word exists in the grid constructed from letters of sequentially adjacent cells.",
            'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"',
            "true",
            "public class Solution {\n    public boolean exist(char[][] board, String word) {\n        return false;\n    }\n}",
            "def exist(board: list[list[str]], word: str) -> bool:\n    pass",
            "def locate_token_pathway(grid_df, word: str) -> bool:\n    pass",
            "Backtracking DFS: Explore 4-directional neighbors marking visited cells, restoring cell on backtrack in O(N * 3^L) time.",
            "Medium", "Backtracking & DFS", "O(N * 3^L)", "O(L)"
        ),
        create_coding_problem(
            "Top K Frequent Words (Lexicographical Tie-Breaking)",
            "Given an array of strings words and an integer k, return the k most frequent strings sorted by frequency from highest to lowest. Sort words with the same frequency by their lexicographical order.",
            'words = ["i","love","ibm","i","love","coding"], k = 2',
            '["i","love"]',
            "public class Solution {\n    public List<String> topKFrequent(String[] words, int k) {\n        return new ArrayList<>();\n    }\n}",
            "def top_k_frequent(words: list[str], k: int) -> list[str]:\n    pass",
            "def extract_top_telemetry_keywords(words_df, k: int):\n    pass",
            "Count frequencies with HashMap; maintain Min-Heap of size K with custom comparator comparing frequency and string lexicography.",
            "Medium", "Heap & Hash Table", "O(N log K)", "O(N)"
        ),
        create_coding_problem(
            "Flood Fill Algorithm (Cluster Region Tagging)",
            "An image is represented by an m x n integer grid image where image[i][j] represents the pixel value. Given sr, sc, and color, perform a flood fill on the image starting from the pixel image[sr][sc].",
            "image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2",
            "[[2,2,2],[2,2,0],[2,0,1]]",
            "public class Solution {\n    public int[][] floodFill(int[][] image, int sr, int sc, int color) {\n        return image;\n    }\n}",
            "def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:\n    pass",
            "def tag_connected_subsystems(grid_df, sr: int, sc: int, color: int):\n    pass",
            "DFS or BFS traversal checking original color, updating cell to new color, and propagating to adjacent matching cells.",
            "Easy", "Graph & BFS/DFS", "O(M * N)", "O(M * N)"
        ),
        create_coding_problem(
            "Binary Tree Level Order Traversal",
            "Given the root of a binary tree, return the level order traversal of its nodes' values (from left to right, level by level).",
            "root = [3,9,20,null,null,15,7]",
            "[[3],[9,20],[15,7]]",
            "public class Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        return new ArrayList<>();\n    }\n}",
            "def level_order(root: Optional[TreeNode]) -> list[list[int]]:\n    pass",
            "def serialize_cluster_topology(tree_df) -> list[list[int]]:\n    pass",
            "Standard BFS queue traversal tracking level size at each depth step.",
            "Medium", "Tree & BFS", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Min Cost Climbing Stairs (IBM Dynamic Programming)",
            "You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can climb one or two steps. Return minimum cost to reach the top.",
            "cost = [10,15,20]",
            "15 (Climb 2 steps from index 1)",
            "public class Solution {\n    public int minCostClimbingStairs(int[] cost) {\n        return 0;\n    }\n}",
            "def min_cost_climbing_stairs(cost: list[int]) -> int:\n    pass",
            "def min_execution_stage_cost(costs_df) -> int:\n    pass",
            "Rolling DP: dp[i] = cost[i] + min(dp[i-1], dp[i-2]) in O(N) time and O(1) space.",
            "Easy", "Dynamic Programming", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Daily Temperatures (Monotonic Stack)",
            "Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.",
            "temperatures = [73,74,75,71,69,72,76,73]",
            "[1,1,4,2,1,1,0,0]",
            "public class Solution {\n    public int[] dailyTemperatures(int[] temperatures) {\n        return new int[0];\n    }\n}",
            "def daily_temperatures(temperatures: list[int]) -> list[int]:\n    pass",
            "def days_until_telemetry_spike(temp_df) -> list[int]:\n    pass",
            "Monotonic decreasing Stack storing indices. When current temp > stack top temp, pop and compute day difference.",
            "Medium", "Monotonic Stack", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Maximum Product Subarray",
            "Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.",
            "nums = [2,3,-2,4]",
            "6 ([2,3])",
            "public class Solution {\n    public int maxProduct(int[] nums) {\n        return 0;\n    }\n}",
            "def max_product(nums: list[int]) -> int:\n    pass",
            "def find_max_compounded_yield(series_df) -> int:\n    pass",
            "Maintain both max_so_far and min_so_far because negative numbers multiplied by negative yield positive max.",
            "Medium", "Dynamic Programming", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the architecture of Red Hat OpenShift on IBM Cloud: Kubernetes foundation, Source-to-Image (S2I), Operator Framework, and CRI-O container runtime.",
            "OpenShift adds enterprise capabilities on top of Kubernetes: integrated CI/CD (S2I), declarative Operators managing lifecycle via CRDs, CRI-O as lightweight OCI-compliant runtime, and built-in HAProxy ingress routing.",
            "IBM Cloud & OpenShift Architecture", "Hard"
        ),
        create_technical_question(
            "How does IBM watsonx.ai orchestrate foundation models, and what is the role of watsonx.governance in tracking AI lifecycle compliance?",
            "watsonx.ai provides an enterprise studio for training, fine-tuning, and serving LLMs. watsonx.governance monitors models for drift, enforces responsible AI guardrails, and automates regulatory compliance reporting.",
            "IBM watsonx AI Architecture", "Hard"
        ),
        create_technical_question(
            "Compare IBM MQ enterprise messaging with Apache Kafka. When should an enterprise architect choose IBM MQ over Kafka for financial transaction routing?",
            "IBM MQ guarantees transactional messaging (JMS XA, strict FIFO per queue, message persistence, and point-to-point delivery). Kafka is an append-only distributed event stream optimized for massive data throughput and event replay.",
            "IBM MQ vs Apache Kafka", "Hard"
        ),
        create_technical_question(
            "Explain Mainframe Modernization strategies: API enablement with z/OS Connect EE, event streaming with Kafka, and mainframe offloading to hybrid cloud.",
            "z/OS Connect EE generates RESTful APIs directly from mainframe COBOL copybooks. Mainframe change data capture (CDC) streams real-time updates to Kafka on OpenShift, enabling cloud microservices without mainframe MIPS spikes.",
            "IBM Mainframe & z/OS Modernization", "Hard"
        ),
        create_technical_question(
            "How do Linux kernel parameters (sysctl.conf) like net.core.somaxconn, vm.swappiness, and fs.file-max impact high-load IBM application server performance?",
            "somaxconn sets listen queue backlog for socket connections; vm.swappiness controls memory swapping aggression (set to 10 for latency-critical DBs); fs.file-max increases system-wide open file descriptors.",
            "IBM Linux Systems Administration", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Monolithic, Microservices, and Event-Driven Architecture (EDA) in large-scale IBM enterprise consulting projects.",
            "Monoliths share single deployment artifact; Microservices decompose into independently deployable services communicating via synchronous REST/gRPC; EDA decouples services asynchronously through message brokers.",
            "IBM Enterprise Architecture Patterns", "Medium"
        ),
        create_technical_question(
            "How does Kubernetes Helm package manager manage microservice releases with values.yaml, templates, and automated rollbacks on deployment failure?",
            "Helm packages Kubernetes manifests into reusable charts. Dynamic values.yaml injects environment configurations. 'helm rollback' immediately restores previous working revision if health checks fail.",
            "IBM Kubernetes & Helm", "Medium"
        ),
        create_technical_question(
            "Explain how IBM Instana provides automated APM (Application Performance Monitoring) and 1-second metric resolution with zero-configuration distributed tracing.",
            "Instana auto-discovers running containers and frameworks using eBPF and runtime bytecode instrumentation, generating complete call graphs without manual code annotations.",
            "IBM Observability & Instana", "Medium"
        ),
        create_technical_question(
            "What is the difference between Public Key Infrastructure (PKI) asymmetric encryption (RSA/ECC) and symmetric encryption (AES-256) in IBM hybrid cloud security?",
            "Asymmetric encryption uses public key for encryption and private key for decryption (ideal for key exchange, TLS handshakes). Symmetric encryption uses one shared secret key, delivering 1000x faster bulk data encryption.",
            "IBM Cryptography & Security", "Medium"
        ),
        create_technical_question(
            "How does Tekton Pipelines implement cloud-native CI/CD workflows inside Kubernetes and OpenShift clusters using Custom Resource Definitions (CRDs)?",
            "Tekton defines Tasks and Pipelines as native Kubernetes CRDs. Each step runs in an isolated container within a Kubernetes pod, scaling dynamically and persisting build artifacts on Kubernetes PVCs.",
            "IBM Tekton & Cloud-Native CI/CD", "Medium"
        ),
        create_technical_question(
            "Explain Java Concurrency: The Fork/Join Framework, Work-Stealing Algorithm, and when Parallel Streams improve or degrade execution performance.",
            "ForkJoinPool divides tasks into subtasks recursively. Idle worker threads 'steal' tasks from the tails of busy threads' double-ended queues. Parallel streams degrade performance when tasks involve blocking I/O.",
            "IBM Java Concurrency", "Medium"
        ),
        create_technical_question(
            "How does IBM Cloud Satellite enable clients to run cloud services (watsonx, OpenShift) on-premises in their own datacenters with centralized cloud management?",
            "Satellite links client on-premise compute hosts via secure WireGuard tunnels to IBM Cloud control plane, allowing IBM managed services to run locally behind customer firewalls.",
            "IBM Hybrid Cloud Satellite", "Hard"
        ),
        create_technical_question(
            "Explain Database Sharding versus Database Partitioning in IBM Db2. How does Hash Partitioning distribute analytical table loads?",
            "Partitioning divides tables logically within a single database instance. Sharding distributes data across independent physical database servers. Hash partitioning uses a hash key algorithm to distribute rows evenly across partitions.",
            "IBM Db2 & Database Architecture", "Medium"
        ),
        create_technical_question(
            "What is Mutual TLS (mTLS) authentication in zero-trust architectures, and how do service meshes automate sidecar certificate rotation?",
            "In mTLS, both client and server present and verify X.509 certificates. Service mesh control planes automatically generate short-lived certificates, rotating them every few hours without application restarts.",
            "IBM Zero Trust Security", "Medium"
        ),
        create_technical_question(
            "How do you design a high-throughput event processing pipeline using Apache Kafka and IBM Event Streams for connected IoT telemetry?",
            "Partition topic by deviceId to preserve order per device; tune consumer batch fetch size; use snappy compression; scale consumer groups horizontally to match partition counts.",
            "IBM Event Streams & IoT", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain the architecture of IBM watsonx.ai and how enterprises build, tune, and deploy foundation models with complete data transparency.",
            "Discuss: Open-source and IBM granite models, multi-tenant and dedicated deployment, parameter-efficient fine-tuning with LoRA, and enterprise data protection.",
            "IBM watsonx.ai Foundation Models"
        ),
        create_ai_question(
            "How does IBM watsonx.governance enforce automated AI model lifecycle monitoring, bias mitigation, and regulatory reporting for EU AI Act compliance?",
            "Cover: Automated fact-sheets capturing model lineage, tracking fairness metrics (disparate impact), monitoring drift, and alerting when model accuracy degrades.",
            "IBM watsonx.governance & Compliance"
        ),
        create_ai_question(
            "How would you architect an enterprise RAG system using IBM watsonx and Milvus vector database for legal contract review and risk scoring?",
            "Architecture: Milvus vector indexing, chunking contracts with metadata filters (jurisdiction, expiration), retrieving relevant clauses with hybrid search, and prompt engineering.",
            "IBM Enterprise RAG Architecture"
        ),
        create_ai_question(
            "Describe how IBM Granite models are trained with rigorous intellectual property indemnity and curated enterprise data to eliminate copyright contamination.",
            "Discuss: Filtering out unlicensed public code, transparent training data provenance, enterprise IP indemnity guarantees, and specialized enterprise language tuning.",
            "IBM Granite Enterprise AI Models"
        ),
        create_ai_question(
            "How do you deploy foundation models onto Red Hat OpenShift using KServe and vLLM for optimized inference throughput and dynamic scaling?",
            "Detail: vLLM PagedAttention memory management, continuous batching, KServe custom inference service manifests, and GPU autoscaling with KEDA.",
            "IBM OpenShift AI & vLLM Inference"
        ),
        create_ai_question(
            "How can Generative AI be applied to automate the modernization of legacy enterprise COBOL routines to modern Java microservices at IBM?",
            "Explain: Parsing COBOL AST, translating procedural paragraphs to object-oriented domain classes, generating unit tests to assert behavioral equivalence, and human review.",
            "IBM AI-Assisted Mainframe Modernization"
        ),
        create_ai_question(
            "What techniques do you use to detect and eliminate hallucinations when using LLMs for generating automated IT incident postmortems in AIOps?",
            "Explain: Grounding prompts strictly in raw Splunk/Instana log snippets, temperature=0, enforcing JSON schema outputs, and requiring exact timestamp references.",
            "IBM AIOps Hallucination Mitigation"
        ),
        create_ai_question(
            "How do you implement responsible AI guardrails to filter sensitive customer data and prevent prompt injection in IBM customer service applications?",
            "Detail: watsonx.ai guardrails filtering PII, regex blocklists, system instruction primacy, and automated toxicity scoring before user display.",
            "IBM AI Safety Guardrails"
        ),
        create_ai_question(
            "How does IBM evaluate model drift and data shift in production predictive maintenance models deployed for industrial client equipment?",
            "Discuss: Population Stability Index (PSI), tracking drift in sensor feature distributions, monitoring F1-score drop, and triggering automated pipeline retraining.",
            "IBM MLOps & Model Drift"
        ),
        create_ai_question(
            "What strategies do you adopt for optimizing GPU memory allocation and batching when hosting multi-tenant LLM services on IBM Cloud?",
            "Explain: Tensor parallelism with Ray, PagedAttention memory allocation, 8-bit quantization (bitsandbytes), and dynamic request queuing.",
            "IBM Cloud GPU Optimization"
        )
    ]

    hr_java = [
        create_hr_question(
            "IBM's core values are: Dedication to every client's success, Innovation that matters—for our company and for the world, and Trust and personal responsibility in all relationships. How have you lived these values?",
            "Provide a concrete academic or project example demonstrating commitment to client/user success, creative innovation, and taking personal accountability.",
            "IBM Core Values & Culture"
        ),
        create_hr_question(
            "Why do you specifically want to start and grow your technology career at IBM?",
            "Highlight: IBM's century-long legacy of computing breakthroughs (from mainframes to quantum and watsonx), leadership in hybrid cloud with Red Hat, and ethical AI culture.",
            "IBM Brand & Innovation Heritage"
        ),
        create_hr_question(
            "IBM operates software development and research labs across India (Bangalore, Pune, Hyderabad, Kochi, Gurgaon). Are you fully flexible with relocation and global project teams?",
            "Affirm: Complete willingness to relocate, eagerness to collaborate across international time zones, and adaptability to hybrid workplace practices.",
            "Relocation & Global Collaboration"
        ),
        create_hr_question(
            "Describe a time you worked on a high-stakes software project where a technical deliverable failed unexpectedly right before a client demonstration. How did you respond?",
            "Use STAR: Outline taking personal ownership, remaining calm, isolating the root cause, communicating transparently, and resolving the issue.",
            "Personal Responsibility & Crisis Management"
        ),
        create_hr_question(
            "How do you approach learning complex, foundational enterprise technologies (e.g. OpenShift, Linux internals, enterprise integration) that require significant depth?",
            "Showcase: Curiosity, reading technical documentation, hands-on lab experimentation, building reference apps, and earning certifications.",
            "Technical Depth & Curiosity"
        ),
        create_hr_question(
            "Tell me about a time you collaborated with team members who had conflicting opinions on software design or tool selection. How did you reach consensus?",
            "Emphasize: Respectful listening, evaluating options against business goals and performance benchmarks, and aligning on the best collective approach.",
            "Constructive Collaboration"
        ),
        create_hr_question(
            "Where do you see yourself contributing within IBM over the next 3 to 5 years as a software engineer?",
            "Connect: Growing from Associate System Engineer to Senior Developer / Technical Specialist, contributing to OpenShift and watsonx ecosystems, and mentoring campus joiners.",
            "Career Vision & Growth"
        ),
        create_hr_question(
            "How do you handle receiving critical constructive feedback on your code quality from an IBM Senior Technical Staff Member (STSM) or Architect?",
            "Demonstrate: Professional humility, analyzing the architectural recommendations objectively, and implementing clean code improvements.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Describe a project where you demonstrated 'Innovation that matters' by creating a solution that had a measurable positive impact on your users or peers.",
            "Highlight: Identifying a real bottleneck, building an innovative tool or workflow, and quantifying time or resource savings achieved.",
            "Innovation That Matters"
        ),
        create_hr_question(
            "Do you have any questions for IBM leadership regarding our technology practices, research labs, or career development pathways?",
            "Candidate asks thoughtful questions about IBM Research initiatives, open source contributions, or career mobility across IBM Cloud and Consulting.",
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
# 13. RED HAT
# ==========================================
def build_redhat_catalog():
    apt_java = [
        create_aptitude_question(
            "In Red Hat Linux Systems Logic: An administrator configures file permissions using octal notation 'chmod 754 deploy.sh'. What are the exact permissions assigned to Owner, Group, and Others respectively?",
            ["Owner: rwx, Group: r-x, Others: r--", "Owner: rwx, Group: rw-, Others: r--", "Owner: r-x, Group: r-x, Others: rwx", "Owner: rwx, Group: rwx, Others: r-x"],
            "Owner: rwx, Group: r-x, Others: r--",
            "Octal: 7 = 4+2+1 (rwx), 5 = 4+0+1 (r-x), 4 = 4+0+0 (r--). Owner has rwx, Group has r-x, Others have r--.",
            "Easy", "Red Hat Linux Permissions Math"
        ),
        create_aptitude_question(
            "In network subnetting with CIDR notation 192.168.10.0/27, how many valid assignable host IP addresses are available within this subnet?",
            ["30 assignable hosts", "32 assignable hosts", "28 assignable hosts", "31 assignable hosts"],
            "30 assignable hosts",
            "/27 leaves 32 - 27 = 5 host bits. Total addresses = 2^5 = 32. Subtracting network address (.0) and broadcast address (.31) yields 32 - 2 = 30 assignable hosts.",
            "Medium", "Red Hat Subnetting CIDR"
        ),
        create_aptitude_question(
            "A Linux process scheduler uses Completely Fair Scheduler (CFS). If two processes have nice values 0 and 5, where nice 0 gets 3 times more CPU weight than nice 5, what percentage of CPU time will process with nice 0 receive?",
            ["75%", "66.7%", "80%", "60%"],
            "75%",
            "Weights are in ratio 3:1. Total parts = 4. CPU percentage for nice 0 = 3 / 4 = 75%.",
            "Medium", "Red Hat Kernel Scheduler Math"
        ),
        create_aptitude_question(
            "A Kubernetes cluster has 8 nodes, each with 16 GB of RAM. The system reserves 2 GB per node for OS and kubelet. If pods require 1.5 GB each, what is the maximum number of pods that can run simultaneously?",
            ["72 pods", "64 pods", "80 pods", "56 pods"],
            "74 pods",
            "Usable RAM per node = 16 - 2 = 14 GB. Total usable RAM = 8 * 14 = 112 GB. Pods = 112 // 1.5 = 74.6 => 74 pods (or 72 without packing fragmentation).",
            "Medium", "Red Hat Kubernetes Capacity Math"
        ),
        create_aptitude_question(
            "In Red Hat Concurrency Logic: Three threads access a shared counter using a counting semaphore initialized to 2. How many threads can enter the critical section simultaneously?",
            ["2 threads", "1 thread", "3 threads", "0 threads"],
            "2 threads",
            "A counting semaphore initialized to value K allows up to K concurrent threads to execute acquire() without blocking. Here K = 2.",
            "Easy", "Red Hat Systems Concurrency"
        ),
        create_aptitude_question(
            "A Linux ext4 file system block size is 4KB. A small file of size 500 bytes is created. How much disk space is allocated on the filesystem block layer?",
            ["4 KB (4,096 bytes)", "500 bytes", "1 KB", "2 KB"],
            "4 KB (4,096 bytes)",
            "The minimum disk allocation unit on a filesystem is a block. Even a 500-byte file occupies 1 complete 4KB filesystem block.",
            "Easy", "Red Hat File System Storage"
        ),
        create_aptitude_question(
            "Convert binary subnet mask 11111111.11111111.11111100.00000000 into standard dotted-decimal notation:",
            ["255.255.252.0", "255.255.248.0", "255.255.254.0", "255.255.240.0"],
            "255.255.252.0",
            "11111100 = 128 + 64 + 32 + 16 + 8 + 4 = 252. Thus the mask is 255.255.252.0 (/22).",
            "Easy", "Red Hat Binary Networking"
        ),
        create_aptitude_question(
            "In an open source community project, 12 core maintainers vote on an RFC proposal. In how many ways can a quorum of at least 8 maintainers be formed?",
            ["794 ways", "495 ways", "620 ways", "850 ways"],
            "794 ways",
            "C(12,8) = 495, C(12,9) = 220, C(12,10) = 66, C(12,11) = 12, C(12,12) = 1. Total = 495 + 220 + 66 + 12 + 1 = 794 ways.",
            "Hard", "Red Hat Combinatorics"
        ),
        create_aptitude_question(
            "A container image layers breakdown: Base OS = 120 MB, JRE layer = 80 MB, Application JAR = 20 MB. If 5 containers share the same Base OS and JRE layers on one Docker host, what is the total host disk space used?",
            ["300 MB", "1,100 MB", "220 MB", "400 MB"],
            "300 MB",
            "Shared read-only layers stored once: 120 + 80 = 200 MB. 5 containers each have their own 20 MB application layer: 5 * 20 = 100 MB. Total = 200 + 100 = 300 MB.",
            "Medium", "Red Hat Container Storage"
        ),
        create_aptitude_question(
            "What is the hexadecimal representation of the 32-bit integer 4095?",
            ["0x0FFF", "0x0EFF", "0x1000", "0x0FFE"],
            "0x0FFF",
            "4095 = (15 * 256) + (15 * 16) + 15 = 0x0FFF (since 0x1000 = 4096).",
            "Easy", "Red Hat Hexadecimal Math"
        ),
        create_aptitude_question(
            "In Red Hat Verbal Ability: Choose the word that best completes the sentence: 'The Linux kernel was patched immediately to ______ the zero-day privilege escalation vulnerability.'",
            ["mitigate", "exacerbate", "perpetuate", "aggregate"],
            "mitigate",
            "'Mitigate' means to make less severe or serious. Security patches mitigate vulnerabilities.",
            "Easy", "Red Hat Verbal Ability"
        ),
        create_aptitude_question(
            "A network packet travels through 4 routers with hop latencies [2ms, 3ms, 1ms, 4ms]. If queuing delay adds 50% to the total transmission time, what is the final one-way latency?",
            ["15 ms", "10 ms", "12 ms", "20 ms"],
            "15 ms",
            "Base hop latency = 2 + 3 + 1 + 4 = 10ms. Queuing delay = 50% of 10ms = 5ms. Total = 10 + 5 = 15 ms.",
            "Easy", "Red Hat Network Math"
        ),
        create_aptitude_question(
            "A 64-bit CPU architecture can theoretically address up to 2^64 bytes of memory. What is 2^64 bytes expressed in standard digital storage units?",
            ["16 Exabytes", "16 Terabytes", "16 Petabytes", "16 Zettabytes"],
            "16 Exabytes",
            "2^10 = KB, 2^20 = MB, 2^30 = GB, 2^40 = TB, 2^50 = PB, 2^60 = EB. 2^64 = 2^4 * 2^60 = 16 Exabytes.",
            "Medium", "Red Hat Computer Architecture"
        ),
        create_aptitude_question(
            "In Red Hat Deductive Logic: All container runtimes implement the CRI spec. Containerd is a container runtime. Which conclusion follows?",
            ["Containerd implements the CRI spec", "All CRI implementations are Containerd", "Containerd is not a container runtime", "None follows"],
            "Containerd implements the CRI spec",
            "Direct syllogistic deduction: All Runtimes -> CRI. Containerd -> Runtime. Therefore, Containerd -> CRI.",
            "Easy", "Red Hat Deductive Logic"
        ),
        create_aptitude_question(
            "A Linux server CPU utilization is 60% user, 20% system, 15% iowait, and 5% idle. What percentage of CPU time is spent actively executing software instructions (user + system)?",
            ["80%", "60%", "95%", "75%"],
            "80%",
            "Active execution = User (60%) + System (20%) = 80%. (iowait and idle represent waiting states).",
            "Easy", "Red Hat Systems Performance"
        )
    ]

    code_java = [
        create_coding_problem(
            "Circular Socket Buffer Ring Implementation",
            "Design a circular ring buffer of fixed capacity supporting write(byte), read(), isFull(), and isEmpty() operations in O(1) time without dynamic memory allocation.",
            "capacity = 3, write(1), write(2), read(), write(3), write(4), isFull()",
            "[1, true]",
            "public class RingBuffer {\n    public RingBuffer(int capacity) {}\n    public boolean write(int b) { return false; }\n    public int read() { return -1; }\n    public boolean isFull() { return false; }\n    public boolean isEmpty() { return false; }\n}",
            "class RingBuffer:\n    def __init__(self, capacity: int): pass\n    def write(self, b: int) -> bool: return False\n    def read(self) -> int: return -1\n    def is_full(self) -> bool: return False\n    def is_empty(self) -> bool: return False",
            "class CircularTelemetryBuffer:\n    def __init__(self, capacity: int): pass\n    def append_record(self, val: int): pass",
            "Red Hat kernel systems standard: Use head and tail pointers modulo capacity to advance in O(1) time without shifting elements.",
            "Medium", "Ring Buffer & Design", "O(1)", "O(Capacity)"
        ),
        create_coding_problem(
            "Directory Path Canonicalization (Linux 'cd ..')",
            "Given an absolute path for a Unix-style file system, convert it to the simplified canonical path (resolving '.', '..', and duplicate slashes '//').",
            'path = "/a/./b/../../c/"',
            '"/c"',
            "public class Solution {\n    public String simplifyPath(String path) {\n        return \"/\";\n    }\n}",
            "def simplify_path(path: str) -> str:\n    pass",
            "def canonicalize_directory_index(path_series) -> str:\n    pass",
            "Split by '/', iterate tokens with a Stack: push valid directory names, pop on '..', ignore '.' and empty tokens. Join with '/'.",
            "Medium", "Stack & File Systems", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "File Permission Bitmask Validation",
            "Given a 3-digit octal permission string (e.g. '754') and an operation ('read', 'write', 'execute') for a role ('owner', 'group', 'others'), return true if permission is granted.",
            'perm = "754", role = "group", op = "write"',
            "false ('5' = r-x, write permission is 0)",
            "public class Solution {\n    public static boolean checkPermission(String perm, String role, String op) {\n        return false;\n    }\n}",
            "def check_permission(perm: str, role: str, op: str) -> bool:\n    pass",
            "def validate_rbac_access_flags(role: str, op: str) -> bool:\n    pass",
            "Extract corresponding octal digit, bitwise AND with mask: Read = 4 (100), Write = 2 (010), Execute = 1 (001).",
            "Easy", "Bit Manipulation", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "Endianness Conversion (Reverse 32-bit Integer Bytes)",
            "Given a 32-bit signed integer n, reverse its bytes (convert from Big-Endian to Little-Endian or vice versa) using bitwise shift operators.",
            "n = 0x12345678",
            "0x78563412 (2018915346)",
            "public class Solution {\n    public static int reverseBytes(int n) {\n        return 0;\n    }\n}",
            "def reverse_bytes(n: int) -> int:\n    pass",
            "def byte_swap_network_packet(packet_id: int) -> int:\n    pass",
            "Extract 4 byte segments using bitwise masks and shift: ((n & 0xFF) << 24) | ((n & 0xFF00) << 8) | ((n & 0xFF0000) >>> 8) | ((n >>> 24) & 0xFF).",
            "Easy", "Bit Manipulation & Kernel", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "Subnet IP Range Validator",
            "Given an IPv4 address and a CIDR subnet (e.g. '192.168.1.50' and '192.168.1.0/24'), return true if the IP address belongs to the subnet.",
            'ip = "192.168.1.50", cidr = "192.168.1.0/24"',
            "true",
            "public class Solution {\n    public static boolean ipInSubnet(String ip, String cidr) {\n        return false;\n    }\n}",
            "def ip_in_subnet(ip: str, cidr: str) -> bool:\n    pass",
            "def filter_internal_vpc_traffic(ip_series, cidr: str) -> bool:\n    pass",
            "Convert IPv4 strings to 32-bit integers; apply CIDR bitmask: (ipInt & mask) == (subnetInt & mask).",
            "Medium", "Networking & Bitwise", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "LRU Buffer Pool for Linux Page Cache",
            "Design an in-memory page cache buffer pool with capacity C, evicting the least recently accessed page upon buffer saturation in O(1) operations.",
            "capacity = 2, access(1), access(2), access(1), access(3), isCached(2)",
            "false (Page 2 was evicted)",
            "public class PageBufferPool {\n    public PageBufferPool(int capacity) {}\n    public void access(int pageId) {}\n    public boolean isCached(int pageId) { return false; }\n}",
            "class PageBufferPool:\n    def __init__(self, capacity: int): pass\n    def access(self, page_id: int) -> None: pass\n    def is_cached(self, page_id: int) -> bool: return False",
            "class MemoryPageAnalytics:\n    def __init__(self, capacity: int): pass\n    def log_page_fault(self, page_id: int): pass",
            "Combine Doubly Linked List with Hash Map for O(1) page lookups, node promotion, and eviction.",
            "Medium", "Linked List & Design", "O(1)", "O(Capacity)"
        ),
        create_coding_problem(
            "Semaphore Concurrency Lock Simulator",
            "Simulate a counting semaphore supporting acquire() and release() methods. Maintain current available permit count and enforce that acquire decrements while release increments.",
            "permits = 2, acquire(), acquire(), release(), getAvailablePermits()",
            "1",
            "public class SimpleSemaphore {\n    public SimpleSemaphore(int permits) {}\n    public boolean tryAcquire() { return false; }\n    public void release() {}\n    public int getAvailablePermits() { return 0; }\n}",
            "class SimpleSemaphore:\n    def __init__(self, permits: int): pass\n    def try_acquire(self) -> bool: return False\n    def release(self) -> None: pass\n    def get_available_permits(self) -> int: return 0",
            "class SemaphorePermitTracker:\n    def __init__(self, permits: int): pass\n    def log_acquisition(self) -> bool: return False",
            "Thread-safe atomic integer or synchronization block verifying permit count > 0 before decrementing.",
            "Easy", "Concurrency & Design", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "Linux Process Scheduler Queue Simulation",
            "Given an array of processes with burst times and a Round Robin time quantum q, compute the total turnaround time for each process to finish execution.",
            "processes = [5, 3, 8], q = 2",
            "Order of completion: P2 finishes at 7, P1 finishes at 11, P3 finishes at 16",
            "public class Solution {\n    public static int[] roundRobinScheduling(int[] burstTimes, int q) {\n        return new int[0];\n    }\n}",
            "def round_robin_scheduling(burst_times: list[int], q: int) -> list[int]:\n    pass",
            "def simulate_process_completion_times(proc_df, q: int):\n    pass",
            "Queue-based simulation: Enqueue processes, run for min(remaining, q), re-enqueue if remaining > 0, record completion time.",
            "Medium", "Queue Simulation", "O(N * maxBurst)", "O(N)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain Linux Kernel cgroups v2 (Control Groups) and Namespaces (PID, Mount, Network, IPC, UTS, User), and how they form the foundation of Linux containers.",
            "Namespaces provide virtualization and isolation (making a process believe it has its own private network stack, process tree, and mount points). Cgroups enforce resource quotas (CPU limits, memory OOM killer triggers, block I/O throttling).",
            "Red Hat Kernel & Container Internals", "Hard"
        ),
        create_technical_question(
            "What is eBPF (Extended Berkeley Packet Filter), and how does it allow developers to run custom sandboxed bytecode inside the Linux kernel without modifying kernel source code?",
            "eBPF programs attach to kernel tracepoints, kprobes, and XDP network hooks. The in-kernel verifier guarantees safety (no unbounded loops, no illegal memory access); JIT compiler executes bytecode at bare-metal speed for tracing, security, and networking.",
            "Red Hat eBPF & Kernel Tracing", "Hard"
        ),
        create_technical_question(
            "Explain the Kubernetes Operator Pattern. How do Custom Resource Definitions (CRDs) and Controller reconciliation loops automate complex stateful application management?",
            "A CRD extends the Kubernetes API with domain-specific schemas. The Operator Controller watches CRD events and executes an infinite reconciliation loop comparing observed cluster state with desired spec, executing compensating actions until convergence.",
            "Red Hat Kubernetes Operator Pattern", "Hard"
        ),
        create_technical_question(
            "Compare Container Runtimes: CRI-O, Podman, Containerd, and Docker. Why did Red Hat engineer Podman to be daemonless and rootless?",
            "Traditional Docker requires a root daemon (dockerd) representing a single point of failure and security risk. Podman directly forks OCI runc containers using the fork/exec model, running securely in unprivileged user namespaces without a daemon.",
            "Red Hat Podman & CRI-O", "Hard"
        ),
        create_technical_question(
            "Explain Linux virtual memory: VMA (Virtual Memory Area), Page Tables, TLB, and how the Linux OOM (Out Of Memory) Killer selects victim processes via oom_score.",
            "When physical memory and swap are exhausted, the kernel OOM killer inspects all processes, computing oom_score based on percentage of RAM consumed and /proc/[pid]/oom_score_adj. It sends SIGKILL to the process with the highest score.",
            "Red Hat Linux Memory & OOM", "Hard"
        ),
        create_technical_question(
            "How does GitOps deployment architecture operate using ArgoCD on Red Hat OpenShift, and how does it handle automated drift reconciliation?",
            "ArgoCD continuously compares the desired state stored in Git repositories with the live Kubernetes cluster state. When configuration drift occurs, ArgoCD alerts or automatically synchronizes the cluster back to match Git.",
            "Red Hat GitOps & ArgoCD", "Medium"
        ),
        create_technical_question(
            "Explain Linux systemd service management: Unit files, Dependencies (Wants vs Requires), Target files, and cgroup resource limits in service definitions.",
            "systemd initializes user space as PID 1. Unit files (.service) configure startup commands. 'Requires' establishes hard dependencies (if dependency fails, unit fails); 'Wants' establishes soft dependencies. MemoryMax sets cgroup limits.",
            "Red Hat systemd Architecture", "Medium"
        ),
        create_technical_question(
            "How do Container Network Interface (CNI) plugins (OVN-Kubernetes, Calico) implement pod-to-pod networking using VXLAN overlays and geneve tunnels?",
            "CNIs assign IP addresses to pods via IPAM. For cross-node pod traffic, VXLAN capsules the inner Ethernet packet inside an outer UDP packet sent between host nodes, unwrapped at destination host and delivered to pod veth interface.",
            "Red Hat CNI & Networking", "Hard"
        ),
        create_technical_question(
            "Explain Linux Inode architecture: What metadata is stored in an inode, and why does exhausting inodes prevent file creation even when disk space is abundant?",
            "An inode stores file metadata (size, permissions, ownership, timestamps, block pointers), but not the filename. Every file requires one inode; if all inodes are allocated, 'No space left on device' errors occur despite free megabytes.",
            "Red Hat Linux File Systems", "Medium"
        ),
        create_technical_question(
            "What is the difference between Hard Links and Symbolic (Soft) Links in Linux? What happens to the target data when the original file is deleted?",
            "A Hard Link is an additional directory pointer sharing the exact same inode number (data remains until all links are deleted). A Soft Link is a separate pointer file containing the text path of the target (becomes broken if original is deleted).",
            "Red Hat Linux Inodes & Links", "Easy"
        ),
        create_technical_question(
            "Explain Linux Inter-Process Communication (IPC): Unix Domain Sockets vs TCP Loopback Sockets. Why are Unix Domain Sockets significantly faster for container IPC?",
            "Unix Domain Sockets operate entirely in kernel memory without executing network stack protocols (no TCP checksums, packet headers, or routing overhead), delivering lower latency and higher bandwidth than 127.0.0.1 loopback.",
            "Red Hat Linux IPC & Sockets", "Medium"
        ),
        create_technical_question(
            "How does SELinux (Security-Enhanced Linux) enforce Mandatory Access Control (MAC) via Type Enforcement, Policies, and Contexts (user:role:type:level)?",
            "SELinux inspects every system call against security policy rules. Unlike Discretionary Access Control (chmod/chown) where root can do anything, SELinux restricts processes based on type (e.g. httpd_t can only read httpd_sys_content_t).",
            "Red Hat SELinux & Security", "Hard"
        ),
        create_technical_question(
            "Explain Concurrency Primitives in systems programming: Mutex vs Spinlock vs RCU (Read-Copy Update) in the Linux kernel.",
            "Mutex puts waiting threads to sleep (context switch). Spinlocks loop actively on CPU (ideal for short critical sections in interrupt handlers). RCU allows lockless readers while writers make a private copy and update pointer atomically.",
            "Red Hat Kernel Concurrency", "Hard"
        ),
        create_technical_question(
            "How does Red Hat Enterprise Linux (RHEL) package management (RPM and DNF) resolve dependencies, verify GPG signatures, and track transaction rollbacks?",
            "RPM stores package metadata and file checksums in a local SQLite/BDB database. DNF calculates dependency graphs using libsolv (SAT solver), downloads packages, verifies SHA-256 and GPG signatures, and supports transaction history rollbacks.",
            "Red Hat RPM & DNF Internals", "Medium"
        ),
        create_technical_question(
            "Explain High Availability Clustering with Pacemaker and Corosync: Quorum votes, Fencing (STONITH), and split-brain prevention.",
            "Corosync provides cluster membership and messaging. Pacemaker manages resource failover. STONITH (Shoot The Other Node In The Head) forcibly powers off unresponsive nodes via IPMI to prevent concurrent writes and data corruption.",
            "Red Hat HA Clustering & STONITH", "Hard"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain the Red Hat OpenShift AI platform architecture and how it enables data science teams to train and serve open source models on Kubernetes.",
            "Discuss: OpenShift AI integration with Kubeflow pipelines, Jupyter notebooks, Ray distributed compute, ModelMesh serving, and hardware GPU acceleration.",
            "Red Hat OpenShift AI"
        ),
        create_ai_question(
            "How do you serve large open source foundation models (Llama 3, Mistral) on Kubernetes using vLLM and PagedAttention for maximum token throughput?",
            "Detail: PagedAttention virtual memory allocation for KV-caches, dynamic request batching, tensor parallel model sharding across GPUs, and KServe integration.",
            "Red Hat vLLM & Kubernetes Inference"
        ),
        create_ai_question(
            "How does Red Hat Ansible Lightspeed utilize Generative AI to translate natural language prompts into production-grade Ansible Playbooks?",
            "Explain: Prompt preprocessing, passing IT automation context to specialized models, generating idempotent task modules, and enforcing linting standards.",
            "Red Hat Ansible Lightspeed AI"
        ),
        create_ai_question(
            "Describe how you design a secure, air-gapped Generative AI deployment for government or defense clients using Red Hat OpenShift.",
            "Architecture: Offline mirror registry of container images and model weights, zero internet egress, self-hosted vector databases, and air-gapped KMS encryption.",
            "Red Hat Air-Gapped AI Architecture"
        ),
        create_ai_question(
            "How do you implement Retrieval-Augmented Generation (RAG) over Linux kernel and Red Hat technical documentation using Chroma / Milvus?",
            "Detail: Markdown and man-page parsing, chunking with header metadata, generating embeddings with open source models, and grounding technical answers with exact man-page citations.",
            "Red Hat Technical Docs RAG"
        ),
        create_ai_question(
            "What techniques do you use to evaluate open source LLM safety, prompt injection resistance, and alignment before enterprise production deployment?",
            "Discuss: Benchmarking on red-teaming datasets, testing jailbreak resistance with automated fuzzers, and configuring Llama-Guard classification filters.",
            "Red Hat Open Source AI Security"
        ),
        create_ai_question(
            "How do you monitor GPU utilization, memory temperature, and power consumption across Kubernetes nodes using NVIDIA GPU Operator and Prometheus?",
            "Detail: NVIDIA Data Center GPU Manager (DCGM) exporter exposing metrics to Prometheus, alerting on thermal throttling, and configuring Grafana dashboard heatmaps.",
            "Red Hat GPU Monitoring & DCGM"
        ),
        create_ai_question(
            "Describe how you fine-tune open source models using Parameter-Efficient Fine-Tuning (PEFT/LoRA) on Red Hat OpenShift compute clusters.",
            "Explain: Freezing base weights, adding low-rank adapter matrices, distributed training with PyTorch FSDP on OpenShift jobs, and exporting merged weights.",
            "Red Hat Model Fine-Tuning"
        ),
        create_ai_question(
            "How do you implement continuous integration testing for AI model containers using Tekton and OpenShift Pipelines?",
            "Architecture: Git push triggers Tekton pipeline; container build with Podman; automated inference latency test on test GPU; pushing verified image to Quay registry.",
            "Red Hat MLOps & Tekton"
        ),
        create_ai_question(
            "How does Red Hat champion Open Source AI and transparent model licensing (e.g. Apache 2.0, MIT) over proprietary black-box cloud APIs?",
            "Discuss: Model weight availability, reproducible training datasets, preventing vendor lock-in, and giving enterprises full ownership of their intellectual property.",
            "Red Hat Open Source AI Philosophy"
        )
    ]

    hr_java = [
        create_hr_question(
            "Red Hat's culture is rooted in the 'Open Source Way': Open Exchange, Participation, Rapid Prototyping, Meritocracy, and Community. How have you practiced these values?",
            "Provide a concrete example of open collaboration, sharing knowledge publicly, accepting peer feedback, or contributing to open projects.",
            "The Open Source Way & Meritocracy"
        ),
        create_hr_question(
            "Why do you specifically choose Red Hat to advance your software systems engineering career?",
            "Highlight: Red Hat's undisputed leadership in enterprise open source, Linux kernel and Kubernetes engineering culture, and community-first philosophy.",
            "Red Hat Brand Motivation"
        ),
        create_hr_question(
            "Red Hat engineering decisions are determined by meritocracy and technical excellence rather than corporate hierarchy. How do you handle defending your technical ideas in an open forum?",
            "Demonstrate: Confidence backed by benchmarks and code prototypes, welcoming constructive critique, and remaining humble when counter-evidence is provided.",
            "Open Debate & Meritocracy"
        ),
        create_hr_question(
            "Tell me about a time you contributed to an open-source project or shared your code publicly on GitHub. What was your experience collaborating with upstream developers?",
            "Showcase: Following project contribution guidelines, addressing PR code review feedback, writing documentation, and respecting community standards.",
            "Open Source Community Contribution"
        ),
        create_hr_question(
            "Red Hat operates major engineering offices in Bangalore, Pune, and globally with extensive remote work. How do you maintain high autonomy and self-discipline?",
            "Focus on: Asynchronous communication, documentation-first mindset, setting clear daily goals, and proactively communicating blockers.",
            "Remote Autonomy & Self-Discipline"
        ),
        create_hr_question(
            "Describe a time you encountered a deeply complex system bug that took multiple days to isolate. What was your debugging strategy?",
            "Use STAR: Isolating variables, reading kernel/system logs, using diagnostic tools (strace, gdb, perf), testing hypotheses systematically, and finding the fix.",
            "Deep Technical Problem Solving"
        ),
        create_hr_question(
            "Tell me about a time you had a fundamental disagreement with a colleague over a software design choice. How did you resolve it constructively?",
            "Explain: Building a small proof-of-concept benchmark, letting empirical data guide the decision, and maintaining professional respect.",
            "Data-Driven Conflict Resolution"
        ),
        create_hr_question(
            "Where do you see yourself growing at Red Hat over the next 3 to 5 years as an engineer?",
            "Connect: Becoming a core contributor to upstream open source projects (Kubernetes, Podman, Linux kernel), and growing into a recognized technical lead.",
            "Career Growth & Open Source Impact"
        ),
        create_hr_question(
            "How do you share technical knowledge with your peers and foster a culture of transparent mentoring?",
            "Highlight: Writing internal blog posts, conducting brown-bag technical sessions, pair programming, and giving thorough supportive code reviews.",
            "Knowledge Sharing & Mentorship"
        ),
        create_hr_question(
            "Do you have any questions for Red Hat engineering leadership regarding our open source initiatives, kernel contributions, or culture?",
            "Candidate asks about upstream-first development policies, contributions to CNCF/Linux Foundation projects, or engineering career tracks.",
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
# 14. HCLTECH
# ==========================================
def build_hcltech_catalog():
    apt_java = [
        create_aptitude_question(
            "In HCL First Careers Quantitative: An arithmetic progression (AP) has first term a = 5 and common difference d = 3. What is the sum of the first 20 terms of this progression?",
            ["670", "650", "700", "640"],
            "670",
            "Formula: S_n = (n/2) * [2a + (n - 1)d] = (20/2) * [2*5 + 19*3] = 10 * [10 + 57] = 10 * 67 = 670.",
            "Easy", "HCL Arithmetic Progression"
        ),
        create_aptitude_question(
            "A hardware engineering team at HCLTech tests 4 IoT sensors. The failure probabilities of the sensors are independent at 0.05 each. What is the probability that all 4 sensors function properly?",
            ["81.45%", "85.00%", "90.25%", "76.00%"],
            "81.45%",
            "P(functions) = 1 - 0.05 = 0.95. P(all 4 function) = (0.95)^4 ≈ 0.8145 = 81.45%.",
            "Medium", "HCL Reliability Probability"
        ),
        create_aptitude_question(
            "In HCL Reasoning Ability: Statements: Some laptops are tablets. All tablets are mobile devices. Conclusion I: Some mobile devices are laptops. Conclusion II: Some mobile devices are tablets.",
            ["Both conclusions I and II follow", "Only conclusion I follows", "Only conclusion II follows", "Neither follows"],
            "Both conclusions I and II follow",
            "Since some laptops are tablets and all tablets are mobile devices, some laptops are mobile devices (conversion gives I). Since all tablets are mobile devices, conversion gives II. Both follow.",
            "Easy", "HCL Syllogisms"
        ),
        create_aptitude_question(
            "A software client pays an invoice of Rs. 72,000 after receiving a 10% loyalty discount and a subsequent 20% trade discount. What was the original invoice price before any discounts?",
            ["Rs. 100,000", "Rs. 95,000", "Rs. 110,000", "Rs. 90,000"],
            "Rs. 100,000",
            "Net multiplier = 0.90 * 0.80 = 0.72. Original price = 72,000 / 0.72 = Rs. 100,000.",
            "Easy", "HCL Commercial Math"
        ),
        create_aptitude_question(
            "Find the next number in the HCL numerical series: 6, 13, 28, 59, ___?",
            ["122", "120", "118", "124"],
            "122",
            "Pattern: Each term is (previous * 2) + 1, +2, +3: 6*2+1=13, 13*2+2=28, 28*2+3=59. Next is 59*2 + 4 = 118 + 4 = 122.",
            "Medium", "HCL Number Series"
        ),
        create_aptitude_question(
            "In how many ways can 5 software engineering trainees and 3 team leads be seated around a circular table if all 3 team leads must sit together?",
            ["720 ways", "120 ways", "144 ways", "360 ways"],
            "720 ways",
            "Bundle 3 leads as 1 unit. Total units = 5 trainees + 1 bundle = 6 units. Circular permutations of 6 units = (6 - 1)! = 5! = 120 ways. The 3 leads can arrange internally in 3! = 6 ways. Total = 120 * 6 = 720 ways.",
            "Medium", "HCL Permutations"
        ),
        create_aptitude_question(
            "A tank can be filled by an inlet pipe in 8 hours and emptied by an outlet pipe in 12 hours. If both pipes are opened simultaneously, how long will it take to fill the tank?",
            ["24 hours", "20 hours", "18 hours", "16 hours"],
            "24 hours",
            "Net rate = 1/8 - 1/12 = (3 - 2) / 24 = 1/24 tank/hour. Total time = 24 hours.",
            "Easy", "HCL Pipes & Cisterns"
        ),
        create_aptitude_question(
            "In HCL Verbal Ability: Identify the word with the correct spelling:",
            ["Accommodate", "Acommodate", "Accomodate", "Acomodate"],
            "Accommodate",
            "The standard correct spelling has double 'c' and double 'm': 'Accommodate'.",
            "Easy", "HCL English Ability"
        ),
        create_aptitude_question(
            "A person travels 180 km at 60 km/h and returns the same distance at 90 km/h. What is the average speed for the entire round trip?",
            ["72 km/h", "75 km/h", "70 km/h", "80 km/h"],
            "72 km/h",
            "Average speed = (2 * v1 * v2) / (v1 + v2) = (2 * 60 * 90) / (60 + 90) = 10,800 / 150 = 72 km/h.",
            "Easy", "HCL Harmonic Mean Speed"
        ),
        create_aptitude_question(
            "If 15% of A equals 20% of B, what is the ratio of A to B?",
            ["4:3", "3:4", "5:4", "4:5"],
            "4:3",
            "0.15 * A = 0.20 * B => A / B = 0.20 / 0.15 = 20 / 15 = 4 / 3.",
            "Easy", "HCL Ratio & Proportion"
        ),
        create_aptitude_question(
            "In HCL Direction Sense: A delivery robot moves 8 meters South, turns Left and moves 6 meters. How far is the robot from its starting location?",
            ["10 meters", "14 meters", "12 meters", "8 meters"],
            "10 meters",
            "Moving South then Left means moving East. By Pythagorean theorem: Distance = sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 meters.",
            "Easy", "HCL Geometry & Direction"
        ),
        create_aptitude_question(
            "What is the simple interest on Rs. 8,000 at 7.5% per annum for 3 years?",
            ["Rs. 1,800", "Rs. 1,600", "Rs. 2,000", "Rs. 1,750"],
            "Rs. 1,800",
            "SI = (P * R * T)/100 = (8000 * 7.5 * 3)/100 = 80 * 22.5 = Rs. 1,800.",
            "Easy", "HCL Simple Interest"
        ),
        create_aptitude_question(
            "A code snippet generates 32 distinct output combinations. How many bits are required to represent each combination uniquely?",
            ["5 bits", "4 bits", "6 bits", "8 bits"],
            "5 bits",
            "2^n >= 32 => 2^5 = 32. Exactly 5 bits are required.",
            "Easy", "HCL Binary Math"
        ),
        create_aptitude_question(
            "In HCL Analogies: COMPILER : BYTECODE :: INTERPRETER : ___?",
            ["Direct Execution", "Source Code", "Hardware", "Operating System"],
            "Direct Execution",
            "A compiler translates source code into bytecode; an interpreter executes source code directly line by line.",
            "Easy", "HCL Analogies"
        ),
        create_aptitude_question(
            "A sum of Rs. 6,400 is divided among three developers A, B, and C in the ratio 3:5:8. What is the share of developer B?",
            ["Rs. 2,000", "Rs. 1,200", "Rs. 3,200", "Rs. 1,800"],
            "Rs. 2,000",
            "Total ratio parts = 3 + 5 + 8 = 16. Share of B = (5 / 16) * 6400 = 5 * 400 = Rs. 2,000.",
            "Easy", "HCL Proportional Math"
        )
    ]

    code_java = [
        create_coding_problem(
            "Array Left Rotation by K Positions",
            "Given an integer array nums, rotate the array to the left by k positions where k is non-negative in O(N) time and O(1) space.",
            "nums = [1,2,3,4,5,6,7], k = 3",
            "[4,5,6,7,1,2,3]",
            "public class Solution {\n    public static void rotateLeft(int[] nums, int k) {\n    }\n}",
            "def rotate_left(nums: list[int], k: int) -> list[int]:\n    pass",
            "def rotate_shift_schedule(schedule_df, k: int):\n    pass",
            "HCLTech First Careers classic: Reverse first k elements, reverse remaining n-k elements, then reverse the entire array.",
            "Easy", "Array & Reversal Algorithm", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Count Pairs with Given Sum (HCLTech Coding)",
            "Given an array of integers and a target sum, find the number of pairs of elements in the array whose sum is equal to the target.",
            "arr = [1, 5, 7, 1], target = 6",
            "2 (Pairs: [1, 5] and [5, 1])",
            "public class Solution {\n    public static int getPairsCount(int[] arr, int target) {\n        return 0;\n    }\n}",
            "def get_pairs_count(arr: list[int], target: int) -> int:\n    pass",
            "def match_transaction_pairs(tx_series, target: int) -> int:\n    pass",
            "Use HashMap to store element frequencies; for each element x, add count of (target - x) to total pairs.",
            "Easy", "Hash Map & Array", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Check if Array is Sorted and Rotated",
            "Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero).",
            "nums = [3,4,5,1,2]",
            "true",
            "public class Solution {\n    public boolean check(int[] nums) {\n        return false;\n    }\n}",
            "def check(nums: list[int]) -> bool:\n    pass",
            "def verify_circular_sorted_timestamps(times_df) -> bool:\n    pass",
            "Count the number of times nums[i] > nums[(i+1)%n]. If count <= 1, it is a valid rotated sorted array.",
            "Easy", "Array Scanning", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "String Run-Length Compression",
            "Given an array of characters chars, compress it using the following algorithm: For each group of consecutive repeating characters, write character followed by count.",
            'chars = ["a","a","b","b","c","c","c"]',
            'Return 6, chars = ["a","2","b","2","c","3"]',
            "public class Solution {\n    public int compress(char[] chars) {\n        return 0;\n    }\n}",
            "def compress(chars: list[str]) -> int:\n    pass",
            "def compress_sensor_packet_stream(stream_df) -> int:\n    pass",
            "Two pointers: Read pointer counts consecutive identical characters; write pointer writes character and digit counts in-place.",
            "Medium", "Two Pointers & In-Place", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Find All Duplicates in an Array in O(N)",
            "Given an integer array nums of length n where all integers are in range [1, n], find all elements that appear twice without extra space.",
            "nums = [4,3,2,7,8,2,3,1]",
            "[2,3]",
            "public class Solution {\n    public List<Integer> findDuplicates(int[] nums) {\n        return new ArrayList<>();\n    }\n}",
            "def find_duplicates(nums: list[int]) -> list[int]:\n    pass",
            "def identify_duplicate_records(records_df) -> list[int]:\n    pass",
            "Index negation trick: Use abs(num)-1 as index; negate value at that index; if already negative, duplicate found.",
            "Medium", "Array In-Place", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Peak Element Finder in O(log N)",
            "A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index in O(log N) time.",
            "nums = [1,2,3,1]",
            "2 (Element 3)",
            "public class Solution {\n    public int findPeakElement(int[] nums) {\n        return 0;\n    }\n}",
            "def find_peak_element(nums: list[int]) -> int:\n    pass",
            "def locate_peak_sensor_anomaly(sensor_df) -> int:\n    pass",
            "Binary search: If nums[mid] < nums[mid+1], peak must lie to the right; else peak must lie to the left.",
            "Medium", "Binary Search", "O(log N)", "O(1)"
        ),
        create_coding_problem(
            "Longest Common Prefix in String Array",
            "Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.",
            'strs = ["flower","flow","flight"]',
            '"fl"',
            "public class Solution {\n    public String longestCommonPrefix(String[] strs) {\n        return \"\";\n    }\n}",
            "def longest_common_prefix(strs: list[str]) -> str:\n    pass",
            "def extract_common_routing_prefix(prefix_series) -> str:\n    pass",
            "Horizontal scanning: Set prefix = strs[0], trim prefix until strs[i].startsWith(prefix) is true for all words.",
            "Easy", "String Scanning", "O(S)", "O(1)"
        ),
        create_coding_problem(
            "Anagram Substring Search (Sliding Window)",
            "Given two strings s and p, return an array of all the start indices of p's anagrams in s.",
            's = "cbaebabacd", p = "abc"',
            "[0, 6]",
            "public class Solution {\n    public List<Integer> findAnagrams(String s, String p) {\n        return new ArrayList<>();\n    }\n}",
            "def find_anagrams(s: str, p: str) -> list[int]:\n    pass",
            "def search_pattern_occurrences(text_df, pattern: str):\n    pass",
            "Sliding window of length p.length() with 26-element character frequency array comparison in O(N).",
            "Medium", "Sliding Window", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain HCLTech's 'Ideapreneurship' engineering approach and how microservices are designed for high throughput in engineering R&D services.",
            "Ideapreneurship empowers grassroots engineers to innovate directly on client platforms. High-throughput microservices utilize non-blocking I/O, asynchronous messaging (RabbitMQ/Kafka), and connection pool tuning to minimize latency.",
            "HCLTech Ideapreneurship & Engineering", "Medium"
        ),
        create_technical_question(
            "In IoT and embedded connected systems at HCLTech, compare MQTT and CoAP protocols for constrained device telemetry transmission.",
            "MQTT runs over TCP using a centralized publish/subscribe broker (ideal for persistent stateful connections). CoAP runs over UDP using RESTful requests (lightweight, designed for resource-constrained microcontroller sensors).",
            "HCLTech IoT & Embedded Protocols", "Hard"
        ),
        create_technical_question(
            "Explain Multithreading Synchronization Primitives in Java: ReentrantLock vs synchronized keyword, and when to use Condition variables.",
            "ReentrantLock provides explicit lock/unlock, tryLock() with timeout, interruptible locks, and multiple Condition variables (await/signal) for fine-grained thread coordination, whereas synchronized is lexical and less flexible.",
            "HCLTech Java Concurrency", "Medium"
        ),
        create_technical_question(
            "What is CountDownLatch and CyclicBarrier in java.util.concurrent, and what are their operational differences in multi-stage batch processing?",
            "CountDownLatch is a one-time gate: threads wait until counter reaches 0 via countDown(). CyclicBarrier can be reset and reused after all threads reach the barrier point.",
            "HCLTech Concurrency Utilities", "Medium"
        ),
        create_technical_question(
            "Explain Database Normalization (1NF, 2NF, 3NF, BCNF) and when engineering R&D platforms intentionally denormalize database schemas.",
            "1NF removes repeating groups; 2NF removes partial key dependencies; 3NF removes transitive dependencies; BCNF ensures every determinant is a candidate key. Analytical logging systems denormalize to eliminate expensive joins.",
            "HCLTech Database Architecture", "Medium"
        ),
        create_technical_question(
            "How does Spring Boot Auto-Configuration work using @EnableAutoConfiguration and META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports?",
            "Spring Boot scans starter dependencies and evaluates @Conditional annotations (@ConditionalOnClass, @ConditionalOnMissingBean) to automatically register default beans only when custom beans are not defined.",
            "HCLTech Spring Boot Internals", "Medium"
        ),
        create_technical_question(
            "Explain Deadlock Prevention using Resource Ordering (Banker's Algorithm concepts) in multi-threaded Java applications.",
            "Deadlock requires mutual exclusion, hold and wait, no preemption, and circular wait. Imposing a global strict acquisition order on resources breaks the circular wait condition, mathematically guaranteeing deadlock immunity.",
            "HCLTech Operating Systems & Deadlocks", "Hard"
        ),
        create_technical_question(
            "How do you configure JUnit 5 and Mockito to perform parameterized unit testing (@ParameterizedTest, @ValueSource, @MethodSource)?",
            "@ParameterizedTest executes a test method multiple times with different arguments specified by @ValueSource or @MethodSource, verifying boundary conditions efficiently without duplicate code.",
            "HCLTech Unit Testing & Quality", "Easy"
        ),
        create_technical_question(
            "Explain Java Non-blocking I/O (Java NIO): Channels, Buffers, and Selectors compared to traditional blocking I/O (java.io).",
            "Traditional I/O blocks a thread per connection. Java NIO uses Selectors where a single thread monitors multiple non-blocking Channels for read/write readiness, scaling to thousands of concurrent network connections.",
            "HCLTech Java NIO", "Hard"
        ),
        create_technical_question(
            "What is the difference between Git Merge and Git Rebase? When should an enterprise developer avoid rebasing public branches?",
            "Git merge creates a merge commit preserving historical chronological branching. Git rebase moves the base of a branch to create a linear history. Rebasing shared public branches rewrites commit hashes, breaking teammates' local clones.",
            "HCLTech Git & Version Control", "Medium"
        ),
        create_technical_question(
            "How do you detect and profile memory leaks in Java applications using VisualVM and analyze Heap Histogram object allocations?",
            "Connect VisualVM to running JVM; inspect Live Objects in Memory profiler; take two consecutive heap dumps during load testing and compute the diff to find classes with continuously growing instance counts.",
            "HCLTech Performance Profiling", "Medium"
        ),
        create_technical_question(
            "Explain the Builder Pattern in Java. How does Project Lombok's @Builder annotation simplify object instantiation in enterprise DTOs?",
            "Builder pattern provides a fluent API for constructing complex objects step-by-step with immutable fields. Lombok generates a private constructor and static builder class at compile time without manual boilerplate.",
            "HCLTech Design Patterns", "Easy"
        ),
        create_technical_question(
            "How does Dockerize a multi-tier Spring Boot application using Dockerfile ENTRYPOINT, environment variable injection, and volume mounts?",
            "Dockerfile builds JAR; ENTRYPOINT ['java', '-jar', 'app.jar'] executes container; environment variables override spring.datasource properties; volume mounts persist application log files to host disk.",
            "HCLTech Docker Deployment", "Medium"
        ),
        create_technical_question(
            "What are SQL Stored Procedures and Triggers, and how do you prevent performance bottlenecks when triggers fire on bulk database imports?",
            "Stored procedures encapsulate procedural SQL on DB server. Triggers execute automatically on row changes. During bulk imports, row-level triggers execute per row, creating severe I/O thrashing; disable triggers during bulk ETL.",
            "HCLTech SQL & Stored Procedures", "Medium"
        ),
        create_technical_question(
            "Explain the difference between HashMap and LinkedHashMap in Java regarding iteration ordering and memory overhead.",
            "HashMap offers no iteration order guarantees. LinkedHashMap maintains a doubly linked list running through all entries, preserving insertion order (or access order for LRU caches) at the cost of slight memory overhead per node.",
            "HCLTech Java Collections", "Easy"
        )
    ]

    ai_java = [
        create_ai_question(
            "How does HCLTech apply Artificial Intelligence and Machine Learning in engineering R&D services to automate IoT sensor predictive maintenance?",
            "Discuss: Collecting vibration/temperature sensor streams via MQTT, training anomaly detection models (Random Forest, LSTM), and predicting equipment failure before downtime occurs.",
            "HCLTech IoT Predictive AI"
        ),
        create_ai_question(
            "Describe how HCLTech's Ideapreneurship culture encourages software engineers to propose and develop generative AI tools for delivery automation.",
            "Explain: Grassroots hackathons, employee innovation portals, incubating internal AI prototypes into commercial client offerings, and rewarding bottom-up problem solving.",
            "HCLTech AI Ideapreneurship"
        ),
        create_ai_question(
            "How do you design an automated unit test generation pipeline using Generative AI for legacy Java enterprise repositories with minimal existing test coverage?",
            "Detail: Parsing Java classes with JavaParser, prompting LLM with class methods and edge-case criteria, compiling generated tests with Maven, and checking code coverage gains in JaCoCo.",
            "HCLTech Automated Test AI"
        ),
        create_ai_question(
            "How do you deploy lightweight computer vision models on edge IoT devices (Raspberry Pi, Nvidia Jetson) for real-time manufacturing defect inspection?",
            "Architecture: Model quantization using ONNX Runtime / TensorRT, capturing camera frames, running inference in < 30ms, and triggering automated alert webhooks.",
            "HCLTech Edge AI & Computer Vision"
        ),
        create_ai_question(
            "What techniques prevent AI hallucinations when using LLMs for automated technical documentation generation from complex source code?",
            "Discuss: Grounding prompts in Abstract Syntax Trees (AST), strictly constraining outputs to documented function parameters, and running docstring linters.",
            "HCLTech Code Documentation AI"
        ),
        create_ai_question(
            "How do you implement Retrieval-Augmented Generation (RAG) for an engineering team to query thousands of internal equipment hardware datasheets?",
            "Architecture: Document ingestion with PyMuPDF, vector embeddings with sentence-transformers, storage in Qdrant/Postgres pgvector, and generating answers with page citations.",
            "HCLTech Hardware Specs RAG"
        ),
        create_ai_question(
            "Describe how AI-powered code analysis tools are integrated into HCLTech CI/CD pipelines to detect security vulnerabilities and enforce coding guidelines.",
            "Detail: Git push triggers webhook; static analysis + LLM scans for OWASP Top 10 vulnerabilities; automated pull request comments suggest secure refactoring.",
            "HCLTech DevSecOps & AI"
        ),
        create_ai_question(
            "How do you measure and optimize model latency when deploying deep learning models on resource-constrained embedded automotive microcontrollers?",
            "Discuss: Pruning unnecessary neural weights, INT8 quantization, using CMSIS-NN libraries, and profiling memory usage with hardware debuggers.",
            "HCLTech Embedded AI Optimization"
        ),
        create_ai_question(
            "How does HCLTech ensure intellectual property security and client confidentiality when developers utilize generative AI programming tools?",
            "Cover: Air-gapped corporate AI instances, zero code retention agreements with AI vendors, automated secret scanning, and enforcing strict peer code reviews.",
            "HCLTech AI IP & Security"
        ),
        create_ai_question(
            "How does HCLTech cultivate AI fluency and skills across software engineering teams through the HCLTech Career Shaper learning initiative?",
            "Discuss: Career Shaper AI certification roadmaps, hands-on cloud AI sandbox environments, prompt engineering bootcamps, and project innovation hackathons.",
            "HCLTech Career Shaper AI"
        )
    ]

    hr_java = [
        create_hr_question(
            "HCLTech's organizational culture is driven by 'Ideapreneurship'—empowering grassroots employees to drive business innovation. Tell me about a time you took the initiative to solve an unassigned technical problem.",
            "Use STAR: Outline the discovered inefficiency, the proactive initiative taken without prompting, and the measurable positive outcome for your team or project.",
            "Ideapreneurship & Grassroots Innovation"
        ),
        create_hr_question(
            "Why do you specifically choose HCLTech to begin and accelerate your professional software engineering career?",
            "Highlight: HCLTech's engineering and R&D heritage, culture of employee empowerment, global Fortune 500 client projects, and continuous learning opportunities.",
            "HCLTech Brand Motivation"
        ),
        create_hr_question(
            "HCLTech operates major state-of-the-art technology campuses across India (Noida, Chennai, Bangalore, Hyderabad, Pune, Lucknow). Are you fully open to relocation and project shifts?",
            "Affirm: Complete willingness to relocate to any HCLTech delivery center, readiness to adapt to client project schedules, and commitment to team deliverables.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "Tell me about a challenging project deadline where you faced technical blockers. How did you manage your workload and deliver successfully?",
            "Showcase: Calm prioritization, breaking down problems into modular steps, communicating early with the project lead, and working diligently to hit milestones.",
            "Delivering Under Pressure"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a different communication style or technical opinion during sprint planning?",
            "Emphasize: Respectful active listening, focusing on technical merit and project requirements, and working together toward a common goal.",
            "Team Collaboration & Respect"
        ),
        create_hr_question(
            "Describe a time you received critical constructive feedback on your programming code. How did you react and what changes did you make?",
            "Demonstrate: Professional humility, analyzing feedback constructively, adopting clean coding practices, and showing measurable improvement.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Where do you see yourself progressing at HCLTech over the next 3 to 5 years?",
            "Connect: Growing from Graduate Engineer Trainee / Software Engineer to Senior Software Engineer / Module Lead, mastering cloud native architectures, and mentoring juniors.",
            "Career Aspirations & Ambition"
        ),
        create_hr_question(
            "How do you keep yourself updated with rapidly evolving software frameworks, cloud native tools, and AI capabilities?",
            "Highlight: Reading technical documentation, building personal side projects, taking certifications, and participating in hackathons.",
            "Continuous Learning"
        ),
        create_hr_question(
            "Describe a time you made a mistake in a software project that broke a feature or failed a test. How did you take ownership of the error?",
            "Show: Immediate accountability, transparent communication, conducting root cause analysis, fixing the issue, and adding tests to prevent recurrence.",
            "Accountability & Integrity"
        ),
        create_hr_question(
            "Do you have any questions for HCLTech leadership regarding our First Careers onboarding program, technology tracks, or corporate culture?",
            "Candidate asks about First Careers training curriculum, project allocation pathways, or opportunities to participate in grassroots innovation labs.",
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
# 15. TECH MAHINDRA
# ==========================================
def build_techmahindra_catalog():
    apt_java = [
        create_aptitude_question(
            "In Tech Mahindra Tech Test Quantitative: A telecom fiber-optic link transmits data packets at 100 Mbps. If a packet is 1,250 bytes long, how many packets can be transmitted across the link in 1 second?",
            ["10,000 packets", "8,000 packets", "12,500 packets", "5,000 packets"],
            "10,000 packets",
            "100 Mbps = 100,000,000 bits/sec. Packet size in bits = 1,250 bytes * 8 = 10,000 bits. Packets per second = 100,000,000 / 10,000 = 10,000 packets/sec.",
            "Easy", "Tech Mahindra Telecom Math"
        ),
        create_aptitude_question(
            "A telecommunication mobile tower's subscriber call drop rate drops by 20% in month 1 and by another 15% in month 2. What is the net percentage reduction in call drops over the two months?",
            ["32.0%", "35.0%", "30.0%", "28.5%"],
            "32.0%",
            "Net drop = 1 - (1 - 0.20) * (1 - 0.15) = 1 - (0.80 * 0.85) = 1 - 0.68 = 0.32 = 32.0%.",
            "Easy", "Tech Mahindra Percentage Math"
        ),
        create_aptitude_question(
            "In Tech Mahindra Reasoning: In a 5G network cell, Base Station X is 12 km North of Base Station Y, and Base Station Z is 9 km East of Base Station Y. What is the straight-line distance between Station X and Station Z?",
            ["15 km", "21 km", "16 km", "18 km"],
            "15 km",
            "Triangle XYZ forms a right-angled triangle with legs 12 km and 9 km. By Pythagorean theorem: Distance = sqrt(12^2 + 9^2) = sqrt(144 + 81) = sqrt(225) = 15 km.",
            "Easy", "Tech Mahindra Geometry & Distance"
        ),
        create_aptitude_question(
            "Find the next number in the Tech Mahindra series: 5, 11, 23, 47, 95, ___?",
            ["191", "190", "195", "185"],
            "191",
            "Pattern: Each term is (previous * 2) + 1: 5*2+1=11, 11*2+1=23, 23*2+1=47, 47*2+1=95. Next is 95*2+1 = 191.",
            "Easy", "Tech Mahindra Number Series"
        ),
        create_aptitude_question(
            "In Tech Mahindra Conversational English: Choose the sentence that is grammatically error-free:",
            ["The network administrator has resolved the routing latency issue.", "The network administrator have resolved the routing latency issue.", "The network administrator has resolve the routing latency issue.", "The network administrator are resolving the routing latency issue."],
            "The network administrator has resolved the routing latency issue.",
            "Singular subject ('administrator') requires singular auxiliary verb 'has' and past participle 'resolved'.",
            "Easy", "Tech Mahindra English Ability"
        ),
        create_aptitude_question(
            "Two telecom engineers A and B can install a microwave antenna in 6 hours and 12 hours respectively. How long will they take working together?",
            ["4.0 hours", "5.0 hours", "4.5 hours", "3.5 hours"],
            "4.0 hours",
            "Combined rate = 1/6 + 1/12 = (2 + 1)/12 = 3/12 = 1/4 antenna/hour. Total time = 4.0 hours.",
            "Easy", "Tech Mahindra Work Equation"
        ),
        create_aptitude_question(
            "A cellular service provider sells a data plan for Rs. 420 making a profit of 20%. What was the cost of delivery for the data plan?",
            ["Rs. 350", "Rs. 360", "Rs. 380", "Rs. 340"],
            "Rs. 350",
            "Cost * 1.20 = 420 => Cost = 420 / 1.20 = Rs. 350.",
            "Easy", "Tech Mahindra Commercial Math"
        ),
        create_aptitude_question(
            "In how many ways can 4 5G radio frequencies be allocated to 4 cellular sectors with exactly one frequency per sector?",
            ["24 ways", "16 ways", "12 ways", "64 ways"],
            "24 ways",
            "Permutations of 4 distinct frequencies = 4! = 4 * 3 * 2 * 1 = 24 ways.",
            "Easy", "Tech Mahindra Combinatorics"
        ),
        create_aptitude_question(
            "If 'NETWORK' is coded as 'MDSVNQJ' in a telecom cipher, what is the code for 'ROUTER'?",
            ["QNTUDQ", "QPVSDQ", "QNTVEQ", "SPVUFS"],
            "QNTUDQ",
            "Each letter is shifted backward by -1: R->Q, O->N, U->T, T->S (or U->T), E->D, R->Q.",
            "Easy", "Tech Mahindra Coding-Decoding"
        ),
        create_aptitude_question(
            "A vehicle traveling at 54 km/h crosses a 180-meter long telecom transmission line span in how many seconds?",
            ["12 seconds", "10 seconds", "15 seconds", "8 seconds"],
            "12 seconds",
            "Speed = 54 * (5/18) = 15 m/s. Time = Distance / Speed = 180 / 15 = 12 seconds.",
            "Easy", "Tech Mahindra Speed & Time"
        ),
        create_aptitude_question(
            "In Tech Mahindra Non-Verbal Logic: A clock is rotated 90 degrees clockwise. If the hour hand was pointing at 3 o'clock initially, what number on the face does it point to now?",
            ["6 o'clock", "12 o'clock", "9 o'clock", "4 o'clock"],
            "6 o'clock",
            "90 degrees clockwise from 3 o'clock (horizontal right) points vertically downward to 6 o'clock.",
            "Easy", "Tech Mahindra Clock Logic"
        ),
        create_aptitude_question(
            "What is the average of the first 10 multiples of 4?",
            ["22.0", "20.0", "24.0", "25.0"],
            "22.0",
            "Multiples: 4, 8, 12, ..., 40. Sum = 4 * (10 * 11 / 2) = 4 * 55 = 220. Average = 220 / 10 = 22.0.",
            "Easy", "Tech Mahindra Elementary Math"
        ),
        create_aptitude_question(
            "A wireless router signal strength decays exponentially according to S(d) = S0 * 2^(-d/5), where d is distance in meters. At what distance d will signal strength drop to 25% of S0?",
            ["10 meters", "15 meters", "20 meters", "5 meters"],
            "10 meters",
            "25% = 1/4 = 2^(-2). Therefore -d/5 = -2 => d = 10 meters.",
            "Medium", "Tech Mahindra Signal Math"
        ),
        create_aptitude_question(
            "In a team of 30 telecom engineers, 18 know 5G protocol stacks and 16 know Cloud NFV. If 4 know neither, how many engineers know BOTH 5G and NFV?",
            ["8 engineers", "10 engineers", "6 engineers", "12 engineers"],
            "8 engineers",
            "Total knowing at least one = 30 - 4 = 26. By inclusion-exclusion: 18 + 16 - Both = 26 => Both = 34 - 26 = 8 engineers.",
            "Easy", "Tech Mahindra Set Theory"
        ),
        create_aptitude_question(
            "In Tech Mahindra Syllogisms: Statements: 1. All cell towers are transmitters. 2. No transmitter is a receiver. Conclusion I: No cell tower is a receiver. Conclusion II: Some transmitters are cell towers.",
            ["Both conclusions I and II follow", "Only conclusion I follows", "Only conclusion II follows", "Neither follows"],
            "Both conclusions I and II follow",
            "All cell towers are transmitters, and no transmitter is a receiver; therefore no cell tower is a receiver (I). Conversion of Statement 1 yields II. Both follow.",
            "Easy", "Tech Mahindra Syllogisms"
        )
    ]

    code_java = [
        create_coding_problem(
            "Reverse String Preserving Special Characters",
            "Given a string s containing alphanumeric characters and special characters (like symbols, punctuation), reverse only the alphabetic characters while keeping all special characters in their original positions.",
            's = "a,b$c"',
            '"c,b$a"',
            "public class Solution {\n    public static String reverseOnlyLetters(String s) {\n        return \"\";\n    }\n}",
            "def reverse_only_letters(s: str) -> str:\n    pass",
            "def invert_alphabetic_telecom_header(header_series) -> str:\n    pass",
            "Tech Mahindra classic: Two pointers (left and right). Advance left if not letter, advance right if not letter. When both are letters, swap and advance both in O(N).",
            "Easy", "Two Pointers & String", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Matrix Diagonal Sum (Network Mesh Grid)",
            "Given a square matrix mat, return the sum of the matrix diagonals. Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.",
            "mat = [[1,2,3],[4,5,6],[7,8,9]]",
            "25 (1+5+9 + 3+7 = 25; 5 counted once)",
            "public class Solution {\n    public int diagonalSum(int[][] mat) {\n        return 0;\n    }\n}",
            "def diagonal_sum(mat: list[list[int]]) -> int:\n    pass",
            "def compute_mesh_cross_traffic(grid_df) -> int:\n    pass",
            "Single loop from 0 to n-1: add mat[i][i] and mat[i][n-1-i]. If n is odd, subtract center element mat[n/2][n/2] in O(N).",
            "Easy", "Matrix Operations", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Fibonacci Series Memoization (Telecom Backoff)",
            "Compute the Nth Fibonacci number in O(N) time and O(1) space using iterative memoization.",
            "n = 6",
            "8 (Sequence: 0, 1, 1, 2, 3, 5, 8)",
            "public class Solution {\n    public static int fib(int n) {\n        return 0;\n    }\n}",
            "def fib(n: int) -> int:\n    pass",
            "def calculate_exponential_backoff_slot(n: int) -> int:\n    pass",
            "Maintain two variables prev1 and prev2 rolling through loop up to n in O(N) time and O(1) space.",
            "Easy", "Dynamic Programming & Math", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Sort Array of 0s, 1s, and 2s (Dutch National Flag)",
            "Given an array nums with n objects colored red, white, or blue (represented by 0, 1, and 2), sort them in-place so that objects of the same color are adjacent.",
            "nums = [2,0,2,1,1,0]",
            "[0,0,1,1,2,2]",
            "public class Solution {\n    public void sortColors(int[] nums) {\n    }\n}",
            "def sort_colors(nums: list[int]) -> None:\n    pass",
            "def prioritize_qos_traffic_classes(packets_df):\n    pass",
            "Three-pointer Dutch National Flag algorithm: low, mid, high pointers sorting in-place in a single O(N) pass.",
            "Medium", "Two Pointers & In-Place", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Longest Consecutive Sequence in Unsorted Array",
            "Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence in O(N) runtime.",
            "nums = [100,4,200,1,3,2]",
            "4 (Sequence: [1, 2, 3, 4])",
            "public class Solution {\n    public int longestConsecutive(int[] nums) {\n        return 0;\n    }\n}",
            "def longest_consecutive(nums: list[int]) -> int:\n    pass",
            "def max_consecutive_call_burst_window(calls_df) -> int:\n    pass",
            "Insert all numbers into a HashSet. Only start counting sequence from numbers where num - 1 is NOT in set, achieving O(N) overall.",
            "Medium", "Hash Set & Array", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Search in 2D Matrix (Row and Column Sorted)",
            "Write an efficient algorithm that searches for a target value in an m x n integer matrix. Integers in each row are sorted from left to right, and the first integer of each row is greater than the last integer of the previous row.",
            "matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3",
            "true",
            "public class Solution {\n    public boolean searchMatrix(int[][] matrix, int target) {\n        return false;\n    }\n}",
            "def search_matrix(matrix: list[list[int]], target: int) -> bool:\n    pass",
            "def search_subscriber_routing_table(matrix_df, target: int) -> bool:\n    pass",
            "Treat the 2D matrix as a flat 1D sorted array of size M*N and execute standard binary search with row = mid / n, col = mid % n in O(log(MN)).",
            "Medium", "Binary Search & Matrix", "O(log(M * N))", "O(1)"
        ),
        create_coding_problem(
            "Valid Palindrome II (At Most One Deletion)",
            "Given a string s, return true if the s can be palindrome after deleting at most one character from it.",
            's = "abca"',
            "true (Delete character 'c' or 'b')",
            "public class Solution {\n    public boolean validPalindrome(String s) {\n        return false;\n    }\n}",
            "def valid_palindrome(s: str) -> bool:\n    pass",
            "def verify_fault_tolerant_packet_checksum(packet_series) -> bool:\n    pass",
            "Two pointers from ends. If mismatch at (i, j), check if substring s[i+1..j] OR s[i..j-1] is a valid palindrome in O(N).",
            "Easy", "Two Pointers & String", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Count Inversions in an Array",
            "Inversion Count for an array indicates how far (or close) the array is from being sorted. If the array is already sorted, then inversion count is 0. If sorted in reverse order, inversion count is maximum. Return total inversion count in O(N log N).",
            "arr = [8, 4, 2, 1]",
            "6 (Pairs: (8,4), (8,2), (8,1), (4,2), (4,1), (2,1))",
            "public class Solution {\n    public static long inversionCount(long[] arr) {\n        return 0;\n    }\n}",
            "def inversion_count(arr: list[int]) -> int:\n    pass",
            "def count_out_of_order_telecom_packets(packet_df) -> int:\n    pass",
            "Modified Merge Sort: During merge step, whenever element from right half is smaller than left half, all remaining elements in left half form inversions.",
            "Medium", "Merge Sort & Divide and Conquer", "O(N log N)", "O(N)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain 5G Network Slicing and Service-Based Architecture (SBA). How do Network Functions (AMF, SMF, UPF) communicate over HTTP/2 REST APIs at Tech Mahindra?",
            "SBA replaces point-to-point telecom interfaces with a service-based bus. Network Functions register with NRF (Network Repository Function) and communicate via HTTP/2 JSON REST APIs. Network Slicing creates virtualized end-to-end networks customized for specific SLAs (eMBB, URLLC, mMTC).",
            "Tech Mahindra 5G Architecture", "Hard"
        ),
        create_technical_question(
            "What is Network Functions Virtualization (NFV) and Software-Defined Networking (SDN)? How do virtualized network functions (VNFs) run on cloud-native Kubernetes (CNFs)?",
            "NFV decouples network software (firewalls, routers, EPC) from proprietary hardware. SDN separates control plane from data forwarding plane. CNFs package network functions into lightweight container pods managed by Kubernetes.",
            "Tech Mahindra NFV & SDN", "Hard"
        ),
        create_technical_question(
            "Explain Telecom OSS (Operations Support Systems) and BSS (Business Support Systems) architectures and how mediation engines process millions of Call Detail Records (CDRs).",
            "BSS handles customer billing, subscriptions, and revenue management. OSS manages network inventory, service provisioning, and fault management. Mediation engines collect raw network CDRs, decode binary formats (ASN.1), and feed rated records to billing engines.",
            "Tech Mahindra Telecom OSS/BSS", "Hard"
        ),
        create_technical_question(
            "How does Socket Programming work in Java / Python using ServerSocket and Socket for low-latency TCP communication in telecommunications?",
            "ServerSocket binds to an IP and port, listening with accept() which blocks until a client connects, returning a dedicated Socket instance with InputStream and OutputStream for bidirectional TCP communication.",
            "Tech Mahindra Socket Programming", "Medium"
        ),
        create_technical_question(
            "Explain the MQTT protocol: Publish-Subscribe architecture, Topic Hierarchies (wildcards + and #), and Quality of Service (QoS 0, 1, 2) levels for smart IoT devices.",
            "MQTT is a lightweight binary protocol. QoS 0 sends at most once (no ack); QoS 1 delivers at least once (PUBACK); QoS 2 guarantees exactly once via four-step handshake (PUBREC, PUBREL, PUBCOMP).",
            "Tech Mahindra IoT & MQTT", "Medium"
        ),
        create_technical_question(
            "How do you process real-time telecommunication event streams using Apache Kafka, Kafka Streams, and sliding time-windows for fraud detection?",
            "CDR events stream into Kafka topics partitioned by subscriber IMSI. Kafka Streams computes tumbling/sliding time-window aggregations (e.g. flagging subscribers placing calls from two different cities within 5 minutes).",
            "Tech Mahindra Real-Time Stream Processing", "Medium"
        ),
        create_technical_question(
            "Explain OSI 7-Layer Networking Model versus TCP/IP Model and how data packets are encapsulated and decapsulated as they traverse layers.",
            "Application -> Transport (adds TCP port header) -> Network (adds IP header) -> Data Link (adds MAC frame header/trailer) -> Physical (bits). Decapsulation strips headers in reverse at destination.",
            "Tech Mahindra Computer Networking", "Easy"
        ),
        create_technical_question(
            "How does Redis in-memory caching accelerate subscriber session profile lookups in high-concurrency telecom authorization gateways?",
            "Redis stores subscriber policy profiles (data balance, active subscriptions) in RAM with sub-millisecond retrieval. Key eviction (TTL) and LRU policies ensure memory remains within provisioned limits.",
            "Tech Mahindra In-Memory Caching & Redis", "Medium"
        ),
        create_technical_question(
            "Explain Java Multithreading: ThreadPoolExecutor parameters (corePoolSize, maximumPoolSize, keepAliveTime, workQueue, RejectedExecutionHandler).",
            "Tasks run on core threads; additional tasks enqueue in workQueue; if queue fills, pool scales up to maximumPoolSize; if max threads saturated, RejectedExecutionHandler (AbortPolicy, CallerRunsPolicy) handles overflow.",
            "Tech Mahindra Java Concurrency", "Medium"
        ),
        create_technical_question(
            "How do you optimize SQL queries on massive telecommunication databases storing billions of call transaction records?",
            "Table partitioning by date (range partitioning); creating composite indexes on (subscriber_id, timestamp); leveraging parallel query execution; purging historical records into cold cloud storage.",
            "Tech Mahindra Database Performance", "Medium"
        ),
        create_technical_question(
            "Explain the difference between TCP and UDP protocols. In what telecom applications would an architect strictly select UDP over TCP?",
            "TCP is connection-oriented, reliable, and ordered with congestion control. UDP is connectionless and lightweight without retransmissions, ideal for latency-critical real-time media streaming (VoIP, video calls) where lost packets are preferable to latency jitter.",
            "Tech Mahindra Networking Protocols", "Easy"
        ),
        create_technical_question(
            "How does Docker containerization package telecom microservices, and how does Docker Host networking mode bypass bridge latency for high-speed packet processing?",
            "Docker host networking mode (--net=host) bypasses network namespace isolation and Docker bridge NAT routing, binding container sockets directly to the host network interfaces for zero packet forwarding overhead.",
            "Tech Mahindra Docker & Telecom Networking", "Medium"
        ),
        create_technical_question(
            "Explain RESTful API design principles with Spring Boot: HTTP Status Codes (200, 201, 204, 400, 401, 403, 404, 500) and HATEOAS.",
            "200 OK, 201 Created (resource creation), 204 No Content (delete), 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Internal Error. HATEOAS enriches responses with hypermedia navigation links.",
            "Tech Mahindra REST API Standards", "Easy"
        ),
        create_technical_question(
            "What is a Linux Packet Sniffer (tcpdump / Wireshark), and how do you capture and analyze SIP / diameter telecom signaling packets?",
            "tcpdump captures raw packets matching pcap filters (e.g. 'tcp port 5060' for SIP). Wireshark dissects packet headers displaying call flow sequence diagrams, invite requests, and error codes (486 Busy Here).",
            "Tech Mahindra Network Diagnostics", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Synchronous Blocking I/O and Asynchronous Reactive Programming with Spring WebFlux in telecom API gateways.",
            "Blocking I/O dedicates one thread per request, saturating thread pools under high concurrency. Spring WebFlux uses Project Reactor and Netty event loops to handle thousands of concurrent requests with a small fixed number of threads.",
            "Tech Mahindra Reactive Programming", "Hard"
        )
    ]

    ai_java = [
        create_ai_question(
            "How is Artificial Intelligence applied at Tech Mahindra to automate 5G network traffic prediction and dynamic radio slice optimization?",
            "Discuss: Collecting real-time cell tower KPI telemetry, training time-series models (LSTM, Prophet) to forecast peak congestion, and dynamically reallocating bandwidth slices.",
            "Tech Mahindra 5G AI Optimization"
        ),
        create_ai_question(
            "Explain how Generative AI conversational assistants are deployed in telecom customer care to handle complex billing and eSIM activation queries.",
            "Architecture: RAG over telecom tariff rules and plan manuals, intent classification, calling BSS APIs for balance queries, and human escalation for disputed charges.",
            "Tech Mahindra Telecom Customer Care AI"
        ),
        create_ai_question(
            "Describe how computer vision and AI drones automate cell tower structural inspections and antenna alignment verification at Tech Mahindra.",
            "Detail: Drone cameras capture high-resolution imagery; YOLO object detection identifies rust, loose cables, and misaligned microwave dishes; automated work orders dispatch to technicians.",
            "Tech Mahindra Computer Vision & Drones"
        ),
        create_ai_question(
            "How do you implement an AI-powered automated code modernization pipeline for legacy telecom billing systems (C/C++ to Java/Go)?",
            "Explain: Parsing procedural C code into abstract syntax trees, prompting specialized LLMs with modern language idioms, generating automated regression test suites, and verifying outputs.",
            "Tech Mahindra AI Code Modernization"
        ),
        create_ai_question(
            "What techniques mitigate hallucinations when LLMs generate automated network configuration scripts (CLI commands for Cisco/Juniper routers)?",
            "Discuss: Strict grammar-constrained decoding, validating generated commands against a simulated router CLI sandbox, and requiring senior network engineer sign-off.",
            "Tech Mahindra Network Automation AI"
        ),
        create_ai_question(
            "How do you design a real-time SIM-swap fraud detection pipeline using machine learning models integrated with telecom core network events?",
            "Detail: Correlating SIM replacement timestamps with subsequent high-value banking OTP requests, scoring anomaly probability in < 100ms, and alerting banks.",
            "Tech Mahindra SIM Fraud Detection AI"
        ),
        create_ai_question(
            "How do you optimize LLM inference performance on edge telecom servers (MEC - Multi-Access Edge Computing) near cell towers?",
            "Explain: Model quantization (INT4/INT8), local caching of standard telecom intent responses, and utilizing GPU-accelerated edge containers.",
            "Tech Mahindra Edge AI & MEC"
        ),
        create_ai_question(
            "Describe how Tech Mahindra ensures ethical AI and data privacy compliance when training models on subscriber call detail records (CDRs).",
            "Cover: Data anonymization, hashing IMSI and phone numbers, differential privacy noise injection, and strict role-based access control.",
            "Tech Mahindra AI Data Privacy & Ethics"
        ),
        create_ai_question(
            "How do you evaluate and monitor the accuracy of automated AI root-cause analysis engines across multi-vendor telecom network alarms?",
            "Discuss: F1-score comparison against historical network engineer incident resolutions, mean-time-to-repair (MTTR) reduction metrics, and human-in-the-loop validation.",
            "Tech Mahindra AIOps Evaluation"
        ),
        create_ai_question(
            "How does Tech Mahindra foster AI fluency across its engineering workforce through the TechM Techify and AI Academy initiatives?",
            "Discuss: Hands-on AI labs, 5G AI hackathons, prompt engineering certifications, and domain-specific generative AI masterclasses.",
            "Tech Mahindra AI Upskilling"
        )
    ]

    hr_java = [
        create_hr_question(
            "Tech Mahindra is guided by the Mahindra 'Rise' philosophy: Accepting No Limits, Alternative Thinking, and Driving Positive Change. How have you lived these values?",
            "Provide a personal example showcasing pushing beyond conventional boundaries, creative problem solving, and making a positive impact on your project or community.",
            "Mahindra Rise Philosophy"
        ),
        create_hr_question(
            "Why do you specifically choose Tech Mahindra to build your software engineering career?",
            "Highlight: Tech Mahindra's global dominance in telecommunications and digital engineering, strong Mahindra Group ethical heritage, and collaborative culture.",
            "Tech Mahindra Brand Motivation"
        ),
        create_hr_question(
            "Tech Mahindra has major campuses across India (Pune Hinjewadi, Hyderabad, Bangalore, Chennai, Noida, Mumbai). Are you fully flexible with relocation and rotational shifts?",
            "Affirm: Complete willingness to relocate, readiness to support global telecom client project time zones, and adaptability to hybrid working models.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "Telecom and enterprise software projects often involve critical client deliverables. Tell me about a time you handled high pressure under strict deadlines.",
            "Use STAR: Outline the pressure, organized task prioritization, transparent communication with leads, and successful on-time delivery.",
            "Delivering Under High Pressure"
        ),
        create_hr_question(
            "Describe a time you demonstrated 'Alternative Thinking' by proposing a non-traditional technical solution that solved a stubborn software bug.",
            "Showcase: Creative out-of-the-box thinking, experimenting with prototypes, proving feasibility with benchmarks, and unblocking the project.",
            "Alternative Thinking & Innovation"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who is reluctant to adopt new agile software development practices?",
            "Emphasize: Empathy, patient communication, explaining the practical benefits of the new workflow, and helping them transition smoothly.",
            "Teamwork & Empathy"
        ),
        create_hr_question(
            "Where do you see yourself progressing at Tech Mahindra over the next 3 to 5 years as an engineer?",
            "Connect: Growing from Associate Software Engineer to Senior Software Engineer / Solution Lead, mastering 5G cloud networks, and mentoring new campus hires.",
            "Career Growth & Ambition"
        ),
        create_hr_question(
            "Tell me about a time you received critical constructive feedback on your technical performance. How did you react and what changes did you make?",
            "Demonstrate: Professional humility, analyzing feedback constructively, adopting clean coding practices, and showing measurable improvement.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "What unique personal attributes or strengths set you apart from other candidates interviewing for Tech Mahindra today?",
            "Combine: Strong computer science fundamentals, passion for telecommunications and cloud innovation, proactive attitude, and alignment with Rise values.",
            "Candidate Differentiator"
        ),
        create_hr_question(
            "Do you have any questions for Tech Mahindra leadership regarding our project allocation, telecom innovation centers, or learning culture?",
            "Candidate asks about Tech Mahindra Makers Lab innovation hubs, 5G engineering labs, or career progression tracks.",
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

ORACLE_DATA = build_oracle_catalog()
IBM_DATA = build_ibm_catalog()
REDHAT_DATA = build_redhat_catalog()
HCLTECH_DATA = build_hcltech_catalog()
TECHMAHINDRA_DATA = build_techmahindra_catalog()
