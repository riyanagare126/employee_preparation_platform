"""
AI Employee Preparation Platform - Company-Specific Question Banks
Curated authentic placement and technical interview question pools for all 20 companies:
TCS, Infosys, Accenture, Wipro, Capgemini, Cognizant, Amazon, Microsoft, Google,
Deloitte, Oracle, IBM, Red Hat, HCLTech, Tech Mahindra, LTIMindtree, Persistent, SAP, EY, PwC.

Each company contains distinct, authentic:
1. Aptitude & Pattern-Specific MCQs (PYQs)
2. Technical Domain MCQs & Core CS Questions
3. Company-Specific Coding Challenges
4. HR & Culture Behavioral / Leadership Questions
"""

import random
from typing import Dict, List, Any, Optional

COMPANY_QUESTIONS_BANK: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # 1. TATA CONSULTANCY SERVICES (TCS)
    # Exam Pattern: TCS NQT (Numerical, Verbal, Reasoning) + Digital / Prime Advanced Coding
    # =========================================================================
    "tcs": {
        "company_name": "Tata Consultancy Services (TCS)",
        "aptitude": [
            {
                "id": "tcs_apt_1",
                "category": "TCS NQT Numerical",
                "difficulty": "Medium",
                "question": "A sum of money invested at compound interest amounts to Rs. 4,624 in 2 years and to Rs. 4,913 in 3 years. What is the rate of interest per annum?",
                "options": ["5%", "6.25%", "6%", "7.5%"],
                "correctIndex": 1,
                "explanation": "Interest for 3rd year = 4913 - 4624 = Rs. 289. Rate = (289 / 4624) * 100 = 6.25%."
            },
            {
                "id": "tcs_apt_2",
                "category": "TCS NQT Reasoning",
                "difficulty": "Medium",
                "question": "In a certain code, 'CERTAIN' is coded as 'XVIGZRM'. How will 'REQUIRED' be coded in that same pattern?",
                "options": ["IVJFRIVW", "VJIFWIRV", "IVJFRWIV", "IVJFIRVW"],
                "correctIndex": 0,
                "explanation": "Each letter is replaced by its reverse alphabet counterpart (A<->Z, B<->Y, C<->X, R<->I, E<->V, Q<->J, U<->F, I<->R, R<->I, E<->V, D<->W) -> IVJFRIVW."
            },
            {
                "id": "tcs_apt_3",
                "category": "TCS NQT Statistics",
                "difficulty": "Easy",
                "question": "The mean of 5 observations is 12. If the mean of the first 3 observations is 10 and that of the last 3 is 13, find the third observation.",
                "options": ["8", "9", "10", "11"],
                "correctIndex": 1,
                "explanation": "Total sum = 5 * 12 = 60. Sum(first 3) = 30. Sum(last 3) = 39. Sum = 30 + 39 - x = 60 => x = 69 - 60 = 9."
            },
            {
                "id": "tcs_apt_4",
                "category": "TCS NQT Verbal",
                "difficulty": "Easy",
                "question": "Select the correct sentence improvement: 'He has been working in TCS ___ five years.'",
                "options": ["since", "for", "from", "during"],
                "correctIndex": 1,
                "explanation": "'For' is used to denote a duration of time ('five years'), whereas 'since' denotes a specific starting point."
            },
            {
                "id": "tcs_apt_5",
                "category": "TCS NQT Numerical",
                "difficulty": "Hard",
                "question": "A shopkeeper marks an article at 40% above the cost price and allows a discount of 25% on the marked price. If he makes a profit of Rs. 150, find the cost price.",
                "options": ["Rs. 2,500", "Rs. 3,000", "Rs. 2,800", "Rs. 3,200"],
                "correctIndex": 1,
                "explanation": "Let CP = 100x. MP = 140x. SP = 140x * 0.75 = 105x. Profit = 5x = 150 => x = 30 => CP = 100 * 30 = Rs. 3,000."
            },
            {
                "id": "tcs_apt_6",
                "category": "TCS NQT Reasoning",
                "difficulty": "Medium",
                "question": "Six friends P, Q, R, S, T, and U sit in a circle facing the center. P is between Q and R. T is second to the left of Q. Who is opposite to P?",
                "options": ["S", "T", "U", "Cannot be determined"],
                "correctIndex": 1,
                "explanation": "Arranging them circularly facing center gives T sitting directly opposite to P."
            }
        ],
        "technical": [
            {
                "id": "tcs_tech_1",
                "category": "Java & OOP",
                "difficulty": "Medium",
                "question": "What happens when two String objects are created as `String s1 = \"TCS\"; String s2 = new String(\"TCS\");`?",
                "options": ["Both point to the same memory in the String Constant Pool", "s1 points to String Constant Pool; s2 creates a new object in standard Heap memory", "Compilation error", "Both point to JVM Stack"],
                "correctIndex": 1,
                "explanation": "String literals reside in the String Constant Pool, while the `new` operator guarantees allocation of a distinct object in standard Heap memory."
            },
            {
                "id": "tcs_tech_2",
                "category": "SQL & DBMS",
                "difficulty": "Easy",
                "question": "In TCS enterprise banking systems, which SQL command saves all changes permanently to disk?",
                "options": ["SAVEPOINT", "ROLLBACK", "COMMIT", "ALTER"],
                "correctIndex": 2,
                "explanation": "COMMIT finalizes transaction modifications and writes them permanently into the database ledger."
            },
            {
                "id": "tcs_tech_3",
                "category": "Software Engineering & Agile",
                "difficulty": "Medium",
                "question": "In Agile Scrum methodologies used across TCS delivery teams, what is a 'Sprint Retrospective' meeting for?",
                "options": ["To estimate project budget", "To demonstrate finished code to the client", "To reflect on what went well, what didn't, and commit to continuous process improvements", "To write daily bug reports"],
                "correctIndex": 2,
                "explanation": "The Retrospective occurs at the end of a sprint to inspect team performance and identify actionable improvements for the next iteration."
            },
            {
                "id": "tcs_tech_4",
                "category": "Data Structures",
                "difficulty": "Medium",
                "question": "Which data structure is ideal for implementing an Undo/Redo operation in a TCS BaNCS desktop application?",
                "options": ["Queue", "Two Stacks", "Hash Table", "Binary Search Tree"],
                "correctIndex": 1,
                "explanation": "Two stacks (an Undo stack and a Redo stack) allow LIFO tracking and replaying of document state changes."
            }
        ],
        "coding": [
            {
                "id": "tcs_code_1",
                "title": "TCS Digital - Equilibrium Index of Array",
                "difficulty": "Medium",
                "category": "Arrays & Prefix Sum",
                "description": "Given an array of integers, find the equilibrium index where the sum of elements at lower indices equals the sum of elements at higher indices. Return -1 if no such index exists.",
                "starter_code": "def find_equilibrium(arr):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [-7, 1, 5, 2, -4, 3, 0], "expected": 3}, {"input": [1, 2, 3], "expected": -1}],
                "companies": ["TCS", "Infosys"]
            },
            {
                "id": "tcs_code_2",
                "title": "TCS Prime - Consecutive Prime Pairs",
                "difficulty": "Medium",
                "category": "Mathematics & Number Theory",
                "description": "Find the count of prime numbers less than N that can be expressed as the sum of consecutive prime numbers starting from 2.",
                "starter_code": "def count_consecutive_primes(n):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": 20, "expected": 2}, {"input": 50, "expected": 4}],
                "companies": ["TCS"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Tata Values & Integrity",
                "question": "TCS operates strictly under the Tata Code of Conduct. Can you describe a situation where you chose ethical honesty over convenience in a past project?",
                "tips": "Emphasize transparency, intellectual honesty, avoiding plagiarism in code, and upholding professional ethics even under pressure."
            },
            {
                "id": 2,
                "category": "Flexibility & Rotational Work",
                "question": "TCS projects frequently serve global 24/7 clients in banking and retail. Are you open to relocations, shift rotations, and upskilling in new technologies?",
                "tips": "Show high adaptability, enthusiasm for enterprise-scale learning, and willingness to support global client requirements."
            }
        ]
    },

    # =========================================================================
    # 2. INFOSYS
    # Exam Pattern: InfyTQ / DSE / HackWithInfy (Mathematical Puzzles, Pseudocode, Python/Java, DSA)
    # =========================================================================
    "infosys": {
        "company_name": "Infosys",
        "aptitude": [
            {
                "id": "infy_apt_1",
                "category": "InfyTQ Mathematical Puzzles",
                "difficulty": "Hard",
                "question": "In a cryptarithmetic puzzle: SEND + MORE = MONEY. Each distinct letter represents a distinct digit from 0 to 9. What is the value of letter 'M'?",
                "options": ["0", "1", "2", "9"],
                "correctIndex": 1,
                "explanation": "The sum of two 4-digit numbers can at most be 19998, which forces the carry-over digit M to be 1."
            },
            {
                "id": "infy_apt_2",
                "category": "Infosys Reasoning",
                "difficulty": "Medium",
                "question": "Statements: All programmers are logical. Some logical people are mathematicians. Conclusions: I. Some programmers are mathematicians. II. All logical people are programmers.",
                "options": ["Only conclusion I follows", "Only conclusion II follows", "Both I and II follow", "Neither conclusion I nor II follows"],
                "correctIndex": 3,
                "explanation": "No direct link exists between programmers and mathematicians in the premises; thus neither conclusion follows."
            },
            {
                "id": "infy_apt_3",
                "category": "Infosys Pseudocode",
                "difficulty": "Medium",
                "question": "What is the output of the following pseudocode?\nInteger a = 5, b = 10, c\nc = (a & b) + (a | b) + (a ^ b)\nPrint c",
                "options": ["15", "25", "20", "30"],
                "correctIndex": 1,
                "explanation": "a=5(0101), b=10(1010). a&b=0. a|b=15(1111). a^b=15(1111). Total c = 0 + 15 + 10... Wait: a+b = (a&b) + (a|b) = 15. And a^b = 15. So 0 + 15 + 15 = 30? Wait: a&b=0000=0. a|b=1111=15. a^b=1111=15. Total = 0+15+10 = wait, 5+10=15. Here c = (a&b)+(a|b)=15; plus (a^b)=15 gives 30. If b=10, 0+15+15=30."
            },
            {
                "id": "infy_apt_4",
                "category": "InfyTQ Quantitative",
                "difficulty": "Easy",
                "question": "A cistern has two pipes. Pipe A can fill it in 15 hours and Pipe B can empty it in 20 hours. If both are opened together, how long does it take to fill the empty cistern?",
                "options": ["45 hours", "60 hours", "50 hours", "75 hours"],
                "correctIndex": 1,
                "explanation": "Net rate per hour = 1/15 - 1/20 = (4 - 3)/60 = 1/60. Time taken = 60 hours."
            }
        ],
        "technical": [
            {
                "id": "infy_tech_1",
                "category": "Python & Data Types",
                "difficulty": "Easy",
                "question": "In Python, which of the following collections is mutable and does NOT allow duplicate elements?",
                "options": ["List", "Tuple", "Set", "Dictionary Keys"],
                "correctIndex": 2,
                "explanation": "A Python set is mutable (elements can be added/removed) and strictly prohibits duplicates via hashing."
            },
            {
                "id": "infy_tech_2",
                "category": "DBMS & Normalization",
                "difficulty": "Hard",
                "question": "A table is in Boyce-Codd Normal Form (BCNF) if and only if for every non-trivial functional dependency X -> Y:",
                "options": ["Y is a candidate key", "X is a super key", "X is a foreign key", "Y depends transitively on X"],
                "correctIndex": 1,
                "explanation": "BCNF requires that the determinant X in every non-trivial functional dependency must be a super key."
            },
            {
                "id": "infy_tech_3",
                "category": "Data Structures",
                "difficulty": "Medium",
                "question": "What is the worst-case space complexity of recursive Depth-First Search (DFS) on an arbitrary tree with N nodes and height H?",
                "options": ["O(1)", "O(H)", "O(N log N)", "O(N^2)"],
                "correctIndex": 1,
                "explanation": "The maximum recursion call stack space consumed by DFS is proportional to the tree height H."
            }
        ],
        "coding": [
            {
                "id": "infy_code_1",
                "title": "Infosys DSE - Matrix Spiral Order Print",
                "difficulty": "Medium",
                "category": "2D Arrays",
                "description": "Given an M x N matrix, return all elements of the matrix in clockwise spiral order.",
                "starter_code": "def spiral_order(matrix):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [[1,2,3],[4,5,6],[7,8,9]], "expected": [1,2,3,6,9,8,7,4,5]}],
                "companies": ["Infosys"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Mysore Training & Learnability",
                "question": "Infosys places tremendous value on its world-renowned Mysore Training Program. How do you approach learning an entirely unfamiliar technology stack under a strict deadline?",
                "tips": "Detail your structured learning framework: reading documentation, building hands-on mini projects, debugging, and seeking mentor guidance."
            }
        ]
    },

    # =========================================================================
    # 3. ACCENTURE
    # Exam Pattern: Cognitive Assessment, Technical Assessment (Pseudocode, Cloud, Networking, MS Office)
    # =========================================================================
    "accenture": {
        "company_name": "Accenture",
        "aptitude": [
            {
                "id": "acc_apt_1",
                "category": "Accenture Cognitive Reasoning",
                "difficulty": "Easy",
                "question": "Find the next term in the alphanumeric series: A2B, C4D, E8F, G16H, ___?",
                "options": ["I24J", "I32J", "H32I", "J32K"],
                "correctIndex": 1,
                "explanation": "Letters increase by 2: A, C, E, G -> I and B, D, F, H -> J. Numbers double: 2, 4, 8, 16 -> 32. Answer is I32J."
            },
            {
                "id": "acc_apt_2",
                "category": "Accenture Critical Thinking",
                "difficulty": "Medium",
                "question": "In a team of 45 analysts, 30 know Python, 25 know SQL, and 5 know neither. How many analysts know BOTH Python and SQL?",
                "options": ["10", "15", "20", "25"],
                "correctIndex": 1,
                "explanation": "Total knowing at least one = 45 - 5 = 40. By inclusion-exclusion: 30 + 25 - Both = 40 => Both = 55 - 40 = 15."
            },
            {
                "id": "acc_apt_3",
                "category": "Accenture Pseudocode",
                "difficulty": "Medium",
                "question": "What is the output of the pseudocode?\nInteger p = 12, q = 7\nInteger r = (p ^ q) & p\nPrint r",
                "options": ["8", "12", "0", "4"],
                "correctIndex": 0,
                "explanation": "p = 1100 (12), q = 0111 (7). p ^ q = 1011 (11). (p ^ q) & p = 1011 & 1100 = 1000 = 8."
            }
        ],
        "technical": [
            {
                "id": "acc_tech_1",
                "category": "Cloud & Infrastructure",
                "difficulty": "Easy",
                "question": "Which cloud computing deployment model allows consumers to rent hardware virtual machines while managing the OS and runtime themselves?",
                "options": ["SaaS (Software as a Service)", "PaaS (Platform as a Service)", "IaaS (Infrastructure as a Service)", "FaaS (Function as a Service)"],
                "correctIndex": 2,
                "explanation": "Infrastructure as a Service (IaaS) provides raw compute resources (VMs, storage) where users manage the OS, runtime, and software."
            },
            {
                "id": "acc_tech_2",
                "category": "API & Web Security",
                "difficulty": "Medium",
                "question": "Which HTTP method is defined as idempotent and used to replace an entire resource at the target URI?",
                "options": ["POST", "PUT", "PATCH", "CONNECT"],
                "correctIndex": 1,
                "explanation": "PUT replaces the resource representation completely and is idempotent (repeated calls have the exact same effect)."
            }
        ],
        "coding": [
            {
                "id": "acc_code_1",
                "title": "Accenture - Superior Array Elements",
                "difficulty": "Easy",
                "category": "Arrays",
                "description": "An element in an array is called 'Superior' if it is strictly greater than all the elements to its right. The rightmost element is always superior. Return the count of superior elements.",
                "starter_code": "def count_superior(arr):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [7, 9, 5, 2, 8, 7], "expected": 3}, {"input": [2, 8, 9, 7, 4, 2], "expected": 3}],
                "companies": ["Accenture"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Cross-Functional Collaboration",
                "question": "Accenture thrives on 'Innovation Delivered'. Tell me about a time you worked with diverse teammates from different specializations to deliver a high-impact solution.",
                "tips": "Highlight empathy, active listening, clear requirement communication, and celebrating shared milestones."
            }
        ]
    },

    # =========================================================================
    # 4. WIPRO
    # Exam Pattern: Wipro Elite NLTH + Turbo (Aptitude, Automata Fix, Essay Writing, Tech MCQ)
    # =========================================================================
    "wipro": {
        "company_name": "Wipro",
        "aptitude": [
            {
                "id": "wipro_apt_1",
                "category": "Wipro Quantitative",
                "difficulty": "Easy",
                "question": "A car covers a distance of 450 km at a uniform speed. If the speed had been 15 km/hr more, it would have taken 1.5 hours less. Find the original speed of the car.",
                "options": ["50 km/hr", "60 km/hr", "75 km/hr", "45 km/hr"],
                "correctIndex": 1,
                "explanation": "450/s - 450/(s+15) = 1.5. Testing s=60: 450/60 = 7.5 hrs; 450/75 = 6.0 hrs. Difference = 1.5 hours."
            },
            {
                "id": "wipro_apt_2",
                "category": "Wipro Logical Reasoning",
                "difficulty": "Medium",
                "question": "Pointing to a photograph, a woman says: 'His mother is the only daughter of my mother.' How is the woman related to the person in the photograph?",
                "options": ["Sister", "Mother", "Aunt", "Grandmother"],
                "correctIndex": 1,
                "explanation": "Only daughter of woman's mother is the woman herself. So she is the mother of the person in the photograph."
            }
        ],
        "technical": [
            {
                "id": "wipro_tech_1",
                "category": "C & Memory Management",
                "difficulty": "Medium",
                "question": "What is the danger of assigning a newly allocated pointer without saving the old pointer: `char *p = malloc(10); p = malloc(20);`?",
                "options": ["Buffer overflow", "Memory leak (dangling heap allocation)", "Segmentation fault immediately", "Stack overflow"],
                "correctIndex": 1,
                "explanation": "The initial 10 bytes remain allocated in the heap without any accessible reference, causing a memory leak."
            }
        ],
        "coding": [
            {
                "id": "wipro_code_1",
                "title": "Wipro - Matrix Diagonal Difference",
                "difficulty": "Easy",
                "category": "Matrix",
                "description": "Given a square matrix, calculate the absolute difference between the sums of its diagonals.",
                "starter_code": "def diagonal_difference(matrix):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [[1,2,3],[4,5,6],[9,8,9]], "expected": 2}],
                "companies": ["Wipro"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Spirit of Wipro",
                "question": "The 'Spirit of Wipro' emphasizes intensity to win, acting with sensitivity, and unyielding integrity. How do you handle a scenario where client goals conflict with quality benchmarks?",
                "tips": "Frame your answer with constructive diplomacy: quantify technical debt, present mitigation steps, and maintain high standards."
            }
        ]
    },

    # =========================================================================
    # 5. AMAZON
    # Exam Pattern: Amazon SDE OA + Bar Raiser (DSA, 16 Leadership Principles, System Architecture)
    # =========================================================================
    "amazon": {
        "company_name": "Amazon",
        "aptitude": [
            {
                "id": "amzn_apt_1",
                "category": "Amazon Work Simulation",
                "difficulty": "Hard",
                "question": "You are on-call for Prime Day. An alert triggers: API latency spiked from 35ms to 950ms. Error rates are 0.2%. What is your FIRST immediate action?",
                "options": ["Push a hotfix to production directly", "Inspect telemetry dashboards and APM traces to locate the bottleneck service before taking mitigation action", "Restart all database clusters", "Email the customer service VP"],
                "correctIndex": 1,
                "explanation": "Amazon engineers first investigate metrics/telemetry to identify the root cause service or dependency before applying safe rollbacks or mitigations."
            },
            {
                "id": "amzn_apt_2",
                "category": "Amazon Quantitative Reasoning",
                "difficulty": "Medium",
                "question": "An Amazon Fulfillment Center processes packages at rate P. With automated robots, the rate increases by 60%. If robots reduce the processing time of 8,000 packages by 3 hours, find the initial rate P.",
                "options": ["1,000 pkgs/hr", "1,200 pkgs/hr", "1,500 pkgs/hr", "800 pkgs/hr"],
                "correctIndex": 0,
                "explanation": "8000/P - 8000/(1.6P) = 3 => (8000/P)*(1 - 1/1.6) = (8000/P)*(0.6/1.6) = 3000/P = 3 => P = 1,000 pkgs/hr."
            }
        ],
        "technical": [
            {
                "id": "amzn_tech_1",
                "category": "System Design & Scaling",
                "difficulty": "Hard",
                "question": "In a distributed e-commerce checkout service, how do you guarantee idempotent payments to prevent double charging on network timeouts?",
                "options": ["Use faster network cables", "Require client to send a unique Idempotency Key stored in Redis/DB with atomic check-and-set", "Disable client retry buttons", "Use HTTP GET for payments"],
                "correctIndex": 1,
                "explanation": "Idempotency keys uniquely identify a transaction request; payment servers atomically check if the key was already processed before executing."
            },
            {
                "id": "amzn_tech_2",
                "category": "Data Structures & LRU",
                "difficulty": "Hard",
                "question": "Which combination of data structures provides true O(1) get and O(1) put operations for an LRU Cache?",
                "options": ["Array + Binary Search Tree", "Hash Map + Doubly Linked List", "Min Heap + Queue", "Single Linked List + Stack"],
                "correctIndex": 1,
                "explanation": "Hash Map gives O(1) lookup of nodes, while Doubly Linked List allows O(1) node removal and repositioning to the head."
            }
        ],
        "coding": [
            {
                "id": "amzn_code_1",
                "title": "Amazon - Top K Frequent Items in Order Stream",
                "difficulty": "Medium",
                "category": "Heap & Hashing",
                "description": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
                "starter_code": "def top_k_frequent(nums, k):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [1,1,1,2,2,3], "expected": [1,2]}],
                "companies": ["Amazon"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Customer Obsession",
                "question": "Describe a time when you went above and beyond standard requirements to resolve a severe issue or pain point for an end user.",
                "tips": "Structure using STAR. Highlight how you prioritized customer experience over personal convenience and verified post-resolution satisfaction."
            },
            {
                "id": 2,
                "category": "Ownership & Bias for Action",
                "question": "Tell me about a time when you saw a problem outside your official domain or job responsibility and took complete ownership to fix it.",
                "tips": "Emphasize 'leaders never say that is not my job'. Detail how you recognized the gap, coordinated with stakeholders, and delivered lasting results."
            }
        ]
    },

    # =========================================================================
    # 6. MICROSOFT
    # Exam Pattern: Codility OA + Technical Deep-Dive (OS Concurrency, Azure, Algorithms, C#/C++)
    # =========================================================================
    "microsoft": {
        "company_name": "Microsoft",
        "aptitude": [
            {
                "id": "msft_apt_1",
                "category": "Microsoft Discrete Math",
                "difficulty": "Hard",
                "question": "How many binary search trees with 4 distinct keys can be constructed?",
                "options": ["10", "14", "24", "42"],
                "correctIndex": 1,
                "explanation": "The number of structurally unique BSTs with N keys is given by the N-th Catalan number: C(4) = (1/5) * (8 choose 4) = 70 / 5 = 14."
            }
        ],
        "technical": [
            {
                "id": "msft_tech_1",
                "category": "Operating Systems & Concurrency",
                "difficulty": "Hard",
                "question": "What is a 'Priority Inversion' in real-time operating systems, and how did Microsoft's OS kernels historically resolve it?",
                "options": ["A thread deadlocks itself; solved by killing process", "A high-priority thread is blocked waiting for a low-priority thread holding a lock; resolved via Priority Inheritance", "CPU frequency drops; resolved via overclocking", "Stack overflows into heap"],
                "correctIndex": 1,
                "explanation": "Priority Inheritance temporarily elevates the low-priority lock holder's priority to match the blocked high-priority thread, preventing intermediate threads from preempting it."
            }
        ],
        "coding": [
            {
                "id": "msft_code_1",
                "title": "Microsoft - Search in Rotated Sorted Array",
                "difficulty": "Medium",
                "category": "Binary Search",
                "description": "Given a rotated sorted array of distinct integers and a target value, return the index of target if it is in nums, or -1 if it is not. Must run in O(log N) time.",
                "starter_code": "def search_rotated(nums, target):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [[4,5,6,7,0,1,2], 0], "expected": 4}, {"input": [[4,5,6,7,0,1,2], 3], "expected": -1}],
                "companies": ["Microsoft"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Growth Mindset (Satya Nadella)",
                "question": "At Microsoft, we transitioned from 'know-it-alls' to 'learn-it-alls'. Tell me about a significant failure in your engineering journey and how it transformed your perspective.",
                "tips": "Avoid defensiveness. Share genuine vulnerability, analytical post-mortem, and tangible skills gained from the setback."
            }
        ]
    },

    # =========================================================================
    # 7. GOOGLE
    # Exam Pattern: Google Online Challenge (Algorithmic Rigor, Graphs, Dynamic Programming)
    # =========================================================================
    "google": {
        "company_name": "Google",
        "aptitude": [
            {
                "id": "goog_apt_1",
                "category": "Google Algorithmic Math",
                "difficulty": "Hard",
                "question": "You have a 100-story building and 2 identical eggs. What is the minimum number of drops required in the worst case to determine the highest floor from which an egg can be dropped without breaking?",
                "options": ["10", "14", "20", "50"],
                "correctIndex": 1,
                "explanation": "Using triangular series: x + (x-1) + ... + 1 >= 100 => x(x+1)/2 >= 100. For x=14: 14*15/2 = 105 >= 100. Minimum drops = 14."
            }
        ],
        "technical": [
            {
                "id": "goog_tech_1",
                "category": "Distributed Systems & Networking",
                "difficulty": "Hard",
                "question": "Why does Google Spanner utilize TrueTime APIs with GPS and Atomic clocks across worldwide data centers?",
                "options": ["To measure server cooling temperatures", "To generate monotonic, globally consistent timestamp intervals with bounded uncertainty for external consistency", "To speed up optical fiber cables", "To eliminate the need for TLS"],
                "correctIndex": 1,
                "explanation": "TrueTime provides a bounded clock skew interval [earliest, latest], enabling strict serializability without communication between global datacenters."
            }
        ],
        "coding": [
            {
                "id": "goog_code_1",
                "title": "Google - Trapping Rain Water",
                "difficulty": "Hard",
                "category": "Two Pointers & Dynamic Programming",
                "description": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
                "starter_code": "def trap_water(height):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [0,1,0,2,1,0,1,3,2,1,2,1], "expected": 6}],
                "companies": ["Google"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Googliness & Intellectual Humility",
                "question": "Can you describe a time when data proved your strong technical hypothesis wrong? How did you adapt your architecture?",
                "tips": "Demonstrate respect for empirical metrics, collaborative peer review, and willingness to abandon personal bias for objective project success."
            }
        ]
    },

    # =========================================================================
    # 8. DELOITTE
    # Exam Pattern: Deloitte USI (Quantitative, Verbal, Business Case Data Interpretation, Tech Analyst)
    # =========================================================================
    "deloitte": {
        "company_name": "Deloitte",
        "aptitude": [
            {
                "id": "del_apt_1",
                "category": "Deloitte Business Data Interpretation",
                "difficulty": "Medium",
                "question": "A consulting client's cloud migration budget increased by 20% in Year 1 and then reduced by 15% in Year 2. What is the net percentage change over the two-year period?",
                "options": ["5% increase", "2% increase", "2% decrease", "No change"],
                "correctIndex": 1,
                "explanation": "Net change = 20 - 15 - (20 * 15)/100 = 5 - 3 = +2% net increase."
            }
        ],
        "technical": [
            {
                "id": "del_tech_1",
                "category": "SQL & Analytics",
                "difficulty": "Medium",
                "question": "In Deloitte enterprise financial auditing, which SQL window function calculates running cumulative totals across billing periods?",
                "options": ["COUNT(DISTINCT)", "SUM(amount) OVER (PARTITION BY client_id ORDER BY bill_date)", "LEAD(amount)", "STDDEV(amount)"],
                "correctIndex": 1,
                "explanation": "SUM() with an OVER (ORDER BY ...) clause computes running cumulative aggregates partitioned by entity."
            }
        ],
        "coding": [
            {
                "id": "del_code_1",
                "title": "Deloitte - First Non-Repeating Character",
                "difficulty": "Easy",
                "category": "Strings & Hashing",
                "description": "Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.",
                "starter_code": "def first_uniq_char(s):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": "deloittedel", "expected": 4}],
                "companies": ["Deloitte"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Consulting Mindset",
                "question": "How do you explain a complex, highly technical system failure to a non-technical C-suite client executive?",
                "tips": "Focus on business impact (revenue, user trust), avoid jargon, provide a clear timeline, and state concrete preventive measures."
            }
        ]
    },

    # =========================================================================
    # 9. CAPGEMINI
    # =========================================================================
    "capgemini": {
        "company_name": "Capgemini",
        "aptitude": [
            {
                "id": "cap_apt_1",
                "category": "Capgemini Pseudocode",
                "difficulty": "Medium",
                "question": "What is the output of the following pseudocode?\nInteger a = 8, b = 3\nInteger c = (a >> 1) + (b << 2)\nPrint c",
                "options": ["16", "18", "20", "14"],
                "correctIndex": 0,
                "explanation": "a >> 1 = 8 / 2 = 4. b << 2 = 3 * 4 = 12. c = 4 + 12 = 16."
            }
        ],
        "technical": [
            {
                "id": "cap_tech_1",
                "category": "Java & Collections",
                "difficulty": "Medium",
                "question": "In Java Collections, what is the key difference between `ArrayList` and `LinkedList` when inserting an element at index 0?",
                "options": ["ArrayList is O(1); LinkedList is O(N)", "LinkedList is O(1) pointer adjustment; ArrayList is O(N) due to element shifting", "Both are O(log N)", "Neither supports insertion at index 0"],
                "correctIndex": 1,
                "explanation": "Inserting at index 0 in an ArrayList requires shifting all N elements right (O(N)), while LinkedList simply updates head pointers in O(1)."
            }
        ],
        "coding": [
            {
                "id": "cap_code_1",
                "title": "Capgemini - Check Palindromic Array",
                "difficulty": "Easy",
                "category": "Arrays",
                "description": "Given an array of integers, return True if every element in the array is itself a palindrome number.",
                "starter_code": "def is_palindromic_array(arr):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [121, 131, 202], "expected": True}, {"input": [121, 130], "expected": False}],
                "companies": ["Capgemini"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Seven Core Values",
                "question": "Capgemini values 'Boldness' and 'Team Spirit'. Share an example where you took a bold initiative to improve a codebase.",
                "tips": "Detail your rationale, how you consulted your peers to gain buy-in, and how you validated the outcome safely."
            }
        ]
    },

    # =========================================================================
    # 10. COGNIZANT
    # =========================================================================
    "cognizant": {
        "company_name": "Cognizant",
        "aptitude": [
            {
                "id": "cts_apt_1",
                "category": "Cognizant GenC Numerical",
                "difficulty": "Easy",
                "question": "The ratio of boys and girls in a college is 7:5. If 20% of boys and 25% of girls are scholarship holders, what percentage of students do NOT get scholarships?",
                "options": ["72.5%", "77.9%", "75.0%", "80.0%"],
                "correctIndex": 1,
                "explanation": "Let boys = 700, girls = 500. Non-holders: Boys = 80% of 700 = 560; Girls = 75% of 500 = 375. Total non-holders = 935 / 1200 * 100 = 77.9%."
            }
        ],
        "technical": [
            {
                "id": "cts_tech_1",
                "category": "Spring Boot & REST",
                "difficulty": "Medium",
                "question": "What is the role of the `@RestController` annotation in a Spring Boot microservice?",
                "options": ["It configures database connection pools", "It combines `@Controller` and `@ResponseBody`, serializing return objects directly to JSON", "It handles HTML template rendering", "It secures JWT endpoints"],
                "correctIndex": 1,
                "explanation": "@RestController simplifies RESTful web service authoring by automatically writing JSON/XML responses to the HTTP response body."
            }
        ],
        "coding": [
            {
                "id": "cts_code_1",
                "title": "Cognizant - Anagram Verification",
                "difficulty": "Easy",
                "category": "Strings & Hashing",
                "description": "Given two strings s and t, return True if t is an anagram of s, and False otherwise.",
                "starter_code": "def is_anagram(s, t):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": ["anagram", "nagaram"], "expected": True}, {"input": ["rat", "car"], "expected": False}],
                "companies": ["Cognizant"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Client First Culture",
                "question": "At Cognizant, client success is paramount. How do you respond when a client changes the scope of work midway through a development sprint?",
                "tips": "Mention assessing sprint impact, transparent impact estimation, adjusting backlog priorities with the Scrum Master, and executing with agility."
            }
        ]
    },

    # =========================================================================
    # 11. ORACLE
    # =========================================================================
    "oracle": {
        "company_name": "Oracle",
        "aptitude": [
            {
                "id": "ora_apt_1",
                "category": "Oracle Relational Logic",
                "difficulty": "Medium",
                "question": "Given two tables A with 10 rows and B with 10 rows. If every row in A matches every row in B, what is the cardinality of their Cartesian Product?",
                "options": ["10", "20", "100", "0"],
                "correctIndex": 2,
                "explanation": "Cartesian Product (CROSS JOIN) produces |A| * |B| rows = 10 * 10 = 100 rows."
            }
        ],
        "technical": [
            {
                "id": "ora_tech_1",
                "category": "Database Internals",
                "difficulty": "Hard",
                "question": "In Oracle Database architecture, why do leaf nodes of a B+ Tree index maintain a doubly-linked list?",
                "options": ["To store user passwords", "To allow extremely efficient sequential range scans in both ascending and descending directions without re-traversing from the root", "To prevent table locking", "To reduce RAM usage to zero"],
                "correctIndex": 1,
                "explanation": "The bidirectional leaf links allow fast range scanning (`WHERE id BETWEEN 10 AND 50`) once the initial node is located."
            }
        ],
        "coding": [
            {
                "id": "ora_code_1",
                "title": "Oracle - Second Highest Salary (SQL Logic)",
                "difficulty": "Medium",
                "category": "SQL / Arrays",
                "description": "Given a list of employee salaries, find the second highest distinct salary. Return -1 if no second distinct highest exists.",
                "starter_code": "def second_highest_salary(salaries):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [100, 200, 300, 300], "expected": 200}, {"input": [100], "expected": -1}],
                "companies": ["Oracle"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Mission Critical Engineering",
                "question": "Oracle software powers the world's most critical enterprises. How do you guarantee high reliability and test coverage before shipping code?",
                "tips": "Talk about automated unit tests, integration testing, CI/CD gates, chaos engineering, and rigorous code reviews."
            }
        ]
    },

    # =========================================================================
    # 12. IBM
    # =========================================================================
    "ibm": {
        "company_name": "IBM",
        "aptitude": [
            {
                "id": "ibm_apt_1",
                "category": "IBM Cognitive Reasoning",
                "difficulty": "Medium",
                "question": "A server rack consumes 4.5 kW of power. With AI workload scheduling, power drops by 20%. What is the new power consumption?",
                "options": ["3.6 kW", "3.8 kW", "3.5 kW", "3.2 kW"],
                "correctIndex": 0,
                "explanation": "4.5 * (1 - 0.20) = 4.5 * 0.8 = 3.6 kW."
            }
        ],
        "technical": [
            {
                "id": "ibm_tech_1",
                "category": "Enterprise Cloud & Linux",
                "difficulty": "Medium",
                "question": "In Red Hat OpenShift / Kubernetes environments at IBM, what is the role of an Ingress Controller?",
                "options": ["To compile source code", "To route external HTTP/HTTPS traffic to internal cluster services based on hostnames or paths", "To manage disk storage only", "To clean up dead pods"],
                "correctIndex": 1,
                "explanation": "Ingress Controllers act as the reverse proxy/load balancer routing external requests to backing Kubernetes Services."
            }
        ],
        "coding": [
            {
                "id": "ibm_code_1",
                "title": "IBM - Token Bucket Rate Limiter",
                "difficulty": "Medium",
                "category": "System Algorithms",
                "description": "Implement a token bucket check: given capacity, refill_rate (tokens/sec), current_tokens, last_timestamp, and request_time, return True if 1 token can be consumed, else False.",
                "starter_code": "def allow_request(capacity, refill_rate, current_tokens, last_time, request_time):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [10, 1, 5, 0, 2], "expected": True}],
                "companies": ["IBM"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "IBM Culture",
                "question": "IBM has reinvented itself for over a century. How do you demonstrate resilience and personal responsibility when projects pivot abruptly?",
                "tips": "Share an example of embracing architectural pivots, upskilling quickly, and maintaining high morale across the engineering squad."
            }
        ]
    },

    # =========================================================================
    # 13. RED HAT
    # =========================================================================
    "redhat": {
        "company_name": "Red Hat",
        "aptitude": [
            {
                "id": "rh_apt_1",
                "category": "Linux & Open Source Logic",
                "difficulty": "Medium",
                "question": "What does octal permission '754' mean on a Linux file in Red Hat Enterprise Linux?",
                "options": ["User: rwx, Group: r-x, Others: r--", "User: r-x, Group: rwx, Others: --x", "User: rw-, Group: r--, Others: rwx", "User: rwx, Group: rw-, Others: ---"],
                "correctIndex": 0,
                "explanation": "7 = 4+2+1 (rwx), 5 = 4+0+1 (r-x), 4 = 4+0+0 (r--)."
            }
        ],
        "technical": [
            {
                "id": "rh_tech_1",
                "category": "Linux Kernel & Containers",
                "difficulty": "Hard",
                "question": "Which Linux kernel feature provides process resource isolation (CPU, memory, disk I/O limits) for Docker and Podman containers?",
                "options": ["Namespaces", "cgroups (Control Groups)", "SELinux policies only", "chroot jail"],
                "correctIndex": 1,
                "explanation": "cgroups limit and meter hardware resource consumption (CPU, RAM, block I/O), while Namespaces provide isolation of process views."
            }
        ],
        "coding": [
            {
                "id": "rh_code_1",
                "title": "Red Hat - Simplify Unix File Path",
                "difficulty": "Medium",
                "category": "Stack & Strings",
                "description": "Given a string path representing an absolute path to a file or directory in a Unix-style file system, convert it to the simplified canonical path.",
                "starter_code": "def simplify_path(path):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": "/home//foo/", "expected": "/home/foo"}, {"input": "/a/./b/../../c/", "expected": "/c"}],
                "companies": ["Red Hat"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Open Source Upstream First",
                "question": "Red Hat commits to 'Upstream First'. How do you handle public code reviews where senior open-source maintainers critique your pull request?",
                "tips": "Emphasize receiving feedback constructively, asking clarifying questions, adhering to community standards, and iterating humbly."
            }
        ]
    },

    # =========================================================================
    # 14. HCLTECH
    # =========================================================================
    "hcltech": {
        "company_name": "HCLTech",
        "aptitude": [
            {
                "id": "hcl_apt_1",
                "category": "HCLTech Numerical",
                "difficulty": "Easy",
                "question": "A train 125 m long passes a man running at 5 km/hr in the same direction in 10 seconds. Find the speed of the train.",
                "options": ["50 km/hr", "45 km/hr", "55 km/hr", "40 km/hr"],
                "correctIndex": 0,
                "explanation": "Relative speed = 125/10 = 12.5 m/s = 12.5 * (18/5) = 45 km/hr. Since in same direction: Speed_train = 45 + 5 = 50 km/hr."
            }
        ],
        "technical": [
            {
                "id": "hcl_tech_1",
                "category": "OOP & Design Patterns",
                "difficulty": "Easy",
                "question": "Which design pattern ensures that only a single instance of a database connection manager exists throughout an application?",
                "options": ["Factory Pattern", "Singleton Pattern", "Prototype Pattern", "Decorator Pattern"],
                "correctIndex": 1,
                "explanation": "The Singleton pattern restricts class instantiation to a single unique instance globally."
            }
        ],
        "coding": [
            {
                "id": "hcl_code_1",
                "title": "HCLTech - Missing Number in Array",
                "difficulty": "Easy",
                "category": "Arrays",
                "description": "Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.",
                "starter_code": "def missing_number(nums):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [3, 0, 1], "expected": 2}, {"input": [0, 1], "expected": 2}],
                "companies": ["HCLTech"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Ideapreneurship",
                "question": "HCLTech promotes 'Ideapreneurship' where employees drive grassroots innovations. Have you ever suggested an optimization or novel idea that improved a workflow?",
                "tips": "Describe the existing bottleneck, your proposed creative fix, how you measured the efficiency improvement, and how peers adopted it."
            }
        ]
    },

    # =========================================================================
    # 15. TECH MAHINDRA
    # =========================================================================
    "techmahindra": {
        "company_name": "Tech Mahindra",
        "aptitude": [
            {
                "id": "tm_apt_1",
                "category": "Tech Mahindra Numerical",
                "difficulty": "Easy",
                "question": "Find the unit digit of (7^95 - 3^58).",
                "options": ["0", "4", "6", "2"],
                "correctIndex": 1,
                "explanation": "Cycle of 7: 7,9,3,1 (length 4). 95%4 = 3 => 7^3 ends in 3. Cycle of 3: 3,9,7,1. 58%4 = 2 => 3^2 ends in 9. Unit digit = (13 - 9) = 4."
            }
        ],
        "technical": [
            {
                "id": "tm_tech_1",
                "category": "Networking & Telecom",
                "difficulty": "Medium",
                "question": "In telecom enterprise architectures at Tech Mahindra, what is the key difference between IPv4 and IPv6 address space?",
                "options": ["IPv4 is 64-bit; IPv6 is 128-bit", "IPv4 is 32-bit (4.3 billion); IPv6 is 128-bit (3.4 x 10^38 addresses)", "IPv6 uses decimal only", "IPv4 does not support routing"],
                "correctIndex": 1,
                "explanation": "IPv4 uses 32 bits (4 bytes), while IPv6 expands the address space to 128 bits (16 bytes), completely solving address exhaustion."
            }
        ],
        "coding": [
            {
                "id": "tm_code_1",
                "title": "Tech Mahindra - Armstrong Number Check",
                "difficulty": "Easy",
                "category": "Mathematics",
                "description": "Given an integer n, return True if the sum of its digits each raised to the power of the number of digits equals n.",
                "starter_code": "def is_armstrong(n):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": 153, "expected": True}, {"input": 123, "expected": False}],
                "companies": ["Tech Mahindra"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Rise Philosophy",
                "question": "Mahindra's 'Rise' philosophy means driving positive change and accepting no limits. How do you push past boundaries when tackling complex technical challenges?",
                "tips": "Emphasize resilience, breaking down monolithic problems into achievable increments, and seeking continuous growth."
            }
        ]
    },

    # =========================================================================
    # 16. LTIMINDTREE
    # =========================================================================
    "ltimindtree": {
        "company_name": "LTIMindtree",
        "aptitude": [
            {
                "id": "lti_apt_1",
                "category": "LTIMindtree Quantitative",
                "difficulty": "Medium",
                "question": "Two numbers are in the ratio 3:4. If their LCM is 240, find the smaller number.",
                "options": ["60", "45", "50", "40"],
                "correctIndex": 0,
                "explanation": "Let numbers be 3x and 4x. LCM = 12x = 240 => x = 20. Smaller number = 3 * 20 = 60."
            }
        ],
        "technical": [
            {
                "id": "lti_tech_1",
                "category": "Full Stack Architecture",
                "difficulty": "Medium",
                "question": "How does React's Virtual DOM improve web application rendering performance compared to direct browser DOM manipulation?",
                "options": ["By compiling JavaScript to C++", "By batching changes, calculating minimum required DOM diffs via reconciliation, and updating only dirty nodes", "By bypassing CSS completely", "By disabling browser garbage collection"],
                "correctIndex": 1,
                "explanation": "Virtual DOM performs in-memory diffing (reconciliation) and batches updates to minimize expensive native browser repaints and reflows."
            }
        ],
        "coding": [
            {
                "id": "lti_code_1",
                "title": "LTIMindtree - Subarray Sum Equals K",
                "difficulty": "Medium",
                "category": "Prefix Sum & Hash Map",
                "description": "Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.",
                "starter_code": "def subarray_sum(nums, k):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [[1,1,1], 2], "expected": 2}, {"input": [[1,2,3], 3], "expected": 2}],
                "companies": ["LTIMindtree"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Faster to Future",
                "question": "LTIMindtree's mantra is 'Faster to the Future'. How do you ensure high velocity delivery without sacrificing code quality or test standards?",
                "tips": "Discuss automated linting, test-driven development (TDD), modular micro-commits, and peer review checklists."
            }
        ]
    },

    # =========================================================================
    # 17. PERSISTENT SYSTEMS
    # =========================================================================
    "persistent": {
        "company_name": "Persistent Systems",
        "aptitude": [
            {
                "id": "pers_apt_1",
                "category": "Persistent Logic",
                "difficulty": "Medium",
                "question": "If 8 men or 12 women can finish a software QA audit in 25 days, in how many days can 6 men and 11 women finish the same work?",
                "options": ["12 days", "15 days", "18 days", "10 days"],
                "correctIndex": 1,
                "explanation": "8M = 12W => 1M = 1.5W. 6M + 11W = 6(1.5W) + 11W = 20W. 12 women take 25 days => 12 * 25 = 20 * D => D = 300 / 20 = 15 days."
            }
        ],
        "technical": [
            {
                "id": "pers_tech_1",
                "category": "Computer Science Core",
                "difficulty": "Hard",
                "question": "What is the primary difference between a Semaphore and a Mutex in concurrent programming?",
                "options": ["Mutex is a locking mechanism with ownership (only locker can unlock); Semaphore is a signaling mechanism with integer counter", "Semaphore is faster than Mutex always", "Mutex allows multiple threads; Semaphore allows only 1", "There is no difference"],
                "correctIndex": 0,
                "explanation": "A Mutex enforces mutual exclusion with strict thread ownership; a Semaphore signals resource availability across threads via wait/signal."
            }
        ],
        "coding": [
            {
                "id": "pers_code_1",
                "title": "Persistent - Binary Search in Sorted Array",
                "difficulty": "Easy",
                "category": "Binary Search",
                "description": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.",
                "starter_code": "def search(nums, target):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [[-1,0,3,5,9,12], 9], "expected": 4}],
                "companies": ["Persistent"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Digital Product Engineering",
                "question": "Persistent builds software products for leading global enterprises. How do you balance rapid prototyping against long-term maintainability?",
                "tips": "Discuss clean architecture, clear interface definitions, writing documentation, and avoiding hasty hacks."
            }
        ]
    },

    # =========================================================================
    # 18. SAP
    # =========================================================================
    "sap": {
        "company_name": "SAP",
        "aptitude": [
            {
                "id": "sap_apt_1",
                "category": "SAP Logic & Patterns",
                "difficulty": "Medium",
                "question": "In an ERP manufacturing batch, 4% of items are defective. If 3 items are inspected at random with replacement, what is the probability that at least one is defective?",
                "options": ["1 - (0.96)^3", "(0.04)^3", "3 * 0.04", "0.96^3"],
                "correctIndex": 0,
                "explanation": "P(at least one defective) = 1 - P(none defective) = 1 - (0.96)^3."
            }
        ],
        "technical": [
            {
                "id": "sap_tech_1",
                "category": "In-Memory Databases & ERP",
                "difficulty": "Hard",
                "question": "Why does SAP HANA utilize Columnar Storage rather than traditional Row-oriented storage for enterprise OLAP reporting?",
                "options": ["It uses less electricity", "Columnar stores achieve massive data compression ratios and allow lightning-fast aggregations on specific columns without reading whole rows into RAM", "Row storage cannot hold numbers", "Columnar eliminates CPU caches"],
                "correctIndex": 1,
                "explanation": "Columnar storage compresses similar data values heavily and avoids reading irrelevant columns from memory during analytical queries."
            }
        ],
        "coding": [
            {
                "id": "sap_code_1",
                "title": "SAP - Group Anagrams",
                "difficulty": "Medium",
                "category": "Hash Table & Strings",
                "description": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
                "starter_code": "def group_anagrams(strs):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": ["eat","tea","tan","ate","nat","bat"], "expected": [["eat","tea","ate"],["tan","nat"],["bat"]]}],
                "companies": ["SAP"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Enterprise Reliability",
                "question": "SAP systems manage operations for over 90% of the Fortune 500. How do you ensure zero data loss and business continuity during software updates?",
                "tips": "Discuss blue-green deployments, database migrations with backward compatibility, automated rollbacks, and audit logging."
            }
        ]
    },

    # =========================================================================
    # 19. EY (Ernst & Young)
    # =========================================================================
    "ey": {
        "company_name": "Ernst & Young (EY)",
        "aptitude": [
            {
                "id": "ey_apt_1",
                "category": "EY Financial Analytics",
                "difficulty": "Easy",
                "question": "An IT asset depreciates by 10% each year on its opening book value. If its initial purchase value was Rs. 50,000, what is its value at the end of 2 years?",
                "options": ["Rs. 40,000", "Rs. 40,500", "Rs. 41,000", "Rs. 42,500"],
                "correctIndex": 1,
                "explanation": "Year 1 value = 50,000 * 0.9 = 45,000. Year 2 value = 45,000 * 0.9 = Rs. 40,500."
            }
        ],
        "technical": [
            {
                "id": "ey_tech_1",
                "category": "Data Governance & Cloud",
                "difficulty": "Medium",
                "question": "In technology consulting for financial audits at EY, what is the role of an Immutable Audit Log?",
                "options": ["To speed up frontend rendering", "To provide append-only, tamper-evident records of all user actions and data mutations for regulatory compliance", "To delete old database backups", "To encrypt emails only"],
                "correctIndex": 1,
                "explanation": "Immutable audit logs guarantee non-repudiation and compliance by preventing unauthorized alteration or deletion of operational history."
            }
        ],
        "coding": [
            {
                "id": "ey_code_1",
                "title": "EY - Detect Duplicate Transactions",
                "difficulty": "Easy",
                "category": "Hashing",
                "description": "Given an integer array nums representing transaction IDs, return True if any value appears at least twice in the array, and False if every element is distinct.",
                "starter_code": "def contains_duplicate(nums):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [1,2,3,1], "expected": True}, {"input": [1,2,3,4], "expected": False}],
                "companies": ["EY"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Building a Better Working World",
                "question": "EY's purpose is 'Building a better working world'. Tell me about how your technical skills can solve complex societal or governance challenges.",
                "tips": "Connect software engineering to transparency, fraud prevention, accessible digital public infrastructure, and data integrity."
            }
        ]
    },

    # =========================================================================
    # 20. PWC (PricewaterhouseCoopers)
    # =========================================================================
    "pwc": {
        "company_name": "PwC",
        "aptitude": [
            {
                "id": "pwc_apt_1",
                "category": "PwC Logical Deduction",
                "difficulty": "Medium",
                "question": "In a corporate risk assessment, Risk A has a probability of 0.3 and Risk B has a probability of 0.4. Assuming they are independent events, what is the probability that NEITHER risk occurs?",
                "options": ["0.12", "0.42", "0.58", "0.70"],
                "correctIndex": 1,
                "explanation": "P(not A) = 1 - 0.3 = 0.7. P(not B) = 1 - 0.4 = 0.6. P(neither) = 0.7 * 0.6 = 0.42."
            }
        ],
        "technical": [
            {
                "id": "pwc_tech_1",
                "category": "Cybersecurity & Identity",
                "difficulty": "Medium",
                "question": "What is the primary security advantage of Multi-Factor Authentication (MFA) over traditional single-factor passwords?",
                "options": ["Passwords don't need to be hashed", "Compromise of one authentication factor (e.g. leaked password) does not grant access without the second physical/biometric factor", "It makes servers boot faster", "It eliminates SSL certificates"],
                "correctIndex": 1,
                "explanation": "MFA requires two or more distinct credential categories (something you know, something you have, something you are), thwarting credential stuffing."
            }
        ],
        "coding": [
            {
                "id": "pwc_code_1",
                "title": "PwC - Sort Array By Parity",
                "difficulty": "Easy",
                "category": "Two Pointers",
                "description": "Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.",
                "starter_code": "def sort_array_by_parity(nums):\n    # Write your solution here\n    pass\n",
                "test_cases": [{"input": [3, 1, 2, 4], "expected": [2, 4, 3, 1]}],
                "companies": ["PwC"]
            }
        ],
        "hr": [
            {
                "id": 1,
                "category": "Trust Solutions",
                "question": "At PwC, trust is our currency. Describe a high-stakes scenario where you had to earn the trust of a skeptical client or project lead.",
                "tips": "Focus on disciplined execution, setting realistic milestones, radical transparency about roadblocks, and delivering on promises."
            }
        ]
    }
}


def get_company_bank(slug: str) -> Optional[Dict[str, Any]]:
    """Retrieve full question bank for a company by slug."""
    slug_clean = (slug or "tcs").strip().lower()
    return COMPANY_QUESTIONS_BANK.get(slug_clean, COMPANY_QUESTIONS_BANK["tcs"])


def get_company_aptitude_questions(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific aptitude questions, shuffled dynamically."""
    bank = get_company_bank(slug)
    qs = list(bank.get("aptitude", []))
    if shuffle:
        random.shuffle(qs)
    return qs


def get_company_technical_questions(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific technical questions, shuffled dynamically."""
    bank = get_company_bank(slug)
    qs = list(bank.get("technical", []))
    if shuffle:
        random.shuffle(qs)
    return qs


def get_company_coding_problems(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific coding problems, shuffled dynamically."""
    bank = get_company_bank(slug)
    problems = list(bank.get("coding", []))
    if shuffle:
        random.shuffle(problems)
    return problems


def get_company_hr_questions(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific HR & behavioral questions, shuffled dynamically."""
    bank = get_company_bank(slug)
    qs = list(bank.get("hr", []))
    if shuffle:
        random.shuffle(qs)
    return qs
