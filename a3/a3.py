print("""
##########################################
#   LIN 127
#   Text Processing and Corpus Linguistics
#   Assignment 3
##########################################

""")

# Welcome to week 3!

# Yet again we're faced with a new sort of file! Last week we had a '.sh' file,
# which is a bash/shell script. This week we're starting to work in python, and
# '.py' is the standard file extension for python scripts and code.

# You may remember me saying file extensions are just a suggestion, which is
# true - '.txt', '.sh', and '.py' are all just plain text files under the hood.
# But they are helpful suggestions that provide your text editor with an idea of
# what sort of syntax highlighting to use. Syntax highlighting is *very* useful
# and I suggest you make sure your editor is doing it. emacs and vim will do it
# by default, and nano requires edits to nanorc, described in the first assignment.

# We will be working with Python 3. In later assignments we will have to handle
# environments and packages, but this assignment should work on nearly any default
# installation of Python 3. 

# You can run this entire file as a script by running:
#   python3 a3.py
# This will print out your answers, as well as output from testing functions
# that will test your code in the later parts of the assignment.


print("""
-----------------------------------------
#### 0. Info
""")

"""
Please do this part by filling in the string variables below once you've
completed the assignment. Notice how you can do multi-line strings by starting
and ending with three double-quotes. This is how most of the instructions in the
assignment are presented as well, which is useful for multi-line comments.
"""

# >>> YOUR ANSWER HERE
name = 'Adriano Melo Filho'
comments_or_questions = """
[i got nothing so far...]
"""
completed = True
# >>> END YOUR ANSWER

print('Name: ' + name)
print('Comments or questions: ' + comments_or_questions)
print('Completed: ' + str(completed))
print("""
-----------------------------------------
#### 1. Variables and Errors Are Your Friends
""")
"""
The fastest way to figure out if you're doing something right is to run it and
see what happens. It's very helpful if you get an error, because the error will
explain what went wrong. The tricky times are when something is wrong but you
don't get an error, so appreciate the errors you do get!

In this section we'll learn more about how variable types in Python interact,
the types of errors you can get, and how to read and understand them. To start,
open the Python interpreter (simply `python3` on the command line), and create
these variables about our class (you can copy paste from here):
"""
university       = 'UC Davis' # str
total_students   = 40848 # int
department       = 'Linguistics' # str
course_number    = 127 # int
class_size       = 61 # int
virtual_class    = False # bool
having_fun       = True # bool
expected_gpa     = 4.0  # float
worries          = None # special None type
"""
For the following questions, you'll be presented with an operation to perform.
Run the operation in the interpreter to find the answer, then write the answer
you found as a string in the associated print statement. Note that you are not
running the entire print() statement, but the expression written inside it.
The questions to answer in each case are:
  - If an error didn't occur, what type is the output and why?
  - If an error occured, what sort of error was it and why?
Just answer very briefly! No need for an essay.

Remember you can wrap anything in type() to display its type if you're unsure.

"""
print('a. university + department')
# >>> YOUR ANSWER HERE
print('[UC DavisLinguistics]')
# >>> END YOUR ANSWER
print('')


print('b. department + course_number')
# >>> YOUR ANSWER HERE
print('[TypeError: can only concatenate str (not "int") to str]')
# >>> END YOUR ANSWER
print('')


print('c. university * class_size')
# >>> YOUR ANSWER HERE
print('[UC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC DavisUC Davis]')
# >>> END YOUR ANSWER
print('')


print('d. int(department)')
# >>> YOUR ANSWER HERE
print("[ValueError: invalid literal for int() with base 10: Linguistics']")
# >>> END YOUR ANSWER
print('')


print('e. class_size / total_students')
# >>> YOUR ANSWER HERE
print('[0.0014933411672542107]')
# >>> END YOUR ANSWER
print('')


print('f. virtual_class and having_fun')
# >>> YOUR ANSWER HERE
print('[False]')
# >>> END YOUR ANSWER
print('')

print('g.  expected_gpa and virtual_class')
# >>> YOUR ANSWER HERE
print('[False]')
# >>> END YOUR ANSWER
print('')

print('h. worries and virtual_class')
# >>> YOUR ANSWER HERE
print('[returns none type which is just moving to next line.]')
# >>> END YOUR ANSWER
print('')

print('i. virtual_class and worries')
# >>> YOUR ANSWER HERE
print('[False]')
# >>> END YOUR ANSWER
print('')

print('j. worries + university')
# >>> YOUR ANSWER HERE
print("[TypeError: unsupported operand type(s) for +: 'NoneType' and 'str']")
# >>> END YOUR ANSWER
print('')


print('k. having_fun > total_students')
# >>> YOUR ANSWER HERE
print('[False]')
# >>> END YOUR ANSWER
print('')


print('l. department[1532:]')
# >>> YOUR ANSWER HERE
print('['']')
# >>> END YOUR ANSWER
print('')

print('m. department[1532]')
# >>> YOUR ANSWER HERE
print('[IndexError: string index out of range]')
# >>> END YOUR ANSWER
print('')

print('n. dprtmnt')
# >>> YOUR ANSWER HERE
print("[NameError: name 'dprtmnt' is not defined. Did you mean: 'department'?]")
# >>> END YOUR ANSWER
print('')

print('o. if worries: print("OH NO")')
# >>> YOUR ANSWER HERE
print('[...]')
# >>> END YOUR ANSWER
print('')


"""
-----------------------------------------
#### Interlude. Notes on working with functions below.

For the rest of the assignment you'll work by writing code to implement
functions. You'll be provided with the `def` line, which for the first function
looks like this:

    def mean(vals):

`def` is a special keyword telling Python that a function definition is coming
up, then the name of the function is given (mean), then the parens with any
input variables inside (though the parens are always necessary whether the
function takes variables or not), and a colon on the end.

Remember that whitespace really matters. Here the code in the body of the
function must be indented one level. The moment there's a line of code at zero
indentation, the function is closed. Then remember of course that the code in
the body of control flow items like `if`, `for`, and `while` must be indented
an additional level.

Each function will have a space for you to write your code clearly demarcated.
Immediately below each function a series of test cases are provided, which are
then run over your function to see if they work as expected, using the function
`run_tests` below this comment. These are not necessarily exhaustive, so feel
free to add additional examples as tuples in the `tests` list following the
format, but please do not otherwise edit the code of these testing functions.

The assignment will start out with these functions blank and therefore not
working; once your functions work, when you run the assignment as a script
(`python assignment.py` on the command line) the tests for each problem should
all say 'All tests passed!'
"""
def run_tests(func, tests):
    print('\tRunning {} tests on the `{}` function...'.format(len(tests), func.__name__))
    errors = 0
    for val, ret in tests:
        try:
            if type(val) == tuple:
                assert func(*val) == ret
            else:
                assert func(val) == ret
        except AssertionError:
            print('\t\terror for input {}'.format(val))
            errors += 1
    if errors == 0:
        print('\tAll tests passed!')


print("""
-----------------------------------------
#### 2. Getting Loopy on Sequences
""")
"""
Here we'll make a few functions to work with `for` and `while` loops over
sequences (both strings and lists).

One thing to note is a very common paradigm when working with loops is to first
do some preliminary setup (like creating a new variable to accumulate values),
then do updates during the loop (like incrementing that variable under certain
conditions), then to do some finishing up (like returning the incremented
variable).
"""

print("""
a. Complete the function `mean` for calculating the mean (average) of a list of
numeric values.
""")
"""
Your function should take a list `vals` as its argument and return a float. It's
okay for your function to not work (and throw an error) if `vals` is anything
other than a list of numbers.

There's at least two ways to do this - one using a for-loop and accumulating
values, and another using the built-in function `sum`. Remember you can look up
help on how particular functions work using e.g. help(sum) in the interpreter.
"""

def mean(vals):
    """Return the mean of the values in `vals`,
    a list of numbers (float or int)."""
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    total = 0
    for values in vals:
        total += values
    return total/len(vals)
    # >>> END YOUR ANSWER

tests = [
    ([1,4,9,16,25,36,49], 20.0),
    ([0], 0),
    ([-2,-1,1,5], 0.75)
]
run_tests(mean, tests)


print("""
b. Complete the function `letters_only` which takes a string `s` and returns a
version of that string with only ascii letters.
""")
""" Note this should mean the output string has no whitespace, no punctuation,
no numbers, and no special characters. In grep/tr terms, only [A-Za-z].
Hint: it'll help to use the 'string' module, which is imported for you. Look at
the attributes on it.
"""
def letters_only(s):
    # Delete pass and fill in.
    import string
    # >>> YOUR ANSWER HERE
    new_string = ''
    for c in s:
        if c in string.ascii_letters:
            new_string += c
    return new_string
    # >>> END YOUR ANSWER

tests = [
    ('a big wild test!!!!', 'abigwildtest'),
    ('17 billion 808s', 'billions'),
    ('?!!!?!', '')
]

run_tests(letters_only, tests)


print("""
c. Complete the function `vowel_count` which counts how many times a vowel
appears in a string.
""")
"""
Vowels here are defined as any of 'aeiou'. The function takes the string `s` and
returns an integer. This should work regardless of whether the vowels are
capitalized.
"""
def vowel_count(s):
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    vowels = 'aeiou'
    s = s.lower()
    
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count
    # >>> END YOUR ANSWER

tests = [
    ('glyph crypt', 0),
    ('Koyaanisqatsi', 6),
    ('AAAAAAAAAAAH!!!!', 11)
]

run_tests(vowel_count, tests)


print("""
d. Complete the function `reverse_string` which takes a string `s` and returns a
reversed version of that string.
""")
"""
So for example, running reverse_string('magic') would return 'cigam'. There's a
number of ways you could do this; one would be to use a `while` loop, another
might be to use negative indexing with `range`. Two hints for the `while` loop
case: a) consider what happens when you cast a string to list, b) look at the
`pop` method that lists have.
"""
def reverse_string(s):
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    rev_s = ''
    for c in s:
        rev_s = c + rev_s  # prepend approach
    return rev_s
    # >>> END YOUR ANSWER

tests = [
    ('nacirema', 'american'),
    ('LiNgUiStIcS', 'ScItSiUgNiL'),
    ('100,000,000', '000,000,001')
]

run_tests(reverse_string, tests)


print("""
-----------------------------------------
#### 3. Conditionally Approved
""")
"""
Here are a few exercises to get a bit more familiarity with conditionals and
boolean logic.
"""

print("""
a. Complete the function `string_squish` which takes two strings `s1` and `s2`,
and returns a string of the form shortLONGshort.
""")
"""
Which is to say, identify which of `s1` and `s2` is longer, and put it in the
middle and uppercased, surrounded by two instances of the shorter string,
lowercased. So for instance, string_squish('hi','o') should return 'oHIo'. If
the strings are the same length you can put either one in the middle.
"""

def string_squish(s1, s2):
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    long = s1
    short = s2
    if (len(s1) < len(s2)):
        long = s2
        short = s1
    return short + long.upper() + short
    # >>> END YOUR ANSWER

tests = [
    (('o','hi'), 'oHIo'),
    (('itlem','ent'), 'entITLEMent'),
    (('in','vigorat'), 'inVIGORATin')
]
run_tests(string_squish, tests)



print("""
b. Complete the function `remove_stopwords` which take a string `s` and returns
a string with very common function words removed.
""")
"""
The term 'stopwords' refers to very common words like 'the', 'a', and 'and'
which are sometimes removed for analysis in computational linguistics
applications.

We talked in class about the string methods split() and join(), and you'll need
to use those here. You can assume the strings will have no punctuation, so we
can use simple whitespace tokenization.

To give a little more detail - first use s.split() to break the string into
a list of words (which will be separated on whitespace). Then create a new empty
list to accumulate words. Loop over the original words, only adding them to the
new list if they aren't in the provided list of stopwords (using the keyword
`in`). Then use ' '.join() to re-join the new list into a string, and return it.
"""
def remove_stopwords(s):
    # Delete pass and fill in.
    stopwords = ['a', 'an', 'and', 'if', 'in', 'it', 'of', 'on', 'the', 'then', 'which','with']
    # >>> YOUR ANSWER HERE
    s_clean = []
    tokens = s.split(' ')
    for w in tokens:
        if w not in stopwords:
            s_clean.append(w)
    final = ' '.join(s_clean)
    print(final)
    return final
    # >>> END YOUR ANSWER

tests = [
    ('the cat in the hat', 'cat hat'),
    ('in a garden full of plants', 'garden full plants'),
    ('it looks like rain', 'looks like rain')
]


run_tests(remove_stopwords, tests)



print("""
c. Complete the function `roll_the_dice` which takes two integers `d1` and `d2`
and tells you the outcome of the roll.
""")
"""
Firstly you need to check if the dice are valid - if either dice is not an
integer, or not between 1 and 6, return `not_dice_message`. If the dice add up
to 7 or 11, return `win_message`. Otherwise return `lose_message`.

Remember the `type` function gives you the type of an object, so e.g.:
   type(d1) != int
will return True if d1 is not an integer.

This will be made a lot easier if you use the 'and' or 'or' keywords to make
compound conditional statements.
"""
def roll_the_dice(d1, d2):
    # Delete pass and fill in.
    not_dice_message = "These aren't dice!"
    win_message = "YOU WIN!!!"
    lose_message = "You lose..."
    # >>> YOUR ANSWER HERE
    if(type(d1)!= int or type(d2)!= int): # int check
        return not_dice_message
    
    if (d1 > 6 or d1 < 1 or d2 > 6 or d2 < 1): # valid die check
        return not_dice_message
    
    sum = (d1 + d2)
    if sum == 7 or sum == 11: # roll outcomes
        return win_message
    else:
        return lose_message
    

    # >>> END YOUR ANSWER

tests = [
    ((3,8), "These aren't dice!"),
    ((3,4), "YOU WIN!!!"),
    ((1,1), 'You lose...'),
    (('Mr. Potato Head', 4.5), "These aren't dice!")
]

run_tests(roll_the_dice, tests)


print("""\n
-----------------------------------------
#### 4. Beatiful Music from a Function Composer
""")
"""
We mentioned in class the importance of the concepts of abstraction and
decomposition - one easy way to do this is to compose functions. Once we wrote
something once and trust it works properly, we don't have to write it again.
Instead we can abstract away from it by trusting what we've already done, and
use it as a piece of a larger puzzle.

To practice this, in this section each problem will require you to use one or
more of the functions you implemented previously.
"""

print("""
a. Complete the function `palindrome_detector`, which takes a string `s` and
returns a boolean representing whether that string is a palindrome.
""")
"""
A palindrome is a word or phrase that is the same backwards and forwards. Your
function should return True if the input string is a palindrome and False
otherwise. Your detector should work regardless of whitespace, punctuation, and
any numbers in the string-- use your letters_only function.
"""

def palindrome_detector(s):
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    
    s_clean = ''.join([char.lower() for char in s if (char.isalpha())])
    
    # print(s_clean) # check string before comparing...

    i = 0
    j = len(s_clean) - 1
    while (i < j):
        if s_clean[i] != s_clean[j]:
            return False
        i += 1
        j -= 1
    return True
    # >>> END YOUR ANSWER

tests = [
    ('UFO tofu?', True),
    ('megalomaniacal', False),
    ('Oozy rat in a sanitary zoo.', True),
    ('Was it a car or a cat I saw?', True),
    ("I'm a palindrome too, I promise!!!", False),
    ('T A C O || C A T', True),
    ('breezy yeezy', False),
    ('Ava, Otto, Hannah, Otto, Ava', True),
    ('3racecar5', True)
]

run_tests(palindrome_detector, tests)


print("""
b. Count the proportion of vowels in English words.
""")
"""
There is a useful file in most Unix operating systems called the `words` file,
which contains a list of words (generally in English). You can get some more
info on it here:
  https://en.wikipedia.org/wiki/Words_(Unix)

On WSL, OSX, and most versions of Linux you can find this file at the path:
  /usr/share/dict/words

First of all, figure out where this file or one like it lives on your system,
since you'll need to use its path to answer this question.

We saw in class how we can use a `for` loop with the `open` function to read
through the lines in a file. Use the functions you've already made to loop
through this file and accumulate counts of the number of letters and number of
vowels for each word in this file.
"""

def proportion_of_vowels_in_english():
    # Delete pass and fill in.
    total_vowels = 0
    total_letters = 0
    # >>> YOUR ANSWER HERE
    import string
    vowels = 'aeiou'
    path = '/usr/share/dict/web2'

    for line in open(path):
        line_merged = ''.join([char.lower() for char in line if (char.isalpha())])
        for char in line_merged:
            total_letters += 1
            if char in vowels:
                total_vowels += 1
        
        
        
    print("Total vowels:", total_vowels, "\nTotal letters: ", total_letters)

    # >>> END YOUR ANSWER
    return total_vowels / total_letters

try:
    print('\tBy my calculations, {0:.2f}% of the letters in English words are vowels.'.format(proportion_of_vowels_in_english() * 100))
except ZeroDivisionError:
    print('\tReturned a divide-by-zero error, or not yet implemented.')



print("""
c. Find long palindromes in the Unix words file.
""")
"""
Complete the function `find_long_palindromes` which accumulates a list of
palindromes in the Unix words file (read with `open` as in the previous problem)
with a length greater than or equal to number of letters specified `min_length`
argument. Note that min_length does not include whitespace, punctuation, etc.A 
min_length of 5 would exclude a word like "bye123! 4567".

Notice this function is written with a default argument of 6, meaning it can be
called with simply `find_long_palindromes()`, in which case min_length will be
6, or with a specified length like `find_long_palindromes(4)` which would set
`min_length` to 4.
"""
def find_long_palindromes(min_length = 6):
    # Delete pass and fill in.
    palindromes = []
    # >>> YOUR ANSWER HERE
    path = '/usr/share/dict/web2'
    
    for line in open(path): # each line is a string 
        word = line.strip() # removes new line char
        word_clean = letters_only(word)
        if len(word_clean) >= min_length and palindrome_detector(word_clean):
            # print(word_clean)
            palindromes.append(word_clean)

    # >>> END YOUR ANSWER
    return palindromes

long_palindromes = find_long_palindromes()
if len(long_palindromes) == 0:
    print('\tNone found, or not yet implemented.')
else:
    for palindrome in long_palindromes:
        print('\t', palindrome)
        





print("""\n
######################
# Extra Exercises
######################
""")


print("""
a. Complete the function `human_number` which takes an integer `num` and
returns a string printing that number in a human-readable way.
""")
"""
Specifically, here you should handle big numbers - millions, billions, and
trillions - and return a string that prints the number to two decimal places
with that big-number word. So for instance, 4230000 should return the string
'4.23 million'. Numbers bigger than trillions should just be printed as
trillions, e.g. 4 quadrillion is just 4000 trillion.

This will require the use of if/elif/else control flow; also look at the
`round` built-in function.
"""
def human_number(num):
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE

    face = 0
    million = 1_000_000
    billion = 1_000_000_000
    trillion = 1_000_000_000_000

    if num < million:
        return str(num)
    
    if num >= million and num < 999_999_999: # handles millions
        face = round(num/million, 2)
        return str(face) + " million"
    
    if num >= billion and num < 999_999_999_999:
        face = round(num/billion, 2)
        return str(face) + " billion"
    
    if num >= trillion:
        face = round(num/trillion, 2)
        return str(face) + " trillion"

    # >>> END YOUR ANSWER

tests = [
    (987654321, '987.65 million'),
    (152637485960718293, '152637.49 trillion'),
    (6100000000, '6.1 billion'),
    (123, '123')
]

run_tests(human_number, tests)


print("""
b. Complete the function `just_add_commas` which takes an integer `num` and
returns a string giving that number with commas every three digits.
""")
"""
So an input of 123456789 would return a string '123,456,789'. Consider using
the modulo operator (%) to achieve this.
"""
def just_add_commas(num):
    # >>> YOUR ANSWER HERE
    
    num_s = str(num)
    num_reverse = list(num_s[::-1])
    # print(num_reverse)
    
    num_list = []
    for i, digit in enumerate(num_reverse):
        if i > 0 and i % 3 == 0: # steps every 3 digits
            num_list.append(',')
        num_list.append(digit)

    num_list.reverse()
    # print(''.join(num_list))
    return ''.join(num_list)

    # >>> END YOUR ANSWER

tests = [
    (1523439, '1,523,439'),
    (999, '999'),
    (5498217632, '5,498,217,632')
]

run_tests(just_add_commas, tests)




print("""
c. Where's Wally?
""")
"""
You may be familiar with the "Where's Waldo?" series of children's books, or
"Where's Wally?" as it's known in the UK. Let's define a word to be a 'wally' if
all the letters of the name 'wally' appear in the word, in order. So 'wallaby'
is a wally but 'alleyway' is not even though it contains the letters because
they're not in the right order.

Complete the below function to search through the Unix words for all the wallys.
The `break` keyword might be useful to break out of a loop once a condition is
met (e.g. looping through characters in a word, once the 'y' is found you know
it's a wally so you can stop looping.)

A variable argument `target` that defaults to 'wally' is given. If you use this
variable to determine the characters used for finding the wallys, you can try
out this function with any word instead of wally for fun!
"""

def find_wallys(target='wally'):
    # Delete pass and fill in.
    wallys = []
    # >>> YOUR ANSWER HERE
    path = '/usr/share/dict/web2'
    
    for line in open(path): # each line is a string
        word = letters_only(line.strip()).lower() # removes new line char

        i = 0 # to compare agianst target 'wally'
        for char in word:
            if i < len(target) and char == target[i]: #while we're still not end of word and chars matches
                i += 1

        if i == len(target): #if we make it to the end, word contains wally
            wallys.append(line.strip())

    # >>> END YOUR ANSWER
    # print(wallys)
    return wallys

wallys = find_wallys()
if len(wallys) == 0:
    print('\tNone found, or not yet implemented.')
else:
    for wally in wallys:
        print('\t', wally)
