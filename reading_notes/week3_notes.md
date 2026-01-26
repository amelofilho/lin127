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

A **recursive function** is a function that calls itself. Recursion is a powerful tool, but it must be used carefully. Every recursive function needs a **base case** that stops the recursion; otherwise, the function will run forever.

    def countdown(n):
        if n <= 0:
            print('Blastoff!')
        else:
            print(n)
            countdown(n-1)

In this example, the base case occurs when n is less than or equal to zero. Without that condition, the function would never terminate.

### Recursive Functions & Stack Frames

Each time a function is called, Python creates a new **stack frame** containing that function’s local variables. Recursive calls create multiple frames, which are resolved in reverse order as the function returns. Understanding this execution model is essential for debugging recursive programs, even though it is not always visible in code.

### Infinite Recursion

If a recursive function lacks a base case or never reaches it, the recursion continues indefinitely until Python raises a runtime error.

    def recurse():
        recurse()

Calling this function results in a **maximum recursion depth exceeded error**. This example exists solely as a warning: *recursion without termination is a guaranteed failure*.

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


## Ch 6: Fruitful Functions
TODO:

### Return Values

A fruitful function is a function that returns a value. Unlike void functions, which perform an action and return None, fruitful functions compute a result and send it back to the caller using a return statement. The simplest example is a function that converts degrees Celsius to Fahrenheit.

    def area(radius):
        return math.pi * radius**2

When this function is called, it evaluates the expression and immediately returns the result to the caller. Execution of the function stops as soon as a return statement is reached.


### Using Return Values

The value returned by a function can be assigned to a variable, used in an expression, or passed as an argument to another function.

    >>> r = area(2)
    >>> print(r)
    12.566370614359172

If a return value is not captured or used, it is effectively discarded. Fruitful functions are most powerful when their results are reused rather than printed directly.

### Multiple Return Statements

A function can have more than one return statement, typically inside conditional branches. Only one return statement executes during any given function call.

    def absolute_value(x):
        if x < 0:
            return -x
        else:
            return x

This structure allows the function to return different results depending on the input while still guaranteeing that a value is returned in all cases.

### Dead Code

Any statements that appear after a return statement in the same block are never executed. This unreachable code is referred to as dead code and usually indicates a logical error.

    def absolute_value(x):
        if x < 0:
            return -x
        return x
        print('This is dead code')

The print statement will never run because the function always returns before reaching it.


### Incremental Development

To avoid complex bugs, the chapter introduces incremental development: building and testing a function in small steps. The process starts with a minimal version that returns a simple value and gradually adds complexity while testing at each stage.

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        return 0.0

This placeholder return value allows the function structure to be tested before implementing the full logic.

### Composition

Fruitful functions can be composed, meaning the return value of one function can be used as input to another. This encourages concise, readable code and mirrors mathematical notation.

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        return math.sqrt(dx**2 + dy**2)

By breaking problems into smaller functions, complex computations become easier to reason about and debug.

### Boolean Functions

Functions can return boolean values, which are especially useful for conditionals.

    def is_divisible(x, y):
        return x % y == 0

This function returns either True or False, allowing it to be used directly in if statements without additional comparison logic.

### More Recursion

Fruitful functions can also be recursive, returning a value from each call until a base case is reached.

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

Each recursive call contributes to the final returned value, which is assembled as the recursion unwinds.

### Leap of Faith

When reasoning about recursive functions, the chapter emphasizes the “leap of faith”: assuming that the recursive call works correctly and focusing only on how the current call combines its result. This mental model simplifies reasoning about recursion and prevents getting lost in infinite expansion.

### One More Example

The chapter concludes with another recursive example that demonstrates returning values through multiple levels of recursion.

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

Although inefficient, this example clearly illustrates how recursive calls can build up a final result from smaller subproblems.

### Key Takeaways
- Fruitful functions return values instead of just producing output.
- return immediately ends a function’s execution.
- Returned values can be composed, stored, or reused.
- Recursive fruitful functions must always move toward a base case.

## Ch 7: Iteration
TODO:

### Multiple Assignment

Python allows multiple variables to be assigned in a single statement. This feature is often used to update related variables simultaneously, which is especially useful in iterative processes.

    >>> a = 5
    >>> b = 3
    >>> a, b = b, a

Both assignments occur at the same time, meaning Python evaluates the right-hand side first before making any changes. This avoids temporary variables and keeps code concise.

### Updating Variables

One of the most common uses of assignment is updating a variable’s value based on its previous value. This pattern is essential for loops and counters.

    >>> x = x + 1

Here, Python evaluates the expression on the right-hand side using the old value of x and then assigns the result back to x. This does not represent a mathematical equality but a reassignment.

### The `while` Statement

Iteration allows a block of code to run repeatedly while a condition remains true. The while statement checks its condition before each iteration.

    def countdown(n):
        while n > 0:
            print(n)
            n = n - 1
        print('Blastoff!')

This loop continues until the condition n > 0 becomes false. Unlike recursion, iteration does not create new stack frames and is often easier to reason about for repetitive tasks.

### Infinite Loops

If the condition in a while loop never becomes false, the loop runs forever. Infinite loops are usually the result of forgetting to update a variable that controls the loop condition.

    def sequence(n):
        while n != 1:
            print(n)
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1

This function relies on the assumption that n will eventually reach 1. If it does not, the loop will never terminate.


### `break`

The `break` statement allows a loop to exit immediately, regardless of the loop condition. This is often used when a terminating condition occurs in the middle of a loop.

    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)
    print('Done!')

This structure creates a loop that runs indefinitely until an explicit break condition is met.


### Finishing Iterations with `continue`

The `continue` statement ends the current iteration and jumps back to the beginning of the loop to re-evaluate the condition.

    while True:
        line = input('> ')
        if line == 'done':
            break
        if line.startswith('#'):
            continue
        print(line)
    print('Done!')

This allows certain cases to be skipped cleanly without deeply nested conditionals.

### Definite Loops Using for

When the number of iterations is known in advance, Python provides the `for` loop, which iterates over the elements of a sequence.

    for i in range(5):
        print(i)

This loop runs exactly five times, with i taking on successive values from the sequence produced by range.

### Loop Patterns

Many loops follow common patterns such as accumulating a sum, counting items, or searching for a value. These patterns appear repeatedly in real programs and form the backbone of algorithmic thinking.

    total = 0
    for i in range(10):
        total = total + i

The loop updates total on each iteration, demonstrating how iteration builds results incrementally.

### Square Roots

The chapter introduces square root computation as a motivating example for iteration and algorithmic thinking. Instead of relying on built-in functions, Python can approximate square roots using Newton’s method, which repeatedly improves an estimate until it is “close enough” to the true value.

    def square_root(a):
        x = a / 2
        while True:
            y = (x + a/x) / 2
            if y == x:
                break
            x = y
        return x

This function starts with an initial guess and refines it iteratively. Each new approximation moves closer to the actual square root. The loop terminates when the estimate stops changing, which signals convergence.

### Algorithms

An **algorithm** is a mechanical process for solving a class of problems, not just a single instance. The square root example illustrates key properties of algorithms: they are finite, precise, and produce correct results when followed exactly. Iteration is presented as a fundamental algorithmic tool because it allows complex results to emerge from simple repeated steps.

    def square_root(a):
        x = a / 2
        while True:
            y = (x + a/x) / 2
            if y == x:
                break
            x = y
        return x

By implementing Newton’s method explicitly, the chapter reinforces that algorithms are not magical formulas but step-by-step procedures that computers execute blindly. Correctness depends entirely on the structure of those steps.

### Debugging

Iteration-related bugs often involve off-by-one errors, incorrect loop conditions, or failure to update loop variables. The chapter emphasizes tracing variable values step by step and using print statements to observe how a loop evolves over time.

### Key Takeaways
- Iteration repeats code while updating state variables.
- while loops depend on conditions; for loops iterate over sequences.
- break and continue give fine-grained loop control.
- Most loop bugs come from incorrect termination logic.
- Newton’s method is a concrete example of an iterative algorithm.
- Algorithms are defined by precision, termination, and correctness.

## Ch 8: Strings
TODO:

### A String Is a Sequence

A string is a sequence of characters, meaning each character has a position (index) within the string. Individual characters can be accessed using square brackets with an index, starting from zero. Attempting to access an index that does not exist results in an error.

    fruit = 'banana'
    letter = fruit[1]

Here, letter refers to 'a'. Using an index outside the valid range raises an IndexError, reinforcing that strings have fixed boundaries.


### `len`

The built-in function `len` returns the number of characters in a string. Since indexing starts at zero, the index of the last character is one less than the length.

    >>> fruit = 'banana'
    >>> len(fruit)
    6

Using `len` is safer than hard-coding indices, especially when working with strings whose lengths may vary.


### Traversal with a for Loop

Strings can be traversed character by character using a for loop. This is the preferred way to iterate over a string in Python.

    for letter in fruit:
        print(letter)

Each iteration assigns the next character in the string to the loop variable, making traversal concise and readable.


### String Slices

A **slice** extracts a substring from a string using a range of indices. The start index is inclusive, and the end index is exclusive.

    s = 'Monty Python'
    >>> s[0:5]
    'Monty'
    >>> s[6:12]
    'Python'

Omitting the start or end index causes Python to assume the beginning or end of the string, respectively.

    >>> s[:5]
    'Monty'
    >>> s[6:]
    'Python'

Slices never raise index errors, even if the specified range exceeds the string’s bounds.

### Strings Are Immutable

Strings cannot be modified after they are created. Attempting to assign to an indexed position in a string results in a TypeError.

    greeting = 'Hello, world!'
    greeting[0] = 'J'

To “modify” a string, a new string must be created using slicing and concatenation.

    new_greeting = 'J' + greeting[1:]

This immutability prevents accidental changes and ensures predictable behavior.

### Searching

The chapter introduces a basic search pattern using a loop and a conditional to locate a character within a string.

    def find(word, letter):
        index = 0
        while index < len(word):
            if word[index] == letter:
                return index
            index = index + 1
        return -1

This function returns the index of the first occurrence of a character or -1 if it is not found. This example reinforces iteration, conditionals, and return values working together.

### Looping and Counting

A common pattern involves traversing a string and counting occurrences of a specific character.

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

This pattern is foundational for text analysis tasks such as frequency counting and filtering.

### String Methods

Strings come with built-in methods that perform common operations. These methods return new values and do not modify the original string.

    >>> word = 'banana'
    >>> new_word = word.upper()
    >>> new_word
    'BANANA'

Methods such as find simplify tasks that would otherwise require manual loops.

    >>> word.find('a')
    1
    >>> word.find('na')
    2
    >>> word.find('na', 3)
    4

The optional second argument specifies a starting index for the search.

### The `in` Operator

The `in` operator checks whether one string appears inside another and returns a boolean result.

    >>> 'a' in 'banana'
    True
    >>> 'seed' in 'banana'
    False

This operator is often clearer and more concise than writing an explicit search loop.

### String Comparison

Strings are compared using relational operators. Python compares strings lexicographically, based on the Unicode values of their characters.

    if word < 'banana':
        print('Your word comes before banana.')
    elif word > 'banana':
        print('Your word comes after banana.')
    else:
        print('All right, bananas.')

Uppercase letters come before lowercase letters, which can lead to unexpected results unless strings are normalized.

### Debugging

Common string-related errors include off-by-one indexing mistakes, confusing slices with indices, and forgetting that strings are immutable. The chapter emphasizes printing intermediate values and checking assumptions about indices and lengths to diagnose these problems effectively.

### Key Takeaways
- Strings are sequences with zero-based indexing.
- Strings cannot be modified; new strings must be created.
- Traversal, slicing, and searching are core string operations.
- Built-in string methods simplify common text tasks.

## Ch 10: Lists
TODO:

### A List Is a Sequence

A **list** is a sequence of values, where each value is called an element. Unlike strings, lists can contain elements of different types, including other lists. Lists are written using square brackets, with elements separated by commas.

    >>> numbers = [10, 20, 30, 40]
    >>> words = ['crunchy frog', 'ram bladder', 'lark vomit']

Lists can also be nested, meaning an element of a list can itself be another list.

    >>> nested = ['spam', 2.0, 5, [10, 20]]

### Lists Are Mutable

One of the most important differences between lists and strings is **mutability**. Lists can be modified after they are created by assigning to individual elements.

    >>> cheeses = ['Cheddar', 'Edam', 'Gouda']
    >>> cheeses[0] = 'Cheddar'

This ability to mutate lists makes them suitable for tasks that involve gradual updates, accumulation, or in-place transformations.

### Traversing a List

Lists can be traversed using a for loop in the same way as strings. Each iteration assigns the next element of the list to the loop variable.

    for cheese in cheeses:
        print(cheese)

This pattern is common for reading or processing each element without modifying the list.


### List Operations

The `+` operator concatenates lists, and the * operator repeats them, producing new lists rather than modifying the originals.

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> a + b
    [1, 2, 3, 4, 5, 6]
    >>> a * 3
    [1, 2, 3, 1, 2, 3, 1, 2, 3]

These operations behave similarly to string concatenation and repetition but operate at the element level.

### List Slices

Slicing a list creates a new list containing a subset of the elements. As with strings, the start index is inclusive and the end index is exclusive.

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> t[1:3]
    ['b', 'c']
    >>> t[:4]
    ['a', 'b', 'c', 'd']
    >>> t[3:]
    ['d', 'e', 'f']

Assigning to a slice allows multiple elements to be replaced at once.

    >>> t[1:3] = ['x', 'y']

### List Methods

Lists come with methods that modify them in place. The append method adds an element to the end of a list.

    >>> t = ['a', 'b', 'c']
    >>> t.append('d')

The `extend()` method adds elements from another list.

    >>> t.extend(['e', 'f'])

The `sort()` method rearranges the elements in ascending order.

    >>> t.sort()

These methods return `None`, emphasizing that they operate by mutating the list rather than producing a new one.


### Map, Filter, and Reduce

Common list-processing patterns include mapping a function over a list, filtering elements based on a condition, and reducing a list to a single value. These patterns are often implemented using loops.

    def add_all(t):
        total = 0
        for x in t:
            total += x
        return total

This example reduces a list of numbers to their sum, illustrating accumulation.

### Deleting Elements

Elements can be removed from a list using several techniques. The pop method removes and returns an element at a given index.

    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)

The del statement removes an element or slice without returning it.

    >>> del t[1]

The remove method deletes the first occurrence of a specific value.

    >>> t.remove('a')


### Lists and Strings

Strings can be split into lists using the `split()` method, which breaks a string at whitespace by default.

    >>> s = 'spam spam spam'
    >>> t = s.split()

Lists can be joined back into strings using the `join()` method.

    >>> delimiter = ' '
    >>> delimiter.join(t)

This conversion between strings and lists is central to many text-processing tasks.

### Objects and Values

Two variables can refer to the same list object, meaning changes made through one variable affect the other.

    >>> a = [1, 2, 3]
    >>> b = a
    >>> b[0] = 17

After this modification, both a and b refer to the modified list. This aliasing behavior is a common source of bugs.

### Aliasing

Aliasing occurs when multiple variables reference the same list. Mutations through one alias are visible through all others.

    >>> a = [1, 2, 3]
    >>> b = a
    >>> a is b
    True

Understanding aliasing is critical for reasoning about side effects.

### List Arguments

When a list is passed to a function, the function receives a reference to the list, not a copy. As a result, mutations inside the function affect the caller’s list.

    def delete_head(t):
        del t[0]

Calling this function permanently modifies the list passed as an argument.

### Debugging

List-related bugs often stem from unintended aliasing, incorrect assumptions about mutability, or misuse of list methods that return None. The chapter emphasizes tracing object identities and being explicit about when copies are needed.

Key Takeaways
- Lists are mutable sequences that can hold mixed types.
- List methods modify lists in place and usually return None.
- Aliasing means multiple names can refer to the same list.
- Passing lists to functions allows side effects through mutation.