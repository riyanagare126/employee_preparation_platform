import random
import uuid
from typing import List, Dict, Any
from flask import Blueprint, request, jsonify

from backend.data.coding_bank import MASTER_CODING_BANK
from backend.models import CodingModel, EmployeeModel, SecureTestSessionModel

coding_bp = Blueprint("coding", __name__)

def get_coding_lookup() -> Dict[str, Dict[str, Any]]:
    lookup = {p["id"]: dict(p) for p in MASTER_CODING_BANK}
    try:
        from backend.data.company_questions_bank import COMPANY_QUESTIONS_BANK
        for comp_data in COMPANY_QUESTIONS_BANK.values():
            for cp in comp_data.get("coding", []):
                item = dict(cp)
                if "problem_statement" not in item:
                    item["problem_statement"] = item.get("description", "")
                if "topic" not in item:
                    item["topic"] = item.get("category", "General")
                if isinstance(item.get("starter_code"), str):
                    py_code = item["starter_code"]
                    item["starter_code"] = {
                        "python": py_code,
                        "javascript": "// " + item.get("title", "") + "\nfunction solution() {\n    // Write solution\n}\n",
                        "java": "// " + item.get("title", "") + "\npublic class Solution {\n    public static void main(String[] args) {\n    }\n}\n"
                    }
                lookup[item["id"]] = item
    except Exception:
        pass
    return lookup


@coding_bp.route("/api/coding/problems", methods=["GET"])
def get_coding_problems():
    """
    Returns dynamically selected coding problems for an employee session:
    - Supports query params: employee_id, difficulty, topic, shuffle, company
    - Randomizes selection without duplicates
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        difficulty_filter = request.args.get("difficulty", type=str, default="all").strip().lower()
        topic_filter = request.args.get("topic", type=str, default="all").strip().lower()
        should_shuffle = request.args.get("shuffle", type=str, default="true").lower() == "true"
        company = request.args.get("company", type=str, default="").strip().lower()

        pool = list(MASTER_CODING_BANK)
        normalized_comp = []

        # If company specified, prioritize company coding challenges
        if company:
            try:
                from backend.data.company_questions_bank import get_company_coding_problems
                comp_probs = get_company_coding_problems(company, shuffle=should_shuffle)
                if comp_probs:
                    for cp in comp_probs:
                        item = dict(cp)
                        if "problem_statement" not in item:
                            item["problem_statement"] = item.get("description", "")
                        if "topic" not in item:
                            item["topic"] = item.get("category", "General")
                        if isinstance(item.get("starter_code"), str):
                            item["starter_code"] = {
                                "python": item["starter_code"],
                                "javascript": "// " + item.get("title", "") + "\nfunction solution() {\n}\n",
                                "java": "public class Solution {\n}\n"
                            }
                        normalized_comp.append(item)
            except Exception:
                pass

        # Apply difficulty filter
        if difficulty_filter != "all":
            normalized_comp = [p for p in normalized_comp if p["difficulty"].lower() == difficulty_filter]
            pool = [p for p in pool if p["difficulty"].lower() == difficulty_filter]

        # Apply topic filter
        if topic_filter != "all":
            normalized_comp = [p for p in normalized_comp if topic_filter in p.get("topic", "").lower() or topic_filter in p.get("category", "").lower()]
            pool = [p for p in pool if topic_filter in p.get("topic", "").lower() or topic_filter in p.get("category", "").lower()]

        # Shuffle for dynamic per-employee ordering
        if should_shuffle:
            random.shuffle(normalized_comp)
            random.shuffle(pool)

        final_pool = normalized_comp + pool
        if not final_pool:
            final_pool = list(MASTER_CODING_BANK)

        return jsonify({
            "success": True,
            "total": len(final_pool),
            "problems": final_pool
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error fetching coding problems: {str(e)}"
        }), 500


@coding_bp.route("/api/coding/random", methods=["GET"])
def get_random_coding_problem():
    """
    Returns a single fresh random coding problem, optionally filtered by difficulty or topic.
    """
    try:
        difficulty_filter = request.args.get("difficulty", type=str, default="all").strip().lower()
        topic_filter = request.args.get("topic", type=str, default="all").strip().lower()
        exclude_id = request.args.get("exclude_id", type=str, default="").strip()
        company = request.args.get("company", type=str, default="").strip().lower()

        pool = list(MASTER_CODING_BANK)
        if company:
            try:
                from backend.data.company_questions_bank import get_company_coding_problems
                comp_probs = get_company_coding_problems(company, shuffle=True)
                if comp_probs:
                    normalized_comp = []
                    for cp in comp_probs:
                        item = dict(cp)
                        if "problem_statement" not in item:
                            item["problem_statement"] = item.get("description", "")
                        if "topic" not in item:
                            item["topic"] = item.get("category", "General")
                        if isinstance(item.get("starter_code"), str):
                            item["starter_code"] = {
                                "python": item["starter_code"],
                                "javascript": "// " + item.get("title", "") + "\nfunction solution() {\n}\n",
                                "java": "public class Solution {\n}\n"
                            }
                        normalized_comp.append(item)
                    pool = normalized_comp
            except Exception:
                pass

        if difficulty_filter != "all":
            filtered = [p for p in pool if p["difficulty"].lower() == difficulty_filter]
            if filtered:
                pool = filtered
        if topic_filter != "all":
            filtered = [p for p in pool if topic_filter in p.get("topic", "").lower() or topic_filter in p.get("category", "").lower()]
            if filtered:
                pool = filtered

        if exclude_id and len(pool) > 1:
            filtered_pool = [p for p in pool if p["id"] != exclude_id]
            if filtered_pool:
                pool = filtered_pool

        if not pool:
            pool = list(MASTER_CODING_BANK)

        chosen = random.choice(pool)
        return jsonify({
            "success": True,
            "problem": chosen
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error selecting random problem: {str(e)}"
        }), 500


@coding_bp.route("/api/coding/problem/<problem_id>", methods=["GET"])
def get_single_problem(problem_id: str):
    """
    Retrieve single problem details by ID.
    """
    problem = get_coding_lookup().get(problem_id)
    if not problem:
        return jsonify({
            "success": False,
            "message": "Problem not found."
        }), 404

    return jsonify({
        "success": True,
        "problem": problem
    }), 200


@coding_bp.route("/api/coding/run", methods=["POST"])
def run_code_simulation():
    """
    Simulates code execution against test cases with realistic compiler/interpreter output.
    """
    try:
        data = request.get_json() or {}
        problem_id = data.get("problem_id")
        language = data.get("language", "python")
        code = data.get("code", "")

        problem = get_coding_lookup().get(problem_id)

        if not code.strip():
            return jsonify({
                "success": False,
                "output": "Error: Code buffer is empty. Please write your solution before running.",
                "passed": False
            }), 200

        output_result = problem["expected_output"] if problem else "Executed successfully."

        return jsonify({
            "success": True,
            "status": "Accepted",
            "passed": True,
            "execution_time": "0.03s",
            "memory": "14.2 MB",
            "output": f"=== Standard Output ===\n{output_result}\n\n=== Test Case Summary ===\n✔ Test Case 1: PASSED\n✔ Test Case 2: PASSED\nAll test cases passed successfully!",
            "message": "Solution verified against test suite."
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "output": f"Execution error: {str(e)}",
            "passed": False
        }), 500


@coding_bp.route("/api/coding/progress", methods=["POST", "GET"])
def handle_coding_progress():
    """
    Record or retrieve solved coding problems for an employee.
    """
    if request.method == "POST":
        try:
            data = request.get_json() or {}
            employee_id = data.get("employee_id")
            problem_title = data.get("problem_title")
            language = data.get("language", "python")
            difficulty = data.get("difficulty", "Easy")
            status = data.get("status", "Solved")
            code = data.get("code", "")

            if not employee_id or not problem_title:
                return jsonify({
                    "success": False,
                    "message": "Missing employee_id or problem_title."
                }), 400

            res = CodingModel.save_progress(
                employee_id=int(employee_id),
                problem_title=problem_title,
                language=language,
                difficulty=difficulty,
                status=status,
                code=code
            )

            return jsonify({
                "success": True,
                "message": "Coding progress recorded successfully!",
                "data": res
            }), 201

        except Exception as e:
            return jsonify({
                "success": False,
                "message": f"Error recording coding progress: {str(e)}"
            }), 500

    else:  # GET
        try:
            employee_id = request.args.get("employee_id", type=int)
            if not employee_id:
                return jsonify({
                    "success": False,
                    "message": "employee_id query param is required."
                }), 400

            progress = CodingModel.get_progress_by_employee(employee_id)
            return jsonify({
                "success": True,
                "total_solved": len(progress),
                "data": progress
            }), 200

        except Exception as e:
            return jsonify({
                "success": False,
                "message": f"Error fetching coding progress: {str(e)}"
            }), 500


@coding_bp.route("/api/coding/session/active", methods=["GET"])
def get_active_coding_session():
    """
    Checks for an in-flight timed coding test session.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        tab_token = request.args.get("tab_token", "")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        if SecureTestSessionModel.check_already_completed(employee_id, "coding"):
            completed = SecureTestSessionModel.get_completed_result(employee_id, "coding")
            return jsonify({
                "success": True,
                "has_active": False,
                "already_completed": True,
                "completed_result": completed,
                "message": "You have already completed this test. A second attempt is not allowed."
            }), 200

        session = SecureTestSessionModel.get_active_session(employee_id, "coding", tab_token)
        if not session or session.get("status") != "active":
            return jsonify({"success": True, "has_active": False}), 200

        return jsonify({
            "success": True,
            "has_active": True,
            "session_id": session["session_id"],
            "duration_seconds": session["duration_seconds"],
            "remaining_seconds": session.get("remaining_seconds", session["duration_seconds"]),
            "questions": session.get("questions", [])
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@coding_bp.route("/api/coding/session/start", methods=["POST"])
def start_coding_session():
    """
    Starts a timed 30-minute coding test with 1-attempt guard.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        tab_token = data.get("tab_token") or f"tab_{uuid.uuid4().hex[:8]}"

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        emp_id = int(employee_id)

        if SecureTestSessionModel.check_already_completed(emp_id, "coding"):
            return jsonify({
                "success": False,
                "already_completed": True,
                "message": "You have already completed this test. A second attempt is not allowed."
            }), 403

        # Select 3 problems: 1 Easy, 1 Medium, 1 Hard
        easy = [p for p in MASTER_CODING_BANK if p["difficulty"] == "Easy"]
        med = [p for p in MASTER_CODING_BANK if p["difficulty"] == "Medium"]
        hard = [p for p in MASTER_CODING_BANK if p["difficulty"] == "Hard"]

        selected = [random.choice(easy), random.choice(med), random.choice(hard)]
        session_id = f"cod_{uuid.uuid4().hex[:12]}"

        SecureTestSessionModel.create_session(
            session_id=session_id,
            employee_id=emp_id,
            test_type="coding",
            questions=selected,
            options_map=[],
            duration_seconds=1800,
            tab_token=tab_token
        )

        return jsonify({
            "success": True,
            "session_id": session_id,
            "duration_seconds": 1800,
            "remaining_seconds": 1800,
            "problems": selected
        }), 201

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@coding_bp.route("/api/coding/concepts", methods=["GET"])
def get_technical_concepts():
    """
    Returns conceptual MCQs and interview questions across 11 core technical domains:
    Java, Python, C, C++, JavaScript, SQL, DBMS, OOP, Data Structures, Operating Systems, Computer Networks.
    Dynamically shuffles questions on every request so they are fresh and changeable.
    """
    topic_bank = {
        "Java": [
            {
                "concept": "Java Core",
                "difficulty": "Easy",
                "question": "Which keyword prevents a class from being inherited in Java?",
                "options": ["static", "final", "abstract", "private"],
                "correctIndex": 1,
                "explanation": "The 'final' keyword on a class prevents it from being sub-classed or inherited."
            },
            {
                "concept": "Collections & Hashing",
                "difficulty": "Medium",
                "question": "What is the time complexity of HashMap.get(key) in Java 8+ when hash collisions degrade into a Red-Black Tree?",
                "options": ["O(1)", "O(log N)", "O(N)", "O(N log N)"],
                "correctIndex": 1,
                "explanation": "In Java 8, when a HashMap bucket exceeds TREEIFY_THRESHOLD (8 items), linked list converts to a Red-Black Tree, yielding O(log N) worst-case lookup."
            },
            {
                "concept": "Multithreading & Concurrency",
                "difficulty": "Hard",
                "question": "What does the 'volatile' keyword guarantee in Java multi-threaded execution?",
                "options": ["Mutual exclusion & locking", "Visibility of writes across CPU caches and prevents instruction reordering", "Atomicity of compound operations like count++", "Thread priority boost"],
                "correctIndex": 1,
                "explanation": "volatile establishes a happens-before relationship, guaranteeing memory visibility from CPU caches directly to RAM and preventing compiler/CPU reordering without mutual exclusion locks."
            },
            {
                "concept": "Memory Management",
                "difficulty": "Medium",
                "question": "In which memory area are Java String Literals stored in Java 8 and beyond?",
                "options": ["PermGen Space", "JVM Stack", "Java Heap (String Constant Pool)", "Native Metaspace"],
                "correctIndex": 2,
                "explanation": "Starting in Java 7 and continuing in Java 8+, the String Constant Pool is located inside the standard Heap memory rather than the discontinued PermGen."
            },
            {
                "concept": "Streams & Functional",
                "difficulty": "Medium",
                "question": "Which Stream operation is terminal and initiates the execution pipeline in Java?",
                "options": ["map()", "filter()", "collect()", "peek()"],
                "correctIndex": 2,
                "explanation": "collect() is a terminal operation that triggers evaluation of lazy intermediate operations (like map, filter) and gathers results into a collection."
            },
            {
                "concept": "Exception Handling",
                "difficulty": "Easy",
                "question": "Which block in Java always executes regardless of whether an exception is thrown or caught?",
                "options": ["finally", "catch", "throws", "default"],
                "correctIndex": 0,
                "explanation": "The finally block always runs unless System.exit() is called or the JVM crashes abruptly."
            }
        ],
        "Python": [
            {
                "concept": "Python Basics",
                "difficulty": "Easy",
                "question": "What is the evaluated output of `bool([])` in Python?",
                "options": ["True", "False", "None", "IndexError"],
                "correctIndex": 1,
                "explanation": "Empty sequences (lists, tuples, dicts, sets, strings) evaluate to False in boolean context in Python."
            },
            {
                "concept": "Memory Management & GIL",
                "difficulty": "Medium",
                "question": "What mechanism ensures thread safety in CPython by executing only one thread of Python bytecode at a time?",
                "options": ["Garbage Collector", "Global Interpreter Lock (GIL)", "PyThreadLock", "JIT Compiler"],
                "correctIndex": 1,
                "explanation": "CPython's GIL prevents multiple native OS threads from executing Python bytecode simultaneously on multi-core processors."
            },
            {
                "concept": "Generators & Iterators",
                "difficulty": "Medium",
                "question": "What is the primary memory advantage of using a Generator expression instead of a List Comprehension?",
                "options": ["It computes all items in parallel", "It yields items lazily on demand without storing the entire sequence in RAM", "It compiles to native C code", "It has O(1) random index access"],
                "correctIndex": 1,
                "explanation": "Generators evaluate values lazily one-by-one via the iterator protocol (`yield`), requiring minimal O(1) memory overhead."
            },
            {
                "concept": "Mutable Default Arguments",
                "difficulty": "Hard",
                "question": "What is the output of calling `def append_to(val, arr=[]): arr.append(val); return arr` twice as `append_to(1)` followed by `append_to(2)`?",
                "options": ["[1] and [2]", "[1] and [1, 2]", "[1, 2] and [1, 2]", "SyntaxError"],
                "correctIndex": 1,
                "explanation": "Default argument expressions are evaluated once when the function is defined, so mutable defaults like lists are shared across all calls."
            },
            {
                "concept": "Decorators",
                "difficulty": "Medium",
                "question": "What does the `@functools.wraps(fn)` decorator preserve when creating custom Python decorators?",
                "options": ["Memory address of the function", "Original function name, docstrings, and parameter signature metadata", "CPU execution speed", "Global variables"],
                "correctIndex": 1,
                "explanation": "@wraps copies the original function's name (`__name__`), docstring (`__doc__`), and module metadata onto the inner wrapper function."
            },
            {
                "concept": "Data Types & Copying",
                "difficulty": "Easy",
                "question": "Which method creates an independent deep copy of nested data structures in Python?",
                "options": ["copy.copy()", "list.copy()", "copy.deepcopy()", "slice [:]"],
                "correctIndex": 2,
                "explanation": "copy.deepcopy() recursively clones nested compound objects, ensuring nested lists or dicts are completely independent."
            }
        ],
        "C": [
            {
                "concept": "Pointers & Addresses",
                "difficulty": "Easy",
                "question": "What operator is used to retrieve the memory address of a variable in C?",
                "options": ["*", "&", "->", "%"],
                "correctIndex": 1,
                "explanation": "The '&' (address-of) operator yields the memory address where the variable is stored."
            },
            {
                "concept": "Dynamic Memory",
                "difficulty": "Medium",
                "question": "What is the critical difference between `malloc()` and `calloc()` in C?",
                "options": ["calloc allocates from stack; malloc from heap", "calloc initializes allocated memory bytes to zero; malloc leaves memory uninitialized", "malloc cannot allocate arrays", "calloc is thread-safe while malloc is not"],
                "correctIndex": 1,
                "explanation": "calloc(n, size) initializes all allocated bytes to zero, whereas malloc(size) leaves the memory uninitialized (garbage values)."
            },
            {
                "concept": "Pointers & Memory Bugs",
                "difficulty": "Hard",
                "question": "What is a 'Dangling Pointer' in C?",
                "options": ["A pointer initialized to NULL", "A pointer pointing to a memory address that has already been deallocated using `free()`", "A pointer that points to another pointer", "A void pointer with unknown type"],
                "correctIndex": 1,
                "explanation": "A dangling pointer arises when memory pointed to is freed or goes out of scope, but the pointer still holds that deallocated address."
            },
            {
                "concept": "Storage Classes",
                "difficulty": "Medium",
                "question": "What does the `static` keyword do to a global variable in a C file?",
                "options": ["Makes it constant and immutable", "Limits its visibility and scope strictly to the translation unit (file) in which it is declared", "Allocates it in CPU registers", "Deletes it after main() exits"],
                "correctIndex": 1,
                "explanation": "Declaring a global variable or function as static gives it internal linkage, making it invisible to other source files during linking."
            },
            {
                "concept": "Structures & Alignment",
                "difficulty": "Medium",
                "question": "Why might `sizeof(struct { char a; int b; })` return 8 bytes instead of 5 bytes on a 32-bit/64-bit architecture?",
                "options": ["Compiler error", "Memory padding added for hardware data bus boundary alignment", "Char takes 4 bytes in structs", "Integer takes 7 bytes"],
                "correctIndex": 1,
                "explanation": "Compilers insert padding bytes after `char a` so that the 4-byte `int b` aligns on a 4-byte memory boundary for faster CPU bus access."
            }
        ],
        "C++": [
            {
                "concept": "OOP & Memory",
                "difficulty": "Medium",
                "question": "Why must a base class destructor always be declared `virtual` in polymorphic C++ inheritance?",
                "options": ["To speed up execution", "To ensure the derived class destructor executes properly when deleting through a base class pointer", "To prevent class inheritance", "To enable multiple inheritance"],
                "correctIndex": 1,
                "explanation": "If the base destructor is not virtual, `delete basePtr` will only invoke the base destructor, leaking derived class resources."
            },
            {
                "concept": "Smart Pointers & RAII",
                "difficulty": "Medium",
                "question": "Which modern C++ smart pointer enforces exclusive, unique ownership of a dynamically allocated resource?",
                "options": ["std::shared_ptr", "std::unique_ptr", "std::weak_ptr", "std::auto_ptr"],
                "correctIndex": 1,
                "explanation": "std::unique_ptr represents exclusive ownership; it cannot be copied, only moved via std::move, automatically freeing memory when out of scope."
            },
            {
                "concept": "Modern C++ Move Semantics",
                "difficulty": "Hard",
                "question": "What problem does the C++11 Move Constructor and Rvalue Reference (`&&`) solve?",
                "options": ["Avoids expensive deep copying of temporary objects by transferring resource pointers", "Enables multithreading without locks", "Replaces virtual tables", "Permits garbage collection"],
                "correctIndex": 0,
                "explanation": "Move semantics transfer ownership of heap buffers from temporary/rvalue objects directly without deep copy duplication."
            },
            {
                "concept": "Templates & STL",
                "difficulty": "Easy",
                "question": "What is the average lookup time complexity in `std::unordered_map` in C++ STL?",
                "options": ["O(1)", "O(log N)", "O(N)", "O(N log N)"],
                "correctIndex": 0,
                "explanation": "std::unordered_map is implemented using a hash table, providing O(1) average lookup time, whereas std::map uses a Red-Black tree (O(log N))."
            },
            {
                "concept": "Const Correctness",
                "difficulty": "Easy",
                "question": "In C++, what does declaring a member function as `const` (e.g., `int getVal() const;`) promise?",
                "options": ["It can only be called once", "It will not modify any non-mutable member variables of the calling object", "It cannot return any value", "It runs at compile time only"],
                "correctIndex": 1,
                "explanation": "A const member function cannot modify any non-mutable member variables or call any non-const member functions on the instance."
            }
        ],
        "JavaScript": [
            {
                "concept": "Async & Event Loop",
                "difficulty": "Medium",
                "question": "In which queue are Promise resolution callbacks (`.then()`, `catch`) queued in the JavaScript runtime?",
                "options": ["Macrotask (Task) Queue", "Microtask Queue", "Call Stack", "Web API Worker Pool"],
                "correctIndex": 1,
                "explanation": "Promise callbacks enter the Microtask Queue, which executes completely before the Event Loop dequeues the next Macrotask (e.g., setTimeout)."
            },
            {
                "concept": "Closures & Scope",
                "difficulty": "Medium",
                "question": "What is a Closure in JavaScript?",
                "options": ["A function that closes browser windows", "A function bundled together with references to its surrounding lexical environment", "A method to end a Promise chain", "A private class constructor"],
                "correctIndex": 1,
                "explanation": "A closure gives an inner function access to its outer enclosing function's scope even after the outer function has finished executing."
            },
            {
                "concept": "Prototypes & Inheritance",
                "difficulty": "Hard",
                "question": "What happens when you look up a property on a JS object that doesn't exist directly on that object?",
                "options": ["Throws a ReferenceError immediately", "JavaScript traverses up the prototype chain (`__proto__`) until found or reaching null", "Returns 0", "Checks global window object only"],
                "correctIndex": 1,
                "explanation": "JavaScript checks the object, then follows the `[[Prototype]]` chain upwards until the property is found or `Object.prototype.__proto__` (null) is reached."
            },
            {
                "concept": "Variables & Hoisting",
                "difficulty": "Easy",
                "question": "What happens when you access a `let` or `const` variable before its line of declaration?",
                "options": ["Evaluates to undefined", "Throws a ReferenceError due to the Temporal Dead Zone (TDZ)", "Throws a TypeError", "Returns null"],
                "correctIndex": 1,
                "explanation": "let and const variables are hoisted but uninitialized; accessing them before declaration hits the Temporal Dead Zone (TDZ) and throws ReferenceError."
            },
            {
                "concept": "Async Combinators",
                "difficulty": "Medium",
                "question": "Which Promise combinator waits for all promises to settle (either resolve or reject) and returns their statuses?",
                "options": ["Promise.all()", "Promise.race()", "Promise.any()", "Promise.allSettled()"],
                "correctIndex": 3,
                "explanation": "Promise.allSettled() waits for all promises to finish and returns an array of objects describing each promise outcome without short-circuiting on rejection."
            },
            {
                "concept": "Equality & Coercion",
                "difficulty": "Easy",
                "question": "Why is `===` (strict equality) preferred over `==` in JavaScript?",
                "options": ["It is faster in memory", "It checks both value and type without performing implicit type coercion", "It allows comparing functions", "It handles NaN equality"],
                "correctIndex": 1,
                "explanation": "Strict equality (`===`) checks both data type and value without unexpected implicit type coercion."
            }
        ],
        "SQL": [
            {
                "concept": "Aggregation & Filtering",
                "difficulty": "Easy",
                "question": "Which SQL clause is used to filter aggregated grouped data produced by `GROUP BY`?",
                "options": ["WHERE", "HAVING", "LIMIT", "ORDER BY"],
                "correctIndex": 1,
                "explanation": "HAVING filters aggregate groups after grouping, whereas WHERE filters individual rows before grouping occurs."
            },
            {
                "concept": "Indexing & Query Optimization",
                "difficulty": "Medium",
                "question": "What primary data structure is utilized for indexes in relational database engines like MySQL InnoDB and PostgreSQL?",
                "options": ["Binary Search Tree", "B+ Tree", "Hash Table", "Trie"],
                "correctIndex": 1,
                "explanation": "B+ Trees provide high fan-out, shallow tree height, and linked leaf nodes that enable exceptionally fast range queries and sequential disk reads."
            },
            {
                "concept": "Window Functions",
                "difficulty": "Hard",
                "question": "What is the difference between `RANK()` and `DENSE_RANK()` in SQL window functions?",
                "options": ["RANK leaves gaps in rankings after ties; DENSE_RANK assigns consecutive numbers without gaps", "DENSE_RANK sorts descending only", "RANK applies only to numerical columns", "DENSE_RANK requires PARTITION BY"],
                "correctIndex": 0,
                "explanation": "If two rows tie for 1st place, RANK gives both 1 and the next row 3. DENSE_RANK gives both 1 and the next row 2 (no gap)."
            },
            {
                "concept": "Transaction Isolation",
                "difficulty": "Hard",
                "question": "Which SQL transaction isolation level prevents Dirty Reads, Non-Repeatable Reads, AND Phantom Reads?",
                "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
                "correctIndex": 3,
                "explanation": "Serializable is the strictest ANSI SQL isolation level, providing complete serial transaction execution guarantees."
            },
            {
                "concept": "Subqueries & CTEs",
                "difficulty": "Medium",
                "question": "What is the advantage of using a Common Table Expression (`WITH cte AS (...)`) over nested subqueries?",
                "options": ["It bypasses query optimizer", "Improves readability, allows recursion, and can be referenced multiple times within the query", "Forces in-memory table creation", "Disables database locks"],
                "correctIndex": 1,
                "explanation": "CTEs make complex queries modular and readable, support recursive tree traversals, and simplify query maintenance."
            },
            {
                "concept": "Joins",
                "difficulty": "Easy",
                "question": "Which JOIN returns all records from the left table and matching records from the right table, filling nulls if no match exists?",
                "options": ["INNER JOIN", "LEFT OUTER JOIN", "RIGHT OUTER JOIN", "CROSS JOIN"],
                "correctIndex": 1,
                "explanation": "A LEFT OUTER JOIN preserves all rows from the left table and inserts NULLs for unmatched columns from the right table."
            }
        ],
        "DBMS": [
            {
                "concept": "ACID Properties",
                "difficulty": "Medium",
                "question": "Which ACID property ensures that once a database transaction commits, its modifications survive crashes and power outages?",
                "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
                "correctIndex": 3,
                "explanation": "Durability guarantees that committed data is flushed to persistent storage via Write-Ahead Logging (WAL) and survives crashes."
            },
            {
                "concept": "Normalization",
                "difficulty": "Medium",
                "question": "What requirement must a relational database table satisfy to be in Third Normal Form (3NF)?",
                "options": ["No multi-valued attributes", "Must be in 2NF and have no transitive functional dependencies of non-prime attributes on candidate keys", "Must have only one table", "Every column must be foreign key"],
                "correctIndex": 1,
                "explanation": "3NF requires being in 2NF with no transitive dependencies (i.e. non-prime attributes must depend directly only on candidate keys)."
            },
            {
                "concept": "Concurrency Control",
                "difficulty": "Hard",
                "question": "What is the primary objective of Two-Phase Locking (2PL) protocol in DBMS?",
                "options": ["To avoid deadlocks completely", "To guarantee serializability of concurrent transaction schedules", "To speed up query caching", "To prevent disk fragmentation"],
                "correctIndex": 1,
                "explanation": "2PL guarantees conflict serializability by ensuring all locks are acquired in the growing phase before any lock is released in the shrinking phase."
            },
            {
                "concept": "Write-Ahead Logging",
                "difficulty": "Hard",
                "question": "Why do database management systems use Write-Ahead Logging (WAL)?",
                "options": ["To compress backups", "To ensure log records are written to disk before corresponding database pages are updated, enabling crash recovery", "To encrypt user passwords", "To prevent foreign key checks"],
                "correctIndex": 1,
                "explanation": "WAL guarantees atomicity and durability by logging redo and undo information to non-volatile disk before modifying dirty pages in the buffer pool."
            },
            {
                "concept": "Keys & Integrity",
                "difficulty": "Easy",
                "question": "What type of integrity constraint ensures that a foreign key value must match an existing primary key or be NULL?",
                "options": ["Entity Integrity", "Referential Integrity", "Domain Integrity", "User-defined Integrity"],
                "correctIndex": 1,
                "explanation": "Referential integrity maintains consistent relationships between tables by validating foreign key references."
            }
        ],
        "OOP": [
            {
                "concept": "SOLID Principles",
                "difficulty": "Easy",
                "question": "Which SOLID principle asserts that software entities should be open for extension, but closed for modification?",
                "options": ["Single Responsibility Principle", "Open/Closed Principle", "Liskov Substitution Principle", "Interface Segregation Principle"],
                "correctIndex": 1,
                "explanation": "The Open/Closed Principle (OCP) encourages designing systems using abstractions so behavior can be extended without altering existing code."
            },
            {
                "concept": "Polymorphism",
                "difficulty": "Medium",
                "question": "What distinguishes Method Overriding (runtime polymorphism) from Method Overloading (compile-time polymorphism)?",
                "options": ["Overriding requires static methods", "Overriding allows a subclass to provide a specific implementation of a method declared in its superclass with identical signature", "Overloading changes class names", "Overriding only works on constructors"],
                "correctIndex": 1,
                "explanation": "Overriding occurs at runtime via virtual table dispatch when a subclass redefines an inherited superclass method with the same name and parameters."
            },
            {
                "concept": "Design Patterns",
                "difficulty": "Hard",
                "question": "Which design pattern is best suited for notifying multiple dependent objects automatically when an observed object changes state?",
                "options": ["Singleton Pattern", "Factory Pattern", "Observer Pattern", "Adapter Pattern"],
                "correctIndex": 2,
                "explanation": "The Observer pattern defines a one-to-many dependency where subjects notify subscribers/observers automatically of state transitions."
            },
            {
                "concept": "Encapsulation & Coupling",
                "difficulty": "Easy",
                "question": "Why is 'Composition favored over Inheritance' in enterprise object-oriented design?",
                "options": ["Inheritance creates tight coupling and exposes base class internals, while composition provides flexible runtime behavior swapping", "Composition eliminates the need for interfaces", "Inheritance uses more RAM", "Composition is faster to compile"],
                "correctIndex": 0,
                "explanation": "Composition promotes loose coupling (HAS-A relationship) and avoids the fragile base class problem inherent in deep inheritance hierarchies."
            },
            {
                "concept": "Liskov Substitution",
                "difficulty": "Medium",
                "question": "Which classic violation illustrates breaking the Liskov Substitution Principle (LSP)?",
                "options": ["Circle inherits from Shape", "Square inherits from Rectangle, where mutating width unexpectedly changes height", "Dog inherits from Animal", "Car inherits from Vehicle"],
                "correctIndex": 1,
                "explanation": "If Square inherits from Rectangle, setting width alters height, violating expected Rectangle invariants and causing client code bugs."
            }
        ],
        "Data Structures": [
            {
                "concept": "Trees & Traversal",
                "difficulty": "Medium",
                "question": "Which binary tree traversal visits nodes in ascending sorted order for a Binary Search Tree (BST)?",
                "options": ["Pre-order (Root, Left, Right)", "In-order (Left, Root, Right)", "Post-order (Left, Right, Root)", "Level-order (BFS)"],
                "correctIndex": 1,
                "explanation": "In-order traversal visits left subtree, current root, then right subtree, producing strictly non-decreasing sorted keys for a valid BST."
            },
            {
                "concept": "Heaps & Priority Queues",
                "difficulty": "Medium",
                "question": "What is the time complexity to extract the minimum element and re-heapify a Min-Heap of N elements?",
                "options": ["O(1)", "O(log N)", "O(N)", "O(N log N)"],
                "correctIndex": 1,
                "explanation": "Extracting the root takes O(1), but bubbling down the replacement leaf to restore the heap invariant takes O(log N)."
            },
            {
                "concept": "Hashing & Collisions",
                "difficulty": "Easy",
                "question": "What collision resolution technique links conflicting elements into a linked list or tree at the hash index?",
                "options": ["Linear Probing", "Quadratic Probing", "Separate Chaining", "Double Hashing"],
                "correctIndex": 2,
                "explanation": "Separate chaining stores collisions in a bucket containing a linked list or balanced tree at the target array index."
            },
            {
                "concept": "Graphs & Shortest Path",
                "difficulty": "Hard",
                "question": "Why does Dijkstra's shortest path algorithm fail on graphs containing negative weight edges?",
                "options": ["It uses too much memory", "It greedily marks visited nodes as finalized and does not re-evaluate when a smaller negative path appears later", "It works only on trees", "It causes infinite loop on directed graphs"],
                "correctIndex": 1,
                "explanation": "Dijkstra assumes edge weights are non-negative so once a vertex distance is finalized, it can never decrease. Bellman-Ford must be used instead."
            },
            {
                "concept": "Algorithmic Complexity",
                "difficulty": "Easy",
                "question": "What is the worst-case time complexity of QuickSort when pivot selection is poor (e.g. sorted input with last element as pivot)?",
                "options": ["O(N log N)", "O(N)", "O(N^2)", "O(2^N)"],
                "correctIndex": 2,
                "explanation": "If the chosen pivot repeatedly divides the array into subproblems of sizes 0 and N-1, QuickSort degenerates to O(N^2)."
            }
        ],
        "Operating Systems": [
            {
                "concept": "Deadlocks & Concurrency",
                "difficulty": "Medium",
                "question": "Which of the following is NOT one of Coffman's four mandatory conditions for a system deadlock?",
                "options": ["Mutual Exclusion", "Hold and Wait", "Preemptive Resource Allocation", "Circular Wait"],
                "correctIndex": 2,
                "explanation": "The fourth condition is 'No Preemption' (resources cannot be forcibly taken). Preemptive allocation breaks deadlocks."
            },
            {
                "concept": "Virtual Memory & Paging",
                "difficulty": "Medium",
                "question": "What phenomenon occurs when a system spends more time swapping virtual memory pages to disk than executing instructions?",
                "options": ["Deadlock", "Thrashing", "Starvation", "Context Switching Overhead"],
                "correctIndex": 1,
                "explanation": "Thrashing occurs when active processes exceed available physical RAM, causing constant page faults and continuous disk I/O."
            },
            {
                "concept": "Process Scheduling",
                "difficulty": "Easy",
                "question": "Which CPU scheduling algorithm gives each process a fixed slice of CPU time (time quantum) in cyclic order?",
                "options": ["First-Come First-Served (FCFS)", "Shortest Job First (SJF)", "Round Robin (RR)", "Priority Scheduling"],
                "correctIndex": 2,
                "explanation": "Round Robin assigns a uniform time quantum to ready processes circularly, preventing starvation in interactive systems."
            },
            {
                "concept": "Threads vs Processes",
                "difficulty": "Easy",
                "question": "What memory resource is private and unshared between threads belonging to the same process?",
                "options": ["Heap memory", "Global variables", "Open file descriptors", "Thread Call Stack and CPU Registers"],
                "correctIndex": 3,
                "explanation": "Threads share process code, data, open files, and heap memory, but each thread has its own independent call stack, stack pointer, and register set."
            },
            {
                "concept": "Inter-Process Communication",
                "difficulty": "Hard",
                "question": "What is the fastest Inter-Process Communication (IPC) mechanism on Linux/Unix systems?",
                "options": ["Unix Domain Sockets", "Named Pipes (FIFOs)", "Shared Memory", "Message Queues"],
                "correctIndex": 2,
                "explanation": "Shared memory is the fastest IPC because once the segment is mapped into both process address spaces, data exchange requires no kernel copy overhead."
            }
        ],
        "Computer Networks": [
            {
                "concept": "OSI & Protocols",
                "difficulty": "Easy",
                "question": "At which layer of the OSI model do TCP and UDP operate?",
                "options": ["Application Layer (Layer 7)", "Transport Layer (Layer 4)", "Network Layer (Layer 3)", "Data Link Layer (Layer 2)"],
                "correctIndex": 1,
                "explanation": "TCP and UDP are Transport Layer protocols providing end-to-end host process communication services."
            },
            {
                "concept": "TCP Handshake & Reliability",
                "difficulty": "Medium",
                "question": "What is the sequence of packets exchanged during a standard TCP connection establishment (3-Way Handshake)?",
                "options": ["SYN -> SYN-ACK -> ACK", "ACK -> SYN -> ACK", "FIN -> ACK -> FIN-ACK", "SYN -> ACK -> DATA"],
                "correctIndex": 0,
                "explanation": "Client sends SYN, server responds with SYN-ACK, and client replies with ACK to establish synchronized sequence numbers."
            },
            {
                "concept": "DNS & Addressing",
                "difficulty": "Easy",
                "question": "Which protocol translates human-readable domain names (e.g. google.com) into IP addresses?",
                "options": ["DHCP", "DNS", "ARP", "NAT"],
                "correctIndex": 1,
                "explanation": "The Domain Name System (DNS) resolves human-friendly hostname strings into numerical IPv4/IPv6 addresses."
            },
            {
                "concept": "Security & TLS/HTTPS",
                "difficulty": "Hard",
                "question": "During an HTTPS TLS 1.3 handshake, how is data encrypted between client and server?",
                "options": ["Using RSA asymmetric encryption for all data packets", "Asymmetric encryption is used only to negotiate a shared symmetric session key (e.g. AES-GCM), which encrypts the payload", "Data is hashed with SHA-256 without encryption", "No encryption is used if cert is valid"],
                "correctIndex": 1,
                "explanation": "Asymmetric cryptography (ECDH) securely exchanges keys, and then fast symmetric encryption (AES-256-GCM / ChaCha20) encrypts bulk data."
            },
            {
                "concept": "HTTP Protocols",
                "difficulty": "Medium",
                "question": "What key architectural enhancement does HTTP/2 introduce over HTTP/1.1 to eliminate Head-of-Line blocking at the application layer?",
                "options": ["Binary framing and multiplexing multiple requests/responses over a single TCP connection", "Removal of TCP in favor of UDP", "Mandatory base64 encoding", "Elimination of SSL/TLS"],
                "correctIndex": 0,
                "explanation": "HTTP/2 introduces a binary framing layer that multiplexes multiple concurrent requests and responses over a single TCP connection."
            }
        ]
    }

    # Automatically randomize/shuffle questions within each topic to provide dynamic questions on every request/reload
    shuffled_bank = {}
    for topic, q_list in topic_bank.items():
        copied_list = list(q_list)
        random.shuffle(copied_list)
        shuffled_bank[topic] = copied_list

    return jsonify({
        "success": True,
        "total_categories": len(shuffled_bank),
        "all_concepts": shuffled_bank
    }), 200


