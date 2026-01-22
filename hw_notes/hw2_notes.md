# HW2 Notes


### Introduced Commmands:

- wget flags
    - `-O` specifies the output filename
    - Example: feteches a txt file and renames it to `shakes.txt`
        - `wget -O shakes.txt https://robvoigt.net/lin127/a2/shakespeare.txt`
- wc
    - Allows us to roughly count words and lines in a file.
- grep
    - A powerful program that allows you to filter by matching on a textual pattern
    - It uses **regular expressions**, a very flexible way to specify complex patterns
        - `[0-9], [A-Z], [Aa],` etc
- head
    - Print the first ten lines of a file
- tail
    - Print the last ten lines of a file
- shuf
    - shuffles the order of the data
- sed
    - Stands for **stream editor**, allowing us to edit the incoming stream of text
        - can replaces instances of patterns with other text
        - similarly, it also delete instances of any patterns
    - The main feature we will use is substitution: `sed 's/pattern/replacement/'`
- sort
    - Sorts input stream lines alphabetically. 
    - This can take a second to run if the file is big (as it is in this case), and many minutes to run if the file is huge. 
    - `-r` flag reverses the order of the sort.
    - Flag `-n` **sorts numerically** rather than alphabetically
- uniq
    - a command that de-duplicates adjacent lines that match exactly. Note the duplicate lines must be immediately adjacent, so we very frequently see `sort | uniq`
    - Flag `-c` counts the number of unique occurrences of each duplicated line
- tr
    - stands for translate; it's like a streamlined version of `sed` for certain operations, in particular manipulating some classes of characters.
    - It can accept sets of characters in square brackets like `grep` ([A-Z]) as well as a few special named classes like '[:punct:]'.
    - `tr '[A-Z]' '[a-z]'`
        - Takes all uppercase characters and makes them the corresponding lowercase one;
    - `tr -d '[:punct:]'`
        - Deletes all characters from the "punctuation" class. Add these into your command from above to make the answer even better!
- cut
    - A useful command to extract pieces of a line. 
    - Key flags to know are:
        - `-f` followed by an integer, representing which field(s) to print.
        - `-d` followed by a character representing the '**delimiter**' which will split the line. 
            - For clarity it's good to surround this character in single quotes, and doing so is necessary if you want the delimiter to be a special character like a blank space.
        - Example:
            - `cut -f 3 -d ',' file.txt`
            - This will take every line in `file.txt`, cut the line up at every comma, and print the third comma-separated chunk. 
            - We can make the delimiter a `' '` too
- source 
    - **source** is a Bash shell built-in command that executes the content of the file passed as an argument in the current shell. It has a synonym in `.` (period). [source](https://superuser.com/questions/46139/what-does-source-do)

### 'Shebang' (`#!`)

    #!/bin/bash

The pound+exclamation combo is called a "**shebang**", and in this case it indicates where the shell program that should be used to execute this script lives. 
`/bin` is a system-level folder that holds compiled programs, and of course bash is our favorite shell program.

### Flags

Some flags are just "switches" (on/off), but some flags **take arguments**.

**Example:**

    adrianomelofilho@Adrianos-MacBook-Pro a2 % grep -v -i -e '[A]' -e '^$' shakes.txt | wc -l
        9910
    adrianomelofilho@Adrianos-MacBook-Pro a2 % grep -v -i -e '[A]' -e '[a]' -e '^$' shakes.txt | wc -l
        9910
    adrianomelofilho@Adrianos-MacBook-Pro a2 % grep -vie '[A]' -e '[a]' -e '^$' shakes.txt | wc -l 
        9910
    adrianomelofilho@Adrianos-MacBook-Pro a2 % grep -eiv '[A]' -e '[a]' -e '^$' shakes.txt | wc -l
    grep: [A]: No such file or directory
    107991
    adrianomelofilho@Adrianos-MacBook-Pro a2 % grep -iev '[A]' -e '[a]' -e '^$' shakes.txt | wc -l
    grep: [A]: No such file or directory
    114413

- `-v` = switch (no argument needed)
- `-i` = switch (no argument needed)
- `-e` = **takes an argument** (the pattern that follows it)

When you write `-vie`, grep reads this as:
- `-v` = invert
- `-i` = case-insensitive  
- `-e` = the next thing is a pattern

The `'[A]'` after `-vie` is correctly associated with the `-e`.

But when you write `-eiv`, grep reads:
- `-e` = the next thing is a pattern
- `-i` = wait, this looks like another flag...
- `-v` = and this too...

So grep gets confused and tries to interpret `[A]` as a **filename** instead of as the argument to `-e`.

**Rule**: Flags that take arguments should generally come last in a combined flag sequence, OR you separate them out.

---

### Special Chars

`^` is a special character for `sed` and `grep` meaning '**the beginning of the line**.'
`*` is another one meaning 'the previous character as many times as needed.'
So we can use `sed` to remove leading whitespace, like so:
    
    sed 's/^ *//'

The following removes all the whitespace leading up to the first char/string :

    cat shakes.txt | sed 's/^ *//' | less

`$` is another that means '**the end of the line**.'

    '^$'

When combined, this means any line that start with nothing and end with nothing (null lines).

---

### Scripting (`.sh` files)

**Scripts** in bash run series of bash commands to achieve some larger goal. First line of an `.sh` file is always `#!/bin/bash`.

**Positional arguments** can be referred to in scripts with `$N`, where `N` is a number showing its position. So if we have a script that is run like `my_script.sh filename.txt`:
- Inside the script, if we use `$1` this will refer to `filename.txt`.
- So if in your original command you started with `cat shakes.txt`, here you can do:
###
    cat "$1" | etc etc

To make scripts **executable**, run:

    chmod +x <script_name.sh>

- `Chmod` changes modes (change **file permission**)
- `+x` adds execute permission.
- This command makes files executable (runnable as a prog). 

By default, when you create a text file (like a script), it's just a text file - the system won't let you run it as a program.

After changing chmod permissions, run the script via:

    ./clean_text.sh

Additionally, scripts can be run inside of other scripts and positional arguments are still followed:
    
    #!/bin/bash

    ./clean_text.sh $1
    # echo "created clean_$1"
    ./word_counts.sh clean_$1
    # echo 'created word_counts.txt'

This script takes a text file cleans the white spaces and empty lines by running `./clean_text.sh $1` on any text file entered as $1 then the second script takes the output from the first script and does counts/orders the words via `./word_counts.sh clean_$1`.