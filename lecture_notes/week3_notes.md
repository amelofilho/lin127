# Notes 1/21: Intro to Python

### Commands:

### A2 Feedback:

- **Regular expressions** are tricky 
    - these are the pattern inputs to sed and grep 
    - we will go over in much more detail later in the quarter!
- **Whitespace** is invisible and therefore tricky e.g. top word = 46401 instances of `‘ ’` Can run another sed to remove this, or a one-command fix: sed `'s/ +/\n/g'`
    - Similar, `sed '/^$/d'` works but misses lines with spaces 
    - `[0-9]` is all digits (doesn’t work to do e.g. `[0-100]`)
        - to capture double digit numbers
            - `[0-9][0-9]`
            - `?[0-9]?[0-9]` if we expect that one digit isn't needed,
- **Quoting**!
    - Be very careful with quoting! And (), [], etc. 
        - Each ' requires another ' to close it, each " requires another " to close it. 
        - Syntax highlighting helps a lot.
    - We can also escape them using `\...`
    - **Double quotes** interpret arguments (e.g. "$1") and escapes, Single quotes leave them be. [(source)](https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash )
    - Whitespace (spaces, tabs, newlines) is interpreted as a delimiter between arguments! (See TLCL Ch. 7)
- **Stream Management**
    - Be aware that almost all text filter commands can accept the input file as an argument (e.g. `sed 's/sad/happy/g' input.txt`)
    -  Careful with `>` (write) vs. `>>` (append)
        - They both end the fstream; using them usually ends the pipeline (you can use `tee` as a workaround for this)
    - `>` and `>>` end the stream (alternatively can use tee)
    - Better to not generate auxiliary files
        - `grep love shakes.txt > lovelines.txt wc -l lovelines.txt `
        - This works, but adds cruft and obscures things later - if we come back in a day, how exactly did we get `lovelines.txt`?
        - Once it’s created we lose the “story,” if you will. Thus piping! `grep love shakes.txt | wc -l`
- **Calling text editors in scripts**
    - Don’t call programs like nano / less from a script: it’ll stop execution of the script until you close that instance.
    - nano/less are not text filters like grep/sed/tr/sort/etc.
        - They can *receive* input from stdin, they just don’t pass it through to stdout
    - This and all further assignments should be runnable! (don’t write the answer, write the code that generates it)
- **Command Versions** 
    - If you tried “*Unix for Poets*” you may have encountered some version differences!
    - The standard `tr` worked differently some years ago! 
    - Welcome to version differences - an eternal problem.

# Python

### Abstraction

Abstraction is powerful but dangerous. Modern software depends on layers of abstraction maintained by people you’ll never meet, and when something breaks, it can be extremely hard to trace the cause. This applies to Unix tools, Python libraries, and everything we build on top of them.

### Data as Objects

Now we shift into Python, where the mental model changes. Programming, at its core, is about manipulating data, and in Python, data is treated as objects. Variable names don’t store values directly; instead, they point to objects in memory. This is very similar to how filenames point to files. Understanding this reference-based model early will save you a lot of confusion later when things start mutating.

### Variable Types and Python’s Data Model

Python organizes data into types, each with different behavior. Numbers can be integers or floats. Sequences include lists, tuples, and strings. There are also sets and dictionaries, booleans for truth values, and None to represent the absence of a value. Each type determines what operations are allowed and how values behave when you manipulate them.

### Statements and Expressions

Statements are units of code that do something. Assignment creates bindings between names and objects. Comparisons evaluate relationships between values. Arithmetic combines values mathematically or, in the case of strings, concatenates them.

    year = 2020
    mssg = 'hooray!'
    year += 18
    mssg *= 5

These examples show that Python’s operators often work across types, but not always in ways you’d expect unless you understand the underlying objects.

### Equality Testing

Python supports standard comparison operators:

    >>> year != 2016
    True
    >>> mssg == 'howdy!'
    False
    >>> e <= 3
    True

### Function: Input–Process–Output Machines

Functions are one of the most important abstractions in programming. Conceptually, every function follows the same pattern: it takes input, performs computation, and produces output. Some functions return values, others return None, but all of them encapsulate logic so you don’t have to repeat yourself.

Built-in functions like print, type, dir, and sorted let you inspect and transform data quickly, while user-defined functions let you package your own logic.

### Defining Your Own Functions

When you define a function, you give Python a reusable block of code with a name and parameters. Indentation is not optional—it defines the function body.

    def my_function(arg1, arg2):
        return 42

This structure is Python’s way of enforcing clarity. If the indentation is wrong, the program is wrong.

Important built-in functions include:
- print(x)
- help(x)
- type(x)
- dir(x)
- sorted(x)
- min(x), max(x)
- sum(x)
- int(x), float(x), bool(x)
- list(x), tuple(x), str(x)

### Control Flow with Conditionals

Control flow determines which code runs and when. Conditional statements allow programs to make decisions based on data.

    if x < 0:
        print('Negative!')
    elif x == 0:
        print('Zero!')
    else:
        print('Positive!')

Only one branch executes, and Python checks conditions from top to bottom until it finds a match.

### Loops for Repetition

Loops let us repeat actions. A `for` loop iterates over items in a sequence, whether that’s a list, a range of numbers, or lines in a file.

    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    
    for i in range(5):
        print(i)

    for line in open('shakes.txt'):
        print(line)

A `while` loop repeats until a condition becomes false, which is useful when you don’t know in advance how many iterations you’ll need.

    a, b = 0, 1
    while a < 10:
        print(a, end=' ')
        a, b = b, a + b

### Whitespace as Syntax

Unlike many languages, Python uses whitespace to define code structure. Function bodies and control-flow blocks must be indented consistently. This design choice forces readability and eliminates entire classes of bugs that come from mismatched braces in other languages. Editors help by auto-indenting Python files, but you must still be careful when closing blocks.

### Indexing and Slicing Sequences

Strings and lists are sequences, which means they support indexing and slicing. 
- Indexing starts at zero, and negative indices count from the end.
- Syntax: `sequence[start:end]`

###

    job_title = 'LINGUIST'
    job_title[3:-1]
    job_title[:5]

Slices include the start index but exclude the end index, a rule that stays consistent across Python.

### Object-Oriented Thinking

Python is an object-oriented language, meaning values come with both data and behavior. Objects have attributes, which store information, and methods, which define actions you can perform.

    s = 'my string'
    s.lower()
    s.find('str')

This is why you’ll often see dot notation—methods belong to objects, not to the language globally.

### String and List Methods

Strings and lists have rich sets of methods. String methods like strip, lower, find, and replace return new strings. List methods like append, remove, and pop modify lists in place. This distinction—**immutability** vs **mutability**—is critical and will come up repeatedly in future weeks.

### Strings vs. Lists

Strings and lists are both sequences, but strings are immutable and lists are mutable. You can change a list element directly, but you cannot change a character inside a string. 

Converting between the two using split and join is a common pattern in text processing.

### Decomposition and Assignment Strategy

Finally, when working on assignments, the key skill is decomposition. Break problems into smaller subproblems, test each piece, and rely on provided tests as guides—not guarantees. Your code must always run from start to finish without manual intervention.






