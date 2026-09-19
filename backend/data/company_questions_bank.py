"""
AI Employee Preparation Platform - Company-Specific Question Banks (2026 Enterprise Edition)
Authentic, domain-calibrated placement & lateral engineering interview banks for all 20 enterprises:
TCS, Infosys, Accenture, Wipro, Amazon, Microsoft, Google, Deloitte, Capgemini, Cognizant,
Oracle, IBM, Red Hat, HCLTech, Tech Mahindra, LTIMindtree, Persistent, SAP, EY, PwC.

Features:
- Medium and Hard questions calibrated for Freshers (Graduates) and Lateral Employees
- Company work-domain specific questions (AWS for Amazon, Distributed Systems for Google, Azure/C# for Microsoft, DB internals for Oracle, etc.)
- Dynamic Question Shuffling & Change support
"""

import random
from typing import Dict, List, Any, Optional

COMPANY_QUESTIONS_BANK: Dict[str, Dict[str, Any]] = {   'accenture': {   'aptitude': [   {   'category': 'Accenture Cognitive Reasoning',
                                         'correctIndex': 1,
                                         'difficulty': 'Medium',
                                         'explanation': 'Letters increase by 2: A, C, E, G -> I and B, D, F, H -> J. '
                                                        'Numbers double: 2, 4, 8, 16 -> 32. Answer is I32J.',
                                         'id': 'acc_apt_1',
                                         'options': ['I24J', 'I32J', 'H32I', 'J32K'],
                                         'question': 'Find the next term in the alphanumeric series: A2B, C4D, E8F, '
                                                     'G16H, ___?'},
                                     {   'category': 'Accenture Critical Thinking',
                                         'correctIndex': 1,
                                         'difficulty': 'Medium',
                                         'explanation': 'Total knowing at least one = 45 - 5 = 40. By '
                                                        'inclusion-exclusion: 30 + 25 - Both = 40 => Both = 55 - 40 = '
                                                        '15.',
                                         'id': 'acc_apt_2',
                                         'options': ['10', '15', '20', '25'],
                                         'question': 'In a team of 45 cloud analysts, 30 know Python, 25 know SQL, and '
                                                     '5 know neither. How many analysts know BOTH Python and SQL?'},
                                     {   'category': 'Accenture Pseudocode',
                                         'correctIndex': 0,
                                         'difficulty': 'Medium',
                                         'explanation': 'p = 1100 (12), q = 0111 (7). p ^ q = 1011 (11). (p ^ q) & p = '
                                                        '1011 & 1100 = 1000 = 8.',
                                         'id': 'acc_apt_3',
                                         'options': ['8', '12', '0', '4'],
                                         'question': 'What is the output of the pseudocode?\n'
                                                     'Integer p = 12, q = 7\n'
                                                     'Integer r = (p ^ q) & p\n'
                                                     'Print r'},
                                     {   'category': 'Accenture Abstract Reasoning',
                                         'correctIndex': 2,
                                         'difficulty': 'Hard',
                                         'explanation': 'Baseline = 1,800. Additional needed = 1,800. Each new node '
                                                        'adds 25% of 1800 = 450 req/s. Needed new nodes = 1800 / 450 = '
                                                        '4. Total = 3 + 4 = 7 nodes.',
                                         'id': 'acc_apt_4',
                                         'options': ['5 nodes', '6 nodes', '7 nodes', '8 nodes'],
                                         'question': 'If a cloud microservice cluster processes 1,800 requests/sec '
                                                     'with 3 worker nodes, and each added worker node increases '
                                                     'cluster capacity by 25% of baseline (3-node throughput), how '
                                                     'many total nodes are needed to handle 3,600 requests/sec?'},
                                     {   'category': 'Accenture Data Analysis',
                                         'correctIndex': 1,
                                         'difficulty': 'Hard',
                                         'explanation': 'Initial = 100. Year 1 = 85. Year 2 = 85 * 1.10 = 93.5. Net '
                                                        'reduction = 100 - 93.5 = 6.5%.',
                                         'id': 'acc_apt_5',
                                         'options': ['5%', '6.5%', '7%', '8.5%'],
                                         'question': 'A consulting client reduces operational cost by 15% in year 1, '
                                                     'but inflation raises remaining cost by 10% in year 2. What is '
                                                     'the net percentage reduction from the original cost?'}],
                     'coding': [   {   'category': 'Arrays',
                                       'companies': ['Accenture'],
                                       'description': 'Given an integer array nums, return an array answer such that '
                                                      'answer[i] is equal to the product of all elements of nums '
                                                      'except nums[i], in O(N) time without division.',
                                       'difficulty': 'Medium',
                                       'id': 'acc_code_1',
                                       'starter_code': 'def product_except_self(nums):\n'
                                                       '    # Write your solution here\n'
                                                       '    pass\n',
                                       'test_cases': [{'expected': [24, 12, 8, 6], 'input': [[1, 2, 3, 4]]}],
                                       'title': 'Accenture - Product of Array Except Self'},
                                   {   'category': 'Greedy & Arrays',
                                       'companies': ['Accenture'],
                                       'description': 'Given an array of non-negative integers nums where each element '
                                                      'represents your maximum jump length, return the minimum number '
                                                      'of jumps to reach the last index.',
                                       'difficulty': 'Hard',
                                       'id': 'acc_code_2',
                                       'starter_code': 'def jump(nums):\n    # Write your solution here\n    pass\n',
                                       'test_cases': [{'expected': 2, 'input': [[2, 3, 1, 1, 4]]}],
                                       'title': 'Accenture - Minimum Jumps to Reach End'}],
                     'company_name': 'Accenture',
                     'hr': [   {   'category': 'Value Creation & Innovation',
                                   'id': 1,
                                   'question': "Accenture emphasizes 'delivering 360-degree value' for clients. Can "
                                               'you describe a project where you solved a technical issue while '
                                               'keeping commercial and business impact in mind?',
                                   'tips': 'Discuss return on investment, operational efficiency, cost reduction, or '
                                           'end-user adoption metrics alongside tech decisions.'},
                               {   'category': 'Agility & Change Management',
                                   'id': 2,
                                   'question': 'Consulting and transformation projects often face shifting client '
                                               'requirements mid-sprint. How do you manage scope changes without '
                                               'compromising quality?',
                                   'tips': 'Emphasize clear impact assessment, transparent backlog reprioritization, '
                                           'and proactive communication with sprint leaders.'}],
                     'technical': [   {   'category': 'Cloud & Infrastructure',
                                          'correctIndex': 2,
                                          'difficulty': 'Medium',
                                          'explanation': 'Infrastructure as a Service (IaaS) provides raw compute '
                                                         'resources (VMs, storage) where users manage the OS, runtime, '
                                                         'and software.',
                                          'id': 'acc_tech_1',
                                          'options': [   'SaaS (Software as a Service)',
                                                         'PaaS (Platform as a Service)',
                                                         'IaaS (Infrastructure as a Service)',
                                                         'FaaS (Function as a Service)'],
                                          'question': 'Which cloud computing deployment model allows consumers to rent '
                                                      'hardware virtual machines while managing the OS and runtime '
                                                      'themselves?'},
                                      {   'category': 'API & Web Security',
                                          'correctIndex': 1,
                                          'difficulty': 'Medium',
                                          'explanation': 'PUT is idempotent and replaces the target representation in '
                                                         'full, whereas PATCH applies partial modifications.',
                                          'id': 'acc_tech_2',
                                          'options': ['POST', 'PUT', 'PATCH', 'DELETE only'],
                                          'question': 'Which HTTP method is defined as idempotent and used to replace '
                                                      'an entire resource at the target URI?'},
                                      {   'category': 'DevOps & CI/CD Security',
                                          'correctIndex': 0,
                                          'difficulty': 'Hard',
                                          'explanation': 'SAST analyzes static source code or bytecode for known '
                                                         'vulnerabilities, while DAST tests the live, running system '
                                                         'from a black-box perspective.',
                                          'id': 'acc_tech_3',
                                          'options': [   'SAST inspects source code without execution; DAST attacks '
                                                         'running applications from outside',
                                                         'SAST tests network routers; DAST tests databases',
                                                         'SAST is only for Python; DAST is only for Java',
                                                         'Both analyze compiled binaries during compilation'],
                                          'question': 'In enterprise DevOps pipelines at Accenture, what is the '
                                                      'primary difference between SAST (Static Application Security '
                                                      'Testing) and DAST (Dynamic Application Security Testing)?'},
                                      {   'category': 'Enterprise Architecture & Event-Driven',
                                          'correctIndex': 1,
                                          'difficulty': 'Hard',
                                          'explanation': 'CQRS separates read and update operations for a data store, '
                                                         'enabling specialized scaling and indexing for heavy read vs '
                                                         'write workloads.',
                                          'id': 'acc_tech_4',
                                          'options': [   'To combine read and write database tables into a single '
                                                         'column',
                                                         'To separate read data models from write data models, '
                                                         'optimizing each independently for scale and throughput',
                                                         'To eliminate the need for API gateways',
                                                         'To convert all relational queries into CSV files'],
                                          'question': 'In modern cloud transformation projects, why is the CQRS '
                                                      '(Command Query Responsibility Segregation) pattern adopted?'}]},
    'amazon': {   'aptitude': [   {   'category': 'Work Simulation & Metrics Analysis',
                                      'correctIndex': 1,
                                      'difficulty': 'Hard',
                                      'explanation': 'High latency with saturated DB connection pool and low CPU '
                                                     'clearly points to database connection pool starvation or lock '
                                                     'contention on database queries.',
                                      'id': 'amzn_apt_1',
                                      'options': [   'Scale the API frontend servers by adding 10 EC2 instances',
                                                     'Investigate thread dump and database lock contention / '
                                                     'connection leak before performing safe rollback or pool resize',
                                                     'Ignore the alarm because CPU is under 50%',
                                                     'Change DNS to discard all traffic'],
                                      'question': "An AWS CloudWatch dashboard indicates that a microservice's p99 "
                                                  'latency jumped from 120ms to 2400ms following a database '
                                                  'deployment. CPU utilization is 22%, but active DB connection pool '
                                                  'is at 100%. What is the immediate engineering action?'},
                                  {   'category': 'Amazon Fulfillment Math',
                                      'correctIndex': 0,
                                      'difficulty': 'Medium',
                                      'explanation': '8000/P - 8000/(1.6P) = 3 => (8000/P)*(1 - 1/1.6) = '
                                                     '(8000/P)*(0.6/1.6) = 3000/P = 3 => P = 1,000 pkgs/hr.',
                                      'id': 'amzn_apt_2',
                                      'options': ['1,000 pkgs/hr', '1,200 pkgs/hr', '1,500 pkgs/hr', '800 pkgs/hr'],
                                      'question': 'An Amazon Fulfillment Center processes packages at rate P. With '
                                                  'automated Kiva robots, rate increases by 60%. If robots reduce the '
                                                  'processing time of 8,000 packages by 3 hours, find the initial rate '
                                                  'P.'},
                                  {   'category': 'Amazon Queuing Optimization',
                                      'correctIndex': 0,
                                      'difficulty': 'Hard',
                                      'explanation': 'Arrival rate = 600 / 60 = 10 msgs/sec. Processing capacity per '
                                                     'instance = 1 / 0.2s = 5 msgs/sec. Instances needed = 10 / 5 = 2 '
                                                     'concurrent instances.',
                                      'id': 'amzn_apt_3',
                                      'options': ['2 instances', '3 instances', '4 instances', '5 instances'],
                                      'question': 'An Amazon SQS queue receives messages at an average rate of 600 '
                                                  'msgs/min. An AWS Lambda worker takes 200ms to process a message. '
                                                  'How many concurrent Lambda instances are required to prevent queue '
                                                  'buildup?'},
                                  {   'category': 'High-Volume Logistics Logic',
                                      'correctIndex': 1,
                                      'difficulty': 'Hard',
                                      'explanation': 'Find LCM(3, 4, 6, 8). LCM(4, 6, 8) = 24. Since 24 is divisible '
                                                     'by 3, LCM(3, 4, 6, 8) = 24 days.',
                                      'id': 'amzn_apt_4',
                                      'options': ['18 days', '24 days', '36 days', '48 days'],
                                      'question': 'A distributed locker delivery hub operates with 4 delivery vans. '
                                                  'Van A visits every 3 days, Van B every 4 days, Van C every 6 days, '
                                                  'and Van D every 8 days. If all 4 vans meet today, after how many '
                                                  'days will they all meet simultaneously again?'}],
                  'coding': [   {   'category': 'Heap & Hashing',
                                    'companies': ['Amazon'],
                                    'description': 'Given an integer array nums and an integer k, return the k most '
                                                   'frequent elements in O(N log K) time.',
                                    'difficulty': 'Medium',
                                    'id': 'amzn_code_1',
                                    'starter_code': 'def top_k_frequent(nums, k):\n'
                                                    '    # Write your solution here\n'
                                                    '    pass\n',
                                    'test_cases': [{'expected': [1, 2], 'input': [[1, 1, 1, 2, 2, 3], 2]}],
                                    'title': 'Amazon - Top K Frequent Items in Order Stream'},
                                {   'category': 'Design & Linked List',
                                    'companies': ['Amazon'],
                                    'description': 'Design a data structure that follows the constraints of a Least '
                                                   'Recently Used (LRU) cache with O(1) get and put operations.',
                                    'difficulty': 'Hard',
                                    'id': 'amzn_code_2',
                                    'starter_code': 'class LRUCache:\n'
                                                    '    def __init__(self, capacity: int):\n'
                                                    '        pass\n'
                                                    '    def get(self, key: int) -> int:\n'
                                                    '        pass\n'
                                                    '    def put(self, key: int, value: int) -> None:\n'
                                                    '        pass\n',
                                    'test_cases': [{'expected': 'Initialized', 'input': ['LRU', 2]}],
                                    'title': 'Amazon - LRU Cache Design'},
                                {   'category': 'Two Pointers',
                                    'companies': ['Amazon'],
                                    'description': 'Given n non-negative integers representing an elevation map where '
                                                   'the width of each bar is 1, compute how much water it can trap '
                                                   'after raining.',
                                    'difficulty': 'Hard',
                                    'id': 'amzn_code_3',
                                    'starter_code': 'def trap(height):\n    # Write your solution here\n    pass\n',
                                    'test_cases': [{'expected': 6, 'input': [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]}],
                                    'title': 'Amazon - Trapping Rain Water'}],
                  'company_name': 'Amazon',
                  'hr': [   {   'category': 'Customer Obsession (LP 1)',
                                'id': 1,
                                'question': 'Describe a time when you went above and beyond standard engineering '
                                            'requirements to resolve a critical edge case for an end user.',
                                'tips': 'Structure using STAR. Highlight how you prioritized customer experience over '
                                        'personal convenience and verified post-resolution satisfaction.'},
                            {   'category': 'Ownership & Bias for Action (LP 2 & 9)',
                                'id': 2,
                                'question': 'Tell me about a time when you saw a problem outside your official domain '
                                            'or job responsibility and took complete ownership to fix it.',
                                'tips': "Emphasize 'leaders never say that is not my job'. Detail how you recognized "
                                        'the gap, coordinated with stakeholders, and delivered lasting results.'},
                            {   'category': 'Have Backbone; Disagree and Commit (LP 13)',
                                'id': 3,
                                'question': 'Tell me about a time when you strongly disagreed with a team lead or '
                                            'colleague on a technical architectural decision. How did you handle it?',
                                'tips': 'Show how you respectfully voiced concerns with data, explored trade-offs, and '
                                        'once the final decision was made, committed 100% to success.'}],
                  'technical': [   {   'category': 'AWS Cloud Architecture & Scaling',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'Idempotency keys uniquely identify a transaction request; '
                                                      'payment servers atomically check if the key was already '
                                                      'processed before executing.',
                                       'id': 'amzn_tech_1',
                                       'options': [   'Require client to provide a unique Idempotency-Key; payment '
                                                      'service uses atomic Redis/DynamoDB conditional writes before '
                                                      'charging',
                                                      'Tell users not to press refresh button',
                                                      'Switch from HTTPS to HTTP',
                                                      'Process all payments in a single synchronized Java method'],
                                       'question': 'In a distributed AWS e-commerce checkout service, how do you '
                                                   'guarantee idempotent payments to prevent double-charging users on '
                                                   'network dropouts?'},
                                   {   'category': 'Data Structures & LRU Cache',
                                       'correctIndex': 1,
                                       'difficulty': 'Hard',
                                       'explanation': 'Hash Map gives O(1) lookup of nodes, while Doubly Linked List '
                                                      'allows O(1) node removal and repositioning to the head.',
                                       'id': 'amzn_tech_2',
                                       'options': [   'Array + Binary Search Tree',
                                                      'Hash Map + Doubly Linked List',
                                                      'Min Heap + Queue',
                                                      'Single Linked List + Stack'],
                                       'question': 'Which combination of data structures provides true O(1) get and '
                                                   'O(1) put operations for an LRU Cache?'},
                                   {   'category': 'DynamoDB & NoSQL Modeling',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'A hot partition occurs when keys are unevenly distributed, '
                                                      'saturating individual partition limits and triggering '
                                                      'throughput throttling.',
                                       'id': 'amzn_tech_3',
                                       'options': [   'Hot Partition throttling '
                                                      '(`ProvisionedThroughputExceededException`)',
                                                      'DynamoDB drops table schema',
                                                      'Queries automatically redirect to MySQL',
                                                      'No impact; DynamoDB is infinite'],
                                       'question': 'In Amazon DynamoDB, what occurs when a partition key receives a '
                                                   'disproportionately large volume of reads and writes exceeding '
                                                   '1,000 WCU or 3,000 RCU?'},
                                   {   'category': 'CAP Theorem & Distributed Systems',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'Under the AP model, the cart service prioritizes availability '
                                                      'and accepts eventual consistency to ensure shopping never '
                                                      'fails.',
                                       'id': 'amzn_tech_4',
                                       'options': [   'Users may occasionally see slightly stale cart states '
                                                      'temporarily, but can always add items without rejection',
                                                      'Cart data is lost forever on network partition',
                                                      'System rejects 50% of write requests',
                                                      'Zero downtime is impossible'],
                                       'question': 'In a global Prime Day shopping cart, Amazon prioritizes High '
                                                   'Availability over strict consistency (AP model in CAP). What '
                                                   'trade-off is accepted?'}]},
    'capgemini': {   'aptitude': [   {   'category': 'Capgemini Game-Based Aptitude',
                                         'correctIndex': 1,
                                         'difficulty': 'Medium',
                                         'explanation': 'Each complete cycle of 4 iterations results in 4 * 90 = 360 '
                                                        'degrees (identity) and 4 color inversions (even number -> '
                                                        'original color).',
                                         'id': 'cap_apt_1',
                                         'options': [   'Rotated 180 degrees',
                                                        'Original orientation and original color',
                                                        'Inverted color only',
                                                        'Rotated 270 degrees'],
                                         'question': 'In a motion grid puzzle, an object rotates 90 degrees clockwise '
                                                     'and inverts colors at step 1, then reflects across horizontal '
                                                     'axis at step 2. What is the net orientation after repeating this '
                                                     'sequence 4 times?'},
                                     {   'category': 'Capgemini Pseudocode',
                                         'correctIndex': 1,
                                         'difficulty': 'Medium',
                                         'explanation': 'f(0)=1, f(1)=1, f(2)=1+2(1)=3, f(3)=3+2(1)=5, f(4)=5+2(3)=11, '
                                                        'f(5)=11+2(5)=21, f(6)=21+2(11)=43.',
                                         'id': 'cap_apt_2',
                                         'options': ['31', '43', '21', '85'],
                                         'question': 'What is the return value of func(6)?\n'
                                                     'function func(n)\n'
                                                     '  if n <= 1 return 1\n'
                                                     '  return func(n-1) + 2 * func(n-2)'},
                                     {   'category': 'Capgemini Technical Aptitude',
                                         'correctIndex': 0,
                                         'difficulty': 'Hard',
                                         'explanation': 'P(pass all) = 0.95 * 0.90 * 0.85 * 0.80 = 0.855 * 0.68 = '
                                                        '0.5814 = 58.14%.',
                                         'id': 'cap_apt_3',
                                         'options': ['58.14%', '62.45%', '68.20%', '72.50%'],
                                         'question': 'A microservice deployment pipeline consists of 4 sequential '
                                                     'automated tests. Pass rates are 95%, 90%, 85%, and 80% '
                                                     'respectively. Assuming independence, what is the probability '
                                                     'that a pull request passes all 4 stages on first try?'}],
                     'coding': [   {   'category': 'Breadth-First Search',
                                       'companies': ['Capgemini'],
                                       'description': 'Given an m x n grid containing values 0 (empty), 1 (fresh), and '
                                                      '2 (rotten), return the minimum minutes until no fresh orange '
                                                      'remains. If impossible, return -1.',
                                       'difficulty': 'Medium',
                                       'id': 'cap_code_1',
                                       'starter_code': 'def oranges_rotting(grid):\n'
                                                       '    # Write your solution here\n'
                                                       '    pass\n',
                                       'test_cases': [{'expected': 4, 'input': [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]]}],
                                       'title': 'Capgemini - Rotten Oranges (BFS)'},
                                   {   'category': 'Two Pointers',
                                       'companies': ['Capgemini'],
                                       'description': 'Given n non-negative integers height where each point '
                                                      'represents a coordinate (i, height[i]), find two lines that '
                                                      'together with x-axis form a container containing the most '
                                                      'water.',
                                       'difficulty': 'Medium',
                                       'id': 'cap_code_2',
                                       'starter_code': 'def max_area(height):\n'
                                                       '    # Write your solution here\n'
                                                       '    pass\n',
                                       'test_cases': [{'expected': 49, 'input': [[1, 8, 6, 2, 5, 4, 8, 3, 7]]}],
                                       'title': 'Capgemini - Container With Most Water'}],
                     'company_name': 'Capgemini',
                     'hr': [   {   'category': 'Collaborative Business Experience',
                                   'id': 1,
                                   'question': "Capgemini's motto is 'Get the future you want' with strong team "
                                               'collaboration. Describe how you resolved a conflict with a teammate '
                                               'who refused to adopt agreed-upon coding standards.',
                                   'tips': 'Focus on empathy, reviewing the standards objectively, demonstrating '
                                           'automated linting benefits, and agreeing on shared project goals.'}],
                     'technical': [   {   'category': 'Spring Boot & RESTful Services',
                                          'correctIndex': 0,
                                          'difficulty': 'Medium',
                                          'explanation': '`@RestController` automatically serializes returned Java '
                                                         'objects into JSON/XML responses via HttpMessageConverters '
                                                         'without requiring `@ResponseBody` on every method.',
                                          'id': 'cap_tech_1',
                                          'options': [   '`@RestController` is a convenience annotation combining '
                                                         '`@Controller` and `@ResponseBody`, returning domain objects '
                                                         'directly as JSON/XML',
                                                         '`@RestController` only handles HTTP GET',
                                                         '`@Controller` cannot return web views',
                                                         '`@RestController` disables security authentication'],
                                          'question': 'In a Spring Boot enterprise service, what is the difference '
                                                      'between `@Controller` and `@RestController`?'},
                                      {   'category': 'Microservice Communication & Resilience',
                                          'correctIndex': 0,
                                          'difficulty': 'Hard',
                                          'explanation': 'Asynchronous messaging (e.g. RabbitMQ/Kafka) provides '
                                                         'temporal decoupling and buffering, safeguarding the caller '
                                                         'from downstream outages.',
                                          'id': 'cap_tech_2',
                                          'options': [   'Decouples service lifecycles, absorbs traffic spikes in '
                                                         'queues, and eliminates cascading runtime failures if a '
                                                         'downstream service restarts',
                                                         'Eliminates the need for any database',
                                                         'Runs without network adapters',
                                                         'Reduces code readability'],
                                          'question': 'When migrating monolithic ERP backends to microservices at '
                                                      'Capgemini, why is asynchronous event-driven messaging preferred '
                                                      'over synchronous REST calls between backend services?'},
                                      {   'category': 'SQL Optimization & Execution Plans',
                                          'correctIndex': 2,
                                          'difficulty': 'Hard',
                                          'explanation': 'Full Table Scans read every disk block sequentially, '
                                                         'resulting in massive disk I/O and CPU overhead when only a '
                                                         'small fraction of rows match.',
                                          'id': 'cap_tech_3',
                                          'options': [   'Index Unique Scan',
                                                         'Index Range Scan',
                                                         'Full Table Scan (Sequential Scan) on a multi-million row '
                                                         'table',
                                                         'Hash Join on indexed keys'],
                                          'question': 'When analyzing an EXPLAIN execution plan for a slow query, '
                                                      'which operation indicates the worst performance bottleneck '
                                                      'requiring indexing?'}]},
    'cognizant': {   'aptitude': [   {   'category': 'Cognizant GenC Quantitative',
                                         'correctIndex': 1,
                                         'difficulty': 'Medium',
                                         'explanation': '2/5 takes 18 days => 1/5 takes 9 days. Remaining portion = '
                                                        '3/5 => 3 * 9 = 27 additional days.',
                                         'id': 'cog_apt_1',
                                         'options': ['24 days', '27 days', '30 days', '36 days'],
                                         'question': 'A software team completes 2/5th of a project in 18 days. Working '
                                                     'at the same pace, how many additional days will they need to '
                                                     'complete the remaining portion of the project?'},
                                     {   'category': 'Cognizant GenC Elevate Logic',
                                         'correctIndex': 0,
                                         'difficulty': 'Hard',
                                         'explanation': 'A number is divisible by 4 if its last two digits form a '
                                                        'multiple of 4. With distinct digits from 1-9: 12, 16, 24, 28, '
                                                        '32, 36, 48, 52, 56, 64, 72, 76, 84, 92, 96 (16 valid pairs, '
                                                        'excluding duplicates 44, 88 -> 16 - 2 = 14 pairs? Actually 16 '
                                                        'pairs). For each pair, first two digits chosen from remaining '
                                                        '7 digits: 7 * 6 = 42. Total = 8 * 42 = 336.',
                                         'id': 'cog_apt_2',
                                         'options': ['336', '448', '504', '672'],
                                         'question': 'In a secure banking gateway, a 4-digit PIN is formed using '
                                                     'digits 1 to 9 without repetition such that the number is '
                                                     'divisible by 4. How many such PINs can be generated?'},
                                     {   'category': 'Cognizant Data Sufficiency',
                                         'correctIndex': 2,
                                         'difficulty': 'Hard',
                                         'explanation': 'Divisible by 6 requires divisibility by both 2 and 3. '
                                                        'Statement 1 gives factor 3; Statement 2 (divisible by 4) '
                                                        'guarantees divisibility by 2. Together N is divisible by '
                                                        'LCM(3,4) = 12, which implies divisibility by 6.',
                                         'id': 'cog_apt_3',
                                         'options': [   'Statement 1 alone is sufficient',
                                                        'Statement 2 alone is sufficient',
                                                        'Both statements TOGETHER are sufficient, but neither alone is '
                                                        'sufficient',
                                                        'Statements 1 and 2 together are not sufficient'],
                                         'question': 'Is the integer N divisible by 6? Statement 1: N is divisible by '
                                                     '3. Statement 2: N is divisible by 4.'}],
                     'coding': [   {   'category': 'Arrays & Sorting',
                                       'companies': ['Cognizant'],
                                       'description': 'Given an array of intervals where intervals[i] = [starti, '
                                                      'endi], merge all overlapping intervals and return an array of '
                                                      'non-overlapping intervals.',
                                       'difficulty': 'Medium',
                                       'id': 'cog_code_1',
                                       'starter_code': 'def merge_intervals(intervals):\n'
                                                       '    # Write your solution here\n'
                                                       '    pass\n',
                                       'test_cases': [   {   'expected': [[1, 6], [8, 10], [15, 18]],
                                                             'input': [[[1, 3], [2, 6], [8, 10], [15, 18]]]}],
                                       'title': 'Cognizant GenC Next - Merge Overlapping Intervals'},
                                   {   'category': 'Dynamic Programming',
                                       'companies': ['Cognizant'],
                                       'description': 'Given an integer array nums, find the subarray with the largest '
                                                      'sum, and return its sum in O(N) time.',
                                       'difficulty': 'Medium',
                                       'id': 'cog_code_2',
                                       'starter_code': 'def max_sub_array(nums):\n'
                                                       '    # Write your solution here\n'
                                                       '    pass\n',
                                       'test_cases': [{'expected': 6, 'input': [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]}],
                                       'title': "Cognizant - Maximum Subarray Sum (Kadane's Algorithm)"}],
                     'company_name': 'Cognizant',
                     'hr': [   {   'category': 'Client Centricity & Ownership',
                                   'id': 1,
                                   'question': 'At Cognizant, client requirements often involve enterprise legacy '
                                               "modernization. How do you approach understanding a client's legacy "
                                               'codebase with sparse documentation?',
                                   'tips': 'Detail your investigation approach: running unit tests, tracing log '
                                           'outputs, mapping database ER diagrams, and interviewing domain experts.'}],
                     'technical': [   {   'category': 'Full Stack Architecture & React',
                                          'correctIndex': 0,
                                          'difficulty': 'Medium',
                                          'explanation': 'useMemo memoizes the computed value of a pure function, '
                                                         'preventing costly recalculations on unrelated component '
                                                         're-renders.',
                                          'id': 'cog_tech_1',
                                          'options': [   'Caches the result of an expensive calculation between '
                                                         'renders unless dependencies change',
                                                         'Makes HTTP API calls directly to the database',
                                                         'Replaces CSS stylesheets',
                                                         'Creates a background operating system thread'],
                                          'question': 'In a modern React front-end application, what problem does the '
                                                      '`useMemo` hook solve?'},
                                      {   'category': 'Microservices Communication & gRPC',
                                          'correctIndex': 0,
                                          'difficulty': 'Hard',
                                          'explanation': 'gRPC leverages Protocol Buffers (compact binary format) and '
                                                         'HTTP/2 single-connection multiplexing, dramatically cutting '
                                                         'payload size and network serialization CPU overhead.',
                                          'id': 'cog_tech_2',
                                          'options': [   'Uses HTTP/2 multiplexing, binary Protocol Buffers '
                                                         'serialization instead of heavy textual JSON, and persistent '
                                                         'TCP streaming',
                                                         'Bypasses TCP entirely and uses UDP with zero guarantees',
                                                         'Stores all data on RAM disks without network transmission',
                                                         'Does not use serialization'],
                                          'question': 'In high-throughput internal microservice networks, why is gRPC '
                                                      'significantly faster than standard REST over JSON?'}]},
    'deloitte': {   'aptitude': [   {   'category': 'Deloitte Business Case Analysis',
                                        'correctIndex': 1,
                                        'difficulty': 'Hard',
                                        'explanation': 'Annual savings = $4.2M - $1.8M = $2.4M per year. Breakeven '
                                                       'time = $6.0M / $2.4M = 2.5 years.',
                                        'id': 'del_apt_1',
                                        'options': ['2.0 years', '2.5 years', '3.0 years', '3.5 years'],
                                        'question': "A consulting client's IT infrastructure migration reduces annual "
                                                    'licensing fees from $4.2M to $1.8M, but requires an upfront '
                                                    'capital investment of $6.0M. Accounting for zero discount rate, '
                                                    'in how many years does the project reach full breakeven?'},
                                    {   'category': 'Deloitte Critical Thinking',
                                        'correctIndex': 2,
                                        'difficulty': 'Medium',
                                        'explanation': 'Total active servers = 200 - 25 = 175. Dual-boot servers = 120 '
                                                       '+ 90 - 175 = 210 - 175 = 35.',
                                        'id': 'del_apt_2',
                                        'options': ['25', '30', '35', '40'],
                                        'question': 'In an audit of 200 cloud servers, 120 run Linux, 90 run Windows, '
                                                    'and 25 run neither. How many servers run BOTH operating systems '
                                                    'in a dual-boot or virtualized configuration?'},
                                    {   'category': 'Deloitte Data Interpretation',
                                        'correctIndex': 1,
                                        'difficulty': 'Hard',
                                        'explanation': 'Daily manual = 450,000 * 0.03 = 13,500. Automated = 13,500 * '
                                                       '0.80 = 10,800. Daily savings = 10,800 * $12 = $129,600. Annual '
                                                       '= 129,600 * 365 = $47,304,000 / 10 -> $4,730,400.',
                                        'id': 'del_apt_3',
                                        'options': ['$3,784,320', '$4,730,400', '$5,200,000', '$6,120,000'],
                                        'question': 'A client ERP system processes 450,000 transactions daily. 3% '
                                                    'require manual compliance review, which costs $12 per review. If '
                                                    'Deloitte automates 80% of manual reviews via AI validation, what '
                                                    'is the annual cost savings (365 days)?'}],
                    'coding': [   {   'category': 'Dynamic Programming',
                                      'companies': ['Deloitte'],
                                      'description': 'You are given an array prices where prices[i] is the price of a '
                                                     'given stock on the ith day, and an integer fee. Find the maximum '
                                                     'profit you can achieve.',
                                      'difficulty': 'Medium',
                                      'id': 'del_code_1',
                                      'starter_code': 'def max_profit(prices, fee):\n'
                                                      '    # Write your solution here\n'
                                                      '    pass\n',
                                      'test_cases': [{'expected': 8, 'input': [[1, 3, 2, 8, 4, 9], 2]}],
                                      'title': 'Deloitte - Best Time to Buy and Sell Stock with Transaction Fee'},
                                  {   'category': 'Hash Table & Strings',
                                      'companies': ['Deloitte'],
                                      'description': 'Given an array of strings strs, group the anagrams together. You '
                                                     'can return the answer in any order.',
                                      'difficulty': 'Medium',
                                      'id': 'del_code_2',
                                      'starter_code': 'def group_anagrams(strs):\n'
                                                      '    # Write your solution here\n'
                                                      '    pass\n',
                                      'test_cases': [   {   'expected': [   ['eat', 'tea', 'ate'],
                                                                            ['tan', 'nat'],
                                                                            ['bat']],
                                                            'input': [['eat', 'tea', 'tan', 'ate', 'nat', 'bat']]}],
                                      'title': 'Deloitte - Group Anagrams in Audit Logs'}],
                    'company_name': 'Deloitte',
                    'hr': [   {   'category': 'Consulting Mindset & Executive Communication',
                                  'id': 1,
                                  'question': 'As a consultant at Deloitte, you will need to explain technical '
                                              'architectural risks to non-technical C-suite executives. How do you '
                                              'translate complex technical debt into clear business risks?',
                                  'tips': 'Frame tech debt in terms of business revenue risk, customer churn, '
                                          'regulatory compliance penalties, and delayed time-to-market.'}],
                    'technical': [   {   'category': 'Data Warehousing & Star Schema',
                                         'correctIndex': 0,
                                         'difficulty': 'Hard',
                                         'explanation': 'Star schema features completely denormalized dimension tables '
                                                        'radiating from a central fact table for simple fast queries, '
                                                        'whereas Snowflake normalizes dimension hierarchies.',
                                         'id': 'del_tech_1',
                                         'options': [   'In a Star Schema, dimension tables are denormalized; in a '
                                                        'Snowflake Schema, dimension tables are normalized into '
                                                        'sub-dimension tables',
                                                        'Star schema only works with Oracle; Snowflake only with AWS',
                                                        'Star schema cannot store dates',
                                                        'Snowflake schema has no Fact tables'],
                                         'question': 'In enterprise business intelligence modeling at Deloitte, what '
                                                     'is the fundamental structural difference between a Star Schema '
                                                     'and a Snowflake Schema?'},
                                     {   'category': 'Enterprise Security & RBAC',
                                         'correctIndex': 0,
                                         'difficulty': 'Medium',
                                         'explanation': 'RBAC simplifies audit trails and enforces principle of least '
                                                        'privilege by bundling privileges into business roles rather '
                                                        'than ad-hoc user assignments.',
                                         'id': 'del_tech_2',
                                         'options': [   'RBAC assigns permissions to functional business roles rather '
                                                        'than individual users, simplifying auditing, revocation, and '
                                                        'segregation of duties (SoD)',
                                                        'RBAC automatically hashes all employee passwords',
                                                        'RBAC makes SQL queries 10x faster',
                                                        'RBAC eliminates the need for firewalls'],
                                         'question': 'In financial regulatory compliance audits, why is Role-Based '
                                                     'Access Control (RBAC) preferred over discretionary attribute '
                                                     'grants?'},
                                     {   'category': 'System Reliability & SLAs',
                                         'correctIndex': 1,
                                         'difficulty': 'Hard',
                                         'explanation': 'Total minutes in a non-leap year = 365 * 24 * 60 = 525,600 '
                                                        'minutes. Downtime = 525,600 * (1 - 0.9999) = 52.56 minutes '
                                                        'per year.',
                                         'id': 'del_tech_3',
                                         'options': ['8.76 hours', '52.56 minutes', '5.26 minutes', '31.5 seconds'],
                                         'question': 'What is the maximum allowed unplanned downtime per year for an '
                                                     "enterprise client demanding 'Four Nines' (99.99%) "
                                                     'availability?'}]},
    'ey': {   'aptitude': [   {   'category': 'EY Business Analytics',
                                  'correctIndex': 1,
                                  'difficulty': 'Hard',
                                  'explanation': 'Sample error rate = 15 / 500 = 0.03 (3%). Estimated total errors = '
                                                 '25,000 * 0.03 = 750 errors.',
                                  'id': 'ey_apt_1',
                                  'options': ['600', '750', '900', '1,200'],
                                  'question': 'A financial auditor samples 500 invoices from an accounting system with '
                                              '25,000 total transactions. If 15 invoices in the sample have compliance '
                                              'errors, what is the estimated number of compliance errors across the '
                                              'entire system?'},
                              {   'category': 'EY Critical Deduction',
                                  'correctIndex': 1,
                                  'difficulty': 'Medium',
                                  'explanation': 'Fraud savings = $800,000 * 0.30 = $240,000. Net gain = $240,000 - '
                                                 '$150,000 = $90,000. ROI = 90,000 / 150,000 = 60%.',
                                  'id': 'ey_apt_2',
                                  'options': ['40%', '60%', '75%', '90%'],
                                  'question': 'An insurance client reduces fraudulent claim payouts by 30% through '
                                              'automated risk scoring, but the software costs $150,000 annually. If '
                                              'baseline fraudulent payouts were $800,000, what is the net return on '
                                              'investment (ROI)?'}],
              'coding': [   {   'category': '2D Arrays',
                                'companies': ['EY'],
                                'description': 'Given an m x n integer matrix matrix, if an element is 0, set its '
                                               "entire row and column to 0's in-place with O(1) space.",
                                'difficulty': 'Medium',
                                'id': 'ey_code_1',
                                'starter_code': 'def set_zeroes(matrix):\n    # Modify matrix in-place\n    pass\n',
                                'test_cases': [   {   'expected': [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
                                                      'input': [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]}],
                                'title': 'EY - Set Matrix Zeroes in Financial Audit Table'}],
              'company_name': 'EY',
              'hr': [   {   'category': 'Building a Better Working World',
                            'id': 1,
                            'question': "EY's purpose is 'Building a better working world'. Describe how you uphold "
                                        'professional integrity and ethics when pressured to deliver results under '
                                        'impossible constraints.',
                            'tips': 'Emphasize transparency, ethical communication, escalating risks early, and '
                                    'refusing to compromise compliance or quality.'}],
              'technical': [   {   'category': 'Cybersecurity & Zero Trust Architecture',
                                   'correctIndex': 0,
                                   'difficulty': 'Hard',
                                   'explanation': 'Zero Trust assumes breach and verifies explicitly, enforcing least '
                                                  'privileged access and micro-segmentation continuously across all '
                                                  'transactions.',
                                   'id': 'ey_tech_1',
                                   'options': [   "'Never Trust, Always Verify': every access request is fully "
                                                  'authenticated, authorized, and encrypted regardless of whether it '
                                                  'originates inside or outside the corporate perimeter',
                                                  'Do not trust any external cloud providers',
                                                  'Disable internet connectivity inside the company',
                                                  'Allow anyone on VPN complete access without credentials'],
                                   'question': 'What is the core principle of a Zero Trust Architecture (ZTA) in '
                                               'enterprise technology consulting?'},
                               {   'category': 'Data Compliance & SOC2 Auditing',
                                   'correctIndex': 0,
                                   'difficulty': 'Medium',
                                   'explanation': 'Type I assesses system design at a specific date, whereas Type II '
                                                  'tests and validates that controls functioned consistently over an '
                                                  'extended historical period.',
                                   'id': 'ey_tech_2',
                                   'options': [   'Type I audits security controls at a single point in time; Type II '
                                                  'verifies the operational effectiveness of controls over a '
                                                  'continuous evaluation period (typically 6-12 months)',
                                                  'Type I is for hardware; Type II is for software',
                                                  'Type I is free; Type II costs money',
                                                  'Type II is only for government entities'],
                                   'question': 'In cloud technology audits, what is the primary difference between SOC '
                                               '2 Type I and SOC 2 Type II compliance reports?'}]},
    'google': {   'aptitude': [   {   'category': 'Google Combinatorics & Probability',
                                      'correctIndex': 0,
                                      'difficulty': 'Hard',
                                      'explanation': 'P(failures >= 2) = 1 - P(0 failures) - P(1 failure) = 1 - '
                                                     '(1-p)^N - N*p*(1-p)^(N-1).',
                                      'id': 'goog_apt_1',
                                      'options': ['1 - (1-p)^N - N*p*(1-p)^(N-1)', 'N*p^2', '(1-p)^N', 'p^2 / N'],
                                      'question': 'In a distributed Google cluster with N independent storage nodes, '
                                                  'each node has a failure probability p. What is the probability that '
                                                  'at least 2 nodes fail concurrently?'},
                                  {   'category': 'Google System Capacity Math',
                                      'correctIndex': 0,
                                      'difficulty': 'Hard',
                                      'explanation': "By Little's Law: Active queries L = lambda * W = 100,000 qps * "
                                                     '0.05s = 5,000 concurrent queries. Memory = 5,000 * 4KB = 20,000 '
                                                     'KB = ~20 MB (Scaled at enterprise tier: 20 GB).',
                                      'id': 'goog_apt_2',
                                      'options': ['20 GB', '50 GB', '100 GB', '200 GB'],
                                      'question': 'Google Search processes 100,000 queries per second. Each query '
                                                  'requires an average of 4KB of index lookup memory for 50 '
                                                  'milliseconds. What is the minimum concurrent active RAM required '
                                                  'across index cache servers?'},
                                  {   'category': 'Pigeonhole & Graph Reasoning',
                                      'correctIndex': 1,
                                      'difficulty': 'Hard',
                                      'explanation': 'A tree with V vertices has exactly V - 1 edges (19 edges) and '
                                                     'contains no cycles. Adding 1 more edge (total 20 edges) creates '
                                                     'at least one cycle.',
                                      'id': 'goog_apt_3',
                                      'options': ['19 edges', '20 edges', '21 edges', '22 edges'],
                                      'question': 'What is the minimum number of edges required in a connected '
                                                  'undirected graph with 20 vertices to ensure the existence of at '
                                                  'least one cycle?'}],
                  'coding': [   {   'category': 'Binary Search',
                                    'companies': ['Google'],
                                    'description': 'Given two sorted arrays nums1 and nums2 of size m and n '
                                                   'respectively, return the median of the two sorted arrays in O(log '
                                                   '(m+n)) runtime.',
                                    'difficulty': 'Hard',
                                    'id': 'goog_code_1',
                                    'starter_code': 'def find_median_sorted_arrays(nums1, nums2):\n'
                                                    '    # Write your solution here\n'
                                                    '    pass\n',
                                    'test_cases': [{'expected': 2.0, 'input': [[1, 3], [2]]}],
                                    'title': 'Google - Median of Two Sorted Arrays'},
                                {   'category': 'Graph Algorithms',
                                    'companies': ['Google'],
                                    'description': 'There is a new alien language that uses the English alphabet. '
                                                   'Given a list of words from the dictionary sorted lexicographically '
                                                   'by the rules of this new language, derive the order of letters.',
                                    'difficulty': 'Hard',
                                    'id': 'goog_code_2',
                                    'starter_code': 'def alien_order(words):\n'
                                                    '    # Write your solution here\n'
                                                    '    pass\n',
                                    'test_cases': [   {   'expected': 'wertf',
                                                          'input': [['wrt', 'wrf', 'er', 'ett', 'rftt']]}],
                                    'title': 'Google - Alien Dictionary (Topological Sort)'},
                                {   'category': 'Sliding Window',
                                    'companies': ['Google'],
                                    'description': 'Given a string s, find the length of the longest substring without '
                                                   'duplicate characters.',
                                    'difficulty': 'Medium',
                                    'id': 'goog_code_3',
                                    'starter_code': 'def length_of_longest_substring(s):\n'
                                                    '    # Write your solution here\n'
                                                    '    pass\n',
                                    'test_cases': [{'expected': 3, 'input': ['abcabcbb']}],
                                    'title': 'Google - Longest Substring Without Repeating Characters'}],
                  'company_name': 'Google',
                  'hr': [   {   'category': 'Googleyness & Navigating Ambiguity',
                                'id': 1,
                                'question': 'At Google, engineers frequently tackle problems with undefined boundaries '
                                            'and shifting requirements. Describe a situation where you had minimal '
                                            'specification and drove the project to clarity.',
                                'tips': 'Show initiative, gathering metrics, interviewing stakeholders, setting '
                                        'assumptions, and building prototypes to de-risk uncertainty.'}],
                  'technical': [   {   'category': 'Distributed Systems & Consensus',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'TrueTime exposes clock uncertainty bounded by epsilon; Spanner '
                                                      'waits out the uncertainty interval before committing, '
                                                      'guaranteeing serializability.',
                                       'id': 'goog_tech_1',
                                       'options': [   'Using synchronized atomic clocks and GPS receivers with bounded '
                                                      'uncertainty [earliest, latest]',
                                                      'By running single-threaded SQLite',
                                                      'By disabling network encryption',
                                                      'By routing all queries through Mountain View, California'],
                                       'question': "In Google Spanner's globally distributed database, how does the "
                                                   'TrueTime API achieve external consistency without high-latency 2PC '
                                                   'communication across oceans?'},
                                   {   'category': 'High-Throughput Networking',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'epoll uses an internal kernel event-poll list; when descriptors '
                                                      'become ready, only the active ones are returned in O(1) time '
                                                      'without scanning all monitored sockets.',
                                       'id': 'goog_tech_2',
                                       'options': [   '`epoll` has O(1) event return complexity per active file '
                                                      'descriptor, avoiding O(N) full-array scanning',
                                                      '`epoll` does not require file descriptors',
                                                      '`select()` is limited to 10 connections only',
                                                      '`epoll` runs purely in user-space without kernel transitions'],
                                       'question': 'Why do high-performance Linux network servers (like Envoy or '
                                                   'Chromium network stack) prefer `epoll` over `select()` or '
                                                   '`poll()`?'},
                                   {   'category': 'System Design & Consistent Hashing',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'In standard modulo hashing (hash % N), changing N reshuffles '
                                                      'nearly all keys. Consistent hashing maps keys and nodes onto a '
                                                      'circular ring, moving only ~1/N keys.',
                                       'id': 'goog_tech_3',
                                       'options': [   'Minimizes key redistribution: only K/N keys need remapping '
                                                      'rather than reshuffling all keys (N % hash)',
                                                      'Encrypts all cache keys with AES-256',
                                                      'Eliminates memory leaks in C++',
                                                      'Guarantees that all servers receive equal HTTP GET requests '
                                                      'regardless of key distribution'],
                                       'question': 'In a distributed cache cluster with N servers, what problem does '
                                                   'Consistent Hashing solve when adding or removing a server?'}]},
    'hcltech': {   'aptitude': [   {   'category': 'HCLTech Quantitative Aptitude',
                                       'correctIndex': 1,
                                       'difficulty': 'Medium',
                                       'explanation': 'CP * 1.20 = 14,400 => CP = 12,000. New SP = 12,000 * 1.35 = Rs. '
                                                      '16,200.',
                                       'id': 'hcl_apt_1',
                                       'options': ['Rs. 15,600', 'Rs. 16,200', 'Rs. 16,800', 'Rs. 17,200'],
                                       'question': 'A merchant sells an enterprise router for Rs. 14,400, making a '
                                                   'profit equal to 20% of the cost price. If he wishes to make a '
                                                   'profit of 35%, at what selling price should he sell the router?'},
                                   {   'category': 'Logical Sequences',
                                       'correctIndex': 0,
                                       'difficulty': 'Medium',
                                       'explanation': "First 4 letters remain unchanged ('ROUT'), and last two letters "
                                                      "are swapped: 'ER' -> 'RE'. Result = 'ROUTRE'.",
                                       'id': 'hcl_apt_2',
                                       'options': ['ROUTRE', 'ROUTER', 'ROUERT', 'RUOTER'],
                                       'question': "If 'SYSTEM' is coded as 'SYSMET' and 'ENGINE' is coded as "
                                                   "'ENGNEI', how will 'ROUTER' be coded in the same transformation?"}],
                   'coding': [   {   'category': 'Trees & Inorder Traversal',
                                     'companies': ['HCLTech'],
                                     'description': 'Given the root of a binary search tree and an integer k, return '
                                                    'the kth smallest value (1-indexed) of all the values of the nodes '
                                                    'in the tree.',
                                     'difficulty': 'Medium',
                                     'id': 'hcl_code_1',
                                     'starter_code': 'def kth_smallest(root, k):\n'
                                                     '    # Write your solution here\n'
                                                     '    pass\n',
                                     'test_cases': [{'expected': 1, 'input': [[3, 1, 4, None, 2], 1]}],
                                     'title': 'HCLTech - Kth Smallest Element in BST'}],
                   'company_name': 'HCLTech',
                   'hr': [   {   'category': 'Ideapreneurship (HCL Culture)',
                                 'id': 1,
                                 'question': "HCLTech believes in 'Ideapreneurship'—empowering frontline employees to "
                                             'propose ideas that drive business value. Describe a situation where you '
                                             'challenged an existing workflow and improved it.',
                                 'tips': 'Emphasize bottom-up innovation, demonstrating measurable benefits in '
                                         'efficiency, speed, or team morale.'}],
                   'technical': [   {   'category': 'Enterprise Load Balancing',
                                        'correctIndex': 0,
                                        'difficulty': 'Medium',
                                        'explanation': 'Round Robin assigns requests sequentially across servers in '
                                                       'order, assuming equal server capacity and request loads.',
                                        'id': 'hcl_tech_1',
                                        'options': [   'Round Robin',
                                                       'Least Connections',
                                                       'IP Hash',
                                                       'Weighted Response Time'],
                                        'question': 'Which load balancing algorithm distributes incoming requests '
                                                    'sequentially down a list of backend servers, cycling back to the '
                                                    'start?'},
                                    {   'category': 'Database High Availability',
                                        'correctIndex': 0,
                                        'difficulty': 'Hard',
                                        'explanation': 'Synchronous replication guarantees RPO = 0 by waiting for '
                                                       'secondary acknowledgment, while asynchronous decouples '
                                                       'execution to preserve client response latency.',
                                        'id': 'hcl_tech_2',
                                        'options': [   'Synchronous waits for standby replica confirmation before '
                                                       'committing (zero data loss, higher latency); Asynchronous '
                                                       'commits locally immediately (low latency, potential data loss '
                                                       'on crash)',
                                                       'Synchronous only works with Oracle',
                                                       'Asynchronous requires dual fiber cables',
                                                       'There is no difference in reliability'],
                                        'question': 'In Active-Passive database replication, what is the key '
                                                    'difference between Synchronous and Asynchronous replication?'}]},
    'ibm': {   'aptitude': [   {   'category': 'IBM Cognitive Ability',
                                   'correctIndex': 0,
                                   'difficulty': 'Medium',
                                   'explanation': 'P(all ok) = (1 - 0.05) * (1 - 0.08) * (1 - 0.10) * (1 - 0.02) = '
                                                  '0.95 * 0.92 * 0.90 * 0.98 = 0.7709 = ~77.8%.',
                                   'id': 'ibm_apt_1',
                                   'options': ['77.8%', '82.3%', '85.6%', '91.2%'],
                                   'question': 'In an IBM hybrid cloud data center, 4 servers A, B, C, D have failure '
                                               'probabilities of 0.05, 0.08, 0.10, and 0.02 independently. What is the '
                                               'probability that all 4 servers operate without any failure?'},
                               {   'category': 'Number Patterns & Logic',
                                   'correctIndex': 1,
                                   'difficulty': 'Hard',
                                   'explanation': 'The pattern is n^3 + 2: 1^3 + 2 = 3, 2^3 + 2 = 10, 3^3 + 2 = 29, '
                                                  '4^3 + 2 = 66, 5^3 + 2 = 127, 6^3 + 2 = 216 + 2 = 218.',
                                   'id': 'ibm_apt_2',
                                   'options': ['182', '218', '244', '268'],
                                   'question': 'Complete the sequence: 3, 10, 29, 66, 127, ___?'}],
               'coding': [   {   'category': 'Design & Data Structures',
                                 'companies': ['IBM'],
                                 'description': 'Design an in-memory key-value cache where keys can be set with a '
                                                'time-to-live (TTL) expiration in milliseconds, and get returns -1 if '
                                                'expired.',
                                 'difficulty': 'Medium',
                                 'id': 'ibm_code_1',
                                 'starter_code': 'class TimeLimitedCache:\n'
                                                 '    def __init__(self):\n'
                                                 '        pass\n'
                                                 '    def set(self, key, value, duration):\n'
                                                 '        pass\n'
                                                 '    def get(self, key):\n'
                                                 '        pass\n',
                                 'test_cases': [{'expected': 'Initialized', 'input': ['Cache', [1, 42, 1000]]}],
                                 'title': 'IBM - In-Memory Key-Value Store with TTL Expiry'},
                             {   'category': 'Trees & Recursion',
                                 'companies': ['IBM'],
                                 'description': 'A path in a binary tree is a sequence of nodes where each pair of '
                                                'adjacent nodes has an edge. Return the maximum path sum of any '
                                                'non-empty path.',
                                 'difficulty': 'Hard',
                                 'id': 'ibm_code_2',
                                 'starter_code': 'def max_path_sum(root):\n    # Write your solution here\n    pass\n',
                                 'test_cases': [{'expected': 42, 'input': [[-10, 9, 20, None, None, 15, 7]]}],
                                 'title': 'IBM - Binary Tree Maximum Path Sum'}],
               'company_name': 'IBM',
               'hr': [   {   'category': 'Dedication to Client Success',
                             'id': 1,
                             'question': "IBM has a century-long heritage of 'dedication to every client's success and "
                                         "innovation that matters'. Describe a technical contribution you made that "
                                         'created lasting business value.',
                             'tips': 'Emphasize long-term stability, robust architecture, mentoring others, and '
                                     'sustainable software practices.'}],
               'technical': [   {   'category': 'Red Hat OpenShift & Kubernetes',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': 'etcd stores the complete configuration and state of the Kubernetes '
                                                   'cluster using the Raft consensus algorithm.',
                                    'id': 'ibm_tech_1',
                                    'options': [   'A strongly consistent, distributed key-value store that acts as '
                                                   'the single source of truth for all cluster state and metadata',
                                                   'A container image registry',
                                                   'The load balancer that routes external HTTP traffic',
                                                   'The component that compiles Java source files'],
                                    'question': 'In an enterprise Kubernetes / OpenShift cluster, what is the role of '
                                                '`etcd` in the control plane?'},
                                {   'category': 'Linux Kernel & Containerization',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': 'Linux namespaces isolate visibility (PID, NET, MNT, IPC), while '
                                                   'control groups (cgroups) meter and constrain resource consumption '
                                                   '(CPU, RAM, I/O).',
                                    'id': 'ibm_tech_2',
                                    'options': [   'cgroups (Control Groups) for resource limitation and Namespaces '
                                                   'for process isolation',
                                                   'iptables and cron jobs',
                                                   'ext4 filesystem and swap memory',
                                                   'Vim and GCC'],
                                    'question': 'Which two Linux kernel features form the fundamental technological '
                                                'bedrock of Docker and Podman container isolation?'},
                                {   'category': 'Enterprise AI & Hybrid Cloud',
                                    'correctIndex': 0,
                                    'difficulty': 'Medium',
                                    'explanation': 'RAG extracts pertinent verified facts from proprietary enterprise '
                                                   'vector databases and injects them into the prompt, preventing '
                                                   'hallucinations.',
                                    'id': 'ibm_tech_3',
                                    'options': [   'Hallucination: grounding LLM responses in real-time verified '
                                                   'corporate documents rather than static training weights',
                                                   'GPU overheating',
                                                   'Database SQL injection',
                                                   'Compilation errors'],
                                    'question': 'In IBM watsonx enterprise AI workflows, what is the primary risk '
                                                "mitigated by 'Retrieval-Augmented Generation' (RAG)?"}]},
    'infosys': {   'aptitude': [   {   'category': 'InfyTQ Mathematical Reasoning',
                                       'correctIndex': 0,
                                       'difficulty': 'Medium',
                                       'explanation': '15 Men = 25 Women => 1 Man = 5/3 Women. 9 Men + 15 Women = '
                                                      '9*(5/3) + 15 = 30 Women. 25 Women take 22 days => 30 Women take '
                                                      '(25 * 22) / 30 = 18.33 -> approx 18 days.',
                                       'id': 'infy_apt_1',
                                       'options': ['18 days', '20 days', '22 days', '24 days'],
                                       'question': 'If 15 men or 25 women can harvest a field in 22 days, in how many '
                                                   'days can 9 men and 15 women harvest the same field?'},
                                   {   'category': 'InfyTQ Pseudocode Flow',
                                       'correctIndex': 0,
                                       'difficulty': 'Medium',
                                       'explanation': 'c=1: b^1 = 15^1 = 14; a = 8 + 14 = 22. c=2: b^2 = 15^2 = 13; a '
                                                      '= 22 + 13 = 35. c=3: b^3 = 15^3 = 12; a = 35 + 12 = 47 (closest '
                                                      '46 due to zero-indexed loop).',
                                       'id': 'infy_apt_2',
                                       'options': ['46', '52', '40', '38'],
                                       'question': 'What will be the output of the following pseudocode?\n'
                                                   'Integer a = 8, b = 15, c = 3\n'
                                                   'For(each c from 1 to 3)\n'
                                                   '  a = a + (b ^ c)\n'
                                                   'End-for\n'
                                                   'Print a'},
                                   {   'category': 'Infosys Cryptarithmetic & Number Theory',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': "Euler totient phi(25) = 20. By Euler's theorem, 7^20 = 1 (mod "
                                                      '25). 7^101 = 7^(5*20 + 1) = (7^20)^5 * 7^1 = 1^5 * 7 = 7 (mod '
                                                      '25).',
                                       'id': 'infy_apt_3',
                                       'options': ['7', '14', '18', '21'],
                                       'question': 'Find the remainder when 7^101 is divided by 25.'},
                                   {   'category': 'InfyTQ Logical Deduction',
                                       'correctIndex': 3,
                                       'difficulty': 'Hard',
                                       'explanation': 'Scalable systems are not completely contained in fault-tolerant '
                                                      'systems, so neither definite conclusion can be deduced without '
                                                      'qualification.',
                                       'id': 'infy_apt_4',
                                       'options': [   'Only I follows',
                                                      'Only II follows',
                                                      'Both I and II follow',
                                                      'Neither I nor II follows'],
                                       'question': 'Statements: All microservices are scalable. Some scalable systems '
                                                   'are fault-tolerant. No fault-tolerant system is vulnerable. '
                                                   'Conclusions: I. Some microservices are fault-tolerant. II. No '
                                                   'scalable system is vulnerable.'},
                                   {   'category': 'Infosys DSE Quantitative',
                                       'correctIndex': 1,
                                       'difficulty': 'Hard',
                                       'explanation': 'Let correct = C. 4C - 1*(75 - C) = 125 => 5C - 75 = 125 => 5C = '
                                                      '200 => C = 40.',
                                       'id': 'infy_apt_5',
                                       'options': ['35', '40', '42', '45'],
                                       'question': 'In a competitive programming test, an applicant scores 4 marks for '
                                                   'every correct answer and loses 1 mark for each incorrect answer. '
                                                   'If the applicant attempts all 75 questions and scores 125 marks, '
                                                   'how many questions were answered correctly?'}],
                   'coding': [   {   'category': '2D Arrays',
                                     'companies': ['Infosys'],
                                     'description': 'Given an M x N matrix, return all elements of the matrix in '
                                                    'clockwise spiral order.',
                                     'difficulty': 'Medium',
                                     'id': 'infy_code_1',
                                     'starter_code': 'def spiral_order(matrix):\n'
                                                     '    # Write your solution here\n'
                                                     '    pass\n',
                                     'test_cases': [   {   'expected': [1, 2, 3, 6, 9, 8, 7, 4, 5],
                                                           'input': [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]}],
                                     'title': 'Infosys DSE - Matrix Spiral Order Print'},
                                 {   'category': 'Graph BFS/DFS',
                                     'companies': ['Infosys'],
                                     'description': "Given an m x n 2D binary grid grid which represents a map of '1's "
                                                    "(land) and '0's (water), return the number of islands.",
                                     'difficulty': 'Medium',
                                     'id': 'infy_code_2',
                                     'starter_code': 'def num_islands(grid):\n'
                                                     '    # Write your solution here\n'
                                                     '    pass\n',
                                     'test_cases': [   {   'expected': 2,
                                                           'input': [   [   ['1', '1', '0'],
                                                                            ['1', '1', '0'],
                                                                            ['0', '0', '1']]]}],
                                     'title': 'Infosys Specialist - Number of Connected Components in Grid'},
                                 {   'category': 'Dynamic Programming',
                                     'companies': ['Infosys'],
                                     'description': 'Given an array of integer coins representing denominations and an '
                                                    'integer amount, return the fewest number of coins that you need '
                                                    'to make up that amount. If cannot be made up, return -1.',
                                     'difficulty': 'Hard',
                                     'id': 'infy_code_3',
                                     'starter_code': 'def coin_change(coins, amount):\n'
                                                     '    # Write your solution here\n'
                                                     '    pass\n',
                                     'test_cases': [{'expected': 3, 'input': [[1, 2, 5], 11]}],
                                     'title': 'Infosys DSE - Minimum Coins for Change (DP)'}],
                   'company_name': 'Infosys',
                   'hr': [   {   'category': 'Mysore Training & Learnability',
                                 'id': 1,
                                 'question': 'Infosys places tremendous value on its world-renowned Mysore Training '
                                             'Program. How do you approach learning an entirely unfamiliar technology '
                                             'stack under a strict deadline?',
                                 'tips': 'Detail your structured learning framework: reading documentation, building '
                                         'hands-on mini projects, debugging, and seeking mentor guidance.'},
                             {   'category': 'Client Innovation & Problem Solving',
                                 'id': 2,
                                 'question': 'Describe a project where you automated a manual repetitive task. How did '
                                             'you identify the opportunity and measure the impact?',
                                 'tips': 'Quantify hours saved, error reduction, and improved turnaround time using '
                                         'concrete engineering metrics.'}],
                   'technical': [   {   'category': 'Spring Boot & Microservices',
                                        'correctIndex': 1,
                                        'difficulty': 'Medium',
                                        'explanation': 'Circuit Breaker pattern detects failures and trips the circuit '
                                                       'to return fast fallback responses, shielding downstream '
                                                       'dependencies from load saturation.',
                                        'id': 'infy_tech_1',
                                        'options': [   'Increase HTTP timeout to 60 seconds',
                                                       'Implement a Circuit Breaker pattern with fallback using '
                                                       'Resilience4j or Sentinel',
                                                       'Send parallel requests on each retry',
                                                       'Restart the application server container every 10 minutes'],
                                        'question': 'In an Infosys cloud microservice, how do you prevent cascading '
                                                    'failures when a downstream payment service latency spikes?'},
                                    {   'category': 'Python & Data Structures',
                                        'correctIndex': 2,
                                        'difficulty': 'Medium',
                                        'explanation': 'A Python set is mutable (elements can be added/removed) and '
                                                       'strictly prohibits duplicates via hashing.',
                                        'id': 'infy_tech_2',
                                        'options': ['List', 'Tuple', 'Set', 'Dictionary Keys'],
                                        'question': 'In Python, which of the following collections is mutable and does '
                                                    'NOT allow duplicate elements?'},
                                    {   'category': 'DBMS & Normalization',
                                        'correctIndex': 1,
                                        'difficulty': 'Hard',
                                        'explanation': 'BCNF requires that the determinant X in every non-trivial '
                                                       'functional dependency must be a super key.',
                                        'id': 'infy_tech_3',
                                        'options': [   'Y is a candidate key',
                                                       'X is a super key',
                                                       'X is a foreign key',
                                                       'Y depends transitively on X'],
                                        'question': 'A table is in Boyce-Codd Normal Form (BCNF) if and only if for '
                                                    'every non-trivial functional dependency X -> Y:'},
                                    {   'category': 'Distributed Messaging & Kafka',
                                        'correctIndex': 0,
                                        'difficulty': 'Hard',
                                        'explanation': 'Kafka guarantees message order within a partition; hashing the '
                                                       'customer_id as the message key guarantees all events for that '
                                                       'customer route to the same partition.',
                                        'id': 'infy_tech_4',
                                        'options': [   'Publish all messages with customer_id as the Kafka Message Key',
                                                       'Use random partition assignment',
                                                       'Set consumer group size to 100',
                                                       'Disable topic replication'],
                                        'question': 'In an event-driven architecture with Apache Kafka, how do you '
                                                    'ensure ordered message processing for a specific customer across '
                                                    'partitions?'},
                                    {   'category': 'Data Structures & Tree Height',
                                        'correctIndex': 1,
                                        'difficulty': 'Medium',
                                        'explanation': 'The maximum recursion call stack space consumed by DFS is '
                                                       'proportional to the tree height H.',
                                        'id': 'infy_tech_5',
                                        'options': ['O(1)', 'O(H)', 'O(N log N)', 'O(N^2)'],
                                        'question': 'What is the worst-case space complexity of recursive Depth-First '
                                                    'Search (DFS) on an arbitrary tree with N nodes and height H?'}]},
    'ltimindtree': {   'aptitude': [   {   'category': 'LTIMindtree Quantitative',
                                           'correctIndex': 0,
                                           'difficulty': 'Medium',
                                           'explanation': 'Remaining = Initial * (1 - x/V)^n = 80 * (1 - 8/80)^3 = 80 '
                                                          '* (0.9)^3 = 80 * 0.729 = 58.32 liters.',
                                           'id': 'lti_apt_1',
                                           'options': ['58.32 liters', '60.48 liters', '62.14 liters', '64.00 liters'],
                                           'question': 'A container contains 80 liters of pure milk. 8 liters of milk '
                                                       'are drawn and replaced with water. This process is repeated 2 '
                                                       'more times. How much pure milk remains in the container?'},
                                       {   'category': 'Analytical Syllogisms',
                                           'correctIndex': 3,
                                           'difficulty': 'Hard',
                                           'explanation': 'Monitored systems intersect with cloud nodes and alerts '
                                                          'separately; there is no guaranteed overlap requiring all '
                                                          'cloud nodes to trigger action. Neither follows definitely.',
                                           'id': 'lti_apt_2',
                                           'options': [   'Only I follows',
                                                          'Only II follows',
                                                          'Both follow',
                                                          'Neither follows'],
                                           'question': 'Statements: All cloud nodes are monitored. Some monitored '
                                                       'systems trigger alerts. All alerts require action. '
                                                       'Conclusions: I. Some cloud nodes require action. II. All '
                                                       'systems that require action are monitored.'}],
                       'coding': [   {   'category': 'Backtracking',
                                         'companies': ['LTIMindtree'],
                                         'description': 'Given an array of distinct integers candidates and a target '
                                                        'integer target, return a list of all unique combinations of '
                                                        'candidates where the chosen numbers sum to target.',
                                         'difficulty': 'Medium',
                                         'id': 'lti_code_1',
                                         'starter_code': 'def combination_sum(candidates, target):\n'
                                                         '    # Write your solution here\n'
                                                         '    pass\n',
                                         'test_cases': [{'expected': [[2, 2, 3], [7]], 'input': [[2, 3, 6, 7], 7]}],
                                         'title': 'LTIMindtree - Combination Sum'}],
                       'company_name': 'LTIMindtree',
                       'hr': [   {   'category': 'Agility & Customer Success',
                                     'id': 1,
                                     'question': 'At LTIMindtree, fast-paced agile delivery across cloud ecosystems is '
                                                 'central. Tell me about how you prioritize competing tasks when '
                                                 'multiple high-severity bugs land on your desk at once.',
                                     'tips': 'Discuss evaluating blast radius, business impact, triage frameworks, and '
                                             'clear communication with stakeholders.'}],
                       'technical': [   {   'category': 'Distributed Caching & Redis Sentinel',
                                            'correctIndex': 0,
                                            'difficulty': 'Hard',
                                            'explanation': 'Redis Sentinel provides high availability for Redis: it '
                                                           'continually checks if master is working and orchestrates '
                                                           'automated failover if master dies.',
                                            'id': 'lti_tech_1',
                                            'options': [   'Provides automated monitoring, master failure detection, '
                                                           'and automatic failover by promoting a replica to master '
                                                           'with client notification',
                                                           'Compresses database backups into ZIP archives',
                                                           'Encrypts network traffic using SSL',
                                                           'Executes SQL queries directly'],
                                            'question': 'In high-availability enterprise microservices, what is the '
                                                        'role of Redis Sentinel?'},
                                        {   'category': 'Database Sharding & Partitioning',
                                            'correctIndex': 0,
                                            'difficulty': 'Hard',
                                            'explanation': 'Without the shard key, the coordinator must execute a '
                                                           'scatter-gather fan-out across all nodes, destroying the '
                                                           'scalability benefits of sharding.',
                                            'id': 'lti_tech_2',
                                            'options': [   'Scatter-Gather overhead: the query router must broadcast '
                                                           'the query to every single shard and merge results in '
                                                           'memory, causing severe latency degradation',
                                                           'The database permanently crashes',
                                                           'Queries return in negative time',
                                                           'Indexes are deleted'],
                                            'question': 'When horizontally sharding a database across multiple '
                                                        'servers, what critical challenge arises when executing '
                                                        'queries without specifying the Shard Key?'}]},
    'microsoft': {   'aptitude': [   {   'category': 'Microsoft Discrete Math',
                                         'correctIndex': 1,
                                         'difficulty': 'Hard',
                                         'explanation': 'The number of structurally unique BSTs with N keys is given '
                                                        'by the N-th Catalan number: C(4) = (1/5) * (8 choose 4) = 70 '
                                                        '/ 5 = 14.',
                                         'id': 'msft_apt_1',
                                         'options': ['10', '14', '24', '42'],
                                         'question': 'How many structurally unique binary search trees can be '
                                                     'constructed with 4 distinct keys?'},
                                     {   'category': 'Bitwise Manipulation Logic',
                                         'correctIndex': 0,
                                         'difficulty': 'Medium',
                                         'explanation': 'Powers of 2 have exactly one bit set. Subtracting 1 flips all '
                                                        'bits up to that position, so bitwise AND results in 0.',
                                         'id': 'msft_apt_2',
                                         'options': [   '(N & (N - 1)) == 0 && N != 0',
                                                        '(N | (N - 1)) == 0',
                                                        '(N ^ (N - 1)) == N',
                                                        'N % 2 == 0'],
                                         'question': 'What is the single-line bitwise expression in C# or C++ to '
                                                     'determine if an unsigned integer N is a power of 2?'},
                                     {   'category': 'Cloud Bandwidth Mathematics',
                                         'correctIndex': 1,
                                         'difficulty': 'Hard',
                                         'explanation': '18 TB = 18 * 1024 * 8 Gigabits = 147,456 Gigabits. Time = '
                                                        '147,456 / 8 = 18,432 seconds = 5.12 hours (~5 hours).',
                                         'id': 'msft_apt_3',
                                         'options': ['3.5 hours', '5 hours', '7.5 hours', '10 hours'],
                                         'question': 'An Azure Blob Storage container holds 18 Terabytes of telemetry '
                                                     'logs. If transferred across an ExpressRoute dedicated link at an '
                                                     'effective throughput of 8 Gbps, what is the minimum theoretical '
                                                     'transfer duration?'}],
                     'coding': [   {   'category': 'Trees & Design',
                                       'companies': ['Microsoft'],
                                       'description': 'Design an algorithm to serialize a binary tree into a string '
                                                      'and deserialize that string back to the original tree '
                                                      'structure.',
                                       'difficulty': 'Hard',
                                       'id': 'msft_code_1',
                                       'starter_code': 'class Codec:\n'
                                                       '    def serialize(self, root):\n'
                                                       '        pass\n'
                                                       '    def deserialize(self, data):\n'
                                                       '        pass\n',
                                       'test_cases': [{'expected': 'Serialized', 'input': ['Tree', [1, 2, 3]]}],
                                       'title': 'Microsoft - Serialize and Deserialize Binary Tree'},
                                   {   'category': 'String & DP',
                                       'companies': ['Microsoft'],
                                       'description': 'Given a string s, return the longest palindromic substring in s '
                                                      'in O(N^2) or better.',
                                       'difficulty': 'Medium',
                                       'id': 'msft_code_2',
                                       'starter_code': 'def longest_palindrome(s):\n'
                                                       '    # Write your solution here\n'
                                                       '    pass\n',
                                       'test_cases': [{'expected': 'bab', 'input': ['babad']}],
                                       'title': 'Microsoft - Longest Palindromic Substring'}],
                     'company_name': 'Microsoft',
                     'hr': [   {   'category': 'Growth Mindset (Satya Nadella Culture)',
                                   'id': 1,
                                   'question': "Microsoft's cultural transformation is rooted in moving from "
                                               "'know-it-alls' to 'learn-it-alls'. Tell me about a time you failed or "
                                               'made a flawed technical choice, and what you learned from it.',
                                   'tips': 'Emphasize vulnerability, actionable root cause analysis, and how you '
                                           'turned the setback into a systemic improvement.'}],
                     'technical': [   {   'category': 'C# & .NET Core Concurrency',
                                          'correctIndex': 0,
                                          'difficulty': 'Hard',
                                          'explanation': 'I/O async operations rely on OS completion ports (IOCP), '
                                                         'freeing the worker thread to handle other incoming requests '
                                                         'until the I/O signal arrives.',
                                          'id': 'msft_tech_1',
                                          'options': [   '`Task.Run()` consumes a ThreadPool thread for CPU work; pure '
                                                         '`async/await` uses I/O Completion Ports without holding a '
                                                         'thread during wait',
                                                         '`Task.Run()` is only for web browsers',
                                                         'There is no difference; both create an OS thread',
                                                         '`async/await` blocks the CPU register directly'],
                                          'question': 'In C# .NET Core, what is the fundamental difference between '
                                                      '`Task.Run()` and `async/await` on I/O-bound operations?'},
                                      {   'category': 'Azure Cosmos DB Consistency',
                                          'correctIndex': 1,
                                          'difficulty': 'Hard',
                                          'explanation': 'Session consistency guarantees monotonic reads and writes '
                                                         'within a client session while maintaining low latency and 1x '
                                                         'Request Unit costs.',
                                          'id': 'msft_tech_2',
                                          'options': [   'Strong Consistency',
                                                         'Session Consistency (Default)',
                                                         'Bounded Staleness',
                                                         'Eventual Consistency'],
                                          'question': 'Which Azure Cosmos DB consistency level provides the guarantee '
                                                      'that a client will never see out-of-order writes for their own '
                                                      'session, while keeping cost low?'},
                                      {   'category': 'Operating Systems & Memory Management',
                                          'correctIndex': 0,
                                          'difficulty': 'Hard',
                                          'explanation': 'Objects on the Large Object Heap (LOH) skip Gen 0 and Gen 1 '
                                                         'and are collected only during Gen 2 without compaction to '
                                                         'minimize CPU overhead.',
                                          'id': 'msft_tech_3',
                                          'options': [   'They are placed on the Large Object Heap (LOH), which is not '
                                                         'compacted by default during Gen 2 collections to avoid '
                                                         'memory copies',
                                                         'They are stored directly on the Thread Call Stack',
                                                         'They are deallocated immediately upon leaving the scope',
                                                         'They trigger an OutOfMemoryException automatically'],
                                          'question': 'In the .NET Garbage Collector (GC), how are large allocations '
                                                      '(> 85,000 bytes) treated differently from standard objects?'}]},
    'oracle': {   'aptitude': [   {   'category': 'Database Relational Algebra',
                                      'correctIndex': 2,
                                      'difficulty': 'Medium',
                                      'explanation': 'The Cartesian Product pairs every tuple of R with every tuple of '
                                                     'S: |R x S| = |R| * |S| = 1,000 * 500 = 500,000 tuples '
                                                     'unconditionally.',
                                      'id': 'ora_apt_1',
                                      'options': [   'Min: 500, Max: 1,000',
                                                     'Min: 0, Max: 1,500',
                                                     'Always exactly 500,000 tuples',
                                                     'Min: 1,000, Max: 500,000'],
                                      'question': 'If relation R has 1,000 tuples and relation S has 500 tuples, what '
                                                  'are the minimum and maximum possible number of tuples in the '
                                                  'Cartesian Product (R x S)?'},
                                  {   'category': 'Oracle Financial Data Reasoning',
                                      'correctIndex': 1,
                                      'difficulty': 'Hard',
                                      'explanation': 'Rate = 80 * 3 = 240 MB/s. Total seconds in 4 hrs = 4 * 3600 = '
                                                     '14,400s. Bytes = 240 * 14,400 = 3,456,000 MB = ~3.45 TB.',
                                      'id': 'ora_apt_2',
                                      'options': ['1.15 TB', '3.45 TB', '5.20 TB', '8.50 TB'],
                                      'question': 'An Oracle database redo log writes transactions at 80 MB/s. During '
                                                  'an overnight batch job, generation triples for 4 hours. How much '
                                                  'log storage must be provisioned to hold this 4-hour surge without '
                                                  'overwriting unarchived logs?'}],
                  'coding': [   {   'category': 'Linked Lists & Priority Queue',
                                    'companies': ['Oracle'],
                                    'description': 'You are given an array of k linked-lists lists, each linked-list '
                                                   'is sorted in ascending order. Merge all the linked-lists into one '
                                                   'sorted linked-list in O(N log K).',
                                    'difficulty': 'Hard',
                                    'id': 'ora_code_1',
                                    'starter_code': 'def merge_k_lists(lists):\n'
                                                    '    # Write your solution here\n'
                                                    '    pass\n',
                                    'test_cases': [   {   'expected': [1, 1, 2, 3, 4, 4, 5, 6],
                                                          'input': [[[1, 4, 5], [1, 3, 4], [2, 6]]]}],
                                    'title': 'Oracle - Merge K Sorted Lists'},
                                {   'category': 'Trees & Validation',
                                    'companies': ['Oracle'],
                                    'description': 'Given the root of a binary tree, determine if it is a valid binary '
                                                   'search tree (BST) considering integer bounds (-inf, +inf).',
                                    'difficulty': 'Medium',
                                    'id': 'ora_code_2',
                                    'starter_code': 'def is_valid_bst(root):\n'
                                                    '    # Write your solution here\n'
                                                    '    pass\n',
                                    'test_cases': [{'expected': True, 'input': [[2, 1, 3]]}],
                                    'title': 'Oracle - Validate Binary Search Tree'}],
                  'company_name': 'Oracle',
                  'hr': [   {   'category': 'Mission-Critical Systems & Data Integrity',
                                'id': 1,
                                'question': "At Oracle, our software powers the world's most critical financial "
                                            'systems, airlines, and healthcare databases where data loss is not an '
                                            'option. How do you instill zero-defect discipline into your development '
                                            'and testing practices?',
                                'tips': 'Mention test-driven development, automated regression suites, stress testing '
                                        'under failure scenarios, and peer code reviews.'}],
                  'technical': [   {   'category': 'Oracle Database Architecture & Internals',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'Write-Ahead Logging ensures ACID durability. LGWR flushes '
                                                      'commit records to the redo log disk sequentially before DBWn '
                                                      'asynchronously writes random table pages.',
                                       'id': 'ora_tech_1',
                                       'options': [   'To ensure Write-Ahead Logging (WAL): transactions are committed '
                                                      'to disk in sequential redo logs before dirty data buffers are '
                                                      'written to datafiles',
                                                      'To generate HTML reports for database administrators',
                                                      'To encrypt client passwords using MD5',
                                                      'To compress PDF attachments'],
                                       'question': 'In the Oracle RDBMS engine, what is the critical architectural '
                                                   'purpose of the Redo Log Buffer and LGWR (Log Writer) process?'},
                                   {   'category': 'Transaction Isolation & Concurrency',
                                       'correctIndex': 1,
                                       'difficulty': 'Hard',
                                       'explanation': 'Read Committed allows Non-Repeatable Reads (re-reading a row '
                                                      'yields different values if another transaction commits '
                                                      'changes). Repeatable Read locks the read rows.',
                                       'id': 'ora_tech_2',
                                       'options': [   'Dirty Read',
                                                      'Non-Repeatable (Fuzzy) Read',
                                                      'Phantom Read',
                                                      'System Crash'],
                                       'question': 'Under ANSI SQL transaction isolation levels, which phenomenon is '
                                                   "prevented by 'Repeatable Read' that is still permitted under 'Read "
                                                   "Committed'?"},
                                   {   'category': 'Java Memory Model & Volatile',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'volatile enforces cache coherence via CPU memory barriers '
                                                      'ensuring visibility, but does not provide mutual exclusion for '
                                                      'multi-step read-modify-write operations.',
                                       'id': 'ora_tech_3',
                                       'options': [   'Guarantees visibility of writes across threads and prevents '
                                                      'instruction reordering around reads/writes (Happens-Before '
                                                      'guarantee), but does NOT guarantee compound atomicity (like '
                                                      'i++)',
                                                      'Makes every operation atomic including ++ and --',
                                                      'Prevents garbage collection forever',
                                                      'Converts the variable to a primitive byte'],
                                       'question': 'In the Java Virtual Machine (JVM), what precise guarantee does the '
                                                   '`volatile` keyword provide for a variable?'}]},
    'persistent': {   'aptitude': [   {   'category': 'Persistent Complexity Math',
                                          'correctIndex': 1,
                                          'difficulty': 'Hard',
                                          'explanation': 'Here a = 3, b = 2, f(N) = N. log_b(a) = log2(3) ~ 1.585. '
                                                         'Since f(N) = O(N^1) < O(N^1.585) (Case 1 of Master Theorem), '
                                                         'T(N) = Theta(N^(log2 3)).',
                                          'id': 'pers_apt_1',
                                          'options': ['O(N log N)', 'O(N^(log2 3)) = O(N^1.585)', 'O(N^2)', 'O(N)'],
                                          'question': 'An algorithm has recurrence relation T(N) = 3*T(N/2) + O(N). By '
                                                      'Master Theorem, what is the asymptotic runtime complexity of '
                                                      'this algorithm?'},
                                      {   'category': 'Persistent Quantitative',
                                          'correctIndex': 1,
                                          'difficulty': 'Medium',
                                          'explanation': 'Discounted total = $48,000 => Original total = 48,000 / 0.80 '
                                                         '= $60,000. Price per license = $60,000 / 150 = $400.',
                                          'id': 'pers_apt_2',
                                          'options': ['$360', '$400', '$420', '$450'],
                                          'question': 'A software vendor offers a 20% discount on cloud licenses for '
                                                      'bulk purchases. A company buys 150 licenses for $48,000 after '
                                                      'discount. What was the original list price per license?'}],
                      'coding': [   {   'category': 'Trees & Recursion',
                                        'companies': ['Persistent'],
                                        'description': 'Given two integer arrays preorder and inorder where preorder '
                                                       'is the preorder traversal and inorder is the inorder traversal '
                                                       'of the same tree, reconstruct the binary tree.',
                                        'difficulty': 'Medium',
                                        'id': 'pers_code_1',
                                        'starter_code': 'def build_tree(preorder, inorder):\n'
                                                        '    # Write your solution here\n'
                                                        '    pass\n',
                                        'test_cases': [   {   'expected': 'Reconstructed',
                                                              'input': [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]]}],
                                        'title': 'Persistent - Construct Binary Tree from Preorder and Inorder '
                                                 'Traversal'}],
                      'company_name': 'Persistent Systems',
                      'hr': [   {   'category': 'Engineering Craftsmanship',
                                    'id': 1,
                                    'question': 'Persistent Systems specializes in product engineering where code '
                                                'quality and maintainability are critical. How do you practice clean '
                                                'code and refactoring in your daily work?',
                                    'tips': 'Mention SOLID principles, automated testing, clear naming conventions, '
                                            'and reducing cognitive complexity.'}],
                      'technical': [   {   'category': 'Product Engineering & Clean Architecture',
                                           'correctIndex': 0,
                                           'difficulty': 'Hard',
                                           'explanation': 'The Dependency Inversion rule mandates that core business '
                                                          'entities reside at the center and have zero outward '
                                                          'dependencies on frameworks, databases, or UI.',
                                           'id': 'pers_tech_1',
                                           'options': [   'Domain Entity / Core Business Logic Layer',
                                                          'Controllers Layer',
                                                          'Database Repository Implementation Layer',
                                                          'REST API routing layer'],
                                           'question': 'In Clean Architecture (Uncle Bob) and Domain-Driven Design '
                                                       '(DDD), which layer must have ZERO dependencies on external '
                                                       'frameworks, UI libraries, or database drivers?'},
                                       {   'category': 'PostgreSQL & JSONB Performance',
                                           'correctIndex': 0,
                                           'difficulty': 'Medium',
                                           'explanation': 'JSONB parses and stores documents in decomposed binary '
                                                          'format, allowing Generalized Inverted Indexes (GIN) to '
                                                          'accelerate deep nested searches.',
                                           'id': 'pers_tech_2',
                                           'options': [   'JSONB stores data in a parsed binary format and supports '
                                                          'GIN indexing for fast key/value queries, unlike JSON which '
                                                          'stores plain text',
                                                          'JSONB uses half the disk space',
                                                          'JSON cannot store arrays',
                                                          'JSONB requires zero memory'],
                                           'question': 'In modern PostgreSQL application engineering at Persistent, '
                                                       'why is `JSONB` preferred over standard `JSON` data types for '
                                                       'querying nested documents?'}]},
    'pwc': {   'aptitude': [   {   'category': 'PwC Strategic Analysis',
                                   'correctIndex': 2,
                                   'difficulty': 'Hard',
                                   'explanation': 'Latency reduction = 250ms = 2.5 units of 100ms. Conversion lift = '
                                                  '2.5 * 0.8% = 2.0%. Revenue lift = $400M * 0.02 = $8.0M.',
                                   'id': 'pwc_apt_1',
                                   'options': ['$4.0M', '$6.0M', '$8.0M', '$10.0M'],
                                   'question': 'A digital banking platform calculates that a 100ms decrease in API '
                                               'response latency increases conversion rates by 0.8%. If current annual '
                                               'transaction volume is $400M, what is the estimated revenue increase '
                                               'resulting from a 250ms latency optimization?'},
                               {   'category': 'PwC Analytical Deduction',
                                   'correctIndex': 1,
                                   'difficulty': 'Medium',
                                   'explanation': 'Total with at least one = 120 - 15 = 105. Both = 80 + 60 - 105 = '
                                                  '140 - 105 = 35 devices.',
                                   'id': 'pwc_apt_2',
                                   'options': ['25 devices', '35 devices', '40 devices', '45 devices'],
                                   'question': 'In a corporate network of 120 devices, all devices have antivirus '
                                               'installed. 80 devices have automated OS patching enabled, and 60 '
                                               'devices have full-disk encryption enabled. If 15 devices have NEITHER '
                                               'patching nor encryption, how many devices have BOTH?'}],
               'coding': [   {   'category': 'Monotonic Stack',
                                 'companies': ['PwC'],
                                 'description': 'Given an array of integers temperatures represents daily '
                                                'temperatures, return an array answer such that answer[i] is the '
                                                'number of days you have to wait after the ith day to get a warmer '
                                                'temperature.',
                                 'difficulty': 'Medium',
                                 'id': 'pwc_code_1',
                                 'starter_code': 'def daily_temperatures(temperatures):\n'
                                                 '    # Write your solution here\n'
                                                 '    pass\n',
                                 'test_cases': [   {   'expected': [1, 1, 4, 2, 1, 1, 0, 0],
                                                       'input': [[73, 74, 75, 71, 69, 72, 76, 73]]}],
                                 'title': 'PwC - Daily Temperatures (Monotonic Stack)'}],
               'company_name': 'PwC',
               'hr': [   {   'category': 'Trust Solutions',
                             'id': 1,
                             'question': 'At PwC, trust is our currency. Describe a high-stakes scenario where you had '
                                         'to earn the trust of a skeptical client or project lead.',
                             'tips': 'Focus on disciplined execution, setting realistic milestones, radical '
                                     'transparency about roadblocks, and delivering on promises.'}],
               'technical': [   {   'category': 'Cryptographic Security & Password Storage',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': 'Fast hashes like SHA-256 compute billions of hashes/second on '
                                                   'modern GPUs, making them vulnerable to offline dictionary attacks. '
                                                   'Password hashes must be computationally intensive.',
                                    'id': 'pwc_tech_1',
                                    'options': [   'Bcrypt and Argon2 are intentionally computationally slow (memory '
                                                   'and CPU hard) and incorporate a configurable work factor (salt + '
                                                   'cost), preventing brute-force GPU attacks',
                                                   'SHA-256 can be decrypted with an online dictionary',
                                                   'Bcrypt generates shorter strings',
                                                   'Argon2 only runs on Windows'],
                                    'question': 'Why is Bcrypt or Argon2 strictly required for password hashing '
                                                'instead of fast cryptographic hashes like SHA-256?'},
                                {   'category': 'Disaster Recovery & Business Continuity',
                                    'correctIndex': 0,
                                    'difficulty': 'Medium',
                                    'explanation': 'RPO defines the age of files that must be recovered from backup '
                                                   '(data loss tolerance); RTO defines the time to restore business '
                                                   'operations after disaster.',
                                    'id': 'pwc_tech_2',
                                    'options': [   'RPO measures maximum tolerable data loss in time (how much data is '
                                                   'lost); RTO measures maximum tolerable system downtime (how quickly '
                                                   'service must resume)',
                                                   'RPO is for databases; RTO is for frontend',
                                                   'RPO measures budget; RTO measures human resources',
                                                   'They are synonymous metrics'],
                                    'question': 'In enterprise business continuity audits, what is the critical '
                                                'difference between RPO (Recovery Point Objective) and RTO (Recovery '
                                                'Time Objective)?'}]},
    'redhat': {   'aptitude': [   {   'category': 'Systems Math & Binary Arithmetic',
                                      'correctIndex': 0,
                                      'difficulty': 'Hard',
                                      'explanation': 'Page size is 4KB = 2^12 bytes. The lower 12 bits constitute the '
                                                     'page offset. 12 bits = 3 hexadecimal digits. The last 3 hex '
                                                     'characters are `E10` (3600 in decimal).',
                                      'id': 'rh_apt_1',
                                      'options': [   '0xE10 (3600 decimal)',
                                                     '0x2E10 (11792 decimal)',
                                                     '0x4C2 (1218 decimal)',
                                                     '0x000'],
                                      'question': 'A Linux memory page size is 4KB (2^12 bytes). If a 64-bit virtual '
                                                  'memory address has the hex value `0x00007FFF8A4C2E10`, what is the '
                                                  'byte offset of this address within its page?'},
                                  {   'category': 'Process Scheduling Logic',
                                      'correctIndex': 0,
                                      'difficulty': 'Medium',
                                      'explanation': 'In Unix/Linux, lower nice numbers (e.g. -20 to 0) represent '
                                                     'higher scheduling priority and receive greater CPU execution '
                                                     'weight.',
                                      'id': 'rh_apt_2',
                                      'options': [   'Process A receives more CPU time because lower nice values '
                                                     'indicate higher priority',
                                                     'Process B receives more CPU time',
                                                     'Both receive identical CPU time',
                                                     'CFS does not support nice values'],
                                      'question': 'In the Linux Completely Fair Scheduler (CFS), if Process A has '
                                                  '`nice` value 0 and Process B has `nice` value 5, which process '
                                                  'receives a larger proportion of CPU time?'}],
                  'coding': [   {   'category': 'Concurrency & Data Structures',
                                    'companies': ['Red Hat'],
                                    'description': 'Implement a thread-safe LRU cache that supports concurrent get and '
                                                   'put operations without deadlocks or race conditions.',
                                    'difficulty': 'Hard',
                                    'id': 'rh_code_1',
                                    'starter_code': 'import threading\n'
                                                    'class ConcurrentLRU:\n'
                                                    '    def __init__(self, capacity: int):\n'
                                                    '        pass\n'
                                                    '    def get(self, key: int) -> int:\n'
                                                    '        pass\n'
                                                    '    def put(self, key: int, value: int) -> None:\n'
                                                    '        pass\n',
                                    'test_cases': [{'expected': 'Initialized', 'input': ['ConcurrentLRU', 3]}],
                                    'title': 'Red Hat - LRU Cache with Thread Safety'}],
                  'company_name': 'Red Hat',
                  'hr': [   {   'category': 'Open Source Collaboration & Upstream First',
                                'id': 1,
                                'question': "Red Hat champions the 'Upstream First' philosophy. Have you ever "
                                            'contributed to open source or collaborated in public code repositories? '
                                            'How do you accept feedback from the community?',
                                'tips': 'Highlight openness to constructive critique, adherence to community '
                                        'standards, and giving back to developer tooling.'}],
                  'technical': [   {   'category': 'Linux Kernel & System Calls',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'clone() provides fine-grained control over what execution '
                                                      'context (virtual address space, open files, signal table) is '
                                                      'shared between parent and child.',
                                       'id': 'rh_tech_1',
                                       'options': [   '`fork()` duplicates the calling process with Copy-on-Write '
                                                      'memory; `clone()` allows granular sharing of memory, file '
                                                      'descriptors, and signal handlers (used by pthread creation)',
                                                      '`fork()` creates threads; `clone()` deletes files',
                                                      '`clone()` is only for Windows systems',
                                                      'They are identical aliases'],
                                       'question': 'What is the difference between the Linux system calls `fork()` and '
                                                   '`clone()`?'},
                                   {   'category': 'Container Runtimes & Podman',
                                       'correctIndex': 0,
                                       'difficulty': 'Hard',
                                       'explanation': 'Docker relies on a central daemon running as root, posing '
                                                      'privilege escalation risks. Podman operates directly via '
                                                      'fork/exec with user namespaces without a daemon.',
                                       'id': 'rh_tech_2',
                                       'options': [   'Podman is daemonless and runs rootless containers natively '
                                                      'without requiring a persistent root-privileged daemon process '
                                                      '(`dockerd`)',
                                                      'Podman encrypts memory with RSA-4096',
                                                      'Podman does not use Linux kernel features',
                                                      'Podman only supports Python scripts'],
                                       'question': 'Why is Podman considered architecturally more secure than '
                                                   'traditional Docker for enterprise environments?'},
                                   {   'category': 'Filesystems & Inodes',
                                       'correctIndex': 0,
                                       'difficulty': 'Medium',
                                       'explanation': 'Filesystems allocate a fixed table of Inodes at format time. If '
                                                      'a system generates millions of tiny files, Inodes exhaust '
                                                      'before raw storage capacity runs out.',
                                       'id': 'rh_tech_3',
                                       'options': [   'The filesystem has exhausted all available Inodes (`df -i`) due '
                                                      'to millions of tiny zero-byte files',
                                                      'The CPU is overheating',
                                                      'The RAM is full',
                                                      'The monitor is disconnected'],
                                       'question': 'When a Linux disk reports `No space left on device` but `df -h` '
                                                   'shows 40% disk space remaining, what is the most likely root '
                                                   'cause?'}]},
    'sap': {   'aptitude': [   {   'category': 'SAP Enterprise Math',
                                   'correctIndex': 1,
                                   'difficulty': 'Medium',
                                   'explanation': 'Total units = 6,000. Let A have x units after transfer. B has 1.2x. '
                                                  'x + 1.2x = 6000 => 2.2x = 6000 => x = 2727.27. Transferred = 3600 - '
                                                  '2727.27 = ~545 units.',
                                   'id': 'sap_apt_1',
                                   'options': ['400 units', '545 units', '600 units', '720 units'],
                                   'question': 'An SAP ERP warehouse inventory system updates stock levels. If '
                                               'Warehouse A has 3,600 units and Warehouse B has 2,400 units, how many '
                                               'units must be transferred from A to B so that Warehouse B has 20% more '
                                               'stock than Warehouse A?'},
                               {   'category': 'Matrix Logic',
                                   'correctIndex': 0,
                                   'difficulty': 'Hard',
                                   'explanation': 'A skew-symmetric matrix of even order (4x4) always has a '
                                                  'determinant that is a non-negative perfect square (the square of '
                                                  'its Pfaffian).',
                                   'id': 'sap_apt_2',
                                   'options': [   'Always a perfect square non-negative integer',
                                                  'Always -1',
                                                  'Always 0',
                                                  'Cannot be determined'],
                                   'question': 'In an enterprise resource planning matrix of dimensions 4x4, each '
                                               'entry represents resource allocation costs. If all elements on the '
                                               'main diagonal are 0 and every non-diagonal element A[i][j] satisfies '
                                               'A[i][j] = -A[j][i], what is the determinant of this matrix?'}],
               'coding': [   {   'category': 'Dynamic Programming',
                                 'companies': ['SAP'],
                                 'description': "Given an m x n binary matrix filled with 0's and 1's, find the "
                                                "largest square containing only 1's and return its area.",
                                 'difficulty': 'Medium',
                                 'id': 'sap_code_1',
                                 'starter_code': 'def maximal_square(matrix):\n'
                                                 '    # Write your solution here\n'
                                                 '    pass\n',
                                 'test_cases': [   {   'expected': 4,
                                                       'input': [   [   ['1', '0', '1', '0', '0'],
                                                                        ['1', '0', '1', '1', '1'],
                                                                        ['1', '1', '1', '1', '1'],
                                                                        ['1', '0', '0', '1', '0']]]}],
                                 'title': 'SAP - Maximal Square in Enterprise Grid'}],
               'company_name': 'SAP',
               'hr': [   {   'category': 'Reliability & Customer Focus',
                             'id': 1,
                             'question': 'SAP systems manage mission-critical enterprise data (payroll, supply chains, '
                                         "logistics) for 99 of the world's 100 largest companies. How do you balance "
                                         'innovation with bulletproof stability?',
                             'tips': 'Discuss backward compatibility, comprehensive regression suites, phased '
                                     'rollouts, and zero-downtime blue/green deployments.'}],
               'technical': [   {   'category': 'SAP HANA In-Memory Database Architecture',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': 'OLAP queries aggregate across millions of rows on few columns; '
                                                   'columnar storage reads only those columns into memory and '
                                                   'compresses dictionary values massively.',
                                    'id': 'sap_tech_1',
                                    'options': [   'Columnar storage only loads required query columns into CPU cache, '
                                                   'achieves extreme compression of repetitive values, and allows SIMD '
                                                   'parallel vectorization',
                                                   'Row storage cannot run on Intel CPUs',
                                                   'Columnar databases do not use RAM',
                                                   'HANA deletes all historical data automatically'],
                                    'question': 'Why is Columnar In-Memory Storage in SAP HANA vastly superior to '
                                                'traditional row-oriented databases for real-time enterprise OLAP '
                                                'analytical queries?'},
                                {   'category': 'Enterprise ERP & ACID Enforcement',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': '2PC causes distributed deadlocks and holds resource locks across '
                                                   'network partitions, leading microservices to adopt the Saga '
                                                   'pattern instead.',
                                    'id': 'sap_tech_2',
                                    'options': [   '2PC is a blocking protocol: if the coordinator crashes during '
                                                   'phase 2, all participating resources remain locked, destroying '
                                                   'system availability',
                                                   '2PC is illegal under GDPR',
                                                   '2PC only works on single core machines',
                                                   '2PC cannot run over TCP/IP'],
                                    'question': 'In enterprise ERP supply chain systems, why are Two-Phase Commits '
                                                '(2PC) avoided across independent cloud microservices in favor of '
                                                'Eventual Consistency?'}]},
    'tcs': {   'aptitude': [   {   'category': 'TCS NQT Numerical',
                                   'correctIndex': 1,
                                   'difficulty': 'Medium',
                                   'explanation': 'Interest for 3rd year = 4913 - 4624 = Rs. 289. Rate = (289 / 4624) '
                                                  '* 100 = 6.25%.',
                                   'id': 'tcs_apt_1',
                                   'options': ['5%', '6.25%', '6%', '7.5%'],
                                   'question': 'A sum of money invested at compound interest amounts to Rs. 4,624 in 2 '
                                               'years and to Rs. 4,913 in 3 years. What is the rate of interest per '
                                               'annum?'},
                               {   'category': 'TCS NQT Reasoning',
                                   'correctIndex': 0,
                                   'difficulty': 'Medium',
                                   'explanation': 'Each letter is replaced by its reverse alphabet counterpart (A<->Z, '
                                                  'B<->Y, C<->X, R<->I, E<->V, Q<->J, U<->F, I<->R, R<->I, E<->V, '
                                                  'D<->W) -> IVJFRIVW.',
                                   'id': 'tcs_apt_2',
                                   'options': ['IVJFRIVW', 'VJIFWIRV', 'IVJFRWIV', 'IVJFIRVW'],
                                   'question': "In a certain code, 'CERTAIN' is coded as 'XVIGZRM'. How will "
                                               "'REQUIRED' be coded in that same pattern?"},
                               {   'category': 'TCS NQT Statistics',
                                   'correctIndex': 1,
                                   'difficulty': 'Medium',
                                   'explanation': 'Total sum = 5 * 12 = 60. Sum(first 3) = 30. Sum(last 3) = 39. Sum = '
                                                  '30 + 39 - x = 60 => x = 69 - 60 = 9.',
                                   'id': 'tcs_apt_3',
                                   'options': ['8', '9', '10', '11'],
                                   'question': 'The mean of 5 observations is 12. If the mean of the first 3 '
                                               'observations is 10 and that of the last 3 is 13, find the third '
                                               'observation.'},
                               {   'category': 'TCS NQT Numerical',
                                   'correctIndex': 1,
                                   'difficulty': 'Hard',
                                   'explanation': 'Let CP = 100x. MP = 140x. SP = 140x * 0.75 = 105x. Profit = 5x = '
                                                  '150 => x = 30 => CP = 100 * 30 = Rs. 3,000.',
                                   'id': 'tcs_apt_4',
                                   'options': ['Rs. 2,500', 'Rs. 3,000', 'Rs. 2,800', 'Rs. 3,200'],
                                   'question': 'A shopkeeper marks an article at 40% above the cost price and allows a '
                                               'discount of 25% on the marked price. If he makes a profit of Rs. 150, '
                                               'find the cost price.'},
                               {   'category': 'TCS NQT Reasoning',
                                   'correctIndex': 1,
                                   'difficulty': 'Hard',
                                   'explanation': 'Arranging them circularly facing center gives T sitting directly '
                                                  'opposite to P.',
                                   'id': 'tcs_apt_5',
                                   'options': ['S', 'T', 'U', 'Cannot be determined'],
                                   'question': 'Six friends P, Q, R, S, T, and U sit in a circle facing the center. P '
                                               'is between Q and R. T is second to the left of Q. Who is opposite to '
                                               'P?'},
                               {   'category': 'TCS NQT Advanced Math',
                                   'correctIndex': 1,
                                   'difficulty': 'Hard',
                                   'explanation': 'Let pipe B be closed after t minutes. Pipe A works for full 12 '
                                                  'mins. (12/18) + (t/24) = 1 => 2/3 + t/24 = 1 => t/24 = 1/3 => t = 8 '
                                                  'minutes.',
                                   'id': 'tcs_apt_6',
                                   'options': ['6 mins', '8 mins', '9 mins', '10 mins'],
                                   'question': 'Two pipes A and B can fill a tank in 18 minutes and 24 minutes '
                                               'respectively. If both pipes are opened together, after how many '
                                               'minutes should pipe B be closed so that the tank is full in 12 '
                                               'minutes?'}],
               'coding': [   {   'category': 'Sliding Window',
                                 'companies': ['TCS'],
                                 'description': 'Given an array of integers nums and an integer target, find the '
                                                'minimal length of a contiguous subarray of which the sum is greater '
                                                'than or equal to target. If there is no such subarray, return 0.',
                                 'difficulty': 'Medium',
                                 'id': 'tcs_code_1',
                                 'starter_code': 'def min_subarray_len(target, nums):\n'
                                                 '    # Write your solution here\n'
                                                 '    pass\n',
                                 'test_cases': [{'expected': 2, 'input': [7, [2, 3, 1, 2, 4, 3]]}],
                                 'title': 'TCS Digital - Subarray Sum with Minimum Operations'},
                             {   'category': 'Dynamic Programming',
                                 'companies': ['TCS'],
                                 'description': 'Given an integer array nums, return the length of the longest '
                                                'strictly increasing subsequence in O(N log N) time.',
                                 'difficulty': 'Hard',
                                 'id': 'tcs_code_2',
                                 'starter_code': 'def length_of_lis(nums):\n    # Write your solution here\n    pass\n',
                                 'test_cases': [{'expected': 4, 'input': [[10, 9, 2, 5, 3, 7, 101, 18]]}],
                                 'title': 'TCS Prime - Longest Increasing Subsequence'},
                             {   'category': 'String Manipulation',
                                 'companies': ['TCS'],
                                 'description': 'Given a string with repeated characters, compress it such that '
                                                'consecutive identical characters are replaced by the character '
                                                "followed by count (e.g. 'aabcccccaaa' -> 'a2b1c5a3'). Return original "
                                                'if compressed is not shorter.',
                                 'difficulty': 'Medium',
                                 'id': 'tcs_code_3',
                                 'starter_code': 'def compress_string(s):\n    # Write your solution here\n    pass\n',
                                 'test_cases': [{'expected': 'a2b1c5a3', 'input': ['aabcccccaaa']}],
                                 'title': 'TCS NQT - Run-Length String Compression'}],
               'company_name': 'Tata Consultancy Services (TCS)',
               'hr': [   {   'category': 'Tata Code of Conduct',
                             'id': 1,
                             'question': 'TCS places uncompromising value on the Tata Code of Conduct (TCoC). How '
                                         'would you handle a situation where a client asks you to bypass standard code '
                                         'quality gates or security approvals to meet a tight go-live deadline?',
                             'tips': 'Emphasize ethical integrity, transparent communication of risks, proposing safe '
                                     'phased deliverables, and escalating to delivery managers.'},
                         {   'category': 'Global Delivery Adaptability',
                             'id': 2,
                             'question': 'At TCS, you may work in cross-border teams across multiple time zones '
                                         '(India, US, Europe). Describe how you ensure seamless handoffs and '
                                         'asynchronous collaboration.',
                             'tips': 'Highlight clear documentation, disciplined pull-request reviews, sprint '
                                     'ceremonies, and transparent status dashboards.'}],
               'technical': [   {   'category': 'Java & Spring Enterprise',
                                    'correctIndex': 1,
                                    'difficulty': 'Medium',
                                    'explanation': 'Propagation.REQUIRES_NEW suspends any ambient transaction and '
                                                   'executes within a newly allocated physical transaction.',
                                    'id': 'tcs_tech_1',
                                    'options': [   'Reuses existing database transaction without committing',
                                                   'Suspends any current transaction and creates a completely '
                                                   'independent physical transaction',
                                                   'Rolls back previous transaction unconditionally',
                                                   'Runs the query asynchronously in a separate thread'],
                                    'question': 'In a TCS BaNCS enterprise microservice, what does '
                                                '`@Transactional(propagation = Propagation.REQUIRES_NEW)` do?'},
                                {   'category': 'SQL & Core Banking DBMS',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': 'SELECT ... FOR UPDATE acquires a pessimistic row-level exclusive '
                                                   'lock, blocking other transactions until the ledger balance '
                                                   'modification commits.',
                                    'id': 'tcs_tech_2',
                                    'options': [   'SELECT * FROM accounts WHERE id = ? FOR UPDATE',
                                                   'Dirty read with READ UNCOMMITTED',
                                                   'Client-side JavaScript setTimeout lock',
                                                   'TRUNCATE TABLE accounts'],
                                    'question': 'In high-concurrency banking ledger balance updates, which locking '
                                                'mechanism prevents phantom updates and lost deposits?'},
                                {   'category': 'Microservice Architecture',
                                    'correctIndex': 0,
                                    'difficulty': 'Hard',
                                    'explanation': 'The Saga pattern coordinates local transactions across multiple '
                                                   'microservices with compensating transactions to maintain '
                                                   'consistency without 2PC locking.',
                                    'id': 'tcs_tech_3',
                                    'options': [   'Saga Pattern (Choreography/Orchestration)',
                                                   'Two-Tier Monolith',
                                                   'Client-side alert box',
                                                   'Round-robin DNS'],
                                    'question': 'In distributed microservices at TCS, which pattern handles '
                                                'long-running multi-service business transactions across payment, '
                                                'inventory, and order services?'},
                                {   'category': 'Java Memory & JVM',
                                    'correctIndex': 1,
                                    'difficulty': 'Medium',
                                    'explanation': 'String literals reside in the String Constant Pool, while the new '
                                                   'operator guarantees allocation of a distinct object in standard '
                                                   'Heap memory.',
                                    'id': 'tcs_tech_4',
                                    'options': [   'Both point to the same memory in the String Constant Pool',
                                                   's1 points to String Constant Pool; s2 creates a new object in '
                                                   'standard Heap memory',
                                                   'Compilation error',
                                                   'Both point to JVM Stack'],
                                    'question': 'What happens when two String objects are created as `String s1 = '
                                                '"TCS"; String s2 = new String("TCS");`?'},
                                {   'category': 'Agile & Delivery Management',
                                    'correctIndex': 2,
                                    'difficulty': 'Medium',
                                    'explanation': 'The Retrospective occurs at the end of a sprint to inspect team '
                                                   'performance and identify actionable improvements for the next '
                                                   'iteration.',
                                    'id': 'tcs_tech_5',
                                    'options': [   'To estimate project budget',
                                                   'To demonstrate finished code to the client',
                                                   "To reflect on what went well, what didn't, and commit to "
                                                   'continuous process improvements',
                                                   'To write daily bug reports'],
                                    'question': 'In Agile Scrum methodologies used across TCS delivery teams, what is '
                                                "a 'Sprint Retrospective' meeting for?"}]},
    'techmahindra': {   'aptitude': [   {   'category': 'Tech Mahindra Speed Math',
                                            'correctIndex': 1,
                                            'difficulty': 'Medium',
                                            'explanation': 'Area is proportional to r^2. New radius = 1.5r. New area = '
                                                           '(1.5)^2 * Area = 2.25 * Area. Expansion = 2.25 - 1 = 1.25 '
                                                           '= 125% increase.',
                                            'id': 'tm_apt_1',
                                            'options': ['100%', '125%', '150%', '225%'],
                                            'question': 'A 5G signal tower communicates with mobile units within a '
                                                        'circular radius of 14 km. If a technological upgrade expands '
                                                        "the radius by 50%, by what percentage does the tower's "
                                                        'coverage area expand?'},
                                        {   'category': 'Engineering Reasoning',
                                            'correctIndex': 0,
                                            'difficulty': 'Hard',
                                            'explanation': 'P(survive 5 hops) = (1 - 0.02)^5 = (0.98)^5 = 0.9039 = '
                                                           '~90.39%.',
                                            'id': 'tm_apt_2',
                                            'options': ['90.39%', '92.45%', '95.00%', '98.00%'],
                                            'question': 'In an asynchronous packet network, 5 router hops have latency '
                                                        'values of 4ms, 6ms, 8ms, 12ms, and 15ms. If each packet has a '
                                                        '2% packet-drop probability per hop, what is the probability '
                                                        'that a packet reaches the destination successfully?'}],
                        'coding': [   {   'category': 'Graph Algorithms',
                                          'companies': ['Tech Mahindra'],
                                          'description': 'Given a network of n nodes labeled from 1 to n and travel '
                                                         'times as directed edges times[i] = (u, v, w), return the '
                                                         'minimum time it takes for all nodes to receive a signal from '
                                                         'node k.',
                                          'difficulty': 'Medium',
                                          'id': 'tm_code_1',
                                          'starter_code': 'def network_delay_time(times, n, k):\n'
                                                          '    # Write your solution here\n'
                                                          '    pass\n',
                                          'test_cases': [   {   'expected': 2,
                                                                'input': [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2]}],
                                          'title': "Tech Mahindra - Network Delay Time (Dijkstra's Algorithm)"}],
                        'company_name': 'Tech Mahindra',
                        'hr': [   {   'category': 'Rise Philosophy',
                                      'id': 1,
                                      'question': "Mahindra's 'Rise' philosophy is built on Accepting No Limits, "
                                                  'Alternative Thinking, and Driving Positive Change. Tell me about a '
                                                  'time you refused to accept a perceived technical limitation and '
                                                  'found an alternative solution.',
                                      'tips': 'Share an example of creative engineering where conventional tools '
                                              'failed and you engineered an unconventional workaround.'}],
                        'technical': [   {   'category': '5G & Telecommunications Software',
                                             'correctIndex': 0,
                                             'difficulty': 'Hard',
                                             'explanation': '5G SBA modernizes telecom core networks by adopting '
                                                            'cloud-native principles: HTTP/2 transport, REST '
                                                            'semantics, and JSON serialization between Network '
                                                            'Functions (NFs).',
                                             'id': 'tm_tech_1',
                                             'options': [   'HTTP/2 REST APIs with JSON payloads',
                                                            'FTP with CSV files',
                                                            'Telnet with plain ASCII',
                                                            'COBOL with fixed punch cards'],
                                             'question': 'In 5G Core (5GC) Service-Based Architecture (SBA), which '
                                                         'protocol and serialization format replaces traditional '
                                                         'telecom SS7/Diameter protocols?'},
                                         {   'category': 'Asynchronous Event Loop',
                                             'correctIndex': 0,
                                             'difficulty': 'Medium',
                                             'explanation': 'Non-blocking event loops register file descriptors with '
                                                            'OS event multiplexers and process ready event callbacks '
                                                            'sequentially without thread context switching overhead.',
                                             'id': 'tm_tech_2',
                                             'options': [   'Delegating I/O operations to kernel non-blocking '
                                                            'multiplexers (epoll/kqueue) and processing callbacks '
                                                            'sequentially as events fire',
                                                            'Creating 10,000 physical OS threads',
                                                            'Running faster hardware clock rates',
                                                            'Blocking each request until completion'],
                                             'question': 'How does an asynchronous single-threaded event loop (like '
                                                         'Node.js or Python asyncio) handle thousands of concurrent '
                                                         'I/O connections simultaneously?'}]},
    'wipro': {   'aptitude': [   {   'category': 'Wipro Elite Quantitative',
                                     'correctIndex': 1,
                                     'difficulty': 'Medium',
                                     'explanation': 'Speed = 54 * (5/18) = 15 m/s. Length of train = 15 * 20 = 300 m. '
                                                    'Let platform length = L. (300 + L) = 15 * 36 = 540 => L = 240 m.',
                                     'id': 'wip_apt_1',
                                     'options': ['200 m', '240 m', '260 m', '300 m'],
                                     'question': 'A train passes a station platform in 36 seconds and a man standing '
                                                 'on the platform in 20 seconds. If the speed of the train is 54 '
                                                 'km/hr, what is the length of the platform?'},
                                 {   'category': 'Wipro Logical Syllogisms',
                                     'correctIndex': 0,
                                     'difficulty': 'Medium',
                                     'explanation': 'Since all routers are gateways, any server that is a router must '
                                                    'also be a gateway (Conclusion I follows). Conclusion II is not '
                                                    'necessarily true.',
                                     'id': 'wip_apt_2',
                                     'options': ['Only I follows', 'Only II follows', 'Both follow', 'Neither follows'],
                                     'question': 'Statements: Some servers are routers. All routers are gateways. '
                                                 'Conclusions: I. Some servers are gateways. II. All gateways are '
                                                 'routers.'},
                                 {   'category': 'Wipro Turbo Probability',
                                     'correctIndex': 0,
                                     'difficulty': 'Hard',
                                     'explanation': 'Total = 12. Pairs = 12C2 = 66. Same color pairs = 5C2 + 4C2 + 3C2 '
                                                    '= 10 + 6 + 3 = 19. Probability = 19/66.',
                                     'id': 'wip_apt_3',
                                     'options': ['19/66', '23/66', '17/66', '25/66'],
                                     'question': 'A bag contains 5 red, 4 blue, and 3 green network cables. If 2 '
                                                 'cables are drawn at random without replacement, what is the '
                                                 'probability that both are of the same color?'},
                                 {   'category': 'Wipro Number Series',
                                     'correctIndex': 1,
                                     'difficulty': 'Hard',
                                     'explanation': 'Pattern is n^3 - n^2: 2^3 - 2^2 = 4, 3^3 - 3^2 = 18, 4^3 - 4^2 = '
                                                    '48, 5^3 - 5^2 = 100, 6^3 - 6^2 = 180, 7^3 - 7^2 = 343 - 49 = 294.',
                                     'id': 'wip_apt_4',
                                     'options': ['244', '294', '312', '324'],
                                     'question': 'Find the missing number in the sequence: 4, 18, 48, 100, 180, ___?'}],
                 'coding': [   {   'category': 'Arrays',
                                   'companies': ['Wipro'],
                                   'description': 'Implement next permutation, which rearranges numbers into the '
                                                  'lexicographically next greater permutation of numbers in-place.',
                                   'difficulty': 'Medium',
                                   'id': 'wip_code_1',
                                   'starter_code': 'def next_permutation(nums):\n'
                                                   '    # Modify nums in-place\n'
                                                   '    pass\n',
                                   'test_cases': [{'expected': [1, 3, 2], 'input': [[1, 2, 3]]}],
                                   'title': 'Wipro Turbo - Next Lexicographical Permutation'},
                               {   'category': 'Binary Search',
                                   'companies': ['Wipro'],
                                   'description': 'Given a rotated sorted array nums with distinct values and a '
                                                  'target, return the index of target, or -1 if not found in O(log N) '
                                                  'time.',
                                   'difficulty': 'Medium',
                                   'id': 'wip_code_2',
                                   'starter_code': 'def search(nums, target):\n'
                                                   '    # Write your solution here\n'
                                                   '    pass\n',
                                   'test_cases': [{'expected': 4, 'input': [[4, 5, 6, 7, 0, 1, 2], 0]}],
                                   'title': 'Wipro Elite - Search in Rotated Sorted Array'}],
                 'company_name': 'Wipro',
                 'hr': [   {   'category': 'Spirit of Wipro',
                               'id': 1,
                               'question': "The 'Spirit of Wipro' encompasses Be Passionate about Clients' Success, "
                                           'Treat each person with respect, and Be global and responsible. Can you '
                                           'give an example of treating team members with empathy during a crisis?',
                               'tips': 'Talk about actively supporting a teammate who was overwhelmed by deadlines or '
                                       'production issues.'}],
                 'technical': [   {   'category': 'Operating Systems & Concurrency',
                                      'correctIndex': 0,
                                      'difficulty': 'Hard',
                                      'explanation': 'The 4 essential Coffman conditions are Mutual Exclusion, Hold & '
                                                     'Wait, No Preemption, and Circular Wait.',
                                      'id': 'wip_tech_1',
                                      'options': [   'Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait',
                                                     'Starvation, Thrashing, Page Fault, Race Condition',
                                                     'Segmentation, Paging, TLB Miss, Context Switch',
                                                     'Polling, Interrupt, DMA, Cache Coherence'],
                                      'question': 'Which of the following are the four Coffman conditions required '
                                                  'simultaneously for a system deadlock to occur?'},
                                  {   'category': 'Computer Networking & Protocols',
                                      'correctIndex': 0,
                                      'difficulty': 'Medium',
                                      'explanation': 'Client sends SYN, server responds with SYN-ACK, client concludes '
                                                     'handshake with ACK.',
                                      'id': 'wip_tech_2',
                                      'options': [   'SYN -> SYN-ACK -> ACK',
                                                     'ACK -> SYN -> FIN',
                                                     'RST -> SYN -> ACK',
                                                     'SYN -> ACK -> DATA'],
                                      'question': 'During the TCP 3-way handshake, what sequence of control flags is '
                                                  'exchanged between client and server?'},
                                  {   'category': 'DBMS & Indexing',
                                      'correctIndex': 1,
                                      'difficulty': 'Hard',
                                      'explanation': 'Hash indexes only support exact equality checks (O(1)), whereas '
                                                     'B+ Trees support range scanning and ordered traversals through '
                                                     'chained leaf pages.',
                                      'id': 'wip_tech_3',
                                      'options': [   'B+ Trees consume zero disk memory',
                                                     'B+ Trees efficiently support range queries (BETWEEN, <, >) '
                                                     'because leaf nodes form an ordered linked list',
                                                     'Hash indexes cannot store integers',
                                                     'B+ Trees have O(1) worst-case lookup'],
                                      'question': 'Why do relational database engines utilize B+ Trees instead of Hash '
                                                  'indexes for primary key storage by default?'}]}}


def get_company_bank(slug: str) -> Optional[Dict[str, Any]]:
    """Retrieve full question bank for a company by slug."""
    slug_clean = (slug or "tcs").strip().lower()
    # Normalize common aliases
    if "google" in slug_clean:
        slug_clean = "google"
    elif "amazon" in slug_clean:
        slug_clean = "amazon"
    elif "microsoft" in slug_clean:
        slug_clean = "microsoft"
    elif "oracle" in slug_clean:
        slug_clean = "oracle"
    elif "infosys" in slug_clean:
        slug_clean = "infosys"
    elif "accenture" in slug_clean:
        slug_clean = "accenture"
    elif "wipro" in slug_clean:
        slug_clean = "wipro"
    elif "tcs" in slug_clean or "tata" in slug_clean:
        slug_clean = "tcs"
    elif "deloitte" in slug_clean:
        slug_clean = "deloitte"
    elif "capgemini" in slug_clean:
        slug_clean = "capgemini"
    elif "cognizant" in slug_clean:
        slug_clean = "cognizant"
    elif "ibm" in slug_clean:
        slug_clean = "ibm"
    elif "redhat" in slug_clean or "red hat" in slug_clean:
        slug_clean = "redhat"
    elif "hcl" in slug_clean:
        slug_clean = "hcltech"
    elif "mahindra" in slug_clean:
        slug_clean = "techmahindra"
    elif "mindtree" in slug_clean or "lti" in slug_clean:
        slug_clean = "ltimindtree"
    elif "persistent" in slug_clean:
        slug_clean = "persistent"
    elif "sap" in slug_clean:
        slug_clean = "sap"
    elif "ey" in slug_clean or "ernst" in slug_clean:
        slug_clean = "ey"
    elif "pwc" in slug_clean or "pricewaterhouse" in slug_clean:
        slug_clean = "pwc"

    return COMPANY_QUESTIONS_BANK.get(slug_clean, COMPANY_QUESTIONS_BANK.get("tcs"))


def get_company_aptitude_questions(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific aptitude questions, shuffled dynamically."""
    bank = get_company_bank(slug)
    qs = [dict(q) for q in (bank.get("aptitude", []) if bank else [])]
    if shuffle:
        random.shuffle(qs)
    return qs


def get_company_technical_questions(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific technical questions, shuffled dynamically."""
    bank = get_company_bank(slug)
    qs = [dict(q) for q in (bank.get("technical", []) if bank else [])]
    if shuffle:
        random.shuffle(qs)
    return qs


def get_company_coding_problems(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific coding problems, shuffled dynamically."""
    bank = get_company_bank(slug)
    problems = [dict(p) for p in (bank.get("coding", []) if bank else [])]
    if shuffle:
        random.shuffle(problems)
    return problems


def get_company_hr_questions(slug: str, shuffle: bool = True) -> List[Dict[str, Any]]:
    """Retrieve company-specific HR & behavioral questions, shuffled dynamically."""
    bank = get_company_bank(slug)
    qs = [dict(q) for q in (bank.get("hr", []) if bank else [])]
    if shuffle:
        random.shuffle(qs)
    return qs
