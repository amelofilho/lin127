#######################################
#   LIN 127
#   Text Processing and Corpus Linguistics
#   Assignment 4
#######################################

"""
This week we'll keep working on basic programming paradigms for text processing:
loops, building up strings and lists, tokenization, and reading text files.
We'll also play with two new and useful data types, the `set` (a set of unique
items) and the `dict` (an extremely versatile key-value mapping type).

We've already seen some built-in functions in Python, that is, pre-defined functions
that you can call at any time like `print` and `dir`. Python also has built-in
modules, where a module is a nicely packed-up set of code that someone else has
written and made available others to use.

We already briefly saw the `string` module, which makes available useful
attributes for working with strings like string.punctuation and
string.ascii_letters. We'll keep working with that this week and add several
exercises playing with the `random` module as well.
"""
import string
import random, math

"""
*** IMPORTANT NOTE ***
One thing that will come up multiple times throughout this assignment is working
with reading in files. For the moment there are three main ways we'll want to do
this. Assume we have a file path as a str `f`.

First we can do `for` loop to directly iterate over lines in the file, e.g.:
    for line in open(f):
Note that each line will have whitespace on the end, a '\n' character! So keep
in mind we will often want to use `.strip()` to remove this and other
surrounding whitespace on a line.

Secondly, if we want to keep all the lines in a list, we can directly do:
    lines = open(f).readlines()
Now `lines` will be a list of strings with the lines in the file, still each
with a '\n' on the end.

And finally if we do *not* want lines but want the entire text of the file as a
string, we can do:
    text = open(f).read()
Again this will maintain whitespace, but `text` will simply be one long string.
You can break that string into the equivalent of open(f).readlines() by doing:
    lines = text.split('\n')

To do these problems you will need to be thoughtful about what sort of format
you want to be working with.
"""



print("""
-----------------------------------------
#### 0. Info
""")

"""
As usual please do this part by filling in the string variables below once
you've completed the assignment.
"""

# >>> YOUR ANSWER HERE
name = 'Adriano Melo Filho'
comments_or_questions = """
[I got a good chuckle on the last activity reading the snippets coming together. Fun stuff!]
"""
completed = True
# >>> END YOUR ANSWER

print('Name: ' + name)
print('Comments or questions: ' + comments_or_questions)
print('Completed: ' + str(completed))

"""
We'll make the same testing function available as in the last assignment; no
need to edit this or look too much at it, just here to produce helpful output.
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
#### 1. Introducing Old Friends to New Ones
""")
"""
In week 2 we worked with tools like grep, sed, and tr to do basic text
processing tasks like tokenizing and counting words. We'll replicate some of
that functionality here, and go a bit beyond it!

*** IMPORTANT NOTE ***
Put a new version of the Shakespeare file in this directory, whether by copying
it from your a2 folder or downloading a fresh copy and renaming it
again to 'shakes.txt':
    https://robvoigt.net/lin127/a2/shakespeare.txt

Note that in this assignment each function will have what's called a "docstring"
at the top under the function definition, which is a longer comment that
explains the inputs and outputs to the function and what it's intended to do.
They'll be in the numpy format - you don't need to know the details, hopefully
it's self-explanatory to read (which is the point!), but if you're interested
more information is here:
    https://numpydoc.readthedocs.io/en/latest/format.html
"""

import os
if not os.path.exists('shakes.txt'):
    print('\tPlease download the Shakespeare file again to this directory and name it shakes.txt.')
    exit(0)

print("""
a. Complete the function `wc_lines` to re-implement the equivalent of `wc -l`.
""")
"""
There is one twist here, however. We will use an optional argument to allow
removing lines from the count that have only whitespace on them. You can make
an argument optional by assigning it a default value. This is done for you:
notice below in the function defintion that the default value for `remove_blank`
is False.

Blank lines are defined as those for which `line.strip() == ''` is True. That
is, those for which only the empty string '' remains after running the
'.strip()' method, which strips all whitespace from either side of the string.

A reminder that the tests here assume you have 'shakes.txt' in the current dir.
You'll notice from the tests that our answers should match exactly what we
got in Assignment 2 from `wc -l` and `sed '/^ *$/d' | wc -l` respectively.
"""
def wc_lines(f, remove_blank=False):
    """Read in file at path `f` and return its line count.

    Parameters
    ----------
    f : str
        The path of the file to line count.
    remove_blank : bool, optional
        Whether or not to remove blank lines from the file.

    Returns
    -------
    int
        The number of lines in the file.
    """
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    
    count = 0
    if (remove_blank):
        for line in open(f):
            if line.strip() == '':
                continue
            else:
                count += 1
    else:
        for line in open(f):
            count += 1

    # otherwise...
    lines = open(f).readlines() # returns list of each line
    print("There are %d lines" % (count))
    return count
    
    # >>> END YOUR ANSWER

tests = [
    # (('sample.txt'), 23),
    (('shakes.txt'), 122458),
    (('shakes.txt', True), 112902),
]
run_tests(wc_lines, tests)



print("""
b. Complete the function `tokenize` to implement a simple word tokenizer, which
takes a string and returns a list of words.
""")
"""
Specifically you should tokenize in a manner analogous to how we did in A2:
 - remove surrounding whitespace with `strip()`
 - lowercase the string
 - split into tokens on whitespace
 - `strip` off all punctuation on either side of the token
   (as defined by string.punctuation)
 - remove tokens that are blank (e.g. when token == '')
Different than A2, though, punctuation inside the word should remain, like
the single quote in "I'll".
"""
def tokenize(s):
    """Break str `s` into a list of str representing word tokens.

    Parameters
    ----------
    s : str
        The string to tokenize.

    Returns
    -------
    list of str
        A list of tokenized words in the string.
    """
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE

    clean_s = s.strip().lower().split() # clean/split entire string
    # print(clean_s)
    tokens = []
    for token in clean_s:   # work on each token indiv...
        clean_token = token.strip(string.punctuation)
        if clean_token != '':
            tokens.append(clean_token)
        # print("%s -> %s where length = %i" % (token, clean_token, len(clean_token)))
        
        # print(token.strip(string.punctuation))
    
    return tokens
    # >>> END YOUR ANSWER
    

tests = [
    ('ZOOLOGISTS ID MYSTERIOUS FUNGUS-KILLING FROGS', ['zoologists', 'id', 'mysterious', 'fungus-killing', 'frogs']),
    ("I'm absolutely freakin' out over this!!!", ["i'm", 'absolutely', 'freakin', 'out', 'over', 'this']),
    ("    This?' is A   -badly-punctuated ?SENTENCE...", ['this', 'is', 'a', 'badly-punctuated', 'sentence']),
    ('"Moshi Moshi? Is anyone there?", she ventured cautiously.', ['moshi', 'moshi', 'is', 'anyone', 'there', 'she', 'ventured', 'cautiously'])
]
run_tests(tokenize, tests)


print("""
c. Complete the function `wc_words` to re-implement the equivalent of `wc -w`.
""")
"""
No need for optional arguments here, but again notice that this should exactly
match what we got from `wc -w`. Use your `tokenize` function to do this! Don't
overthink it, this should be only a few lines.
"""
def wc_words(f):
    """Read in file at path `f` and return its word count.

    Parameters
    ----------
    f : str
        The path of the file to word count.

    Returns
    -------
    int
        The number of words in the file.
    """
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    word_count = 0
    for line in open(f):
        word_count += len(tokenize(line))
    
    # print("Word count: %d" % word_count)
    return word_count
    # >>> END YOUR ANSWER

tests = [
    ('shakes.txt', 882996)
]
run_tests(wc_words, tests)


print("""
d. Complete the function `vocabulary_size` to count how many unique words appear
in a file.
""")
"""
The command-line equivalent of this would be to split the words of a file onto
separate lines and run `sort | uniq | wc -l`. Here, however, it will be much
simpler.

Remember from class that a set is like a list of only unique items. So we can
use our tokenizer to get all the words into a list, then cast that list to a
`set` to remove duplicates, and return the set's size with `len`.

Your answer here should ideally only be a very small modification on the
previous problem.
"""

def vocabulary_size(f):
    """Read in file at path `f` and return its vocabulary size (number of unique
    word types that appear).

    Parameters
    ----------
    f : str
        The path of the input file.

    Returns
    -------
    int
        The number of word types appearing in the file.
    """
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    unique_words = set()
    for line in open(f):
        for word in tokenize(line):
            unique_words.add(word)
    # >>> END YOUR ANSWER

    print(len(unique_words))
    return len(unique_words)

tests = [
    ('shakes.txt', 28920)
]
run_tests(vocabulary_size, tests)



print("""\n
-----------------------------------------
#### 2. Dabbling with Dictionaries
""")
"""
In Chapter 11 of Think Python we read about dictionaries, an extremely powerful
data type we will use over and over again. Dictionaries are constituted by
key-value pairs, where a given key (which could be a string, int, float, or
bool, but for us most commonly a string) maps to a value, which can itself be a
complex data type - even another dictionary! Here we'll see how useful this
paradigm can be to organize data.
"""

print("""
a. Complete the function `word_counts` to accumulate counts for each word in a
string.
""")
"""
As computational linguists, one of the most common functions we might use a
dictionary for is word counting. Here we want to accumulate separate counts for
each word that appears in a (potentially long) string, and use the words as
str *keys* that map to int *values* representing how many times the word
appeared.

So given a trivial example string like this:
    'a a b a b b c a'
We want to accumulate a dictionary that would look like this:
    {'a': 4,
     'b': 3,
     'c': 1}

One crucial point here is that initially, the dictionary will have no keys.
Therefore for every word we have to check whether it appears in the dictionary
already. If it doesn't appear, we have to assign it a starting value of the
correct type (in this case an integer of 0 or 1, depending on how you structure
your code). We can check this with a conditional using the keyword `in`, e.g.:
    if word not in counts:
        # create an entry for word in counts with a starting value

If it does appear, we can simply index into the dictionary using the word as we
would use an integer to index into a list (e.g. counts[word]) and use an
accumulator to increment the value (e.g. += 1).
"""
def word_counts(s):
    """Tokenize the str `s` and accumulate counts for each word that appears
    in a dictionary.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    dict of { str : int }
        Word counts in the string, with words as keys and their corresponding
        counts as values.
    """
    # Delete pass and fill in your function.
    counts = {}
    # >>> YOUR ANSWER HERE
    
    # print(tokenize(s))

    tokens = tokenize(s)

    if len(tokens) == 0:
        return {}

    for word in tokens:
        if word not in counts:  # first time seeing token
            counts[word] = 1
        elif word in counts:    # other occurances
            counts[word] = counts.get(word, 0) + 1 # add 0 argument for empty key values
        else:
            continue

    # >>> END YOUR ANSWER
    return counts

tests = [
    ('a a b a b b c a', {'a': 4, 'b': 3, 'c': 1}),
    ('I wish to wish the wish you wish to wish', {'i': 1, 'wish': 5, 'to': 2, 'the': 1, 'you': 1}),
    ('      ', {}),
    ("RaZzLe dAzZlE", {'razzle': 1, 'dazzle': 1})
]
run_tests(word_counts, tests)


print("""
b. Complete the function `letter_counts` to accumulate counts for each letter in
a string.
""")
"""
This is analogous to the above, but should work by directly looping over the
characters in the string rather than tokenizing. You should first lowercase the
string, and only accumulate counts for letters (e.g., string.ascii_lowercase).
"""
def letter_counts(s):
    """Tokenize the str `s` and accumulate counts for each word that appears
    in a dictionary.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    dict of { str : int }
        Letter counts in the string, with characters as keys and their
        corresponding counts as values.
    """
    # Delete pass and fill in your function.
    counts = {}
    # >>> YOUR ANSWER HERE

    tokens = tokenize(s)
    # print(tokens)
    
    for word in tokens:
        for letter in word:
            # print(letter)
            if letter not in counts:
                counts[letter] = 1
            elif letter in counts:
                counts[letter] = counts.get(letter, 0) + 1
            else:
                continue
                
    # >>> END YOUR ANSWER
    return counts

tests = [
    ('a a b a b b c a', {'a': 4, 'b': 3, 'c': 1}),
    ('I wish to wish the wish you wish to wish', {'i': 6, 'w': 5, 's': 5, 'h': 6, 't': 3, 'o': 3, 'e': 1, 'y': 1, 'u': 1}),
    ('      ', {}),
    ("RaZzLe dAzZlE", {'r': 1, 'a': 2, 'z': 4, 'l': 2, 'e': 2, 'd': 1})

]
run_tests(letter_counts, tests)

print("""
c. Complete the function `proportion_of_oneoff_types` to calculate how many word
types in a dictionary of counts appeared only once.
""")
"""
You may have heard of Zipf's Law, in computational linguistics known as the
conjecture that when word types are sorted by frequency, those frequencies
decline exponentially, so the most common words appear many many times more
frequently than the least common words.

One corrolary of this is that in any large body of text, a substantial
proportion of the word types will only occur once. In this function we'll
calculate just how many in an example corpus like Shakespeare.
"""
def proportion_of_oneoff_types(d):
    """Given a dictionary of word counts `d` return the proportion of word types
    that only occurred once.

    Parameters
    ----------
    d : dict of { str : int }
        A dictionary of counts such as generated by `word_count`

    Returns
    -------
    float
        # of keys that have a value of 1 / total # of keys
    """
    # Delete pass and fill in your function.
    # >>> YOUR ANSWER HERE
    single_word_count = 0
    for key, value in d.items():
        if value == 1:
            # print(key)
            single_word_count += 1

    result = single_word_count/len(d)
    # print("Unique Words: %d \nRatio: %f" % (len(d), result))
    return result
        
    # >>> END YOUR ANSWER

try:
    tests = [
        ({'a': 4, 'b': 3, 'c': 1}, 0.3333333333333333),
        ({'testing!': 1, 'teeesting!': 1}, 1)
    ]
    run_tests(proportion_of_oneoff_types, tests)
    # raw_prop = proportion_of_oneoff_types(word_counts(open('shakes.txt')))
    raw_prop = proportion_of_oneoff_types(word_counts(open('shakes.txt').read()))
    if raw_prop is not None:
        prop = round(raw_prop, 4) * 100
        print("\t{}% of word types in Shakespeare only appear once.".format(prop))
except Exception as error:
    import traceback, sys
    traceback.print_exc(file=sys.stdout)


print("""\n
-----------------------------------------
#### 3. That's, Like, Soooo Random!!!
""")
"""
The `random` module provides functionality for generating randomness, which can
be surprisingly useful for things like taking random samples, or simulating
outcomes. We'll play with some of its functionality here.

FYI, this section will have custom (and sometimes fuzzy) tests because of the
inherent random nature of what your work will generate!
"""


print("""
a. Complete the function `dice_simulation` to calculate the outcomes of
successive rolls of two dice.
""")
"""
Last week we rolled the dice, but it was hardly a real roll - we had to provide
the numbers! This week we'll go big and simulate thousands of actual dice rolls.

Look up and use the `random.randint` function to generate simulated rolls for
two dice, and calculate how frequently different outcomes occur.
"""
def dice_simulation(n_rolls=10000):
    """Simulate rolling two dice int `n_rolls` times, and return a dictionary
    counting the number of occurrences of their possible sums.

    Parameters
    -------
    n_rolls : int
        The number of times to roll both dice.

    Returns
    -------
    dict { int : int }
        Dictionary mapping dice roll sums to count of occurrences of that sum.
    """
    # Delete pass and fill in.
    # >>> YOUR ANSWER HERE
    
    roll_outcomes = {}

    for i in range(n_rolls):
        sum = random.randint(1,6) + random.randint(1,6)

        if sum not in roll_outcomes:
            roll_outcomes[sum] = 1
        elif sum in roll_outcomes:
            roll_outcomes[sum] = roll_outcomes.get(sum, 0)  + 1
        else:
            continue
    
    # print(roll_outcomes)
    return roll_outcomes

    # >>> END YOUR ANSWER

def test_dice_simulation():
    counts = dice_simulation(5000)
    try:
        assert(sum(counts.values()) == 5000)
    except:
        print("\tError: dice roll counts didn't sum to the number of rolls")
        return
    try:
        assert( math.fabs((counts[7] / 5000) - 0.166) < 0.02 )
        assert( math.fabs((counts[11] / 5000) - 0.055) < 0.02 )
        print("\tWorked out, and the numbers looked reasonable!")
        print("\t\tProbability of sum 7: ", counts[7] / 5000)
        print("\t\tProbability of sum 11: ", counts[11] / 5000)
    except:
        print("\tError: the counts didn't come out making sense...")
        print("\t\tProbability of sum 7: ", counts[7] / 5000, '\t(should be near 0.166)')
        print("\t\tProbability of sum 11: ", counts[11] / 5000, '\t(should be near 0.055)')
test_dice_simulation()

print("""
b. Complete the function `random_word_generator` which produces simple nonce
words.
""")
"""
Nonce words - one-time-use nonsense words - have a long history in linguistics
because they allow us to test how people interpret words based on context or
usage even with no prior knowledge of their meaning. The most famous of these
has to be Jean Berko Gleason's "Wug" which is the nonce name of a cartoon bird
used in her language acquisition experiments.

Here you'll generate nonce words of the forms V, CV, VC, or CVC, where C stands
for consonant and V stands for vowel. Simply put, every word will have one
vowel, which may or may not have a consonant on either side.

To do this, use two functions of the `random` module. The first is simply:
    random.random()
This generates a random number between 0 and 1. You can use this in a
conditional to have an event happen with a certain probability, e.g.:
    if random.random() < 0.7: # will be True 70% of the time

The second is:
    random.choice(seq)
Which chooses one random element from a sequence.
"""
def random_word_generator():
    """Generate a random V, CV, VC, or CVC word.
    Words should be one V 30% of the time, CVC 40% of the time, and then split
    equally between CV and VC the rest of the time (15% each).

    Returns
    -------
    str
        A nonce word.
    """
    # Delete pass and fill in.
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # >>> YOUR ANSWER HERE

    word = []
    p = random.random()
    if p < 0.3: # generates a single V
        word.append(random.choice(vowels))
    elif p < 0.7:
        word.append(random.choice(consonants))
        word.append(random.choice(vowels))
        word.append(random.choice(consonants))
    elif p < 0.85:
        word.append(random.choice(consonants))
        word.append(random.choice(vowels))
    else:
        word.append(random.choice(vowels))
        word.append(random.choice(consonants))


    # print(''.join(word))
    return ''.join(word)
    # >>> ENG YOUR ANSWER
# random_word_generator()


# Loooong custom testing function, no need to read this
def test_random_word_generator():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    def convert_to_cvc(s):
        cvc = ''
        for c in s:
            if c in vowels: cvc += 'V'
            elif c in consonants: cvc += 'C'
            else: return '[other]'
        return cvc
    templates = {'V':0, 'CV': 0, 'VC': 0, 'CVC': 0}
    words = []
    for i in range(10000):
        word = random_word_generator()
        words.append(word)
        cvc = convert_to_cvc(word)
        if cvc == 'O':
            print("\tGot an output with characters other than consonants or vowels")
            return
        templates[cvc] += 1
    fail = False
    try:
        assert set(templates.keys()) == set(['V','CV','VC','CVC'])
    except:
        print("\tError: didn't fit the templates, got these:", ' '.join(templates))
        fail = True
    try:
        assert 3700 < templates['CVC'] < 4300
        assert 2700 < templates['V'] < 3300
    except:
        print("\tError: the probabilities didn't make sense")
        print('\t\tprobabilities: ', '  '.join(t+ " " + str(round(templates[t]/10000,2)) for t in templates))
        fail = True
    if not fail:
        print("\tTried 10,000 nonce words and they looked reasonable!")
    print('\t\tsample outputs: ', ' '.join(random.sample(words, k=10)))
if random_word_generator():
    test_random_word_generator()
else:
    print("\tNot yet implemented.")

print("""
c. Complete the function `random_qa_generator` which produces short
nonce question-and-answer pairs.
""")
"""
Many languages display some amount of syntactic movement in questions, where the
syntactic ordering of constituent words is different in a question versus a
statement. We'll take that to an extreme here by generating questions and
answers using the same words but with random ordering.

To do this we'll use `random.shuffle`, which shuffles a list randomly.
Importantly `random.shuffle` shuffles a list *in-place*, which means it does not
return anything but rather changes the order of an existing list.

So here you should generate a list of words between three and five tokens long,
generate a question string with it, shuffle the list, and generate an answer
string. With a 50% chance the answer can lose one of the words in the question,
and it should be prepended with one additional random word and a comma.

Here's two examples my answer generated:
      a. Neh gow e u zir?              	b. Ce nub giy ah waj?
         Gej, neh gow zir e.               E, giy nub ah ce!

Almost sounds like they could be from a real language, right? It's kind of
amazing how easy it is for us to project meaning onto these meaningless
collections of letters!
"""
def random_qa_generator():
    """Generate a nonce question and answer pair. Rules:
    - Question is randomly three to five words long, ending in a question mark.
    - Answer is made up of the same words shuffled in a random order.
    - With an equal probability the answer ends in a period or an exclamation mark.
    - With a 50% chance the answer loses one of the words from the question.
    - Answer starts with one additional random word and a comma.

    Returns
    -------
    question : str
        A nonce question.
    answer : str
        The nonce answer.
    """
    question = ''
    answer = ''
    # Delete pass and fill in.
    # >>> YOUR ANSWER HERE

    words = [] # keep track of words generated for question
    question = random_word_generator() # first word in question
    
    n = random.randrange(3, 4 + 1)
    for i in range(n): # add remaining 3-4 words
        new_word = random_word_generator()
        question = question + " " + new_word
        words.append(new_word)
    
    question = question.strip() + "?" # remove last added gap
    
    # first word in answer
    answer = random_word_generator() + ","
    p = random.random()
    if p < 0.5:
        i = random.randint(0, len(words) - 1)
        words.pop(i)
        
    random.shuffle(words)
    for word in words: # add 3-4 words
        answer = answer + " " + word
    
    answer = answer.strip() + random.choice(".!") # remove last added gap

    # >>> END YOUR ANSWER
    return question.capitalize(), answer.capitalize()

question, answer = random_qa_generator()
if question == answer == '':
    print('\tNot yet implemented.')
else:
    print('\tSample babbling convos:')
    for i in range(3):
        question, answer = random_qa_generator()
        print('\t\tQ: ', question, '\n\t\tA: ', answer, '\n')


print("""
d. Complete the function `monkeys_typing_shakespeare` to generate snippets of
Shakespeare-y text.
""")
"""
Finally let's use the `random.sample` method to generate Shakespearean snippets.
Here's a sample my function generated:

    "is shall? my they acts if undergo now his, proceed my cousin, foulness the
     heaven's for without bide muffle. before is love do? the me. dance i!"

To do this all we have to do is tokenize our Shakespeare file and sample from
the tokens. Again kind of surprising how almost-maybe-reasonable this randomness
can seem!
"""
def monkeys_typing_shakespeare():
    """Generate snippets of text with whitespace-separated words occurring
    according to their prevalence in Shakespeare. Snippets should be randomly
    between 20 and 40 words in length. After each word in the snippet with
    probability 10% add one of ',.!?' for punctuation, and every time add one
    of '.!?' at the end.

    Returns
    -------
    str
        A sample of Shakespeare-y text.
    """
    # Delete pass and fill in.
    # >>> YOUR ANSWER HERE
    
    tokens = []
    for line in open('shakes.txt'):
        if line == '':
            continue
        else:
            tokens.extend(tokenize(line))

    all_words = [word for word in tokens if not word.isdigit()] # remove digits
    # print(all_words)
    
    sample_words = random.sample(all_words, random.randint(20, 40))
    # print("\nSample words: %d" % random.randint(20, 40))
    # print(sample_words)

    snippet = []
    for i in range(len(sample_words)): # go through all sampled words
        p = random.random()
        if p < 0.1:
            snippet.append(sample_words[i] + random.choice(',.!?'))
        else:
            snippet.append(sample_words[i])
    
    result = ' '.join(snippet).capitalize()
    result += random.choice('.!?') # always end in one of these
    # print(result)
    return result
    # >>> END YOUR ANSWER HERE

# monkeys_typing_shakespeare()
for i in range(2):
    output = monkeys_typing_shakespeare()
    if output:
        print("\tHere's a few snippets of what the monkeys came up with:\n")
        import textwrap
        for i in range(3):
            output = monkeys_typing_shakespeare()
            print(textwrap.indent('\n'.join(textwrap.wrap(output, width=50)),'\t'))
            print('')
    else:
        print('\tNot yet implemented.')


# print("""\n
# ######################
# # Extra Exercises
# ######################
# """)
# print("""
# a. Complete the function `smarter_monkeys_typing_shakespeare` which generates
# even more reasonable random Shakespeare-y text.
# """)
# """
# What we just built in the previous problem is a kind of language model.
# Specifically, we it's roughly a unigram language model. Unigram refers
# to the idea that we are sampling single ("uni") words ("gram") in
# proportion to how frequently they appear in the original text.

# For this problem, I challenge you to build an analogous bigram language
# model. This might be a tricky one! What this means is now we have to sample
# pairs ("bi") of words ("gram") in proportion to the sequential probabilities
# wwith which they appear in the original text.

# There are a boatload of ways you could do this, and if you're interested
# in learning more you should absolutely read the N-Gram Language Modeling
# chapter of the Jurafsky and Martin book (Speech and Language Processing).

# But for this simple case, here's my suggestion: use a nested dictionary.
# The dictionary should hold counts for how many types those keys appeared
# in sequence. So for example, if the dictionary is called `bigrams`,
# `bigrams['this']['place']` should hold the counts for how frequently
# 'place' followed 'this' in Shakespeare. Note that when you're making this
# dictionary, each time a word first appears you'll need to set its value to
# a fresh, second-level empty dictionary. E.g., `bigrams['this'] = {}`.

# For this exercise I would simply first tokenize the Shakespeare file, and
# then iterate over it to build such a dictionary. Then when it comes time
# to generate text, for the first word in each sentence sample randomly from
# all the Shakespeare tokens (as in the last problem), but for every other word,
# sample it in proportion to all the words that could follow the one you just
# chose. You can do this with weighted sampling using `random.choices` - look
# it up! - where the weights are the counts in the nested dictionary starting
# with the previous word.

# Check out how this relatively simple change from unigrams to bigrams
# changes things - is it more comprehensible or "Shakespearean"?
# """

# def smarter_monkeys_typing_shakespeare():
#     """Generate snippets of text with whitespace-separated words occurring
#     according to their bigram prevalence in Shakespeare. Snippets should be
#     randomly between 2 and 4 sentences in length. Each sentence should start
#     with a word according to its unigram probability (e.g. sampled from all
#     Shakespeare tokens), and thereafter each word should appear in proportion
#     to its bigram probability. After each word in the snippet with
#     probability 10% add a comma, and with probability 5% add a sentence-ending
#     punctuation (e.g. one of '.!?'), after which move on to the next sentence.

#     Returns
#     -------
#     str
#         A sample of Shakespeare-y text.
#     """
#     # Delete pass and fill in.
#     # >>> YOUR ANSWER HERE
#     pass
#     # >>> END YOUR ANSWER HERE

# output = smarter_monkeys_typing_shakespeare()
# if output:
#     print("\tHere's a few snippets of what the brainy monkeys came up with:\n")
#     import textwrap
#     for i in range(3):
#         output = smarter_monkeys_typing_shakespeare()
#         print(textwrap.indent('\n'.join(textwrap.wrap(output, width=50)),'\t'))
#         print('')
# else:
#     print('\tNot yet implemented.')
