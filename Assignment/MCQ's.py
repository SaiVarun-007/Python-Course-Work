questions = [
    {
        "question": "What are Python's key features?",
        "options": [
            "A) Easy-to-read syntax, large standard library, object-oriented",
            "B) Only supports web development",
            "C) Low-level memory management required",
            "D) Only works on Windows"
        ],
        "correct": "A"
    },
    {
        "question": "What is the difference between is and == in Python?",
        "options": [
            "A) 'is' compares identities, '==' compares values",
            "B) 'is' compares values, '==' compares identities",
            "C) Both compare values",
            "D) Both compare identities"
        ],
        "correct": "A"
    },
    {
        "question": "Explain the difference between a list, tuple, and set.",
        "options": [
            "A) List: ordered & mutable, Tuple: ordered & immutable, Set: unordered & mutable",
            "B) List: unordered, Set: ordered, Tuple: mutable",
            "C) Tuple: unordered & mutable, Set: ordered & immutable",
            "D) All are the same"
        ],
        "correct": "A"
    },
    {
        "question": "What are Python's data types? Can you give examples?",
        "options": [
            "A) int, float, str, list, dict, set, tuple",
            "B) HTML, XML, JSON, CSV",
            "C) Car, Bike, Airplane, Boat",
            "D) None of the above"
        ],
        "correct": "A"
    },
    {
        "question": "Explain the concept of classes and objects in Python.",
        "options": [
            "A) A class is a blueprint; objects are instances of the class",
            "B) Classes are functions; objects are variables",
            "C) Classes store only numbers; objects store only strings",
            "D) Both are the same thing"
        ],
        "correct": "A"
    },
    {
        "question": "What is inheritance in Python? How do you implement it?",
        "options": [
            "A) It allows a class to inherit attributes/methods from another class using class Child(Parent)",
            "B) It means storing many values in a list",
            "C) Running a function recursively",
            "D) Building logic gates"
        ],
        "correct": "A"
    },
    {
        "question": "What is the difference between @staticmethod and @classmethod?",
        "options": [
            "A) @staticmethod doesn't access class state, @classmethod does",
            "B) @staticmethod accesses self, @classmethod accesses nothing",
            "C) @classmethod makes functions run faster",
            "D) They are the same"
        ],
        "correct": "A"
    },
    {
        "question": "What is method overriding and method overloading in Python?",
        "options": [
            "A) Overriding: redefining inherited methods; Overloading: multiple methods with same name but different args",
            "B) Overriding: using decorators; Overloading: using lists",
            "C) Both mean deleting methods",
            "D) None of the above"
        ],
        "correct": "A"
    },
    {
        "question": "What is __init__ in Python classes?",
        "options": [
            "A) It's the constructor method used to initialize objects",
            "B) It's a function to end a class",
            "C) It deletes class variables",
            "D) None of the above"
        ],
        "correct": "A"
    },
    {
        "question": "What is the difference between global, local, and nonlocal variables?",
        "options": [
            "A) Global: accessible everywhere, Local: inside function, Nonlocal: in nested function",
            "B) Global: in lists, Local: in classes, Nonlocal: in sets",
            "C) Global: only in loops, Local: in files",
            "D) No difference"
        ],
        "correct": "A"
    },
    {
        "question": "What are *args and **kwargs in function definitions?",
        "options": [
            "A) *args: variable positional arguments, **kwargs: variable keyword arguments",
            "B) Only used in classes",
            "C) Used for importing modules",
            "D) For mathematical calculations"
        ],
        "correct": "A"
    },
    {
        "question": "What is a lambda function? How is it different from a regular function?",
        "options": [
            "A) Lambda is an anonymous, single-expression function; regular functions use def and are named",
            "B) Lambda takes no arguments always",
            "C) Lambda is only for loops",
            "D) No difference"
        ],
        "correct": "A"
    },
    {
        "question": "What is recursion? Give an example using Python.",
        "options": [
            "A) A function calling itself",
            "B) Looping over a list",
            "C) Printing variables",
            "D) None of the above"
        ],
        "correct": "A"
    },
    {
        "question": "What is the purpose of decorators in Python?",
        "options": [
            "A) To modify or enhance functions without changing their code",
            "B) To decorate text output",
            "C) For styling web pages",
            "D) No purpose"
        ],
        "correct": "A"
    },
    {
        "question": "What are list comprehensions and dictionary comprehensions? Give an example.",
        "options": [
            "A) Ways to construct lists/dictionaries using concise syntax",
            "B) Syntax errors",
            "C) Used only in classes",
            "D) For making databases"
        ],
        "correct": "A"
    },
    {
        "question": "What are Python generators? How are they different from iterators?",
        "options": [
            "A) Generators yield items one by one; every generator is an iterator but not vice versa",
            "B) Generators only run once",
            "C) Generators store all items in memory",
            "D) Generators don't exist in Python"
        ],
        "correct": "A"
    },
    {
        "question": "How do you handle exceptions in Python? What's the difference between try, except, finally, and else blocks?",
        "options": [
            "A) try: code to test, except: handle errors, else: no error, finally: always runs",
            "B) try: for loops, except: for variables",
            "C) try: for importing, except: for classes",
            "D) No difference"
        ],
        "correct": "A"
    },
    {
        "question": "What are modules and packages in Python? How do you import them?",
        "options": [
            "A) Modules: Python files, Packages: collection of modules; import using import/module from package",
            "B) Modules and packages are the same",
            "C) Packages work only for images",
            "D) Can't import in Python"
        ],
        "correct": "A"
    },
    {
        "question": "What is the difference between shallow copy and deep copy in Python?",
        "options": [
            "A) Shallow copy copies references, deep copy copies objects recursively",
            "B) Both are identical",
            "C) Shallow copy only for strings",
            "D) Deep copy only for numbers"
        ],
        "correct": "A"
    }
]

score = 0
print("Welcome to the Python Quiz!\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}. {q['question']}")
    for option in q["options"]:
        print(option)
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    if user_ans == q["correct"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The right answer is {q['correct']}.\n")

print(f"Quiz complete! You got {score} out of {len(questions)}.")
