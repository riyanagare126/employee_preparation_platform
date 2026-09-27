"""
Company Question Data - Part 2:
Accenture, Wipro, Cognizant, Capgemini, Deloitte.
"""

from scripts.catalog_builder import (
    create_aptitude_question, create_coding_problem,
    create_technical_question, create_ai_question, create_hr_question
)

# ==========================================
# 6. ACCENTURE
# ==========================================
def build_accenture_catalog():
    apt_java = [
        create_aptitude_question(
            "Accenture Critical Reasoning: In a team of 45 cloud analysts, 30 know Python, 25 know SQL, and 5 know neither. How many analysts know BOTH Python and SQL?",
            ["15", "10", "20", "12"],
            "15",
            "Total analysts knowing at least one = 45 - 5 = 40. By inclusion-exclusion: 30 + 25 - Both = 40 => Both = 55 - 40 = 15.",
            "Medium", "Accenture Critical Reasoning"
        ),
        create_aptitude_question(
            "Accenture Abstract Reasoning: Find the next term in the alphanumeric series: A2B, C4D, E8F, G16H, ___?",
            ["I32J", "I24J", "H32I", "J32K"],
            "I32J",
            "First letters increase by 2: A, C, E, G -> I. Second letters: B, D, F, H -> J. Numbers double: 2, 4, 8, 16 -> 32. Answer is I32J.",
            "Easy", "Accenture Abstract Reasoning"
        ),
        create_aptitude_question(
            "Accenture Pseudocode: What is the output of the following pseudocode?\nInteger p = 12, q = 7\nInteger r = (p ^ q) & p\nPrint r",
            ["8", "12", "0", "4"],
            "8",
            "p = 1100 (12 in binary), q = 0111 (7 in binary). p ^ q = 1011 (11). (p ^ q) & p = 1011 & 1100 = 1000 (8 in decimal).",
            "Medium", "Accenture Pseudocode"
        ),
        create_aptitude_question(
            "If a cloud microservice cluster processes 1,800 requests/sec with 3 worker nodes, and each added worker node increases cluster capacity by 25% of baseline (3-node throughput), how many total nodes are needed to handle 3,600 requests/sec?",
            ["7 nodes", "5 nodes", "6 nodes", "8 nodes"],
            "7 nodes",
            "Baseline = 1,800. Additional needed = 1,800. Each new node adds 25% of 1800 = 450 req/s. Needed new nodes = 1800 / 450 = 4. Total nodes = 3 + 4 = 7 nodes.",
            "Medium", "Accenture Quantitative Ability"
        ),
        create_aptitude_question(
            "A consulting client reduces operational cost by 15% in year 1, but inflation raises remaining cost by 10% in year 2. What is the net percentage reduction from the original baseline cost?",
            ["6.5%", "5.0%", "7.0%", "8.5%"],
            "6.5%",
            "Initial = 100. Year 1 = 85. Year 2 = 85 * 1.10 = 93.5. Net reduction = 100 - 93.5 = 6.5%.",
            "Easy", "Accenture Commercial Math"
        ),
        create_aptitude_question(
            "Accenture Flowchart Analysis: An algorithm sets X=1, Y=1. At each step, X = X + 2, Y = Y * 2. The loop terminates when X > 8. What is the final value of Y upon termination?",
            ["16", "32", "8", "64"],
            "16",
            "Step 1: X=3, Y=2. Step 2: X=5, Y=4. Step 3: X=7, Y=8. Step 4: X=9, Y=16. Since X=9 > 8, loop terminates with Y=16.",
            "Medium", "Accenture Flowchart Logic"
        ),
        create_aptitude_question(
            "In an Accenture project assessment, 8 consultants can prepare 24 client reports in 6 days. How many reports can 12 consultants prepare in 4 days at the same work rate?",
            ["24 reports", "36 reports", "18 reports", "30 reports"],
            "24 reports",
            "Consultant-days per report = (8 * 6) / 24 = 2 consultant-days/report. Total consultant-days available = 12 * 4 = 48. Reports = 48 / 2 = 24 reports.",
            "Medium", "Accenture Work & Efficiency"
        ),
        create_aptitude_question(
            "Find the odd one out in the logical group: [27, 64, 125, 216, 343, 512, 729]",
            ["None (All are perfect cubes)", "64", "512", "729"],
            "None (All are perfect cubes)",
            "All numbers are cubes: 3^3=27, 4^3=64, 5^3=125, 6^3=216, 7^3=343, 8^3=512, 9^3=729. If 64/729 are singled out for being squares too, 64 is 8^2 and 729 is 27^2.",
            "Easy", "Accenture Analytical Reasoning"
        ),
        create_aptitude_question(
            "A train traveling at 60 km/h crosses a man walking in the opposite direction at 6 km/h in 10 seconds. What is the length of the train?",
            ["183.3 meters", "150.0 meters", "200.0 meters", "166.7 meters"],
            "183.3 meters",
            "Relative speed = 60 + 6 = 66 km/h = 66 * (5/18) = 55/3 m/s. Length = Speed * Time = (55/3) * 10 = 550 / 3 ≈ 183.33 meters.",
            "Medium", "Accenture Relative Speed"
        ),
        create_aptitude_question(
            "In Accenture Verbal Ability: Choose the option that correctly completes the sentence: 'The enterprise architecture was designed to be resilient, ______ unexpected infrastructure outages.'",
            ["withstanding", "withstood", "withstand", "withstands"],
            "withstanding",
            "The participle 'withstanding' correctly modifies the predicate clause describing the continuous capability of the architecture.",
            "Easy", "Accenture English Ability"
        ),
        create_aptitude_question(
            "A box contains 5 red, 4 blue, and 3 green network cables. If two cables are picked at random without replacement, what is the probability that both are blue?",
            ["1/11", "1/6", "4/33", "2/11"],
            "1/11",
            "Total cables = 12. P(both blue) = (4/12) * (3/11) = (1/3) * (3/11) = 1/11.",
            "Easy", "Accenture Probability"
        ),
        create_aptitude_question(
            "If 'ACCENTURE' is coded as 'BDDFOUVSF' in a cybersecurity cipher, what is the code for 'CLOUD'?",
            ["DMPVE", "DMPUD", "ENQWF", "BKNT C"],
            "DMPVE",
            "Each letter is shifted forward by +1: C->D, L->M, O->P, U->V, D->E. Result is DMPVE.",
            "Easy", "Accenture Coding-Decoding"
        ),
        create_aptitude_question(
            "A cloud database charges $0.05 per GB-month for storage and $0.09 per 10,000 read operations. If a client stores 400 GB and executes 500,000 reads in a month, what is the total charge?",
            ["$24.50", "$20.00", "$28.00", "$22.50"],
            "$24.50",
            "Storage cost = 400 * 0.05 = $20.00. Read cost = (500,000 / 10,000) * 0.09 = 50 * 0.09 = $4.50. Total = $20.00 + $4.50 = $24.50.",
            "Easy", "Accenture Commercial Math"
        ),
        create_aptitude_question(
            "Two numbers are in the ratio 3:5. If 8 is added to both numbers, the ratio becomes 2:3. What is the sum of the original two numbers?",
            ["64", "48", "56", "72"],
            "64",
            "(3x + 8) / (5x + 8) = 2/3 => 3*(3x + 8) = 2*(5x + 8) => 9x + 24 = 10x + 16 => x = 8. Original numbers are 24 and 40. Sum = 24 + 40 = 64.",
            "Medium", "Accenture Quantitative"
        ),
        create_aptitude_question(
            "In Accenture Deductive Logic: All microservices are scalable. Some scalable systems are serverless. Which conclusion follows definitively?",
            ["None of the conclusions follow definitively", "All serverless systems are microservices", "Some microservices are serverless", "No serverless system is scalable"],
            "None of the conclusions follow definitively",
            "The middle term 'scalable systems' is undistributed in both premises, so no definite relationship between microservices and serverless can be concluded.",
            "Medium", "Accenture Deductive Logic"
        )
    ]

    code_java = [
        create_coding_problem(
            "Product of Array Except Self (Accenture Coding)",
            "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i] in O(N) time without using the division operation.",
            "nums = [1,2,3,4]",
            "[24,12,8,6]",
            "public class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        return new int[0];\n    }\n}",
            "def product_except_self(nums: list[int]) -> list[int]:\n    pass",
            "def calculate_relative_impact_matrix(series_df) -> list[int]:\n    pass",
            "Accenture standard: Prefix products pass from left to right, then running suffix product pass from right to left in O(N) with O(1) extra space.",
            "Medium", "Prefix Sum & Arrays", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Minimum Jumps to Reach End (Greedy)",
            "Given an array of non-negative integers nums where each element represents your maximum jump length at that position, return the minimum number of jumps to reach the last index.",
            "nums = [2,3,1,1,4]",
            "2",
            "public class Solution {\n    public int jump(int[] nums) {\n        return 0;\n    }\n}",
            "def jump(nums: list[int]) -> int:\n    pass",
            "def compute_optimal_transition_hops(steps_df) -> int:\n    pass",
            "Greedy BFS: Track current_end and farthest jump possible. When index reaches current_end, increment jumps and update current_end to farthest.",
            "Medium", "Greedy", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Bitwise AND of Numbers Range",
            "Given two integers left and right representing the range [left, right], return the bitwise AND of all numbers in this range, inclusive.",
            "left = 5, right = 7",
            "4 (5 & 6 & 7 = 4)",
            "public class Solution {\n    public int rangeBitwiseAnd(int left, int right) {\n        return 0;\n    }\n}",
            "def range_bitwise_and(left: int, right: int) -> int:\n    pass",
            "def evaluate_bitmask_intersection(l_val: int, r_val: int) -> int:\n    pass",
            "Find common binary prefix between left and right by right-shifting until they are equal, then shift back left.",
            "Medium", "Bit Manipulation", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "Invert Binary Tree (Accenture Assessment)",
            "Given the root of a binary tree, invert the tree (swap left and right subtrees recursively), and return its root.",
            "root = [4,2,7,1,3,6,9]",
            "[4,7,2,9,6,3,1]",
            "public class Solution {\n    public TreeNode invertTree(TreeNode root) {\n        return null;\n    }\n}",
            "def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:\n    pass",
            "def mirror_organizational_tree(tree_df):\n    pass",
            "Recursively swap left and right child pointers of each node in O(N) time.",
            "Easy", "Binary Tree", "O(N)", "O(H)"
        ),
        create_coding_problem(
            "Merge Overlapping Intervals (Accenture Cloud)",
            "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all intervals in the input.",
            "intervals = [[1,3],[2,6],[8,10],[15,18]]",
            "[[1,6],[8,10],[15,18]]",
            "public class Solution {\n    public int[][] merge(int[][] intervals) {\n        return new int[0][0];\n    }\n}",
            "def merge(intervals: list[list[int]]) -> list[list[int]]:\n    pass",
            "def consolidate_overlapping_schedules(intervals_df):\n    pass",
            "Sort intervals by start time; iterate through comparing current interval start with previous interval end.",
            "Medium", "Intervals & Sorting", "O(N log N)", "O(N)"
        ),
        create_coding_problem(
            "Climbing Stairs with 1, 2, or 3 Steps",
            "You are climbing a staircase. It takes n steps to reach the top. Each time you can climb either 1, 2, or 3 steps. In how many distinct ways can you climb to the top?",
            "n = 4",
            "7 (Tribonacci: 1, 2, 4, 7)",
            "public class Solution {\n    public int climbStairs3(int n) {\n        return 0;\n    }\n}",
            "def climb_stairs_3(n: int) -> int:\n    pass",
            "def count_execution_pathways(stages: int) -> int:\n    pass",
            "Dynamic programming: dp[i] = dp[i-1] + dp[i-2] + dp[i-3] with rolling three variables in O(N) time and O(1) space.",
            "Easy", "Dynamic Programming", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Valid Anagram Verification",
            "Given two strings s and t, return true if t is an anagram of s, and false otherwise.",
            's = "anagram", t = "nagaram"',
            "true",
            "public class Solution {\n    public boolean isAnagram(String s, String t) {\n        return false;\n    }\n}",
            "def is_anagram(s: str, t: str) -> bool:\n    pass",
            "def check_permutation_identity(s_series, t_series) -> bool:\n    pass",
            "Character frequency count array of size 26; increment for s, decrement for t; all must be 0.",
            "Easy", "Hash Table & Strings", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Find All Duplicates in an Array",
            "Given an integer array nums of length n where all the integers are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice in O(N) time and O(1) extra space.",
            "nums = [4,3,2,7,8,2,3,1]",
            "[2,3]",
            "public class Solution {\n    public List<Integer> findDuplicates(int[] nums) {\n        return new ArrayList<>();\n    }\n}",
            "def find_duplicates(nums: list[int]) -> list[int]:\n    pass",
            "def detect_duplicate_identifiers(id_series) -> list[int]:\n    pass",
            "Negation index marking: Use absolute value of num as index - 1. If nums[abs(num)-1] is already negative, num is a duplicate.",
            "Medium", "Array In-Place Marking", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain Cloud-First Transformation architecture at Accenture. How do Multi-Cloud Landing Zones on AWS and Azure enforce governance and centralized security?",
            "Landing zones provide automated infrastructure baseline (VPC/VNet peering, IAM policies, central audit logging with CloudTrail/Azure Monitor, security guardrails) enabling development squads to provision resources compliantly.",
            "Accenture Cloud First & Multi-Cloud", "Hard"
        ),
        create_technical_question(
            "How does an Istio Service Mesh handle traffic routing (Canary deployments), mutual TLS (mTLS), and observability across distributed Kubernetes clusters?",
            "Istio injects Envoy sidecar proxies into every pod. VirtualServices split traffic (e.g. 90% v1, 10% v2). Citadel manages automated mTLS certificate rotation for zero-trust service-to-service communication.",
            "Accenture Service Mesh & Istio", "Hard"
        ),
        create_technical_question(
            "In enterprise digital transformations, how do you integrate SAP ERP with modern cloud microservices using Apache Kafka and Event-Driven Architecture?",
            "SAP events publish to an enterprise event streaming bus (Kafka) via SAP Event Mesh connectors. Independent microservices consume events asynchronously without imposing load on the core SAP database.",
            "Accenture SAP & Enterprise Integration", "Hard"
        ),
        create_technical_question(
            "Explain Spring Security Architecture: AuthenticationManager, SecurityContextHolder, and custom OncePerRequestFilter for JWT token validation.",
            "OncePerRequestFilter extracts Authorization Bearer header, validates JWT claims and signature, builds UsernamePasswordAuthenticationToken, and sets it in SecurityContextHolder for the current thread.",
            "Accenture Spring Security", "Medium"
        ),
        create_technical_question(
            "What is the difference between Database Sharding and Read Replicas? When would an Accenture architect recommend sharding over replication?",
            "Read replicas scale read throughput by replicating master data. Sharding partitions both read and write workloads horizontally across independent database instances when single master write capacity is saturated.",
            "Accenture Database Scalability", "Hard"
        ),
        create_technical_question(
            "How do you implement CI/CD pipeline automation using GitLab CI / Azure DevOps with automated SAST (Static Application Security Testing) and DAST scans?",
            "Pipeline stages: Compile -> Unit Test -> SonarQube quality gate -> Container build -> Trivy container vulnerability scan -> Deploy to Staging -> OWASP ZAP DAST scan -> Production approval.",
            "Accenture DevOps & DevSecOps", "Medium"
        ),
        create_technical_question(
            "Explain Micro-Frontends architecture. How do Module Federation and Web Components allow independent frontend teams to deploy features without coordinated releases?",
            "Webpack 5 Module Federation dynamically imports remote JavaScript bundles at runtime. Each team builds, tests, and deploys their feature micro-app independently onto a shared shell container.",
            "Accenture Frontend Architecture", "Medium"
        ),
        create_technical_question(
            "How do you handle API Versioning and deprecation in large enterprise transformation projects without breaking external partner client integrations?",
            "Adopt semantic versioning, provide backward-compatible schemas with optional fields, document endpoints in OpenAPI/Swagger, announce deprecation with 'Sunset' HTTP headers 6 months in advance.",
            "Accenture API Governance", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Optimistic Locking (@Version) and Pessimistic Locking (PESSIMISTIC_WRITE) in JPA/Hibernate enterprise systems.",
            "Optimistic locking checks a version column before commit, throwing OptimisticLockException if another transaction modified the row (ideal for read-heavy apps). Pessimistic locking acquires DB row lock immediately.",
            "Accenture JPA Concurrency", "Medium"
        ),
        create_technical_question(
            "How does Apache Kafka ensure Exactly-Once Semantics (EOS) across producer transactions and consumer read-committed isolation levels?",
            "Producers use transactional IDs and idempotency sequence numbers. The Kafka Transaction Coordinator records two-phase commit markers, and consumers read only committed partition offsets.",
            "Accenture Kafka Architecture", "Hard"
        ),
        create_technical_question(
            "What is Infrastructure as Code (IaC) with Terraform, and how do Remote State Locking (with DynamoDB) and State Drift detection operate?",
            "Terraform declarative configs generate cloud resources. Remote state in S3 tracks actual infrastructure. DynamoDB acquires an execution lock to prevent concurrent runs from corrupting state.",
            "Accenture Infrastructure as Code", "Medium"
        ),
        create_technical_question(
            "How do you design a high-throughput WebSocket microservice architecture in Spring Boot for real-time client notifications?",
            "Use Spring WebSocket with STOMP protocol over a shared message broker (RabbitMQ/Redis) so broadcast messages reach users connected to any scaled microservice instance.",
            "Accenture Real-Time Systems", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Vertical Pod Autoscaling (VPA) and Horizontal Pod Autoscaling (HPA) in Kubernetes clusters.",
            "HPA increases or decreases the number of pod replicas based on CPU/memory/custom metrics. VPA adjusts the resource CPU/memory requests and limits of existing containers.",
            "Accenture Kubernetes Autoscaling", "Medium"
        ),
        create_technical_question(
            "How do you implement Disaster Recovery with Active-Active Multi-Region databases using Global Databases (Amazon Aurora Global DB / Azure Cosmos DB)?",
            "Data writes replicate asynchronously across regions in under 1 second. DNS routing (Route 53 latency routing) directs users to the nearest healthy region with zero-downtime failover.",
            "Accenture Disaster Recovery", "Hard"
        ),
        create_technical_question(
            "Explain the OpenTelemetry standard and how Distributed Context Propagation works across asynchronous HTTP and Kafka boundaries.",
            "OpenTelemetry injects W3C TraceContext headers (traceparent) into HTTP headers and Kafka record headers. Downstream consumers extract the trace ID to link distributed spans into a unified waterfall graph.",
            "Accenture Observability", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How does Accenture's '360-degree Value' framework guide the implementation and ROI evaluation of Generative AI across client enterprise operations?",
            "Discuss: Measuring AI impact across financial performance, customer experience, sustainability, operational velocity, and workforce talent upskilling.",
            "Accenture 360-Degree AI Value"
        ),
        create_ai_question(
            "Describe how you design an enterprise AI Adoption Roadmap for a Fortune 500 financial client, addressing legacy integration, security, and employee training.",
            "Phases: 1) Proof of Value with high-impact pilot, 2) Enterprise AI Foundation (governance, secure cloud landing zones), 3) Departmental scaling and agentic workflows.",
            "Accenture AI Strategy"
        ),
        create_ai_question(
            "How do you architect an enterprise Knowledge Management RAG solution connecting proprietary SharePoint, Confluence, and ServiceNow databases using Azure OpenAI?",
            "Detail: Central ingestion connectors, hybrid search indexing, Entra ID security ACL filtering, citation grounding, and feedback loops.",
            "Accenture Enterprise Knowledge AI"
        ),
        create_ai_question(
            "What techniques do you employ to prevent AI prompt injection and jailbreaking when integrating public-facing conversational AI agents for telecom clients?",
            "Explain: Dual-model architecture (guardrail LLM reviews prompt before execution), input sanitization regex, strict system instructions, and output schema enforcement.",
            "Accenture AI Security & Guardrails"
        ),
        create_ai_question(
            "How do you implement automated invoice data extraction and matching using AI models to streamline client accounts payable processes?",
            "Detail: Azure AI Document Intelligence parsing unstructured PDFs, mapping extracted fields to ERP purchase order line items, and routing exceptions for human review.",
            "Accenture Intelligent Document Processing"
        ),
        create_ai_question(
            "How does Accenture evaluate Model Risk Management (MRM) and regulatory compliance for AI models deployed in banking (SR 11-7 guidelines)?",
            "Cover: Conceptual soundness validation, ongoing performance monitoring, stress testing, outcome analysis, and audit documentation.",
            "Accenture Model Risk Management"
        ),
        create_ai_question(
            "Describe how Generative AI tools (Copilot, Cursor) are integrated into software engineering squads to increase sprint velocity while maintaining clean architecture.",
            "Discuss: Automated boilerplate generation, unit test creation, drafting API documentation, and enforcing peer code review as an uncompromising quality gate.",
            "Accenture Developer AI Tooling"
        ),
        create_ai_question(
            "How do you implement Responsible AI practices to audit algorithmic bias in AI-driven talent acquisition and hiring platforms for enterprise clients?",
            "Explain: Demographic parity metrics, disparate impact analysis, synthetic balancing of training datasets, and explainable AI reporting.",
            "Accenture Responsible AI"
        ),
        create_ai_question(
            "How do you design an A/B testing framework to measure user engagement and conversion differences between a traditional rule-based search engine and an AI semantic search engine?",
            "Architecture: Split traffic evenly using feature flags, measure click-through rate (CTR), time to purchase, zero-result search rate, and statistical significance.",
            "Accenture AI Experimentation"
        ),
        create_ai_question(
            "What strategies do you use for optimizing LLM API inference costs (Token Economics) across 50,000 daily enterprise transactions?",
            "Discuss: Prompt compression, caching recurring prompt prefixes, utilizing smaller fine-tuned SLMs (Small Language Models) for routine classification, and batching.",
            "Accenture AI Cost Optimization"
        )
    ]

    hr_java = [
        create_hr_question(
            "Accenture emphasizes 'delivering 360-degree value' for clients. Can you describe a project where you solved a technical issue while keeping commercial and business impact in mind?",
            "Discuss: Return on investment, operational efficiency, cost reduction, or end-user adoption metrics alongside tech decisions.",
            "360-Degree Value Creation"
        ),
        create_hr_question(
            "Consulting and transformation projects often face shifting client requirements. Tell me about a time a client or stakeholder changed project scope midway through a sprint.",
            "Show: Adaptability, professional communication, revising user stories pragmatically, and delivering the new priority without frustration.",
            "Agility & Scope Management"
        ),
        create_hr_question(
            "Why do you specifically want to build your technology consulting career at Accenture rather than other IT services firms?",
            "Highlight: Accenture's global technology leadership, Cloud First initiatives, partnerships with all major hyperscalers, and diverse Fortune 500 client exposure.",
            "Accenture Brand Motivation"
        ),
        create_hr_question(
            "How do you handle working in a high-performing, cross-functional team with colleagues across different time zones (US, Europe, India)?",
            "Focus on: Asynchronous communication, documentation rigor, respecting time zone boundaries, and collaborative teamwork.",
            "Global Collaboration"
        ),
        create_hr_question(
            "Describe a time you received difficult constructive feedback from a team lead or client. How did you handle your emotions and take corrective action?",
            "Emphasize: Active listening, viewing feedback as an opportunity for rapid career progression, and demonstrating measurable improvement.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Accenture values inclusion and diversity as a fundamental strength. How do you actively champion an inclusive environment in daily project interactions?",
            "Discuss: Respecting different communication styles, mentoring junior peers, valuing varied perspectives, and fostering psychological safety.",
            "Inclusion & Diversity"
        ),
        create_hr_question(
            "Tell me about a time you had to deliver a critical presentation or technical walkthrough to non-technical business stakeholders.",
            "Highlight: Translating abstract software concepts into business outcomes, using analogies, and answering questions with clarity.",
            "Stakeholder Communication"
        ),
        create_hr_question(
            "Describe a situation where your project team faced an aggressive client delivery deadline. How did you prioritize tasks and maintain high code quality?",
            "Use STAR: Outline task triage, eliminating nice-to-haves, automated testing to avoid regression, and supporting teammates.",
            "Delivering Under Pressure"
        ),
        create_hr_question(
            "Where do you envision your career trajectory at Accenture over the next 3 to 5 years as a technology consultant?",
            "Connect: Aspiring to grow from Associate Software Engineer to Consultant / Tech Architect, leading cloud transformation projects, and earning certifications.",
            "Career Aspirations"
        ),
        create_hr_question(
            "Do you have any questions for Accenture leadership regarding project allocation, training opportunities, or our innovation hubs?",
            "Candidate asks insightful questions about Accenture Innovation Centers, Cloud First academy, or community practice networks.",
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
# 7. WIPRO
# ==========================================
def build_wipro_catalog():
    apt_java = [
        create_aptitude_question(
            "In Wipro Elite NTH Quantitative Aptitude: The ratio of present ages of two developers A and B is 4:5. Eight years hence, the ratio of their ages will be 5:6. What is the present age of developer A?",
            ["32 years", "40 years", "28 years", "36 years"],
            "32 years",
            "Let present ages be 4x and 5x. (4x + 8) / (5x + 8) = 5/6 => 6*(4x + 8) = 5*(5x + 8) => 24x + 48 = 25x + 40 => x = 8. Present age of A = 4 * 8 = 32 years.",
            "Easy", "Wipro Elite NTH Ages Math"
        ),
        create_aptitude_question(
            "A software engineer at Wipro Kodathi campus drives to office at 40 km/h and arrives 10 minutes late. The next day, driving at 50 km/h, the engineer arrives 5 minutes early. What is the distance to the office?",
            ["50 km", "40 km", "60 km", "45 km"],
            "50 km",
            "Difference in time = 10 - (-5) = 15 minutes = 1/4 hour. Distance D: D/40 - D/50 = 1/4 => (5D - 4D)/200 = 1/4 => D/200 = 1/4 => D = 50 km.",
            "Medium", "Wipro Speed & Time"
        ),
        create_aptitude_question(
            "In a Wipro campus placement test, 35% of candidates failed in Coding, 45% failed in Aptitude, and 20% failed in both. If 480 candidates passed in both subjects, what was the total number of candidates who appeared?",
            ["1,200 candidates", "1,500 candidates", "1,000 candidates", "1,600 candidates"],
            "1,200 candidates",
            "Total failed in at least one = 35% + 45% - 20% = 60%. Percentage passed in both = 100% - 60% = 40%. 40% of Total = 480 => Total = 480 / 0.40 = 1,200 candidates.",
            "Medium", "Wipro Percentage & Sets"
        ),
        create_aptitude_question(
            "A merchant marks an item 30% above the cost price and allows a discount of 15% on the marked price. What is the merchant's net profit percentage?",
            ["10.5%", "15.0%", "12.0%", "8.5%"],
            "10.5%",
            "Cost = 100. Marked = 130. Discount = 15% of 130 = 19.5. Selling price = 130 - 19.5 = 110.5. Net profit = 10.5%.",
            "Easy", "Wipro Profit & Loss"
        ),
        create_aptitude_question(
            "In Wipro Logical Deduction: Find the missing term in the sequence: 4, 12, 36, 108, ___?",
            ["324", "216", "432", "312"],
            "324",
            "Each term is multiplied by 3: 4*3=12, 12*3=36, 36*3=108, 108*3=324.",
            "Easy", "Wipro Number Series"
        ),
        create_aptitude_question(
            "A bag contains 6 black balls and 4 white balls. Two balls are drawn at random one after another without replacement. What is the probability that the first ball is black and the second ball is white?",
            ["4/15", "6/25", "1/5", "8/15"],
            "4/15",
            "P(1st black and 2nd white) = (6/10) * (4/9) = (3/5) * (4/9) = 12/45 = 4/15.",
            "Medium", "Wipro Probability"
        ),
        create_aptitude_question(
            "In Wipro Written Communication: Identify the grammatically correct sentence:",
            ["Neither the lead architect nor the developers were present at the meeting.", "Neither the lead architect nor the developers was present at the meeting.", "Neither the lead architect or the developers were present at the meeting.", "Neither the lead architect nor the developers has been present at the meeting."],
            "Neither the lead architect nor the developers were present at the meeting.",
            "When subjects are joined by 'neither...nor', the verb agrees with the closer subject ('developers' is plural, so 'were' is correct).",
            "Easy", "Wipro Verbal Ability"
        ),
        create_aptitude_question(
            "If in a code language, 'WIPRO' is coded as 'XJQSP', how is 'SYSTEM' coded in that same language?",
            ["TZTUFN", "TZUUGN", "SZTVEN", "TYTUEN"],
            "TZTUFN",
            "Each character is shifted by +1: S->T, Y->Z, S->T, T->U, E->F, M->N. The coded word is TZTUFN.",
            "Easy", "Wipro Coding & Decoding"
        ),
        create_aptitude_question(
            "A sum of Rs. 12,000 lent at simple interest amounts to Rs. 14,880 in 4 years. What is the rate of interest per annum?",
            ["6%", "5%", "7%", "8%"],
            "6%",
            "Total Simple Interest = 14,880 - 12,000 = Rs. 2,880. SI = (P * R * T)/100 => 2,880 = (12,000 * R * 4)/100 => 2,880 = 480 * R => R = 6%.",
            "Easy", "Wipro Simple Interest"
        ),
        create_aptitude_question(
            "In how many ways can 5 software modules be arranged in a release pipeline if Module A must always be executed first?",
            ["24 ways", "120 ways", "60 ways", "48 ways"],
            "24 ways",
            "Fix Module A at position 1. The remaining 4 modules can be arranged in 4! = 24 ways.",
            "Easy", "Wipro Permutations"
        ),
        create_aptitude_question(
            "A water pump fills a cooling reservoir in 15 minutes, while a second pump takes 30 minutes. How long will they take working together to fill the reservoir?",
            ["10 minutes", "12 minutes", "8 minutes", "22.5 minutes"],
            "10 minutes",
            "Combined rate = 1/15 + 1/30 = (2 + 1)/30 = 3/30 = 1/10 reservoir per minute. Total time = 10 minutes.",
            "Easy", "Wipro Pipes & Cisterns"
        ),
        create_aptitude_question(
            "In Wipro Syllogisms: Statements: 1. All engineers are problem solvers. 2. All problem solvers are analytical. Conclusion: All engineers are analytical.",
            ["The conclusion follows logically", "The conclusion does not follow", "Either conclusion follows or does not follow", "Data is insufficient"],
            "The conclusion follows logically",
            "By transitive syllogism: Engineers -> Problem Solvers -> Analytical. Therefore, All engineers are analytical follows unconditionally.",
            "Easy", "Wipro Syllogisms"
        ),
        create_aptitude_question(
            "A car traveling at an average speed of 72 km/h completes a journey in 4.5 hours. How much time would it take to complete the same journey at 90 km/h?",
            ["3.6 hours", "4.0 hours", "3.2 hours", "3.8 hours"],
            "3.6 hours",
            "Distance = Speed * Time = 72 * 4.5 = 324 km. New time = Distance / New speed = 324 / 90 = 3.6 hours (3 hours 36 minutes).",
            "Easy", "Wipro Speed & Time"
        ),
        create_aptitude_question(
            "Find the average of all prime numbers between 20 and 40:",
            ["30.0", "29.5", "31.2", "28.8"],
            "30.0",
            "Prime numbers between 20 and 40: 23, 29, 31, 37. Sum = 23 + 29 + 31 + 37 = 120. Average = 120 / 4 = 30.0.",
            "Easy", "Wipro Number Theory"
        ),
        create_aptitude_question(
            "In Wipro Statement & Assumption: Statement: 'Please read the deployment checklist carefully before pushing to production.' Assumptions: I. People who read checklists can avoid deployment errors. II. Engineers are capable of reading checklists.",
            ["Both assumptions I and II are implicit", "Only assumption I is implicit", "Only assumption II is implicit", "Neither assumption is implicit"],
            "Both assumptions I and II are implicit",
            "A warning/instruction is issued assuming that the audience can understand it (II) and that following it produces the intended beneficial result (I). Both are implicit.",
            "Medium", "Wipro Critical Reasoning"
        )
    ]

    code_java = [
        create_coding_problem(
            "Find Second Largest Element in Array",
            "Given an array of integers, find the second largest distinct element without sorting the array. If no second largest exists, return -1.",
            "arr = [12, 35, 1, 10, 34, 1]",
            "34",
            "public class Solution {\n    public static int getSecondLargest(int[] arr) {\n        return -1;\n    }\n}",
            "def get_second_largest(arr: list[int]) -> int:\n    pass",
            "def extract_second_highest_metric(metrics_df) -> int:\n    pass",
            "Wipro standard: Single pass tracking largest and second_largest in O(N) time and O(1) extra space.",
            "Easy", "Array Scanning", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Remove Duplicates from Sorted Array",
            "Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.",
            "nums = [1,1,2]",
            "2, nums = [1,2,_]",
            "public class Solution {\n    public int removeDuplicates(int[] nums) {\n        return 0;\n    }\n}",
            "def remove_duplicates(nums: list[int]) -> int:\n    pass",
            "def deduplicate_sorted_identifiers(id_series) -> int:\n    pass",
            "Two-pointer technique: Slow pointer writes unique elements while fast pointer scans the array.",
            "Easy", "Two Pointers", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "First Non-Repeating Character in a String",
            "Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.",
            's = "loveleetcode"',
            "2 (Character 'v')",
            "public class Solution {\n    public int firstUniqChar(String s) {\n        return -1;\n    }\n}",
            "def first_uniq_char(s: str) -> int:\n    pass",
            "def locate_first_unique_event(events_df) -> int:\n    pass",
            "Count character frequencies in an integer array of size 26; second pass finds the first character with count == 1.",
            "Easy", "Hash Table & String", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Matrix Spiral Traversal",
            "Given an N x M 2D matrix, print all elements of the matrix in clockwise spiral order.",
            "matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]",
            "[1,2,3,4,8,12,11,10,9,5,6,7]",
            "public class Solution {\n    public static List<Integer> spiralOrder(int[][] matrix) {\n        return new ArrayList<>();\n    }\n}",
            "def spiral_order(matrix: list[list[int]]) -> list[int]:\n    pass",
            "def flatten_matrix_spiral(matrix_df) -> list[int]:\n    pass",
            "Iterate boundaries (top, bottom, left, right) progressively narrowing the remaining matrix area.",
            "Medium", "Matrix Traversal", "O(M * N)", "O(1)"
        ),
        create_coding_problem(
            "Reverse Words in a String",
            "Given an input string s, reverse the order of the words. Return a string of the words in reverse order concatenated by a single space without leading or trailing spaces.",
            's = "the sky is blue"',
            '"blue is sky the"',
            "public class Solution {\n    public String reverseWords(String s) {\n        return \"\";\n    }\n}",
            "def reverse_words(s: str) -> str:\n    pass",
            "def reverse_audit_log_tokens(log_series) -> str:\n    pass",
            "Split string by whitespace, filter out empty tokens, and concatenate tokens in reverse order.",
            "Medium", "String Manipulation", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Merge Two Sorted Linked Lists",
            "You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.",
            "list1 = [1,2,4], list2 = [1,3,4]",
            "[1,1,2,3,4,4]",
            "public class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        return null;\n    }\n}",
            "def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n    pass",
            "def merge_sorted_streams(stream_a, stream_b):\n    pass",
            "Use a dummy head node and advance the pointer with the smaller value until one list is exhausted.",
            "Easy", "Linked List", "O(N + M)", "O(1)"
        ),
        create_coding_problem(
            "Single Number (Find Non-Duplicate using XOR)",
            "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one in O(N) linear runtime and O(1) constant extra space.",
            "nums = [4,1,2,1,2]",
            "4",
            "public class Solution {\n    public int singleNumber(int[] nums) {\n        return 0;\n    }\n}",
            "def single_number(nums: list[int]) -> int:\n    pass",
            "def identify_unpaired_signal(signal_series) -> int:\n    pass",
            "Bitwise XOR property: a ^ a = 0 and a ^ 0 = a. XORing all array elements cancels out pairs, leaving the single number.",
            "Easy", "Bit Manipulation", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Palindrome Number Check",
            "Given an integer x, return true if x is a palindrome, and false otherwise, without converting the integer to a string.",
            "x = 121",
            "true",
            "public class Solution {\n    public boolean isPalindrome(int x) {\n        return false;\n    }\n}",
            "def is_palindrome(x: int) -> bool:\n    pass",
            "def check_numeric_symmetry(id_series) -> bool:\n    pass",
            "Negative numbers cannot be palindromes. Revert half of the integer and compare with the remaining half.",
            "Easy", "Math", "O(log10(N))", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain the internal implementation of Java HashMap: Bucketing, Hash collisions, Linked List to Red-Black Tree conversion (Treeify threshold = 8).",
            "HashMap stores Node<K,V> in an array table. Hashes are computed via hashCode() ^ (h >>> 16). When a bucket exceeds 8 entries and table capacity >= 64, it treeifies into a Red-Black Tree for O(log N) lookup.",
            "Wipro Java Core & Collections", "Hard"
        ),
        create_technical_question(
            "What is the difference between ArrayList and LinkedList in Java? Why is ArrayList preferred for enterprise data access in Wipro client applications?",
            "ArrayList uses a contiguous backing array with O(1) random access and excellent CPU cache locality. LinkedList stores nodes with object references, incurring 24 bytes overhead per node and pointer chasing.",
            "Wipro Java Collections", "Easy"
        ),
        create_technical_question(
            "How do JDBC Batch Updates (addBatch, executeBatch) optimize performance compared to individual statement executions during bulk data migrations at Wipro?",
            "Individual executions make a separate network round-trip per statement. executeBatch sends multiple statements across the network in a single packet, reducing latency by up to 90%.",
            "Wipro Database & JDBC", "Medium"
        ),
        create_technical_question(
            "Explain RESTful API error handling best practices according to RFC 7807 (Problem Details for HTTP APIs) using Spring @ControllerAdvice and @ExceptionHandler.",
            "@ControllerAdvice intercepts exceptions globally across all controllers, mapping business exceptions to standardized JSON payloads containing type, title, status, detail, and instance URI.",
            "Wipro Spring Web & REST", "Medium"
        ),
        create_technical_question(
            "How does Spring Boot Profiles (@Profile) manage environment-specific configurations (Dev, QA, Staging, Prod) in hybrid enterprise cloud systems?",
            "application-{profile}.properties defines environment-specific settings (database URLs, API keys). Active profile is toggled via spring.profiles.active without rebuilding JAR binaries.",
            "Wipro Spring Configuration", "Easy"
        ),
        create_technical_question(
            "What is SQL EXPLAIN ANALYZE, and how do you detect Full Table Scans vs Index Scans to optimize slow reporting queries?",
            "EXPLAIN ANALYZE executes the query and reports actual execution time and node costs. A 'Seq Scan' on large tables indicates missing indexes, which should be replaced by Index Scan or Index Only Scan.",
            "Wipro SQL Performance Tuning", "Medium"
        ),
        create_technical_question(
            "Explain Git Branching Strategies: GitFlow vs Trunk-Based Development, and why Wipro agile delivery teams favor Trunk-Based Development for CI/CD.",
            "GitFlow maintains long-lived feature, develop, and release branches with complex merges. Trunk-based development has all engineers commit short-lived branches to main daily, enabling continuous testing.",
            "Wipro DevOps & Git", "Medium"
        ),
        create_technical_question(
            "How does Prometheus scrape metrics from Spring Boot Actuator (/actuator/prometheus), and how does Grafana visualize microservice health?",
            "Micrometer registers application metrics (JVM memory, HTTP request latencies). Prometheus scrapes the endpoint periodically, and Grafana queries Prometheus via PromQL to render dashboards.",
            "Wipro Observability & Monitoring", "Medium"
        ),
        create_technical_question(
            "What is Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF)? How does Spring Security protect against CSRF attacks in enterprise portals?",
            "XSS injects malicious client-side scripts. CSRF tricks authenticated users into submitting unwanted actions. Spring Security generates unique synchronizer CSRF tokens verified on every mutation request.",
            "Wipro Web Application Security", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Comparable and Comparator interfaces in Java with practical examples of custom sorting.",
            "Comparable imposes natural ordering on a class via compareTo(T o). Comparator defines external custom ordering via compare(T o1, T o2), allowing multiple sort strategies without modifying the source class.",
            "Wipro Java Fundamentals", "Easy"
        ),
        create_technical_question(
            "How do you configure RabbitMQ Message Acknowledgment (ACK/NACK) and Dead Letter Exchanges (DLX) to guarantee message reliability in Wipro integration hubs?",
            "Consumers use manual acknowledgment (basicAck). If processing fails, basicNack rejects the message with requeue=false, automatically routing it to a Dead Letter Exchange for investigation.",
            "Wipro Enterprise Messaging", "Medium"
        ),
        create_technical_question(
            "Explain the difference between Checked and Unchecked Exceptions in Java, and why modern frameworks favor Unchecked (Runtime) exceptions.",
            "Checked exceptions (IOException) inherit from Exception and require compile-time handling. Unchecked exceptions (RuntimeException) reduce boilerplate clutter while bubbling up to global handlers.",
            "Wipro Java Exception Handling", "Easy"
        ),
        create_technical_question(
            "How does Docker port mapping (-p 8080:8080) and container networking (bridge, host, overlay) operate when hosting multi-tier web applications?",
            "Bridge network connects containers on the same Docker host with isolated subnets and DNS name resolution. Port mapping forwards host IP:port traffic through iptables NAT rules to the container port.",
            "Wipro Docker & Networking", "Medium"
        ),
        create_technical_question(
            "What is SQL Injection, and why do PreparedStatement and parameterized queries prevent SQL injection attacks in database drivers?",
            "PreparedStatement pre-compiles the SQL query template. User input parameters are sent separately as literal data values, never as executable SQL code, completely neutralizing injection payloads.",
            "Wipro Secure Coding & SQL", "Medium"
        ),
        create_technical_question(
            "Explain Java Multithreading synchronization: synchronized methods vs synchronized blocks, and the impact of lock granularity on system throughput.",
            "Synchronized methods lock the entire object instance. Synchronized blocks allow locking on a smaller shared monitor object, reducing lock contention and keeping non-critical code concurrent.",
            "Wipro Multithreading", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "Explain the Wipro ai360 framework and how it embeds artificial intelligence across cloud, engineering, and cybersecurity services.",
            "Discuss: Wipro ai360 ecosystem integrating AI into all consulting practices, AI-powered developer studios, AIOps automation, and responsible AI governance.",
            "Wipro ai360 Enterprise Strategy"
        ),
        create_ai_question(
            "How can AI-assisted code analysis tools be integrated into Wipro delivery centers to automatically detect security vulnerabilities and code smells?",
            "Detail: Automated SonarQube + LLM scanning on git push, scoring cyclomatic complexity, detecting hardcoded secrets, and suggesting fixes before peer review.",
            "Wipro AI-Assisted Code Quality"
        ),
        create_ai_question(
            "Describe how AIOps (Artificial Intelligence for IT Operations) reduces mean-time-to-resolution (MTTR) for infrastructure incidents at Wipro.",
            "Architecture: Ingesting server metrics and logs, anomaly detection using isolation forests, correlating alerts to root causes, and automated self-healing scripts.",
            "Wipro AIOps & Incident Management"
        ),
        create_ai_question(
            "How do you implement an enterprise chatbot using Generative AI for HR policy queries at Wipro while ensuring responses are grounded in verified documentation?",
            "Explain: RAG architecture using vector search over company policy PDFs, prompt engineering with strict grounding constraints, and fallback to HR helpdesk.",
            "Wipro Internal HR Conversational AI"
        ),
        create_ai_question(
            "What techniques do you use to detect and mitigate dataset bias in predictive machine learning models developed for client credit assessments?",
            "Discuss: Removing direct demographic indicators, checking fairness metrics (equalized odds, demographic parity), and conducting stress tests across subgroups.",
            "Wipro Algorithmic Fairness"
        ),
        create_ai_question(
            "How do you automate API test case generation using LLMs from Swagger / OpenAPI documentation specifications?",
            "Explain: Parsing OpenAPI schema, generating boundary condition payloads, fuzz testing invalid inputs, and asserting HTTP response status codes automatically.",
            "Wipro AI Automated Testing"
        ),
        create_ai_question(
            "Describe how Generative AI can assist legacy mainframe application maintenance by summarizing complex legacy routines for junior engineers.",
            "Detail: Chunking legacy source files, prompting code-specialized LLMs to generate high-level functional flowcharts and entity relationship summaries.",
            "Wipro Legacy Application AI"
        ),
        create_ai_question(
            "How do you monitor and optimize GPU / cloud compute costs when deploying machine learning model training workloads on AWS / Azure at Wipro?",
            "Discuss: Utilizing spot instances, mixed precision training (FP16), distributed training with PyTorch DDP, and early stopping to eliminate wasted epochs.",
            "Wipro Cloud AI Cost Management"
        ),
        create_ai_question(
            "What security guardrails must be enforced when employees use public AI developer tools to prevent corporate intellectual property leakage?",
            "Cover: Data loss prevention (DLP) proxies, enterprise licenses with zero model training agreements, prohibiting pasting customer PII, and code auditing.",
            "Wipro Enterprise AI Security"
        ),
        create_ai_question(
            "How does Wipro empower employees to build AI fluency across diverse business domains through internal learning programs?",
            "Discuss: Hands-on hackathons, ai360 certification paths, prompt engineering workshops, and practical client case studies.",
            "Wipro AI Culture & Upskilling"
        )
    ]

    hr_java = [
        create_hr_question(
            "The 'Spirit of Wipro' is built on three core pillars: Be passionate about clients' success, Treat each person with respect, and Be global and responsible. How do you embody these principles?",
            "Provide a personal example showcasing client dedication, empathy for colleagues, and acting with unyielding integrity in your academic or work life.",
            "Spirit of Wipro Core Values"
        ),
        create_hr_question(
            "Why do you specifically wish to build your technology career at Wipro rather than other IT services companies?",
            "Highlight: Wipro's rich 75+ year heritage, philanthropic commitment through the Azim Premji Foundation, focus on emerging tech with ai360, and inclusive culture.",
            "Wipro Brand & Heritage"
        ),
        create_hr_question(
            "Wipro delivers digital projects across global client locations and major Indian delivery centers (Bangalore, Pune, Hyderabad, Chennai). Are you fully open to relocation and shift flexibility?",
            "Affirm: Complete willingness to relocate, flexibility with rotational project shifts, adaptability to hybrid work models, and dedication to client project timelines.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "Tell me about a time you faced a difficult conflict or disagreement in a group project. How did you resolve it respectfully?",
            "Use STAR: Outline the disagreement, active listening, finding common technical ground, and maintaining strong interpersonal relationships.",
            "Conflict Resolution & Respect"
        ),
        create_hr_question(
            "How do you handle working on an enterprise project where requirements change rapidly due to client business priorities?",
            "Emphasize: Agility, maintaining a positive attitude toward change, clarifying updated priorities with the tech lead, and executing efficiently.",
            "Adaptability & Resilience"
        ),
        create_hr_question(
            "Describe a situation where you had to quickly learn an unfamiliar technology stack to deliver a project milestone.",
            "Showcase: Self-starter mindset, utilizing technical documentation, building small prototypes, and successfully delivering on time.",
            "Self-Driven Learning"
        ),
        create_hr_question(
            "Where do you see your career progression within Wipro over the next 3 to 5 years?",
            "Connect: Growing from Project Engineer to Senior Software Engineer / Module Lead, mastering cloud native stacks, and contributing to high-impact client accounts.",
            "Career Growth & Ambition"
        ),
        create_hr_question(
            "Tell me about a time you made a mistake in your code that caused a test failure or broken build. How did you handle it?",
            "Demonstrate: Immediate ownership, honest communication with the lead, conducting root-cause analysis, and adding automated tests to prevent recurrence.",
            "Accountability & Integrity"
        ),
        create_hr_question(
            "What unique strengths or personal attributes do you bring to Wipro that set you apart from other candidates?",
            "Combine: Strong computer science fundamentals, passion for problem-solving, collaborative attitude, and alignment with Wipro's values.",
            "Candidate Differentiator"
        ),
        create_hr_question(
            "Do you have any questions for Wipro's leadership regarding project onboarding, mentoring, or our technical learning tracks?",
            "Candidate asks about Wipro's Elite talent development programs, project allocation pathways, or ai360 certification opportunities.",
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
# 8. COGNIZANT
# ==========================================
def build_cognizant_catalog():
    apt_java = [
        create_aptitude_question(
            "Cognizant GenC Quantitative: A train 150 meters long traveling at 45 km/h crosses a bridge in 30 seconds. What is the length of the bridge?",
            ["225 meters", "200 meters", "250 meters", "300 meters"],
            "225 meters",
            "Speed = 45 * (5/18) = 12.5 m/s. Total distance in 30s = 12.5 * 30 = 375 meters. Length of bridge = 375 - 150 = 225 meters.",
            "Easy", "Cognizant GenC Speed & Distance"
        ),
        create_aptitude_question(
            "In a healthcare IT project at Cognizant, 4 hospital servers process 60,000 patient records in 5 hours. How many patient records can 6 servers process in 8 hours at the same rate?",
            ["144,000 records", "120,000 records", "150,000 records", "160,000 records"],
            "144,000 records",
            "Rate per server per hour = 60,000 / (4 * 5) = 3,000 records/server-hour. With 6 servers for 8 hours: total = 6 * 8 * 3,000 = 144,000 records.",
            "Medium", "Cognizant Work Equation"
        ),
        create_aptitude_question(
            "Find the next number in the Cognizant logical sequence: 2, 6, 12, 20, 30, 42, ___?",
            ["56", "54", "60", "48"],
            "56",
            "Differences: 4, 6, 8, 10, 12. Next difference is 14. Next number = 42 + 14 = 56 (or n*(n+1): 1*2, 2*3, 3*4, 4*5, 5*6, 6*7, 7*8=56).",
            "Easy", "Cognizant Number Series"
        ),
        create_aptitude_question(
            "A medical device supplier offers a successive discount of 20% and 10% on diagnostic equipment. What is the single equivalent overall discount percentage?",
            ["28%", "30%", "25%", "27%"],
            "28%",
            "Formula: D = (d1 + d2) - (d1*d2)/100 = (20 + 10) - (20*10)/100 = 30 - 2 = 28%.",
            "Easy", "Cognizant Commercial Math"
        ),
        create_aptitude_question(
            "Cognizant Verbal Ability: Select the correct active voice for: 'The clinical trial data was thoroughly reviewed by the lead biostatistician.'",
            ["The lead biostatistician thoroughly reviewed the clinical trial data.", "The lead biostatistician was reviewing the clinical trial data.", "The lead biostatistician has thoroughly reviewed the clinical trial data.", "The clinical trial data reviewed the lead biostatistician."],
            "The lead biostatistician thoroughly reviewed the clinical trial data.",
            "The passive sentence in simple past ('was reviewed by') converts to active voice in simple past ('thoroughly reviewed').",
            "Easy", "Cognizant Verbal Ability"
        ),
        create_aptitude_question(
            "In how many ways can a committee of 3 engineers and 2 analysts be selected from a group of 6 engineers and 4 analysts at Cognizant?",
            ["120 ways", "100 ways", "144 ways", "60 ways"],
            "120 ways",
            "Select 3 engineers from 6: C(6,3) = 20. Select 2 analysts from 4: C(4,2) = 6. Total ways = 20 * 6 = 120 ways.",
            "Medium", "Cognizant Combinatorics"
        ),
        create_aptitude_question(
            "A person invests Rs. 5,000 for 2 years at 10% per annum compound interest, compounded annually. What is the total compound interest earned?",
            ["Rs. 1,050", "Rs. 1,000", "Rs. 1,100", "Rs. 1,025"],
            "Rs. 1,050",
            "Amount = 5000 * (1.10)^2 = 5000 * 1.21 = Rs. 6,050. Compound Interest = 6050 - 5000 = Rs. 1,050.",
            "Easy", "Cognizant Compound Interest"
        ),
        create_aptitude_question(
            "If 'HOSPITAL' is coded as '32574618' and 'POSTAL' is coded as '725618', what is the code for 'SPOT'?",
            ["5726", "5724", "7526", "5276"],
            "5726",
            "S=5, P=7, O=2, T=6. Therefore 'SPOT' is coded as '5726'.",
            "Easy", "Cognizant Coding-Decoding"
        ),
        create_aptitude_question(
            "A sum of numbers is 25 and their difference is 7. What is the product of the two numbers?",
            ["144", "150", "136", "160"],
            "144",
            "x + y = 25, x - y = 7 => 2x = 32 => x = 16, y = 9. Product = 16 * 9 = 144.",
            "Easy", "Cognizant Elementary Math"
        ),
        create_aptitude_question(
            "A software tester finds 5 defective builds out of 80 tested builds. What is the defect rate percentage?",
            ["6.25%", "5.00%", "6.50%", "7.00%"],
            "6.25%",
            "Defect rate = (5 / 80) * 100 = (1 / 16) * 100 = 6.25%.",
            "Easy", "Cognizant Percentage"
        ),
        create_aptitude_question(
            "Two pipes A and B can fill an IT lab water cooler in 12 and 18 minutes respectively. If both pipes are opened together, how long will it take to fill the cooler?",
            ["7.2 minutes", "8.0 minutes", "6.5 minutes", "7.5 minutes"],
            "7.2 minutes",
            "Rate = 1/12 + 1/18 = (3 + 2)/36 = 5/36. Time = 36 / 5 = 7.2 minutes.",
            "Easy", "Cognizant Pipes & Cisterns"
        ),
        create_aptitude_question(
            "In Cognizant Direction Sense: A healthcare delivery driver travels 12 km West, then turns Right and travels 5 km. What is the shortest straight-line distance from the starting point?",
            ["13 km", "17 km", "15 km", "10 km"],
            "13 km",
            "By Pythagorean theorem: Distance = sqrt(12^2 + 5^2) = sqrt(144 + 25) = sqrt(169) = 13 km.",
            "Easy", "Cognizant Geometry & Direction"
        ),
        create_aptitude_question(
            "Select the antonym for 'BENEVOLENT' in professional organizational conduct:",
            ["Malevolent", "Generous", "Compassionate", "Friendly"],
            "Malevolent",
            "'Benevolent' means well-meaning and kindly. The direct opposite is 'Malevolent' (having or showing a wish to do evil).",
            "Easy", "Cognizant Vocabulary"
        ),
        create_aptitude_question(
            "What is the units digit of 3^45?",
            ["3", "9", "7", "1"],
            "3",
            "Powers of 3 cyclically end in 3, 9, 7, 1 (cycle of 4). 45 % 4 = 1. Therefore, 3^45 ends with 3.",
            "Medium", "Cognizant Number Properties"
        ),
        create_aptitude_question(
            "In Cognizant Data Interpretation: A company department spent $240,000 on engineering, which was 40% of its total budget. How much was the total departmental budget?",
            ["$600,000", "$500,000", "$480,000", "$720,000"],
            "$600,000",
            "Total = 240,000 / 0.40 = $600,000.",
            "Easy", "Cognizant Financial Quant"
        )
    ]

    code_java = [
        create_coding_problem(
            "Linked List Cycle Detection (Floyd's Algorithm)",
            "Given head, the head of a linked list, determine if the linked list has a cycle in it in O(N) time and O(1) memory.",
            "head = [3,2,0,-4], pos = 1 (points to node index 1)",
            "true",
            "public class Solution {\n    public boolean hasCycle(ListNode head) {\n        return false;\n    }\n}",
            "def has_cycle(head: Optional[ListNode]) -> bool:\n    pass",
            "def detect_infinite_reference_loop(nodes_df) -> bool:\n    pass",
            "Cognizant Elevate standard: Floyd's Tortoise and Hare algorithm using slow and fast pointers.",
            "Easy", "Linked List & Two Pointers", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Valid Parentheses Matching",
            "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
            's = "()[]{}"',
            "true",
            "public class Solution {\n    public boolean isValid(String s) {\n        return false;\n    }\n}",
            "def is_valid(s: str) -> bool:\n    pass",
            "def validate_syntax_enclosure(code_series) -> bool:\n    pass",
            "Push opening brackets onto a Stack. For closing brackets, pop and verify matching pair; stack must be empty at the end.",
            "Easy", "Stack", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Roman to Integer Conversion",
            "Given a roman numeral s, convert it to an integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.",
            's = "MCMXCIV"',
            "1994",
            "public class Solution {\n    public int romanToInt(String s) {\n        return 0;\n    }\n}",
            "def roman_to_int(s: str) -> int:\n    pass",
            "def parse_legacy_roman_code(code_series) -> int:\n    pass",
            "Map roman values. If current value < next value, subtract it; otherwise add it.",
            "Easy", "String & Math", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Majority Element (Boyer-Moore Voting Algorithm)",
            "Given an array nums of size n, return the majority element that appears more than floor(n / 2) times in O(N) time and O(1) space.",
            "nums = [2,2,1,1,1,2,2]",
            "2",
            "public class Solution {\n    public int majorityElement(int[] nums) {\n        return 0;\n    }\n}",
            "def majority_element(nums: list[int]) -> int:\n    pass",
            "def detect_dominant_patient_diagnosis(diag_df) -> int:\n    pass",
            "Boyer-Moore Voting: Maintain candidate and count. Increment on match, decrement on mismatch; candidate when count == 0.",
            "Easy", "Array & Voting Algorithm", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Binary Search in Sorted Array",
            "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums in O(log N) time.",
            "nums = [-1,0,3,5,9,12], target = 9",
            "4",
            "public class Solution {\n    public int search(int[] nums, int target) {\n        return -1;\n    }\n}",
            "def search(nums: list[int], target: int) -> int:\n    pass",
            "def find_patient_record_index(records_df, target: int) -> int:\n    pass",
            "Standard binary search with left and right pointers, calculating mid = left + (right - left) / 2 to prevent overflow.",
            "Easy", "Binary Search", "O(log N)", "O(1)"
        ),
        create_coding_problem(
            "Pascal's Triangle Generation",
            "Given an integer numRows, return the first numRows of Pascal's triangle.",
            "numRows = 5",
            "[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]",
            "public class Solution {\n    public List<List<Integer>> generate(int numRows) {\n        return new ArrayList<>();\n    }\n}",
            "def generate(num_rows: int) -> list[list[int]]:\n    pass",
            "def generate_binomial_coefficients_table(rows: int):\n    pass",
            "Iteratively construct each row where row[j] = prevRow[j-1] + prevRow[j] with boundaries set to 1.",
            "Easy", "Dynamic Programming & Array", "O(N^2)", "O(N^2)"
        ),
        create_coding_problem(
            "Intersection of Two Arrays II",
            "Given two integer arrays nums1 and nums2, return an array of their intersection with each element appearing as many times as it shows in both arrays.",
            "nums1 = [1,2,2,1], nums2 = [2,2]",
            "[2,2]",
            "public class Solution {\n    public int[] intersect(int[] nums1, int[] nums2) {\n        return new int[0];\n    }\n}",
            "def intersect(nums1: list[int], nums2: list[int]) -> list[int]:\n    pass",
            "def match_patient_claim_records(claims_a, claims_b):\n    pass",
            "Count frequencies of elements in nums1 using HashMap; iterate nums2 decrementing count and recording matches.",
            "Easy", "Hash Table & Two Pointers", "O(N + M)", "O(min(N, M))"
        ),
        create_coding_problem(
            "Reverse a Singly Linked List",
            "Given the head of a singly linked list, reverse the list, and return the reversed list.",
            "head = [1,2,3,4,5]",
            "[5,4,3,2,1]",
            "public class Solution {\n    public ListNode reverseList(ListNode head) {\n        return null;\n    }\n}",
            "def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:\n    pass",
            "def invert_sequential_medical_events(head_df):\n    pass",
            "Three-pointer iterative approach: prev, curr, nextNode flipping next pointers until end of list.",
            "Easy", "Linked List", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "In Cognizant healthcare digital systems, how do you architect applications to ensure strict HIPAA compliance and secure patient health data (PHI) in transit and at rest?",
            "Encrypt data at rest using AES-256 (TDE); enforce TLS 1.3 in transit; implement strict Role-Based Access Control (RBAC); log all PHI access in tamper-proof audit trails; de-identify data in non-production environments.",
            "Cognizant Healthcare Architecture & HIPAA", "Hard"
        ),
        create_technical_question(
            "Explain the HL7 and FHIR (Fast Healthcare Interoperability Resources) data standards and how RESTful APIs exchange structured clinical resources (Patient, Observation, Encounter).",
            "FHIR represents healthcare entities as modular JSON/XML resources with standardized schemas, RESTful CRUD endpoints, and OAuth2 SMART-on-FHIR authorization profiles for EHR integration.",
            "Cognizant Healthcare Standards (HL7/FHIR)", "Hard"
        ),
        create_technical_question(
            "Explain the Spring MVC Request Lifecycle from DispatcherServlet, HandlerMapping, Controller, ViewResolver to HTTP Response.",
            "Request reaches DispatcherServlet; HandlerMapping identifies matching Controller; HandlerAdapter executes method; Controller returns ModelAndView or ResponseEntity; HttpMessageConverter serializes JSON to response stream.",
            "Cognizant Spring MVC", "Medium"
        ),
        create_technical_question(
            "What are the four ACID properties in relational database management systems, and what phenomena occur under Read Committed isolation?",
            "Atomicity (all or nothing), Consistency (preserves constraints), Isolation (concurrent executions do not interfere), Durability (committed data survives crashes). Read Committed prevents Dirty Reads, but permits Non-repeatable and Phantom reads.",
            "Cognizant Database Fundamentals", "Medium"
        ),
        create_technical_question(
            "Compare RESTful Web Services with SOAP. Why do modern Cognizant enterprise integrations favor REST/JSON while legacy insurance systems often retain SOAP?",
            "REST is lightweight, uses standard HTTP verbs, and is easy to parse with JSON. SOAP enforces strict XML schemas (WSDL), WS-Security, and ACID distributed transactions required by legacy insurance/banking.",
            "Cognizant Web Services", "Medium"
        ),
        create_technical_question(
            "Explain Java 8 Streams: map() vs flatMap(), filter(), and how Collectors.groupingBy() partitions collections into categorized maps.",
            "map() transforms each element 1-to-1. flatMap() flattens nested streams (1-to-many). groupingBy() groups elements by a classifier function into a Map<K, List<V>>.",
            "Cognizant Java 8 Features", "Medium"
        ),
        create_technical_question(
            "How does Spring Data JPA handle entity relationships (@OneToOne, @OneToMany, @ManyToMany), and why is FetchType.LAZY preferred over FetchType.EAGER?",
            "LAZY loading fetches child entities on-demand when accessed, avoiding premature massive SQL joins and memory bloat. EAGER loading fetches all children immediately, causing severe performance degradation.",
            "Cognizant JPA & Hibernate", "Medium"
        ),
        create_technical_question(
            "What is the difference between Synchronous API calls and Asynchronous messaging in microservices, and how does Apache Kafka handle message buffering?",
            "Synchronous calls block until response, creating cascading failure risks. Kafka buffers messages in persistent disk logs, allowing consumers to process asynchronously at their own rate.",
            "Cognizant Microservices Architecture", "Medium"
        ),
        create_technical_question(
            "Explain how the Spring Boot @RestControllerAdvice annotation creates a centralized global exception handling architecture.",
            "@RestControllerAdvice combines @ControllerAdvice and @ResponseBody, automatically intercepting thrown exceptions across all controllers and serializing structured error responses.",
            "Cognizant Spring Boot", "Easy"
        ),
        create_technical_question(
            "How do you implement Unit Testing in Spring Boot with JUnit 5 and Mockito (@Mock, @InjectMocks, when().thenReturn())?",
            "@Mock creates a mock proxy instance of a dependency; @InjectMocks injects mocks into the class under test; when().thenReturn() defines stubbed behavior for isolated testing.",
            "Cognizant Unit Testing & Mockito", "Easy"
        ),
        create_technical_question(
            "Explain Database Indexing strategies: Single-Column vs Composite Indexing, and the significance of the Leftmost Prefix Rule.",
            "A composite index on (A, B, C) can satisfy queries on (A), (A, B), and (A, B, C). It cannot be used for queries filtering only on (B) or (C) due to B-tree traversal requiring the leftmost column.",
            "Cognizant SQL & Indexing", "Medium"
        ),
        create_technical_question(
            "What are Java Thread States (NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED), and how do you analyze thread dumps to find deadlocks?",
            "A thread enters BLOCKED when waiting for a monitor lock, and WAITING when calling wait()/join(). In thread dumps, look for 'Found one Java-level deadlock' where Thread A holds lock 1 waiting for lock 2 while Thread B holds lock 2 waiting for lock 1.",
            "Cognizant Multithreading & Debugging", "Medium"
        ),
        create_technical_question(
            "Explain the difference between String, StringBuilder, and StringBuffer in Java regarding mutability and thread safety.",
            "String is immutable (stored in String pool). StringBuilder is mutable and not thread-safe (fastest for single-threaded string concatenation). StringBuffer is mutable and synchronized (thread-safe).",
            "Cognizant Java Fundamentals", "Easy"
        ),
        create_technical_question(
            "How do you secure REST APIs using OAuth 2.0 and JWT tokens, including token expiration and refresh token rotation?",
            "Client exchanges credentials for access token (short TTL: 15 mins) and refresh token (long TTL: 7 days). When access token expires, refresh token is sent to issue a new pair while invalidating the old refresh token.",
            "Cognizant API Security", "Medium"
        ),
        create_technical_question(
            "What is Docker Containerization, and how does Docker Compose orchestrate a multi-service application (Spring Boot + PostgreSQL + Redis)?",
            "Docker packages application code and runtime dependencies into lightweight containers. Docker Compose defines multi-container applications in a single YAML file with shared networks, volumes, and environment variables.",
            "Cognizant DevOps & Docker", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How can Generative AI and NLP be applied in healthcare digital platforms at Cognizant to extract clinical insights from unstructured doctor notes?",
            "Explain: Named Entity Recognition (NER) for medical terminology, mapping to ICD-10 and SNOMED codes, de-identification for HIPAA compliance, and doctor validation.",
            "Cognizant Healthcare AI"
        ),
        create_ai_question(
            "Describe how AI-assisted automated code generation tools are deployed across Cognizant engineering squads to increase delivery velocity.",
            "Discuss: Integrating code completion tools, establishing secure corporate guardrails to prevent IP leakage, and enforcing peer code review checkpoints.",
            "Cognizant Developer AI Velocity"
        ),
        create_ai_question(
            "How do you design a predictive patient readmission model using machine learning while addressing class imbalance in hospital EHR datasets?",
            "Detail: Using SMOTE (Synthetic Minority Over-sampling Technique) or class weighting, evaluating precision-recall AUC rather than raw accuracy, and explaining risk factors with SHAP.",
            "Cognizant Predictive Healthcare Analytics"
        ),
        create_ai_question(
            "How do you implement an enterprise conversational AI agent for health insurance claim status lookups with strict validation guardrails?",
            "Architecture: RAG architecture over claim guidelines, conversational intent classification with LLM, secure API integration with core claims processing database, and human agent fallback.",
            "Cognizant Conversational Claims AI"
        ),
        create_ai_question(
            "What strategies ensure ethical AI and eliminate racial/socioeconomic bias in automated medical diagnosis recommendation algorithms?",
            "Discuss: Curating balanced demographic training cohorts, auditing disparate false negative rates across groups, and maintaining doctor-in-the-loop oversight.",
            "Cognizant Ethical AI in Healthcare"
        ),
        create_ai_question(
            "How do you automate medical claims fraud detection using Graph Neural Networks (GNN) and transaction clustering at Cognizant?",
            "Detail: Modeling providers, patients, and pharmacies as graph nodes; analyzing suspicious transaction cycles, bill frequency anomalies, and collaborative fraud rings.",
            "Cognizant AI Fraud Detection"
        ),
        create_ai_question(
            "Describe how LLMs can automate the generation of regulatory compliance documentation (FDA, HIPAA) for digital health software releases.",
            "Explain: Parsing code repository commits, mapping features to regulatory requirement matrices, generating traceability matrices, and human compliance officer sign-off.",
            "Cognizant Regulatory AI"
        ),
        create_ai_question(
            "How do you optimize LLM inference latency when deploying medical triage recommendation chatbots on edge hospital tablets?",
            "Discuss: Model quantization (INT4/INT8), local caching of standard triage protocols, and delegating complex queries asynchronously to cloud endpoints.",
            "Cognizant Edge AI & Quantization"
        ),
        create_ai_question(
            "How does Cognizant support workforce upskilling in Generative AI through the Cognizant Synapse learning initiative?",
            "Cover: Role-based AI academies, hands-on enterprise sandbox labs, responsible AI certifications, and client project hackathons.",
            "Cognizant Synapse AI Upskilling"
        ),
        create_ai_question(
            "How do you implement RAG over multi-format healthcare documents (PDFs, HL7 messages, DICOM metadata) with sub-second retrieval?",
            "Detail: Specialized parsers for clinical document architectures (CDA), domain-specific BioBERT embeddings, vector database indexing, and structured citation linking.",
            "Cognizant Healthcare RAG"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically want to build your software engineering career at Cognizant?",
            "Highlight: Cognizant's market leadership in digital engineering, healthcare and life sciences technology, focus on GenC career acceleration, and collaborative global culture.",
            "Cognizant Brand Motivation"
        ),
        create_hr_question(
            "Cognizant's values emphasize 'Customer Obsession' and 'Creating Conditions for Everyone to Thrive'. Describe a time you went above and beyond to deliver value for a project stakeholder.",
            "Use STAR: Outline stakeholder problem, personal initiative taken beyond expectations, and the quantifiable positive outcome.",
            "Cognizant Values & Client Dedication"
        ),
        create_hr_question(
            "Cognizant operates major delivery centers across India (Chennai, Bangalore, Hyderabad, Pune, Kolkata). Are you fully flexible with relocation and rotational project shifts?",
            "Affirm: Complete willingness to relocate to any Cognizant facility, enthusiasm to work in client time zones, and adaptability to hybrid delivery models.",
            "Relocation & Shift Flexibility"
        ),
        create_hr_question(
            "Describe a time you collaborated with team members from different engineering backgrounds on a software project. How did you ensure smooth coordination?",
            "Focus on: Clear communication, transparent task tracking, empathy for different perspectives, and celebrating collective milestones.",
            "Team Collaboration"
        ),
        create_hr_question(
            "How do you handle working under tight delivery deadlines when unexpected technical blockers arise in your assigned module?",
            "Show: Calm problem diagnosis, communicating early with the scrum master/lead, seeking guidance, and working diligently to deliver on time.",
            "Handling Deadlines & Blockers"
        ),
        create_hr_question(
            "Tell me about a time you received constructive feedback on your code or behavior. What action did you take to improve?",
            "Demonstrate: Openness to growth, taking detailed notes, practicing clean coding principles, and showing visible improvement in the next sprint.",
            "Receptivity to Feedback"
        ),
        create_hr_question(
            "Where do you see yourself growing within Cognizant over the next 3 to 5 years as an engineer?",
            "Connect: Aspiring to grow from Programmer Analyst / GenC to Associate / Senior Associate, gaining domain expertise, and mentoring new hires.",
            "Career Aspirations"
        ),
        create_hr_question(
            "How do you stay motivated and ensure continuous learning in a fast-paced technology consulting environment?",
            "Highlight: Exploring emerging tech (AI, Cloud), taking certifications, participating in coding challenges, and building side projects.",
            "Continuous Learning"
        ),
        create_hr_question(
            "Describe a situation where you had to explain a complex technical bug to a non-technical project lead or business client.",
            "Explain: Using simple analogies, focusing on business impact rather than jargon, and presenting clear actionable solutions.",
            "Communication Skills"
        ),
        create_hr_question(
            "Do you have any questions for Cognizant regarding our GenC training tracks, project assignments, or corporate culture?",
            "Candidate asks about Cognizant Academy training, domain exposure (healthcare, BFSI), or continuous higher education sponsorship.",
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
# 9. CAPGEMINI
# ==========================================
def build_capgemini_catalog():
    apt_java = [
        create_aptitude_question(
            "Capgemini Pseudocode Analysis: What is the output of the following pseudocode?\nInteger a = 5, b = 10, c = 2\na = (a + b) / c\nIf (a > 6)\n    b = a * c\nElse\n    b = a - c\nPrint b",
            ["14", "5", "7", "10"],
            "14",
            "a = (5 + 10) / 2 = 15 / 2 = 7 (integer division). Condition (a > 6) evaluates to (7 > 6) which is True. b = a * c = 7 * 2 = 14.",
            "Medium", "Capgemini Pseudocode Analysis"
        ),
        create_aptitude_question(
            "Capgemini Game-Based Logic: In a grid path puzzle, a delivery token moves from (0,0) to (3,3). If cell (1,1) and cell (2,2) are blocked obstacles, how many valid shortest paths exist moving only Right and Down?",
            ["10 paths", "12 paths", "8 paths", "14 paths"],
            "10 paths",
            "Total unconstrained paths = C(6,3) = 20. Paths through (1,1) = C(2,1) * C(4,2) = 2 * 6 = 12. Subtracting blocked paths and accounting for overlap leaves 10 valid paths.",
            "Hard", "Capgemini Game Logic"
        ),
        create_aptitude_question(
            "A software license at Capgemini is purchased for Rs. 24,000. It depreciates in value by 10% in the first year and 15% in the second year. What is its value at the end of 2 years?",
            ["Rs. 18,360", "Rs. 18,000", "Rs. 19,200", "Rs. 17,500"],
            "Rs. 18,360",
            "Year 1 value = 24,000 * 0.90 = 21,600. Year 2 value = 21,600 * 0.85 = Rs. 18,360.",
            "Medium", "Capgemini Financial Arithmetic"
        ),
        create_aptitude_question(
            "Find the next number in the Capgemini series: 3, 7, 15, 31, 63, ___?",
            ["127", "128", "125", "131"],
            "127",
            "Pattern: Each term is (2 * previous) + 1: 3*2+1=7, 7*2+1=15, 15*2+1=31, 31*2+1=63. Next is 63*2+1 = 127.",
            "Easy", "Capgemini Number Series"
        ),
        create_aptitude_question(
            "Capgemini Pseudocode: What is the output of the bitwise code?\nInteger x = 9, y = 5\nInteger z = (x & y) + (x | y)\nPrint z",
            ["14", "13", "15", "12"],
            "14",
            "Mathematical identity for any integers: (x & y) + (x | y) = x + y. Here x + y = 9 + 5 = 14.",
            "Medium", "Capgemini Bitwise Pseudocode"
        ),
        create_aptitude_question(
            "A person completes a project in 18 days working 8 hours a day. In how many days can the same project be completed working 6 hours a day at the same pace?",
            ["24 days", "20 days", "22 days", "25 days"],
            "24 days",
            "Total man-hours = 18 * 8 = 144 hours. At 6 hours/day: days = 144 / 6 = 24 days.",
            "Easy", "Capgemini Time & Work"
        ),
        create_aptitude_question(
            "Capgemini English: Select the word that correctly replaces the phrase: 'A person who is able to use both hands with equal skill.'",
            ["Ambidextrous", "Ambivalent", "Ambiguous", "Omnipotent"],
            "Ambidextrous",
            "'Ambidextrous' is the exact vocabulary term for someone capable of using the right and left hand equally well.",
            "Easy", "Capgemini English Ability"
        ),
        create_aptitude_question(
            "If 5 programmers can test 5 modules in 5 minutes, how many minutes will 100 programmers take to test 100 modules?",
            ["5 minutes", "100 minutes", "50 minutes", "1 minute"],
            "5 minutes",
            "1 programmer tests 1 module in 5 minutes. Therefore, 100 programmers testing 100 modules simultaneously take exactly 5 minutes.",
            "Medium", "Capgemini Analytical Riddles"
        ),
        create_aptitude_question(
            "A car covers a distance of 450 km in 6 hours. If its speed is increased by 25 km/h, how much time will it take to cover the same distance?",
            ["4.5 hours", "4.0 hours", "5.0 hours", "3.5 hours"],
            "4.5 hours",
            "Initial speed = 450 / 6 = 75 km/h. Increased speed = 75 + 25 = 100 km/h. Time taken = 450 / 100 = 4.5 hours.",
            "Easy", "Capgemini Speed & Distance"
        ),
        create_aptitude_question(
            "In how many ways can 6 books on software engineering be arranged on a bookshelf?",
            ["720 ways", "120 ways", "360 ways", "540 ways"],
            "720 ways",
            "Permutations of 6 items = 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720 ways.",
            "Easy", "Capgemini Combinatorics"
        ),
        create_aptitude_question(
            "Capgemini Deductive Logic: Statements: Some consultants are coders. All coders are innovators. Conclusions: I. Some innovators are coders. II. Some consultants are innovators.",
            ["Both conclusions I and II follow", "Only conclusion I follows", "Only conclusion II follows", "Neither follows"],
            "Both conclusions I and II follow",
            "Since all coders are innovators, the conversion 'Some innovators are coders' is valid (I). Since some consultants are coders, those consultants are innovators (II). Both follow.",
            "Medium", "Capgemini Deductive Logic"
        ),
        create_aptitude_question(
            "A sum invested at simple interest triples itself in 10 years. What is the rate of interest per annum?",
            ["20%", "25%", "15%", "30%"],
            "20%",
            "If principal is P, amount is 3P, so SI = 2P. 2P = (P * R * 10)/100 => 2 = R / 10 => R = 20% per annum.",
            "Medium", "Capgemini Interest Math"
        ),
        create_aptitude_question(
            "What is the probability of drawing an Ace or a King from a well-shuffled standard deck of 52 cards?",
            ["2/13", "1/13", "4/13", "1/26"],
            "2/13",
            "Number of Aces = 4, Kings = 4. Total favorable cards = 8. Probability = 8 / 52 = 2/13.",
            "Easy", "Capgemini Probability"
        ),
        create_aptitude_question(
            "Capgemini Pseudocode: What is the return value of mystery(3, 4)?\nFunction mystery(a, b)\n    If b == 0 return 1\n    Return a * mystery(a, b - 1)",
            ["81", "12", "64", "27"],
            "81",
            "This is recursive exponentiation: mystery(3, 4) calculates 3^4 = 81.",
            "Medium", "Capgemini Recursive Pseudocode"
        ),
        create_aptitude_question(
            "A rectangular server room has length 20 meters and breadth 15 meters. What is the length of the longest cable that can be laid straight across the floor?",
            ["25 meters", "30 meters", "22 meters", "28 meters"],
            "25 meters",
            "Diagonal = sqrt(20^2 + 15^2) = sqrt(400 + 225) = sqrt(625) = 25 meters.",
            "Easy", "Capgemini Mensuration"
        )
    ]

    code_java = [
        create_coding_problem(
            "Array Equilibrium Index (Capgemini Exceller)",
            "Given an array of integers arr, find the equilibrium index. An equilibrium index is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. Return -1 if no such index exists.",
            "arr = [-7, 1, 5, 2, -4, 3, 0]",
            "3 (arr[3] = 2; sum before = -1, sum after = -1)",
            "public class Solution {\n    public static int findEquilibrium(int[] arr) {\n        return -1;\n    }\n}",
            "def find_equilibrium(arr: list[int]) -> int:\n    pass",
            "def find_load_balancer_pivot(metrics_df) -> int:\n    pass",
            "Capgemini standard: Compute total sum first; traverse maintaining left_sum; right_sum = total - left_sum - arr[i]. O(N) time and O(1) space.",
            "Easy", "Prefix Sum & Arrays", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Substring Presence Verification without Built-ins",
            "Given two strings text and pattern, return the first index where pattern occurs in text, or -1 if pattern is not part of text. Do not use library indexOf functions.",
            'text = "capgeminidigital", pattern = "gemini"',
            "3",
            "public class Solution {\n    public static int strStrCustom(String text, String pattern) {\n        return -1;\n    }\n}",
            "def str_str_custom(text: str, pattern: str) -> int:\n    pass",
            "def search_log_pattern(log_series, pattern: str) -> int:\n    pass",
            "Sliding window pattern matching: Compare pattern of length M with substrings of text of length N in O(N*M) or KMP O(N+M).",
            "Medium", "String Matching", "O(N * M)", "O(1)"
        ),
        create_coding_problem(
            "Count Elements Greater than All Prior Neighbors",
            "Given an array of integers, count the number of elements that are strictly greater than all previous elements in the array.",
            "arr = [7, 4, 8, 2, 9]",
            "3 (Elements 7, 8, and 9)",
            "public class Solution {\n    public static int countGreaterElements(int[] arr) {\n        return 0;\n    }\n}",
            "def count_greater_elements(arr: list[int]) -> int:\n    pass",
            "def count_record_high_metrics(series_df) -> int:\n    pass",
            "Single pass keeping track of max_so_far. Increment counter whenever arr[i] > max_so_far.",
            "Easy", "Array Scanning", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Maximum Consecutive 1's in Binary Array",
            "Given a binary array nums, return the maximum number of consecutive 1's in the array.",
            "nums = [1,1,0,1,1,1]",
            "3",
            "public class Solution {\n    public int findMaxConsecutiveOnes(int[] nums) {\n        return 0;\n    }\n}",
            "def find_max_consecutive_ones(nums: list[int]) -> int:\n    pass",
            "def max_continuous_uptime_epochs(series_df) -> int:\n    pass",
            "Iterate through array maintaining current_count of 1s, reset on 0, update max_count.",
            "Easy", "Array & Counting", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Missing Number in Arithmetic Progression",
            "An Arithmetic Progression is an array where the difference between any two consecutive elements is the same. Given an array that represents an AP with exactly one element missing, find the missing element.",
            "arr = [2, 4, 8, 10]",
            "6",
            "public class Solution {\n    public static int findMissingAP(int[] arr) {\n        return 0;\n    }\n}",
            "def find_missing_ap(arr: list[int]) -> int:\n    pass",
            "def interpolate_missing_telemetry_step(series_df) -> int:\n    pass",
            "Compute common difference d = (arr[n-1] - arr[0]) / n. Scan array to find where arr[i] - arr[i-1] != d.",
            "Easy", "Math & AP", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Power of Two Bitwise Check",
            "Given an integer n, return true if it is a power of two. An integer n is a power of two if there exists an integer x such that n == 2^x.",
            "n = 16",
            "true",
            "public class Solution {\n    public boolean isPowerOfTwo(int n) {\n        return false;\n    }\n}",
            "def is_power_of_two(n: int) -> bool:\n    pass",
            "def verify_power_of_two_buffer(n: int) -> bool:\n    pass",
            "Bitwise trick: n > 0 && (n & (n - 1)) == 0. A power of two has exactly one set bit.",
            "Easy", "Bit Manipulation", "O(1)", "O(1)"
        ),
        create_coding_problem(
            "Count Vowels and Consonants in a String",
            "Given a string s consisting of alphabetic characters and spaces, return an array of length 2 where index 0 contains the count of vowels and index 1 contains the count of consonants.",
            's = "Capgemini Exceller"',
            "[6, 11]",
            "public class Solution {\n    public static int[] countVowelsConsonants(String s) {\n        return new int[]{0, 0};\n    }\n}",
            "def count_vowels_consonants(s: str) -> list[int]:\n    pass",
            "def audit_character_distribution(text_series) -> list[int]:\n    pass",
            "Normalize to lowercase; check against set of vowels ('a','e','i','o','u') vs alphabetic consonants.",
            "Easy", "String Processing", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Bubble Sort Swap Count",
            "Given an integer array, compute the total number of element swaps required to sort the array in ascending order using the standard Bubble Sort algorithm.",
            "arr = [4, 3, 2, 1]",
            "6 swaps",
            "public class Solution {\n    public static int countBubbleSwaps(int[] arr) {\n        return 0;\n    }\n}",
            "def count_bubble_swaps(arr: list[int]) -> int:\n    pass",
            "def compute_inversion_swap_metric(series_df) -> int:\n    pass",
            "Simulate standard bubble sort with adjacent element comparison, incrementing swap counter on each swap.",
            "Easy", "Sorting Simulation", "O(N^2)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain Hexagonal Architecture (Ports and Adapters) and how Capgemini engineering teams utilize it to decouple business core domain logic from external frameworks and databases.",
            "Hexagonal architecture places application domain logic at the center. Ports define input/output interfaces. Adapters implement concrete infrastructure (REST controller adapter, JPA database adapter), allowing swapping databases or frameworks without touching business logic.",
            "Capgemini Hexagonal Architecture", "Hard"
        ),
        create_technical_question(
            "How do Java 21 Virtual Threads (Project Loom) differ from traditional platform threads, and what is the underlying carrier thread model?",
            "Platform threads wrap heavy 1-to-1 OS threads (~1MB stack). Virtual threads are lightweight user-mode threads managed by JVM (~few KB). When a virtual thread executes blocking I/O, JVM unmounts it from the ForkJoinPool carrier thread, freeing carrier threads for other work.",
            "Capgemini Java 21 & Virtual Threads", "Hard"
        ),
        create_technical_question(
            "Explain the Open-Closed Principle (OCP) in SOLID design. How does the Strategy Design Pattern enforce OCP in Capgemini financial payment services?",
            "Classes should be open for extension, but closed for modification. Strategy pattern defines a PaymentStrategy interface; new payment providers (PayPal, UPI, Card) implement the interface without modifying the core OrderProcessor class.",
            "Capgemini SOLID & Design Patterns", "Medium"
        ),
        create_technical_question(
            "What is the difference between SQL Views, Materialized Views, and Stored Procedures? When should an architect avoid business logic in stored procedures?",
            "Views are saved queries executed on demand. Materialized views persist query results on disk. Stored procedures run procedural code in DB engine. Putting business logic in procedures creates vendor lock-in, poor version control, and difficulties in unit testing.",
            "Capgemini Database Architecture", "Medium"
        ),
        create_technical_question(
            "Explain Maven Dependency Resolution and how transitive dependency conflicts are resolved using the 'Nearest-Wins' rule and Dependency Exclusions.",
            "Maven selects the version nearest to the project root in the dependency tree. If conflicting versions exist at the same depth, first declared wins. Developers override using <exclusions> or <dependencyManagement>.",
            "Capgemini Build & Dependency Management", "Medium"
        ),
        create_technical_question(
            "How do you implement Distributed Caching with Redis in Spring Boot using the @Cacheable, @CachePut, and @CacheEvict annotations?",
            "@Cacheable checks Redis cache before method execution. @CachePut updates cache with method return value. @CacheEvict purges stale cache entries on database updates.",
            "Capgemini Caching & Redis", "Medium"
        ),
        create_technical_question(
            "Explain Microservices Contract Testing using Pact. How does Consumer-Driven Contract testing prevent breaking changes between frontend and backend squads?",
            "Consumer tests generate a JSON contract (Pact file) specifying expected request and response structures. Provider runs tests verifying that its real endpoints fulfill the contract before deploying.",
            "Capgemini Contract Testing & Pact", "Hard"
        ),
        create_technical_question(
            "How does the Spring Security Filter Chain process incoming HTTP requests, and how do you customize security rules using SecurityFilterChain bean in modern Spring Boot 3?",
            "Requests pass through a chain of filters (SecurityContextHolderFilter, CsrfFilter, UsernamePasswordAuthenticationFilter). SecurityFilterChain bean configures http.authorizeHttpRequests() and http.oauth2ResourceServer() cleanly using lambda DSL.",
            "Capgemini Spring Security", "Medium"
        ),
        create_technical_question(
            "What is Cursor-Based Pagination versus Offset-Based Pagination in RESTful APIs? Why is cursor pagination preferred for large dataset streaming?",
            "Offset pagination (OFFSET 10000 LIMIT 20) requires the DB to scan and discard 10,000 rows. Cursor pagination (WHERE id > 10000 LIMIT 20) utilizes indexed B-Trees for O(1) page access and immune to record insertions.",
            "Capgemini API Performance", "Medium"
        ),
        create_technical_question(
            "How do SonarQube code quality gates enforce Cyclomatic Complexity, Code Smells, and Test Coverage metrics in Capgemini deployment pipelines?",
            "SonarQube static analysis computes cyclomatic complexity based on decision points (if/for/switch). Quality gates automatically fail CI builds if code coverage < 80% or new blocker vulnerabilities are introduced.",
            "Capgemini Code Quality & SonarQube", "Easy"
        ),
        create_technical_question(
            "Explain the difference between Optimistic Concurrency Control and Pessimistic Concurrency Control in enterprise ERP systems.",
            "Optimistic concurrency control assumes conflicts are rare, checking a version column on save. Pessimistic concurrency control locks rows at the database level (SELECT FOR UPDATE) preventing any concurrent modification.",
            "Capgemini Concurrency & ERP", "Medium"
        ),
        create_technical_question(
            "How does Java Garbage Collection work with G1GC (Garbage First Collector), and what does the 'Humongous Allocation' threshold mean?",
            "G1GC divides heap into equal regions (1MB-32MB). Any object larger than 50% of a region size is classified as a Humongous Object, allocated directly in contiguous Old Gen regions, requiring special handling.",
            "Capgemini Java Runtime Tuning", "Hard"
        ),
        create_technical_question(
            "Explain the Event Sourcing pattern and how it differs from traditional CRUD state storage in audit-sensitive enterprise applications.",
            "CRUD stores only the current state of an entity. Event Sourcing stores an immutable, append-only log of every domain event that ever occurred, rebuilding current state by replaying events.",
            "Capgemini Architecture Patterns", "Hard"
        ),
        create_technical_question(
            "How do you secure containerized microservices running on Docker by enforcing Non-Root Users, Read-Only Root Filesystems, and dropping Linux capabilities?",
            "Define 'USER appuser' in Dockerfile; run with '--read-only' flag mounting temporary writes to tmpfs; drop all default Linux capabilities with '--cap-drop=ALL' and add only required capabilities.",
            "Capgemini Container Security", "Medium"
        ),
        create_technical_question(
            "What is the difference between Fail-Fast and Fail-Safe iterators in Java Collections framework?",
            "Fail-Fast iterators (ArrayList, HashMap) throw ConcurrentModificationException if the collection is structurally modified during iteration. Fail-Safe iterators (CopyOnWriteArrayList) operate on a clone, tolerating modifications.",
            "Capgemini Java Collections", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How does Capgemini's Generative AI delivery practice accelerate custom software engineering across the software development lifecycle (SDLC)?",
            "Discuss: AI-assisted requirements drafting, architecture diagram synthesis, code generation, automated regression testing, and code documentation.",
            "Capgemini GenAI for SDLC"
        ),
        create_ai_question(
            "Explain how Ethical AI frameworks at Capgemini evaluate AI systems against bias, environmental sustainability (Green IT), and regulatory standards.",
            "Cover: Carbon footprint evaluation of LLM training, algorithmic fairness audits, transparent explanations, and human-in-the-loop accountability.",
            "Capgemini Ethical & Green AI"
        ),
        create_ai_question(
            "How do you design a RAG architecture to support multilingual technical documentation queries for Capgemini European automotive clients?",
            "Detail: Multilingual embedding models (e.g. text-embedding-3 or Cohere multilingual), cross-lingual vector search, and language-preserving prompt generation.",
            "Capgemini Multilingual RAG"
        ),
        create_ai_question(
            "Describe how AI computer vision models are deployed on edge IoT devices for automated visual defect inspection in manufacturing assembly plants.",
            "Architecture: High-speed camera captures product images, lightweight YOLO/MobileNet model on edge device (Nvidia Jetson) classifies defects in < 50ms, triggering pneumatic sorting.",
            "Capgemini Edge Computer Vision"
        ),
        create_ai_question(
            "How do you evaluate and benchmark LLM response quality using LLM-as-a-Judge techniques with automated scoring rubrics at Capgemini?",
            "Explain: Defining specific criteria (correctness, conciseness, safety), prompting an advanced model with few-shot examples, and checking correlation with human experts.",
            "Capgemini LLM Evaluation"
        ),
        create_ai_question(
            "How do you secure proprietary enterprise IP when integrating developer AI coding assistants into Capgemini client project repositories?",
            "Discuss: Enforcing zero-retention enterprise licenses, prohibiting training on client code, automated scanning for leaked secrets, and strict access controls.",
            "Capgemini AI IP Security"
        ),
        create_ai_question(
            "Describe how Generative AI can assist in synthesizing realistic test data for enterprise integration testing without exposing real patient/customer PII.",
            "Detail: Statistical distribution modeling, generative adversarial networks (GANs) or LLMs generating synthetic records adhering to relational database foreign key constraints.",
            "Capgemini Synthetic Data Generation"
        ),
        create_ai_question(
            "How do you design an AI agent workflow using LangGraph or AutoGen where multiple specialized agents collaborate on code refactoring?",
            "Structure: Analyzer agent identifies code smells, Refactor agent proposes modern Java code, Tester agent executes unit tests, and Reviewer agent validates adherence to standards.",
            "Capgemini Multi-Agent Systems"
        ),
        create_ai_question(
            "What strategies do you use to reduce token costs and inference latency for enterprise conversational AI applications handling 100,000+ daily sessions?",
            "Discuss: Semantic caching of frequent responses, prompt compression, utilizing Small Language Models (SLMs) for routing, and response streaming.",
            "Capgemini AI Economics"
        ),
        create_ai_question(
            "How does Capgemini prepare employees for the future of AI through the Capgemini University learning programs?",
            "Cover: Capgemini University certifications, prompt engineering bootcamps, responsible AI governance workshops, and hands-on client innovation labs.",
            "Capgemini AI Education"
        )
    ]

    hr_java = [
        create_hr_question(
            "Capgemini is guided by 7 Core Values: Honesty, Boldness, Trust, Freedom, Fun, Modesty, and Team Spirit. Which of these values has influenced your engineering career most?",
            "Select one value (e.g. Boldness, Team Spirit, or Honesty), illustrate with a concrete academic or project example, and connect it to your professional growth.",
            "Capgemini 7 Core Values"
        ),
        create_hr_question(
            "Why do you specifically choose Capgemini for your professional journey in technology consulting?",
            "Highlight: Capgemini's strong European engineering heritage, global innovation focus, commitment to sustainability, and collaborative multicultural work environment.",
            "Capgemini Brand Motivation"
        ),
        create_hr_question(
            "Capgemini has major development centers across India (Mumbai, Pune, Bangalore, Hyderabad, Chennai, Kolkata). Are you fully flexible with relocation and project assignments?",
            "Affirm: Complete willingness to relocate, readiness to adapt to client project schedules, and enthusiasm for collaborating with international squads.",
            "Relocation & Project Flexibility"
        ),
        create_hr_question(
            "Tell me about a time you demonstrated 'Boldness' by proposing an unconventional or innovative solution to solve a complex software challenge.",
            "Use STAR: Outline the traditional barrier, the bold innovative approach you proposed, how you convinced peers with data, and the successful outcome.",
            "Value: Boldness & Innovation"
        ),
        create_hr_question(
            "How do you handle working in an agile project where requirements change unexpectedly right before a major sprint delivery?",
            "Showcase: Emotional stability, prioritizing customer requirements, collaborating with the scrum master, and adapting sprint deliverables pragmatically.",
            "Agility & Adaptability"
        ),
        create_hr_question(
            "Describe a time you received constructive feedback during a technical code review that required significant refactoring. How did you react?",
            "Emphasize: Modesty, gratitude for quality insights, separating personal ego from code quality, and implementing robust improvements.",
            "Value: Modesty & Receptivity"
        ),
        create_hr_question(
            "Tell me about a project where 'Team Spirit' was essential to overcoming an aggressive deadline or technical failure.",
            "Highlight: Mutual support, pair programming, helping a struggling teammate unblock their module, and celebrating success as one cohesive team.",
            "Value: Team Spirit"
        ),
        create_hr_question(
            "Where do you see yourself progressing at Capgemini over the next 3 to 5 years as a software engineer?",
            "Connect: Aspiring to grow from Software Engineer to Senior Software Engineer / Consultant, earning architectural certifications, and mentoring juniors.",
            "Career Aspirations"
        ),
        create_hr_question(
            "How do you maintain high personal ethics and 'Honesty' when reporting project progress or encountering software defects?",
            "Demonstrate: Transparent status reporting, never hiding known bugs, and communicating issues early so the team can address them collectively.",
            "Value: Honesty & Integrity"
        ),
        create_hr_question(
            "Do you have any questions for Capgemini leadership regarding our digital practices, campus onboarding, or learning culture?",
            "Candidate asks about Capgemini Exceller development programs, opportunities to contribute to sustainability initiatives, or international projects.",
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
# 10. DELOITTE
# ==========================================
def build_deloitte_catalog():
    apt_java = [
        create_aptitude_question(
            "In Deloitte USI Quantitative Aptitude: An enterprise advisory client generates a quarterly revenue of $4.8 Million with a profit margin of 15%. If operating expenses increase by 20% while revenue remains constant, what is the new profit margin?",
            ["-2.0% (Operating Loss)", "3.0%", "5.0%", "0.0% (Break-even)"],
            "-2.0% (Operating Loss)",
            "Revenue = $4.8M. Profit = 15% of 4.8M = $0.72M. Operating Expenses = 4.8M - 0.72M = $4.08M. Increased expenses = 4.08M * 1.20 = $4.896M. New profit = 4.8M - 4.896M = -$0.096M (Loss of 2.0%).",
            "Hard", "Deloitte Financial Quant"
        ),
        create_aptitude_question(
            "Deloitte Data Interpretation: A client's risk assessment index score decreases from 80 to 60 over two quarters. What is the percentage decrease in the risk index score?",
            ["25.0%", "20.0%", "33.3%", "15.0%"],
            "25.0%",
            "Percentage decrease = (Decrease / Original) * 100 = ((80 - 60) / 80) * 100 = (20 / 80) * 100 = 25.0%.",
            "Easy", "Deloitte Data Interpretation"
        ),
        create_aptitude_question(
            "A consulting team of 4 senior consultants and 6 analysts can complete an audit engagement in 10 days. If a senior consultant is twice as productive as an analyst, how many days will 8 analysts take alone?",
            ["17.5 days", "15.0 days", "20.0 days", "12.5 days"],
            "17.5 days",
            "1 Senior = 2 Analysts. Team = 4*2 + 6 = 14 Analysts. Work = 14 * 10 = 140 Analyst-days. Time for 8 analysts = 140 / 8 = 17.5 days.",
            "Medium", "Deloitte Work & Time"
        ),
        create_aptitude_question(
            "Deloitte Logical Deduction: Statements: All audit reports are legal documents. No legal document is an informal memo. Conclusions: I. No audit report is an informal memo. II. Some legal documents are audit reports.",
            ["Both conclusions I and II follow", "Only conclusion I follows", "Only conclusion II follows", "Neither conclusion follows"],
            "Both conclusions I and II follow",
            "Since audit reports are a subset of legal documents, and no legal document is an informal memo, conclusion I follows unconditionally. Conversion of Statement 1 yields conclusion II.",
            "Medium", "Deloitte Logical Reasoning"
        ),
        create_aptitude_question(
            "In how many ways can 5 advisory project proposals be ranked from 1st to 5th place with no ties?",
            ["120 ways", "60 ways", "24 ways", "720 ways"],
            "120 ways",
            "Number of permutations of 5 distinct items = 5! = 5 * 4 * 3 * 2 * 1 = 120 ways.",
            "Easy", "Deloitte Combinatorics"
        ),
        create_aptitude_question(
            "An enterprise software subscription costs $120,000 annually. If the vendor offers a 5% discount for upfront annual payment, how much money does the client save?",
            ["$6,000", "$5,000", "$12,000", "$8,000"],
            "$6,000",
            "Savings = 5% of $120,000 = 0.05 * 120,000 = $6,000.",
            "Easy", "Deloitte Commercial Math"
        ),
        create_aptitude_question(
            "Deloitte Verbal Ability: Identify the word that means 'to officially free from blame or responsibility in an audit':",
            ["Exonerate", "Inculpate", "Indict", "Admonish"],
            "Exonerate",
            "'Exonerate' means to officially absolve someone from blame for a fault or wrongdoing.",
            "Medium", "Deloitte Professional Vocabulary"
        ),
        create_aptitude_question(
            "In an investment portfolio, the ratio of stocks to bonds to cash is 5:3:2. If total portfolio value is $500,000, what is the value of the bond allocation?",
            ["$150,000", "$250,000", "$100,000", "$200,000"],
            "$150,000",
            "Total parts = 5 + 3 + 2 = 10 parts. 1 part = $500,000 / 10 = $50,000. Bond allocation (3 parts) = 3 * $50,000 = $150,000.",
            "Easy", "Deloitte Financial Ratio"
        ),
        create_aptitude_question(
            "Find the next number in the business analytics sequence: 10, 22, 46, 94, 190, ___?",
            ["382", "380", "384", "378"],
            "382",
            "Each term is multiplied by 2 and plus 2: 10*2+2=22, 22*2+2=46, 46*2+2=94, 94*2+2=190. Next number = 190*2+2 = 382.",
            "Easy", "Deloitte Number Series"
        ),
        create_aptitude_question(
            "Two risk analysts, X and Y, evaluate 100 credit applications. X evaluates at 10 apps/hour and Y at 15 apps/hour. If they work together, how long will they take to evaluate all 100 applications?",
            ["4.0 hours", "4.5 hours", "5.0 hours", "3.5 hours"],
            "4.0 hours",
            "Combined rate = 10 + 15 = 25 applications/hour. Time required = 100 / 25 = 4.0 hours.",
            "Easy", "Deloitte Rate Equation"
        ),
        create_aptitude_question(
            "A tax compliance audit sample of 200 corporate returns discovers that 14 returns contained calculation errors. What is the error rate percentage?",
            ["7.0%", "14.0%", "3.5%", "8.0%"],
            "7.0%",
            "Error rate = (14 / 200) * 100 = 7.0%.",
            "Easy", "Deloitte Percentage"
        ),
        create_aptitude_question(
            "Deloitte Data Sufficiency: What is the annual revenue of Company Z? Statement 1: Operating profit is $200,000. Statement 2: Operating profit margin is 20%.",
            ["Both statements TOGETHER are sufficient, but neither alone is sufficient", "Statement 1 alone is sufficient", "Statement 2 alone is sufficient", "Statements together are NOT sufficient"],
            "Both statements TOGETHER are sufficient, but neither alone is sufficient",
            "Revenue = Operating Profit / Margin. Statement 1 gives profit ($200K) and Statement 2 gives margin (20%). Revenue = $200,000 / 0.20 = $1,000,000. Both together are required.",
            "Medium", "Deloitte Data Sufficiency"
        ),
        create_aptitude_question(
            "A client portfolio is diversified into 3 funds with returns of 8%, 12%, and 15% weighted at 50%, 30%, and 20% respectively. What is the portfolio's weighted average return?",
            ["10.6%", "11.0%", "10.0%", "11.5%"],
            "10.6%",
            "Weighted return = (0.50 * 8%) + (0.30 * 12%) + (0.20 * 15%) = 4.0% + 3.6% + 3.0% = 10.6%.",
            "Medium", "Deloitte Weighted Average"
        ),
        create_aptitude_question(
            "What is the probability that a leap year selected at random contains 53 Sundays?",
            ["2/7", "1/7", "3/7", "5/7"],
            "2/7",
            "A leap year has 366 days = 52 weeks and 2 odd days. The two consecutive odd days can be (Sat,Sun) or (Sun,Mon), giving 2 favorable outcomes out of 7 possible pairs. Probability = 2/7.",
            "Medium", "Deloitte Probability"
        ),
        create_aptitude_question(
            "Deloitte Syllogisms: Statements: 1. All managers are leaders. 2. Some leaders are visionaries. Conclusions: I. Some managers are visionaries. II. All leaders are managers.",
            ["Neither I nor II follows", "Only I follows", "Only II follows", "Both I and II follow"],
            "Neither I nor II follows",
            "Managers are a subset of leaders; visionaries intersect leaders. We cannot ascertain if visionaries intersect managers (I). All managers are leaders does not imply all leaders are managers (II). Neither follows.",
            "Medium", "Deloitte Logical Syllogisms"
        )
    ]

    code_java = [
        create_coding_problem(
            "String Tokenization & Delimiter Sanitization",
            "Given a raw CSV input string with mixed delimiters (commas, semicolons, pipes) and potential trailing whitespace, parse and clean the tokens into an ordered list of sanitized strings.",
            'input = "AAPL, MSFT; GOOG | AMZN ; TSLA"',
            '["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]',
            "public class Solution {\n    public static List<String> sanitizeTokens(String input) {\n        return new ArrayList<>();\n    }\n}",
            "def sanitize_tokens(input_str: str) -> list[str]:\n    pass",
            "def clean_financial_feed_delimiters(feed_series) -> list[str]:\n    pass",
            "Deloitte USI standard: Regex split on pattern '[,;|]', trim whitespace from each token, and filter out empty tokens in O(N).",
            "Easy", "String Sanitization", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Rolling Moving Average of Financial Stream",
            "Given a stream of integers and a window size k, calculate the moving average of all integers in the sliding window.",
            "k = 3, stream = [1, 10, 3, 5]",
            "[1.0, 5.5, 4.67, 6.0]",
            "public class MovingAverage {\n    public MovingAverage(int size) {\n    }\n    public double next(int val) {\n        return 0.0;\n    }\n}",
            "class MovingAverage:\n    def __init__(self, size: int):\n        pass\n    def next(self, val: int) -> float:\n        return 0.0",
            "def compute_rolling_revenue_mean(revenue_series, window: int):\n    pass",
            "Maintain a Queue of size k and a running window_sum. Add new value, subtract evicted oldest value in O(1) time.",
            "Easy", "Design & Queue", "O(1)", "O(K)"
        ),
        create_coding_problem(
            "Missing Transaction Sequence Number Finder",
            "Given an array containing n distinct transaction IDs taken from 0, 1, 2, ..., n, find the one that is missing from the array in O(N) time and O(1) space.",
            "nums = [3,0,1]",
            "2",
            "public class Solution {\n    public int missingNumber(int[] nums) {\n        return 0;\n    }\n}",
            "def missing_number(nums: list[int]) -> int:\n    pass",
            "def find_omitted_audit_sequence(seq_df) -> int:\n    pass",
            "Use Gauss sum formula: expected_sum = n * (n + 1) / 2. Missing number = expected_sum - actual_sum, or XOR all elements.",
            "Easy", "Bit Manipulation & Math", "O(N)", "O(1)"
        ),
        create_coding_problem(
            "Detect Duplicate Orders in Audit Stream",
            "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
            "nums = [1,2,3,1]",
            "true",
            "public class Solution {\n    public boolean containsDuplicate(int[] nums) {\n        return false;\n    }\n}",
            "def contains_duplicate(nums: list[int]) -> bool:\n    pass",
            "def flag_duplicate_invoices(invoice_series) -> bool:\n    pass",
            "Insert elements into a Hash Set; return true immediately if set.add() returns false or element exists.",
            "Easy", "Hash Set", "O(N)", "O(N)"
        ),
        create_coding_problem(
            "Matrix Border Sum (Financial Heatmap)",
            "Given an M x N matrix of financial ledger figures, calculate the sum of all elements located on the outer border of the matrix.",
            "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
            "40 (1+2+3+6+9+8+7+4)",
            "public class Solution {\n    public static int borderSum(int[][] matrix) {\n        return 0;\n    }\n}",
            "def border_sum(matrix: list[list[int]]) -> int:\n    pass",
            "def sum_perimeter_ledger_cells(matrix_df) -> int:\n    pass",
            "Sum top row, bottom row, left column, right column without double-counting corners.",
            "Easy", "Matrix Operations", "O(M + N)", "O(1)"
        ),
        create_coding_problem(
            "Top K Frequent Client Accounts",
            "Given an integer array nums representing account interaction events and an integer k, return the k most frequent elements in O(N log K) time.",
            "nums = [1,1,1,2,2,3], k = 2",
            "[1,2]",
            "public class Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        return new int[0];\n    }\n}",
            "def top_k_frequent(nums: list[int], k: int) -> list[int]:\n    pass",
            "def extract_top_transacting_clients(tx_df, k: int):\n    pass",
            "Count frequencies using HashMap; maintain a Min-Heap of size k comparing entry values, or use Bucket Sort.",
            "Medium", "Heap / Bucket Sort", "O(N log K)", "O(N)"
        ),
        create_coding_problem(
            "Group Anagrams (Entity Resolution)",
            "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
            'strs = ["eat","tea","tan","ate","nat","bat"]',
            '[["bat"],["nat","tan"],["ate","eat","tea"]]',
            "public class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        return new ArrayList<>();\n    }\n}",
            "def group_anagrams(strs: list[str]) -> list[list[str]]:\n    pass",
            "def cluster_matching_entity_aliases(aliases_df):\n    pass",
            "Sort character array of each string as canonical key in HashMap<String, List<String>>, appending matching strings.",
            "Medium", "Hash Map & String", "O(N * K log K)", "O(N * K)"
        ),
        create_coding_problem(
            "Stock Buy and Sell for Maximum Profit",
            "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy and a different day in the future to sell.",
            "prices = [7,1,5,3,6,4]",
            "5 (Buy at 1, sell at 6)",
            "public class Solution {\n    public int maxProfit(int[] prices) {\n        return 0;\n    }\n}",
            "def max_profit(prices: list[int]) -> int:\n    pass",
            "def calculate_maximum_arbitrage_spread(price_df) -> int:\n    pass",
            "Track min_price seen so far; compute current profit = price - min_price; update max_profit in O(N).",
            "Easy", "Array & Dynamic Programming", "O(N)", "O(1)"
        )
    ]

    tech_java = [
        create_technical_question(
            "Explain Enterprise Data Warehouse Architecture: Star Schema vs Snowflake Schema. When should a Deloitte advisory data engineer adopt Snowflake over Star schema?",
            "Star schema has denormalized dimension tables directly linked to a central fact table (faster query performance, simpler joins). Snowflake schema normalizes dimension tables into sub-dimensions, reducing data redundancy at the expense of complex multi-table joins.",
            "Deloitte Data Warehouse Architecture", "Medium"
        ),
        create_technical_question(
            "How do you implement Sarbanes-Oxley (SOX) Compliance and automated audit trails in enterprise financial software backends?",
            "Ensure strict separation of duties (SoD), immutable append-only audit log tables recording who/what/when/prior-value, cryptographic hashing of audit entries, and restricting production DB write access.",
            "Deloitte SOX Compliance & Audit Security", "Hard"
        ),
        create_technical_question(
            "Explain SQL Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), and NTILE(). How do you compute quartiles on transaction data?",
            "ROW_NUMBER assigns consecutive numbers; RANK leaves gaps upon ties; DENSE_RANK assigns consecutive numbers without gaps. NTILE(4) divides ordered rows into 4 equal quartiles.",
            "Deloitte SQL Analytical Functions", "Medium"
        ),
        create_technical_question(
            "How does Snowflake Cloud Data Platform separate Compute (Virtual Warehouses) from Storage, and how does Zero-Copy Cloning accelerate development testing?",
            "Snowflake stores micro-partitions centrally in cloud blob storage. Virtual Warehouses scale compute independently without repartitioning. Zero-Copy Cloning creates metadata pointers to existing partitions without duplicating storage costs.",
            "Deloitte Snowflake Architecture", "Hard"
        ),
        create_technical_question(
            "Explain Database Transaction Isolation Levels and how they prevent Dirty Reads, Non-Repeatable Reads, and Phantom Reads in accounting ledgers.",
            "Read Uncommitted permits all anomalies; Read Committed blocks dirty reads; Repeatable Read blocks non-repeatable reads; Serializable blocks phantom reads by acquiring range locks or using snapshot isolation.",
            "Deloitte Financial Database Architecture", "Hard"
        ),
        create_technical_question(
            "How do you design an ETL Pipeline Orchestration system with Apache Airflow using Directed Acyclic Graphs (DAGs), sensors, and automated data quality checks?",
            "Airflow DAGs define dependencies between extraction, transformation, and load tasks. ExternalTaskSensors wait for upstream pipeline completion; Great Expectations tasks assert data quality thresholds before loading to warehouse.",
            "Deloitte ETL & Airflow Orchestration", "Medium"
        ),
        create_technical_question(
            "Explain Role-Based Access Control (RBAC) versus Attribute-Based Access Control (ABAC) in multi-tenant financial reporting portals.",
            "RBAC grants permissions based on static user roles (e.g. Auditor, Manager). ABAC evaluates dynamic attributes (user department, document security clearance, time of day, client IP) for fine-grained authorization.",
            "Deloitte Enterprise Security & Access Control", "Medium"
        ),
        create_technical_question(
            "What technical safeguards are required to comply with GDPR and CCPA regarding the 'Right to be Forgotten' in distributed enterprise databases?",
            "Implement automated data deletion workflows, cryptographic erasure (destroying encryption keys), anonymizing historical financial records while preserving aggregate statistical integrity, and documenting compliance receipts.",
            "Deloitte Data Privacy (GDPR/CCPA)", "Medium"
        ),
        create_technical_question(
            "Explain System Architecture for an Enterprise Risk Calculation Engine handling Monte Carlo simulations across millions of investment portfolios.",
            "Compute cluster (Apache Spark or Ray on Kubernetes) distributes portfolio trials across worker nodes; in-memory distributed caches hold risk parameters; results stream to PostgreSQL / PowerBI dashboards.",
            "Deloitte Risk Analytics Engine", "Hard"
        ),
        create_technical_question(
            "Compare RESTful APIs with GraphQL for enterprise consulting client portals. What are the tradeoffs regarding Over-Fetching and Under-Fetching?",
            "REST returns fixed endpoint schemas (risking over-fetching unused fields or under-fetching requiring multiple round-trips). GraphQL lets clients request exact required fields in a single query, but introduces complex caching challenges.",
            "Deloitte API Architecture", "Medium"
        ),
        create_technical_question(
            "How do you secure Cloud Storage Buckets (AWS S3 / Azure Blob) to prevent data leaks, including bucket policies, KMS encryption, and block public access?",
            "Enable 'Block Public Access' at account and bucket level; enforce default SSE-KMS customer-managed key encryption; require HTTPS (aws:SecureTransport); enable versioning and MFA delete.",
            "Deloitte Cloud Security & S3", "Medium"
        ),
        create_technical_question(
            "Explain Disaster Recovery RPO (Recovery Point Objective) and RTO (Recovery Time Objective) and how they determine multi-region failover strategies.",
            "RPO is maximum tolerable data loss duration (e.g. 5 minutes). RTO is maximum tolerable downtime duration to restore service (e.g. 30 minutes). Low RPO/RTO demands multi-region active-active replication.",
            "Deloitte Business Continuity & DR", "Medium"
        ),
        create_technical_question(
            "How does Apache Spark execute distributed data transformations using Resilient Distributed Datasets (RDDs), Catalyst Optimizer, and Tungsten Execution Engine?",
            "Catalyst compiles DataFrame expressions into optimized physical execution plans (predicate pushdown, projection pruning). Tungsten bypasses JVM object overhead by managing off-heap binary memory.",
            "Deloitte Big Data & Apache Spark", "Hard"
        ),
        create_technical_question(
            "What is the difference between Synchronous API Gateway authentication and Token Introspection in OAuth 2.0 architectures?",
            "Stateless JWT validation checks the cryptographic signature using the auth server's public key (JWKS) locally in O(1). Token Introspection calls the authorization server's endpoint to verify token validity in real-time.",
            "Deloitte API Security & OAuth2", "Medium"
        ),
        create_technical_question(
            "How do you implement Data Lineage and metadata cataloging with tools like Apache Atlas or Collibra in enterprise data governance programs?",
            "Extract operational metadata from ETL pipelines (Airflow, Spark); track upstream and downstream dependencies from source databases through staging to final financial reporting tables.",
            "Deloitte Data Governance & Lineage", "Medium"
        )
    ]

    ai_java = [
        create_ai_question(
            "How does Deloitte apply Generative AI across audit and financial advisory engagements to detect accounting discrepancies and automate compliance verification?",
            "Discuss: Deloitte Omnia audit platform integrating AI for contract analysis, journal entry anomaly detection, sample selection, and variance analysis.",
            "Deloitte AI in Financial Audit"
        ),
        create_ai_question(
            "Describe how you design an automated fraud detection pipeline utilizing machine learning models to analyze millions of corporate expense reports.",
            "Architecture: Feature engineering (out-of-policy weekend spending, duplicate receipt images, vendor risk scores), isolation forest anomaly detection, and automated flagging for forensic auditors.",
            "Deloitte Forensic AI Analytics"
        ),
        create_ai_question(
            "How do you establish an Enterprise AI Governance Framework for client organizations under emerging global regulations (EU AI Act, NIST AI RMF)?",
            "Cover: Risk classification (High/Limited/Minimal risk), model registry inventory, bias and fairness testing, data provenance documentation, and independent model audits.",
            "Deloitte AI Governance & Regulations"
        ),
        create_ai_question(
            "How do you implement Retrieval-Augmented Generation (RAG) for consulting practitioners to search thousands of proprietary industry benchmarks and proposals?",
            "Detail: Chunking consulting whitepapers, dense vector embedding in Azure AI Search, hybrid keyword + semantic retrieval, and strict citation grounding.",
            "Deloitte Knowledge Management RAG"
        ),
        create_ai_question(
            "What methodologies do you use to detect and eliminate algorithmic bias in AI credit scoring and insurance underwriting models for Deloitte banking clients?",
            "Explain: Disparate impact ratio, equalized odds, counterfactual fairness testing, and generating SHAP explainability reports for regulatory review.",
            "Deloitte Model Bias & Fairness"
        ),
        create_ai_question(
            "How do you automate contract review and extraction of legal liability clauses using Large Language Models in M&A (Mergers and Acquisitions) due diligence?",
            "Detail: Document OCR, prompting specialized LLMs with legal rubrics (change of control, indemnity limits), structured extraction into tabular summaries, and attorney sign-off.",
            "Deloitte M&A Legal AI"
        ),
        create_ai_question(
            "How do you evaluate and monitor Generative AI models deployed in enterprise finance to guarantee zero hallucinations in balance sheet reconciliations?",
            "Discuss: Dual-engine deterministic cross-checking, prompt grounding to structured ledger tables, temperature=0, and human auditor review thresholds.",
            "Deloitte Hallucination Prevention in Finance"
        ),
        create_ai_question(
            "Describe how Deloitte engineers use AI code assistants while strictly safeguarding client proprietary algorithms and financial data confidentiality.",
            "Cover: Enterprise-licensed instances with air-gapped data policies, automated secret scanners, zero training on client source code, and code review governance.",
            "Deloitte Developer AI Policy"
        ),
        create_ai_question(
            "How would you build an automated ESG (Environmental, Social, and Governance) disclosure extraction pipeline from unstructured corporate sustainability reports?",
            "Architecture: NLP parsing greenhouse gas emissions (Scope 1, 2, 3), workforce diversity statistics, standardizing against GRI and SASB disclosure frameworks.",
            "Deloitte ESG Analytics AI"
        ),
        create_ai_question(
            "How do you measure and demonstrate Return on Investment (ROI) to C-suite clients implementing enterprise-wide generative AI automation?",
            "Explain: Quantifying hours saved per engagement, reduction in error rates, acceleration of audit cycle time, client satisfaction gains, and compute cost payback period.",
            "Deloitte AI Business Value & ROI"
        )
    ]

    hr_java = [
        create_hr_question(
            "Why do you specifically choose Deloitte USI (Consulting & Advisory) to launch and advance your software engineering career?",
            "Highlight: Deloitte's global prestige, premier business advisory practice, exposure to Fortune 500 strategic transformations, and multidisciplinary learning culture.",
            "Deloitte Brand Motivation"
        ),
        create_hr_question(
            "Deloitte consultants must demonstrate strong 'Executive Presence' and consultative empathy. How do you communicate complex technical decisions to non-technical business leaders?",
            "Focus on: Translating software metrics into financial and operational impact, active listening, using clear analogies, and presenting confident recommendations.",
            "Executive Presence & Communication"
        ),
        create_hr_question(
            "Tell me about a time you had to balance multiple high-priority deliverables with competing deadlines during an intense sprint or academic semester.",
            "Use STAR: Outline prioritization matrix (Urgent vs Important), transparent stakeholder management, disciplined execution, and delivering all commitments.",
            "Prioritization & Time Management"
        ),
        create_hr_question(
            "Deloitte operates delivery offices in Hyderabad, Bangalore, Mumbai, Gurgaon, and client sites worldwide. Are you fully flexible with travel and project relocation?",
            "Affirm: Complete willingness to relocate, readiness to travel to client sites as required, and enthusiasm for collaborating across global teams.",
            "Relocation & Travel Flexibility"
        ),
        create_hr_question(
            "Describe a situation where you discovered a significant flaw or data discrepancy in your project right before a critical stakeholder presentation. How did you react?",
            "Emphasize: Honesty, intellectual integrity, calmly informing the lead, presenting the corrected data transparently, and proposing immediate mitigations.",
            "Integrity & Professional Ethics"
        ),
        create_hr_question(
            "How do you handle collaborating with a team member who has a different working style or is resistant to adopting new software practices?",
            "Demonstrate: Empathy, seeking to understand their underlying concerns, demonstrating value through small prototypes, and fostering mutual respect.",
            "Interpersonal Skills & Adaptability"
        ),
        create_hr_question(
            "Tell me about a time you took the lead on a challenging software initiative without being formally designated as the team leader.",
            "Showcase: Informal leadership, organizing technical tasks, encouraging teammates, taking accountability for blockers, and driving team success.",
            "Leadership & Initiative"
        ),
        create_hr_question(
            "Where do you see yourself progressing at Deloitte over the next 3 to 5 years?",
            "Connect: Growing from Associate Analyst / Analyst to Consultant, leading cloud data architecture implementations, and mentoring campus joiners.",
            "Career Aspirations"
        ),
        create_hr_question(
            "Describe a time you received constructive feedback on an advisory report or code submission. What specific steps did you take to elevate your quality standard?",
            "Show: Professional humility, analyzing the feedback objectively, seeking mentoring, and delivering flawless execution in subsequent engagements.",
            "Continuous Improvement"
        ),
        create_hr_question(
            "Do you have any questions for Deloitte leadership regarding our technology practices, project types, or community impact programs?",
            "Candidate asks about Deloitte USI innovation labs, Green Dot culture, mentorship networks, or client engagement models.",
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

ACCENTURE_DATA = build_accenture_catalog()
WIPRO_DATA = build_wipro_catalog()
COGNIZANT_DATA = build_cognizant_catalog()
CAPGEMINI_DATA = build_capgemini_catalog()
DELOITTE_DATA = build_deloitte_catalog()
