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

---

### Python

#### Variable Types
#### Statements

Statements are units of code that do something.

**Assignment**:

    year = 2020 # integer 
    mssg = 'hooray!' # string 
    e = 2.71828 # float

**Equality Testing:**

    >>> year != 2016 
    True 
    >>> mssg == 'howdy!' 
    False 
    >>> e <= 3 
    True

#### Functions 


 FININSHED

#### Control Flow
#### Whitespace
#### String & List Indexing
#### OOP
#### String Methods
#### List Methods