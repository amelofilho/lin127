# Think Python: Ch 1, 2, 3, 5.1-5.7, 6.1-6.4, 7, 8, 10

### Functions:
- print()
- type()
- 

## Ch 1: Programs
TODO:

### What Is a Program

A program is a sequence of precise instructions that tells a computer how to perform a computation. That computation might be numerical, like arithmetic, symbolic, like manipulating text, or visual, like processing images or video. While programs can look wildly different on the surface, they are all built from the same basic ideas: receiving input, producing output, performing mathematical operations, making decisions, and repeating actions. Programming, at its core, is the skill of breaking down a complex task into small enough steps that a computer can execute them exactly as written.


### Running Python

Python programs are executed by the Python interpreter, which reads code and runs it line by line. When the interpreter starts, it displays a prompt that looks like `>>>`, signaling that it is ready for input. Any valid Python expression typed at this prompt is evaluated immediately, and the result is shown on the screen.

    >>> 1 + 1
    Output: 2

This immediate feedback makes Python especially useful for learning, experimenting, and debugging. The book is written for Python 3, and while Python 2 is mentioned for historical context, the syntax and behavior shown throughout the chapter assume Python 3.



### The First Program

Traditionally, the first program written in any language prints the phrase “Hello, World!”. In Python 3, this is done using the print function.

    >>> print('Hello, World!')

The quotation marks `' '` define a string, and the parentheses indicate that print is a function call. The output appears on the screen exactly as written inside the quotes. For comparison, the chapter briefly shows the older Python 2 syntax, where print was a statement rather than a function.

    >>> print 'Hello, World!'

This example introduces the idea that syntax matters and that even small differences can change how a program behaves—or whether it runs at all.


### Arithmetic Operators

Python supports standard arithmetic operators such as addition, subtraction, and multiplication, which behave as expected.

    >>> 40 + 2
    42
    >>> 43 - 1
    42
    >>> 6 * 7
    42

Division behaves slightly differently because **it always produces a floating-point result**, even when the mathematical answer is a whole number.

    >>> 84 / 2
    42.0

Exponentiation is performed using the `**` operator.

    >>> 6**2 + 6
    42

The chapter also warns that the **caret symbol** (`^`) is not used for exponentiation in Python. Instead, it represents a **bitwise XOR operation**, which can produce unexpected results if misused.

    >>> 6 ^ 2
    4


### Values and Types

A **value** is one of the basic units of data that a program manipulates, such as a number or a piece of text. Every value in Python has a type, which determines how it behaves and what operations can be performed on it. **Integers, floating-point numbers**, and **strings** are the first types introduced.

    >>> type(2)
    <class 'int'>
    >>> type(42.0)
    <class 'float'>
    >>> type('Hello, World!')
    <class 'str'>

Even values that look like **numbers can be strings** if they are enclosed in quotation marks.

    >>> type('2')
    <class 'str'>
    >>> type('42.0')
    <class 'str'>

This distinction becomes critical later, since Python treats numbers and strings very differently, even when they appear similar to a human reader.


### Formal and Natural Languages

Python is a **formal language**, meaning it has strict rules for syntax and structure. Unlike **natural languages**, which tolerate ambiguity and variation, formal languages require exact spelling, punctuation, and ordering. A missing quote, extra symbol, or misplaced parenthesis can cause a program to fail entirely. This rigidity is not a weakness but a feature, because it **allows programs to be interpreted unambiguously** by a computer.

### Debugging

Errors in programs, known as **bugs**, are inevitable and expected. **Debugging** is the process of finding and correcting these errors, and the chapter emphasizes that learning to debug is just as important as learning to write code. Experimenting, intentionally making mistakes, and carefully reading error messages are presented as essential habits. Debugging is framed not as a sign of failure, but as a normal and necessary part of programming.


#### Ch 1 Key Takeaways
- Programming is about problem-solving, not memorizing syntax.
- Python executes instructions exactly as written, so precision matters.
- Values always have types, and types determine behavior.
- Errors are expected; debugging is a core skill, not an afterthought.

## Ch 2: Vars, Expressions, Statements
TODO:

### Values and Variables

A **variable** is a name that refers to a value stored in memory. **Assignment statements** are used to create variables and give them values using the equals sign, which should be read as “gets” rather than “equals.” Once a variable is assigned, it can be used in expressions and reused throughout the program.

    >>> message = 'And now for something completely different'
    >>> n = 17
    >>> pi = 3.141592653589793

In this example, the variable message refers to a string, `n` refers to an integer, and `pi` refers to a floating-point number. Variables allow programs to store data, reuse results, and make code easier to read and modify.

**Variable names** can contain letters, numbers, and underscores, but they must start with a letter or an underscore. Python is **case-sensitive**, so spam, Spam, and SPAM are all different variables. Certain words are reserved by Python for special purposes and cannot be used as variable names.

    >>> 76trombones = 'big parade'
    SyntaxError: invalid syntax
    >>> more@ = 1000000
    SyntaxError: invalid syntax
    >>> class = 'Advanced Theoretical Zymurgy'
    SyntaxError: invalid syntax

These examples demonstrate that illegal characters, incorrect starting symbols, and reserved keywords all result in **syntax errors**. Choosing descriptive variable names is encouraged, as it improves readability and reduces confusion.

### Expressions and Statements

An **expression** is a combination of values, variables, and operators that Python evaluates to produce a result. A **statement** is a unit of code that performs an action, such as assigning a value to a variable. Expressions have values, while statements do things.

    >>> 1 + 1
    2
    >>> x = 3

The first line is an expression whose value is displayed by the interpreter. The second line is a statement that assigns a value to a variable but does not display anything. In script files, expressions do not automatically print their results, which makes statements like print necessary.

### Script Mode

When Python code is written in a file and executed as a script, it behaves differently from the interactive interpreter. Expressions are evaluated but not displayed unless explicitly printed. This distinction reinforces the difference between calculating a value and producing output.

x = 3
x + 1

Running this code in a script produces no output, even though the expression x + 1 is valid. To see the result, a print statement is required.

### Order of Operations

When an expression contains multiple operators, Python follows the **standard mathematical order of operations**: parentheses first, then exponentiation, followed by multiplication and division, and finally addition and subtraction. This ensures consistent and predictable evaluation of expressions.

    >>> 2 + 3 * 4
    14
    >>> (2 + 3) * 4
    20

Parentheses can be used to override the default order and make expressions clearer to human readers.

### String Operations

Strings can be combined using the `+` operator, which performs concatenation, and repeated using the `*` operator. These operations behave differently from numeric addition and multiplication, even though the symbols are the same.

    >>> first = 'throat'
    >>> second = 'warbler'
    >>> first + second
    'throatwarbler'
    >>> 'Spam' * 3
    'SpamSpamSpam'

Attempting to mix strings and numbers without conversion results in a type error, reinforcing the importance of understanding types.

### Comments

Comments are notes written in code that are ignored by the Python interpreter. They are used to explain what the code does, clarify intent, or temporarily disable parts of a program.

    # compute the percentage of the hour that has elapsed  
    percentage = (minute * 100) / 60

Comments improve readability for humans without affecting how the program runs.

### Debugging

A common source of errors in this chapter comes from confusing assignment with equality, using invalid variable names, or mixing incompatible types. Syntax errors prevent programs from running at all, while runtime errors occur when Python encounters an illegal operation during execution. The chapter emphasizes slowing down, reading error messages carefully, and checking assumptions about types and values.

### Ch 2 Key Takeaways
- Variables store values and make programs flexible and readable.
- Expressions compute values; statements perform actions.
- Python is strict about syntax, names, and types.
- Scripts require explicit output using print.

## Ch 3: Functions
TODO:

### Function Calls
A ***function*** is a named sequence of statements that performs a computation. Python provides built-in functions that can be called by writing the function name followed by parentheses containing arguments. Calling a function causes Python to execute the function’s body and, in some cases, return a result.

    >>> type(42)
    <class 'int'>
    >>> type('spam')
    <class 'str'>
    >>> type(3.14)
    <class 'float'>

In these examples, type is a function that takes a value as an argument and returns its type. The parentheses indicate a function call, and the argument inside determines what the function operates on.

### Type Conversion Functions
Python includes functions that convert values from one type to another. These conversions are explicit and must be requested by the programmer.

    >>> int('32')
    32
    >>> int('Hello')
    ValueError: invalid literal for int() with base 10: 'Hello'
    >>> int(3.99999)
    3
    >>> int(-2.3)
    -2
    >>> float(32)
    32.0
    >>> str(3.14159)
    '3.14159'

These examples show that conversion only works when the value makes sense in the target type. Converting a string that does not represent a number results in a runtime error.

### Math Functions

Python provides a **math module** that contains common mathematical functions. Before using it, the module must be imported.

    >>> import math
    >>> math
    <module 'math' (built-in)>

Once imported, functions inside the module are accessed using dot notation.

    >>> math.log10(100)
    2.0
    >>> math.sin(0)
    0.0

This introduces the idea that functions can be grouped into modules, which helps organize large collections of related functionality.

### Composition

Function calls can be combined, or composed, by using the result of one function as the argument to another. Python evaluates the innermost function first.

    >>> math.sin(math.pi / 2)
    1.0

Composition allows complex computations to be written concisely and mirrors the way mathematical expressions are structured.

### Adding New Functions

In addition to built-in functions, programmers can define their own using the `def` keyword. A **function definition** specifies the function’s name and the statements that run when the function is called.

    >>> def print_lyrics():
    ...     print("I'm a lumberjack, and I'm okay.")
    ...     print("I sleep all night and I work all day.")

Once defined, the function can be called by name.

    >>> print_lyrics()
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.

Defining functions allows code to be reused and organized into meaningful chunks.
 
### Definitions and Uses

A function definition creates the function but does not execute it. The body of the function runs only when the function is called. This distinction is important because defining a function produces no output by itself.

    >>> def repeat_lyrics():
    ...     print_lyrics()
    ...     print_lyrics()

Calling the function causes the statements inside it to execute.

    >>> repeat_lyrics()
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.

This example shows how functions can call other functions.

### Flow of Execution

When a program runs, Python executes statements one at a time from top to bottom. Function definitions are executed first, but their bodies are skipped until the function is called. When a function is called, execution jumps to the function’s body and returns to the point of the call when the function finishes. Understanding this flow is critical for reasoning about how programs behave.

### Parameters and Arguments

Some functions take arguments, which are values passed into the function when it is called. Parameters are variables inside the function that refer to those arguments.

    >>> def print_twice(bruce):
    ...     print(bruce)
    ...     print(bruce)

Calling the function with an argument assigns that value to the parameter.

    >>> print_twice('Spam')
    Spam
    Spam
    >>> print_twice(17)
    17
    17

Parameters make functions more flexible by allowing them to operate on different values.


### Variables and Parameters Are Local

Variables created inside a function, including parameters, are local to that function. They exist only while the function is running and cannot be accessed from outside.

    >>> def cat_twice(part1, part2):
    ...     cat = part1 + part2
    ...     print_twice(cat)

Here, cat exists only inside cat_twice. This isolation prevents accidental interference between different parts of a program.

### Stack Diagrams

The chapter introduces stack diagrams as a conceptual tool for visualizing function calls and local variables. Each function call creates a new frame containing its local variables and parameters. While no code is involved, this idea helps explain how Python keeps track of multiple active function calls.

### Void Functions and Return Values

Some functions return values, while others perform actions without returning anything. Functions like print_lyrics are void functions; they return None implicitly. This distinction matters when composing functions or assigning results to variables.

### Debugging

Common mistakes in this chapter include forgetting parentheses when calling a function, confusing a function name with a function call, and misunderstanding the order of execution. The chapter emphasizes testing functions incrementally and using print statements to trace execution when things go wrong.


### Ch 3: Key Takeaways
- Functions package code into reusable, named operations.
- Defining a function does not run it; calling it does.
- Parameters make functions flexible and reusable.
- Local variables exist only inside their functions.



## Ch 5: Conditionals & Recursion
TODO:

### Conditional Statements

Conditional execution allows a program to choose different paths based on whether a condition is true or false. The simplest **conditional** is the `if` statement, which executes its body only when the condition evaluates to `True`.

    if x > 0:
        print('x is positive')

If the condition is `false`, the indented block is skipped entirely. Indentation is not stylistic in Python—it defines the structure of the program and determines which statements belong to the conditional.

### Boolean Expressions

A **boolean expression** is an expression that evaluates to either `True` or `False`. **Comparison operators** such as `==`, `!=`, `<`, `>`,`<=`, and `>=` are used to form these expressions.

    >>> x == y
    False
    >>> x != y
    True
    >>> x > y
    False
    >>> x < y
    True

Boolean expressions are the foundation of conditionals, since they determine which branch of code executes.


### Logical Operators

Python provides logical operators that allow boolean expressions to be combined. The `and` operator requires both expressions to be true, `or` requires at least one to be true, and `not` negates a boolean value.

    >>> x > 0 and x < 10
    True
    >>> n % 2 == 0 or n % 3 == 0
    True
    >>> not x > y
    True

These operators allow complex conditions to be expressed clearly and concisely.

### Conditional Branching

More complex decisions require multiple possible paths. The `if–else` statement allows one block to run when the condition is true and another when it is false.

    if x % 2 == 0:
        print('x is even')
    else:
        print('x is odd')

Only one branch executes, never both. This structure makes mutually exclusive logic explicit.


### Chained Conditionals

When there are more than two possible cases, chained conditionals can be used with `elif`, which stands for “else if.”

    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')

The conditions are checked in order, and execution stops as soon as one condition is true. The final else acts as a catch-all.

### Nested Conditionals

Conditionals can also be placed inside other conditionals. While this is sometimes necessary, deeply nested conditionals can quickly become hard to read and reason about.

    if x == y:
        print('x and y are equal')
    else:
        if x < y:
            print('x is less than y')
        else:
            print('x is greater than y')

The chapter emphasizes that nested conditionals can often be rewritten as chained conditionals for clarity.

### Recursion

A **recursive function** is a function that calls itself. Recursion is a powerful tool, but it must be used carefully. Every recursive function needs a base case that stops the recursion; otherwise, the function will run forever.

    def countdown(n):
        if n <= 0:
            print('Blastoff!')
        else:
            print(n)
            countdown(n-1)

In this example, the base case occurs when n is less than or equal to zero. Without that condition, the function would never terminate.

### Recursive Functions and Stack Frames

Each time a function is called, Python creates a new **stack frame** containing that function’s local variables. Recursive calls create multiple frames, which are resolved in reverse order as the function returns. Understanding this execution model is essential for debugging recursive programs, even though it is not always visible in code.

### Infinite Recursion

If a recursive function lacks a base case or never reaches it, the recursion continues indefinitely until Python raises a runtime error.

    def recurse():
        recurse()

Calling this function results in a maximum recursion depth exceeded error. This example exists solely as a warning: recursion without termination is a guaranteed failure.

### Keyboard Input

The chapter introduces the input function, which pauses program execution and waits for user input. The result of input is always a string.

    text = input()

To use numeric input, the returned string must be converted explicitly.

    n = int(input())

This reinforces earlier lessons about types and the need for explicit conversions.

### Debugging

Common errors in this chapter include using = instead of == in conditionals, forgetting base cases in recursive functions, and misunderstanding indentation. The chapter stresses simplifying conditions, testing branches independently, and adding temporary print statements to trace execution paths.


### Key Takeaways
- Conditionals let programs make decisions based on boolean logic.
- Logical operators combine conditions into more expressive tests.
- Recursion requires a clear base case to terminate safely.
- Indentation defines structure and control flow in Python.