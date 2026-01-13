# Chapters 6-8 Reading

## Chapter 6: Redirection

This chapter introduces I/O redirection, one of the most powerful features of the Unix/Linux command line. I/O stands for input/output, and redirection allows commands to send output to files, read input from files, and connect commands together using pipelines. This chapter focuses on how small commands can be combined to solve complex problems.

### Introduced Commands:
- cat – Concatenate files
- sort – Sort lines of text
- uniq – Report or omit repeated lines
- grep – Print lines matching a pattern
- wc – Print line, word, and byte counts
- head – Output the first part of a file
- tail – Output the last part of a file
- tee – Read from standard input and write to standard output and files

---

### Standard Input, Output, and Error

Unix programs use three standard data streams:

***Standard input*** (stdin, file descriptor 0)
This is where a program receives input. By default, it comes from the keyboard.

***Standard output*** (stdout, file descriptor 1)
This is where a program sends its normal results. By default, it goes to the screen.

***Standard error*** (stderr, file descriptor 2)
This is where a program sends error and status messages. By default, it also goes to the screen.

Because Unix treats everything as a file, these streams can be redirected.

---

### Redirecting Standard Output (`>`)

***Standard output*** can be redirected to a file using the `>` operator:

	ls -l /usr/bin > ls-output.txt

This sends the long directory listing of /usr/bin to the file ls-output.txt instead of the screen.

**Checking the file:**

	ls -l ls-output.txt

**Viewing its contents:**

	less ls-output.txt

**If the directory does not exist:**

	ls -l /bin/usr > ls-output.txt

The error message still appears on the screen because errors go to stderr, not stdout.

**Checking the file afterward:**

	ls -l ls-output.txt

The file is empty because > always truncates the file before writing.

**Explicitly truncate or create an empty files**:

	ls-output.txt

---

### Appending Output (`>>`)

To append output instead of overwriting, use `>>`:

    ls -l /usr/bin >> ls-output.txt

**Repeating the command multiple times**:

    ls -l /usr/bin >> ls-output.txt
    ls -l /usr/bin >> ls-output.txt
    ls -l /usr/bin >> ls-output.txt

**Checking the file**:

    ls -l ls-output.txt

The file grows each time output is appended.

---

### Group Commands (`{ }`)

When running multiple commands and redirecting them to the same file, grouping avoids repetition.

**Without grouping**:

    command1 > logfile.txt
    command2 >> logfile.txt
    command3 >> logfile.txt

**On one line**:

    command1 > logfile.txt; command2 >> logfile.txt; command3 >> logfile.txt

**Using a group command**:

    { command1; command2; command3; } > logfile.txt

The shell treats the group as a single command for redirection.

**Rules**:
1. Spaces are required around the braces
2. The last command must end with a semicolon or newline

---

### Redirecting Standard Error (`2>`)

***Standard error*** is redirected using its file descriptor number (2):

    ls -l /bin/usr 2> ls-error.txt

This sends only error messages to ls-error.txt.

---

### Redirecting stdout and stderr Together

**Traditional method (order matters)**:

    ls -l /bin/usr > ls-output.txt 2>&1

**Correct order:**

    ls-output.txt 2>&1

**Incorrect order** (stderr goes to screen):

    2>&1 > ls-output.txt

**Modern bash shortcut**:
    
    ls -l /bin/usr &> ls-output.txt

**Appending both streams**:

    ls -l /bin/usr &>> ls-output.txt

---

### Discarding Output (`/dev/null`)

Unwanted output can be discarded by redirecting it to `/dev/null`, known as the “***bit bucket***”:

    ls -l /bin/usr 2> /dev/null

Anything sent to /dev/null disappears.

---

### Redirecting Standard Input (`<`)

The `cat` command is used to demonstrate standard input behavior:

    cat [file…]

**Display a file**:

    cat ls-output.txt

**Join multiple files**:

    cat movie.mpeg.0* > movie.mpeg

**Cat without arguments**.
    
    cat
    The quick brown fox jumps over the lazy dog.
    Ctrl-D

If cat is run with no arguments, it waits for keyboard input. After typing text, press Ctrl-D to signal end-of-file. The text is echoed because stdin is copied to stdout.

**Create a file from stdin**:
    
    cat > lazy_dog.txt
    The quick brown fox jumps over the lazy dog.
    Ctrl-D

**View the file:**

    cat lazy_dog.txt

**Redirect stdin from a file:**

    cat < lazy_dog.txt

**Which is equivalent to...**

    cat lazy_dog.txt

---

### Pipelines (`|`)

***Pipelines*** connect commands so the output of one becomes the input of another.

**Syntax:**

    command1 | command2

Example:

    ls -l /usr/bin | less

**Difference between > and |**:

    command1 > file1   (output goes to a file)
    command1 | command2 (output goes to another command)

**Dangerous mistake:**

    command1 > command2

For example:

    cd /usr/bin
    ls > less

This overwrites the less program with text output, breaking it. 

**Lesson:** `>` silently overwrites files and must be used carefully.

---

### Filters and Pipelines

Commands used in pipelines are often called ***filters*** because they transform data.

**Sorting:**

    ls /bin /usr/bin | sort | less

**Removing duplicates:**

    ls /bin /usr/bin | sort | uniq | less

**Showing duplicates only:**
    
    ls /bin /usr/bin | sort | uniq -d | less

---

### Counting with `wc`

**Count lines, words, and bytes:**

    wc ls-output.txt

**Count lines only in a pipeline:**

    ls /bin /usr/bin | sort | uniq | wc -l

---

### Searching with `grep`

Basic usage:

    grep pattern [file…]

Example:

    ls /bin /usr/bin | sort | uniq | grep zip

**Common flags**:
- `-i` ignore case
- `-l` print filenames only
- `-v` invert match
- `-w` match whole words

---

### `head` and `tail`

Display first or last lines of output:

    head -n 5 ls-output.txt
    tail -n 5 ls-output.txt

Use in pipelines:

    ls /usr/bin | tail -n 5

**Extract the middle of a file**:

    head -n -5 text_header_footer.txt | tail -n +5 > text.txt

**Follow a file in real time**:

    tail -f /var/log/messages

Stop with Ctrl-C.

---

### `tee`

***tee*** copies stdin to stdout and to a file at the same time:

    ls /usr/bin | tee ls.txt | grep zip

This saves the full output to ls.txt while still allowing the pipeline to continue.

---

### Ch 6 Takeaways:

Redirection and pipelines are core Unix concepts. Commands are designed to work with stdin, stdout, and stderr so they can be combined freely. Small tools can be connected to build powerful workflows. Linux emphasizes flexibility, composition, and user control—like building with an Erector Set instead of using sealed cartridges.

---
## Chapter 7: Seeing the World as the Shell Sees it

This chapter explains what the shell actually does to a command line after you press Enter but before the command runs. Bash performs a series of transformations called expansions, which replace certain characters and expressions with other text. Understanding expansion and quoting is critical to using the shell correctly and safely.

### Introduced commands:
echo – Displays a line of text (used to demonstrate expansion)

---

### Expansion

***Expansion*** is the process by which the shell replaces text you type with something else before executing the command. The command itself never sees the original text—only the expanded result:

    echo this is a test
    Output:
    this is a test

Wildcard (`*`) expansion example:
    
    echo *

Output:

    Desktop Documents ls-output.txt Music Pictures Public Templates Videos

The * character was expanded by the shell into filenames before echo ran.

---

### Pathname Expansion (Wildcards)

Wildcard matching is called ***pathname expansion***.

Given a directory containing:

    Desktop Documents Music Pictures Public Templates Videos

**Examples:**
|Command|Output|
|:-|:-|
|`echo D*`|Desktop Documents|
|`echo *s`|Documents Pictures Templates Videos|
|`echo [[:upper:]]*`|Desktop Documents Music Pictures Public Templates Videos|
|`echo /usr/*/share`|/usr/kerberos/share /usr/local/share|

---

### Hidden Files and Expansion

***Hidden files*** begin with a period (.).

This does NOT show hidden files:

    echo *

This almost works:

    echo .*

But it includes . and .. (current and parent directories).

Demonstration:

    ls -d .* | less

**Correct pattern for most hidden files:**

    echo .[!.]*

Alternatively:

    ls -A

---

### Tilde Expansion (~)

The tilde expands to a user’s home directory.

**Current user:**

    echo ~
    Expands to:
    /home/me

**Specific user:**

    echo ~bob
    Expands to:
    /home/bob

---

### Arithmetic Expansion

Arithmetic expansion allows integer math using: `$((expression))`:

    echo $((2 + 2)) //output = 4

**Other Examples:**

|Command Type|Command|Output|
|:-|:-|:-|
|Nested| `echo $(($((5**2)) * 3))`|75|
|Single| `echo $(((5**2) * 3))`|75|
|Division|`echo Five divided by two equals $((5/2))`|Five divided by two equals 2|
|Remainder|`echo with $((5%2)) left over`|with 1 left over.|

***NOTE:*** Only integers are supported.

---

### Brace Expansion

***Brace expansion*** generates multiple strings from a pattern:

    echo Front-{A,B,C}-Back
    
Output:

    Front-A-Back Front-B-Back Front-C-Back

|Command Type|Command|Output|
|:-|:-|:-|
|Numeric ranges|`echo Number_{1..5}`|Number_1 Number_2 Number_3 Number_4 Number_5|
|Zero-padded ranges|`echo {01..15}` or `echo {001..15}`||
|Reverse order|`echo {Z..A}`| Z Y X ...|
|Nested braces|`echo a{A{1,2},B{3,4}}b`|aA1b aA2b aB3b aB4b|


**Practical example (directory creation):**

    mkdir Photos
    cd Photos
    mkdir {2007..2009}-{01..12}

This creates year-month directories automatically.

---

### Parameter Expansion

***Parameter expansion*** retrieves variable values:
    
    echo $USER // out = me


**List environment variables:**

    printenv | less

**Misspelled variables expand to empty:**

    echo $SUER //output is blank

---

### Command Substitution

***Command substitution*** uses command output as text: `$(command)`

Example:

    echo $(ls)

or:

    ls -l $(which cp)

**Pipeline substitution**:

    file $(ls -d /usr/bin/* | grep zip)

**Older syntax (still supported):**

    ls -l which cp

---

### Quoting (Why It Matters)

Without quoting, expansions and word splitting can change meaning.

Example:

    echo The total is $100.00 // output: The total is 00.00

---

### Double Quotes (`” “`)

***Double quotes*** suppress:
- word splitting
- pathname expansion
- tilde expansion
- brace expansion

But still allow:
- parameter expansion
- arithmetic expansion
- command substitution

**Filename with spaces:**

    ls -l two words.txt
(fails)

**Correct usage:**

    ls -l “two words.txt”
    mv “two words.txt” two_words.txt

**Expansion still occurs:**

    echo “$USER $((2+2)) $(df -h)”

**Effect on command substitution:**

    echo $(df -h)
Produces many arguments (spaces and newlines split)

Or...

    echo “$(df -h)”
Preserves formatting as one argument

---

### Single Quotes (`’ ’`)

***Single quotes*** suppress all expansions.

Comparison:

    echo text ~/.txt {a,b} $(echo foo) $((2+2)) $USER
    echo “text ~/.txt {a,b} $(echo foo) $((2+2)) $USER”
    echo ‘text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER’

Each level of quoting suppresses more expansions.

---

### Escaping Characters ()

A backslash escapes a single character:

    echo “The balance for user $USER is: $5.00”

**Escaping filenames**:

    mv bad&filename good_filename

**Literal backslash**:

    \

**Suppressing aliases:**

    \ls

---

### Backslash Escape Sequences

|Common Escape Sequences|Meaning|
|:-|:-|
|`\a`  |Bell|
|`\b` | Backspace|
|`\n` | Newline|
|`\r` | Carriage return|
|`\t` | Tab|

**Enable with `echo -e`:**

    sleep 10; echo -e “Time’s up\a”

Alternative:

    sleep 10; echo “Time’s up” $’\a’

---

### Key Takeaways
- The shell expands text before executing commands
- Most “magic” happens before the command runs
- Quoting controls expansion
- Double quotes allow some expansion; single quotes allow none
- Escaping suppresses individual characters
- Understanding expansion prevents errors and surprises

Without understanding expansion and quoting, the shell feels unpredictable. With it, the shell becomes precise, powerful, and reliable.