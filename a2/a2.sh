#!/bin/bash

echo '##########################################'
echo '#   LIN 127                               '
echo '#   Text Processing and Corpus Linguistics'
echo '#   Assignment 2                          '
echo '##########################################'
echo ''
#
# Hello there, and welcome to week 2!
#
# You may notice this week's assignment looks a bit different than last week's.
# For one thing, the file extension is '.sh' rather than '.txt'. That is because
# this file will ultimately be an executable script, that is, a program that you
# can run.
#
# Relevantly, look at the top of this file to see that it starts with an
# interesting line:
#   #!/bin/bash
# The pound+exclamation combo is called a "shebang", and in this case it
# indicates where the shell program that should be used to execute this script
# lives. /bin is a system-level folder that holds compiled programs, and of
# course bash is our favorite shell program.
#
# Lastly you'll notice that all this explanatory text is written in comments,
# which is to say lines beginning with a pound sign ('#'). The pound sign
# indicates that the line is only a comment and should not be run with the
# program. The shebang line at the top is the only exception of a line
# beginning with '#' but which is not strictly a comment.
#
# This week we'll be playing around with many tools for text processing on the
# command line, each of which will be a section with sub-questions to answer.
# I suggest that you work out the correct answers first outside of your text
# editor before adding them in here, though ultimately you'll be able to check
# your outputs by simply running this file.
#
# The main goal here will be to learn about Unix command-line programs we can
# use as filters to manipulate streams of text. Their biggest strength comes
# from the way they can be chained together with '|' (known as pipes) to process
# text one step at a time through the chain. Each problem here will potentially
# build on the previous ones - to answer these problems any commands used in
# any previous problem are fair game and potentially necessary.
#
# I'll bracket all the places in the file where you need to fill something in
# with '# >>> YOUR ANSWER HERE' and '# >>> END YOUR ANSWER. Remember though
# that you can't put your answer on either of those lines, since they start with
# pound symbols, they're comments and won't run. In a few cases your answer may
# be more than one line, but most of this assignment should be doable with
# one-liner commands.
#
# **** IMPORTANT ****
# All your answers should be in the form of commands that can be run on the
# command line. That is, don't simply write out the answer, write down the
# command you would use to find the answer. You can (and should) run this
# assignment yourself to see its output by running `bash a2.sh`. Alternatively,
# you can make this file executable by running `chmod +x a2.sh`, and then run
# it with `./a2.sh`.
#
# For questions where I'm asking you to write out a comment or idea I'll give
# you an `echo` to start. Be careful about using quotes and other special
# characters in an `echo` command - remember they may have to be escaped.
# (See TLCL Ch. 7)
#

echo '#### 0. Info'
echo ''

# When you're done, come back here and fill out these commands with your answers:
# >>> YOUR ANSWER HERE
echo 'Name: Adriano Melo Filho'
echo 'My comments or questions on the assignment are: '
# >>> END YOUR ANSWER
echo ''

echo -e '\n'
# FYI, as you saw in TLCL Chapter 7, \n is a special 'backslash escape
# sequence', so the above produces two newlines.
echo '######################'
echo '# Core Exercises (1-7)'
echo '######################'

echo -e '\n'
echo '#### 1. Preparations'
echo ''
# To start, make a directory in main course directory called 'a2' and navigate
# to it. Like you did in the week 1 assignment, download this file using `wget`
# into your a2 directory so it can be edited.
#
# As you work here, I recommend opening two terminal windows, one to hold this file
# in a text editor (nano/emacs/vim) and another to play around on the command
# line and work on the answers to these problems until you figure them out.
#
# We're going to work with some real data here, so we need to start by obtaining
# it. And we're going straight to big data! This file:
#   https://robvoigt.net/lin127/a2/shakespeare.txt
# contains the complete works of Shakespeare from Project Gutenberg, which we're
# going to play around with in this assignment.
#
# We should now be pretty familiar with `wget`; open the `man` page for `wget`,
# and figure out how to write the `wget` command to obtain that file but have it
# saved as 'shakes.txt' rather than 'shakespeare.txt'. Why not save a few
# keystrokes every time we type all our commands in this assignment?
#
# There are multiple options for output, so note that you want to be naming the
# document you're obtaining rather than the logfile or messages. Remember you
# can search a `man` page by typing '/' then your search query, and pressing
# '/'+'enter' a second time will find the next instance of your search.
echo '1.a. Obtain the complete works of Shakespeare (using wget)! Make sure to rename the file as "shakes.txt" as you download it.'
# >>> YOUR ANSWER HERE
wget https://robvoigt.net/lin127/a2/shakespeare.txt | mv shakespeare.txt shakes.txt
# >>> END YOUR ANSWER
echo ''

echo -e '\n'
echo '#### 2. wc'
echo ''
# Now you've got all of Shakespeare - nice! Last week we tried out the very
# useful program `wc` which allows us to roughly count words and lines in a
# file. Use it here with the appropriate flags to print out the answers to these
# questions.
echo '2.a. About how many lines did Shakespeare write?'
# >>> YOUR ANSWER HERE
< shakes.txt wc -l
# >>> END YOUR ANSWER
echo ''

echo '2.b. About how many words did Shakespeare write?'
# >>> YOUR ANSWER HERE
< shakes.txt wc -w
# >>> END YOUR ANSWER
echo ''

# `wc` makes a lot of assumptions in doing its calculations, does not do any
# fancy processing to remove blank space, and defines words as strings of
# characters separated by whitespace (spaces, newlines). Use `less` to look at
# the file. What might the above estimates be missing?
echo '2.c. What might be wrong about these estimates?'
# >>> YOUR ANSWER HERE
echo "[they might not be accurate because wc counts words based on whitespace, so words with punctuation or special characters might be miscounted]"
# >>> END YOUR ANSWER
echo ''



echo -e '\n'
echo '#### 3. head/tail'
echo ''
# Last week we saw `cat` which prints the entire contents of a file to standard
# output. Try `cat shakes.txt`; it'll work fine but will take a while to print
# the entire thing. You can use Ctrl-c to cut this short - a very useful tidbit!
#
# The commands `head` and `tail` can help in cases like this with big data,
# which with no arguments default to printing the first and last ten lines of
# a file, respectively, so you can see what's in it.
#
# Use `cat` and a pipe with `head`/`tail` as filters to answer questions a. and
# b. below. Starting a long piped command with 'cat filename | ' is very common
# and will be useful throughout this assignment.
echo '3.a. Print the first ten lines of shakes.txt!'
# >>> YOUR ANSWER HERE
head shakes.txt
# >>> END YOUR ANSWER
echo ''

echo '3.b. Print the last ten lines of shakes.txt!'
# >>> YOUR ANSWER HERE
tail shakes.txt
# >>> END YOUR ANSWER
echo ''

# The file starts with Shakespeare's sonnets. If you recall `less` is a program
# for viewing (but not editing) files. It has an argument that will cause it to
# display line numbers for every line. Use `man` to find that argument, then
# open the file using it to answer these questions.
echo "3.c. What line does Shakespeare's eighteenth sonnet start on in the file?"
# >>> YOUR ANSWER HERE
echo '[298]'
# >>> END YOUR ANSWER
echo ''

echo "3.d. What line does Shakespeare's eighteenth sonnet end on in the file?"
# >>> YOUR ANSWER HERE
echo '[312]'
# >>> END YOUR ANSWER
echo ''

# Both `head` and `tail` have arguments allowing you to specify a number of
# first/last lines to print rather than simply ten. You chain them together to
# print only certain parts of a file.
echo "3.e. Print the text of Shakespeare's eighteenth sonnet in one command."
# >>> YOUR ANSWER HERE
head -n 312 shakes.txt | tail -n 15
# >>> END YOUR ANSWER
echo ''

echo "3.f. How many words are in Shakespeare's eighteenth sonnet?"
# >>> YOUR ANSWER HERE
115
# >>> END YOUR ANSWER
echo ''


echo -e '\n'
echo '#### 4. grep'
echo ''
# `grep` is an extremely powerful program that allows you to filter by matching
# on a textual pattern. Specifically, `grep` uses 'regular expressions,' a very
# flexible way to specify complex patterns, which we'll spend a bunch of time on
# in a later week.
#
# For now, we'll use some of its more simple features. Giving any string of
# characters after grep will match lines containing that exact string.
echo "4.a. Print all the lines containing 'commendable'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# Remember about exactitude - `grep` will only find exactly what we're asking
# for. What about capitalized lines? Check out the `man` page for `grep` to find
# a flag for grep that allows us to ignore case.
echo "4.b. Print all the lines containing 'conspiracy' or 'Conspiracy'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# Another way to do this is to use square brackets, which allow us to
# specify a list of characters that can all match. For instance, we can use
# [Cc] in place of either 'c' or 'C' to match both.
echo "4.c. Print all lines containing 'concerning' or 'Concerning' without any flags."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

echo "4.d. How many lines in all of Shakespeare contain the string 'love'?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

echo "4.e. Print the first ten lines in the file containing the string 'love'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# Notice in the outputs of above answer that if we're just interested in the
# word 'love' rather than that string of characters, we get other stuff we
# don't want - 'loveliness', 'beloved', 'lovely', and so on.
#
# To start fixing this, recall that program arguments within quotes are
# interpreted as one argument. So try putting the query in quotes with a space
# on either side, like ' love '.
echo "4.f. How many lines in Shakespeare contain the string ' love '?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# The above approach is now likely missing out on lots of "real" cases -
# at least capitalization and 'love' followed by punctuation. Use what we've
# learned so far to modify the above command to catch as many of these as you
# can. Remember that brackets are flexible in `grep`: just like using '[Cc]' to
# match both capitalized and lowercase 'C', you can use brackets to match any
# set of characters, including punctuation, e.g. [.,!?]
echo "4.h. Approximately how many lines in Shakespeare contain the word 'love'?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# `shuf` is a simple command that shuffles the lines of the input stream. Either
# head with n=1 or a flag on `shuf` to do this problem.
echo "4.i. Print one random line containing the word 'midnight'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# Square brackets in `grep`, matching sets of characters, can also be used to
# reference ranges of characters separated by a desh, like [0-9] (digits), [a-z]
# (lowercase ascii letters), and [A-Z] (uppercase ascii letters). These can be
# composed by placing them next to each other, e.g. [A-Za-z] means all letters.
# Note this problem might require using `grep` twice.
echo "4.j. Print one random line containing at least one number and one uppercase letter."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# A very powerful feature in `grep` is the '-v' flag, which is opposite day - it
# only prints the lines that do *not* match the pattern.
echo "4.k. Print one random line which contains no uppercase or lowercase 'A's."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''


echo -e '\n'
echo '#### 5. sed'
echo ''
# `sed` is another powerful tool that stands for 'stream editor', allowing us
# to edit the incoming stream of text as it passes through `sed`. The main
# feature we will use is substitution, which looks like this:
#    sed 's/pattern/replacement/'
# The first 's' stands for substitute. We will also often do:
#    sed 's/pattern/replacement/g'
# where the final 'g' stands for 'global'. Without the 'g' it will only replace
# the first instance in a line, with it it will replace every instance.
#
# Let's make Shakespeare a little less old-timey. For this problem pipe `sed`
# twice to deal with capitalization.
echo "5.a. Print the first ten lines containing 'thy', but with every 'thy' changed to 'your'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# It'll be useful to us in a moment to use sed for some textual cleanup. '^' is
# a special character for `sed` and `grep` meaning 'the beginning of the line.'
# '*' is another one meaning 'the previous character as many times as needed.'
# So we can use `sed` to remove leading whitespace, like so:
#    sed 's/^ *//'
# Try running this on the entire file and see what it looks like:
#    cat shakes.txt | sed 's/^ *//' | less
echo "5.b. In \`sed 's/^ *//'\`, what is getting substituted with what?"
# >>> YOUR ANSWER HERE
echo '[write_out_an_answer_here]'
# >>> END YOUR ANSWER
echo ''

# Remember, '^' also means 'the beginning of the line' for `grep` too.
echo "5.c. Print all the lines of Shakespeare that start with the word 'thanks'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# `sed` also has a functionality to simply delete parts of the stream, like so:
#    sed '/pattern/d'
# where of course 'd' stands for 'delete'. '$' is yet another special character
# meaning 'the end of the line'. Using this and the information from b.,
# consider how we can delete blank lines (e.g. lines with only whitespace).
echo "5.d. How many lines is the Shakespeare file without any blank lines?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# Recall that '>' is an operator that sends the standard output stream to a
# file. Let's make a new cleaned-up file so we don't have to keep running these
# `sed` commands over and over.
echo "5.e. Use \`sed\` to make a new file called 'clean_shakes.txt' with no blank lines and no leading whitespace."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# NOTE:
# Use clean_shakes.txt for the rest of the processing in this assignment.

# Another very useful `sed` expression is to put every word on its own line,
# which we can do like so:
#    sed 's/ /\n/g'
# since '\n' is an escape character meaning 'newline', this substitutes
# every space with a line. Combining this with our ability to delete blank
# lines, replicate your answer from problem 2.b. using `wc -l` instead of
# `wc -w`. It should match exactly - keep the naive idea of "word" used by `wc`.
echo "5.f. How many words are in clean_shakes.txt (using \`wc -l\` rather than \`wc -w\`)?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''


echo -e '\n'
echo '#### 6. sort, uniq, tr, and cut'
echo ''
# `sort` simply sorts input stream lines alphabetically. Note this can take a
# second to run if the file is big (as it is in this case), and many minutes to
# run if the file is huge. Note that `sort` has a '-r' flag that reverses the
# order of the sort.
echo "6.a. Order the lines in clean_shakes.txt alphabetically, and print the last ten of them."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# `uniq` (for 'unique') is a command that de-duplicates adjacent lines that
# match exactly. Note the duplicate lines must be immediately adjacent, so
# we very frequently see `sort | uniq`.
echo "6.b. How many unique lines are there beginning with the stage direction to 'Enter'?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# `uniq` has a useful flag '-c' that counts the number of unique occurrences of
# each duplicated line. `sort` in turn has a useful flag '-n' that sorts
# numerically rather than alphabetically, so we can get sorted counts with
# `uniq` using this chain:
#    sort | uniq -c | sort -n
# Combine this with your answer from 5.f. to do this problem, again using the
# naive whitespace-separated idea of "word" used by `wc`. This answer will have
# at least 4 pipes in it.
echo "6.c. What are the top 10 most common words in Shakespeare (naive \`wc\`-style counting)?"
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# This naive definition of "word" might not be enough for us, because the above
# will see capitalized words as different, and punctuation adjacent to a word
# will be part of it too, so 'hi' and 'hi!' and 'Hi' will all be different.
#
# For this we can use `tr`, which strands for translate. `tr` is like a
# streamlined version of `sed` for certain operations, in particular
# manipulating some classes of characters. `tr` can accept sets of characters in
# square brackets like `grep` (e.g. [A-Z]) as well as a few special named
# classes like '[:punct:]'. The most useful operations will be these:
#    tr '[A-Z]' '[a-z]'
#    tr -d '[:punct:]'
# The first command takes all uppercase characters and makes them the
# corresponding lowercase one; the second command deletes all characters from the
# "punctuation" class. Add these into your command from above to make the answer
# even better!
echo "6.d. Save an ordered list of all the words in Shakespeare with their counts (smarter counting) to a file called 'word_counts.txt'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''

# This is still not perfect. Take a look at the file and think about how.
echo "6.e. We fixed a bunch of problems - with this method, what new ones did we create?"
# >>> YOUR ANSWER HERE
echo "[write_out_an_answer_here]"
# >>> END YOUR ANSWER
echo ''

# `cut` is a useful command to extract pieces of a line. Key flags to know are:
#   '-f' followed by an integer, representing which field(s) to print.
#   '-d' followed by a character representing the 'delimiter' which will split
#        the line. for clarity it's good to surround this character in single
#        quotes, and doing so is necessary if you want the delimiter to be a
#        special character like a blank space.
# For instance, if we do:
#    cut -f 3 -d ',' file.txt
# This will take every line in file.txt, cut the line up at every comma, and
# print the third comma-separated chunk. We can make the delimiter a ' ' too,
# use that here. This problem should only be a minor modification on 6.d.
echo "6.f. Use \`cut\` to extract the first words from each line, and save an ordered list with counts to a file called 'firstword_counts.txt'."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''


echo -e '\n'
echo '#### 7. Scripting'
echo ''

# Rob talked about abstraction and decomposition in class. As you've built the
# long pipelines in the previous sections of the assignment, you've built up
# ever more abstract mini-systems that achieve a high-level goal through the
# combination of many small goals.
#
# This file is a script; scripts in bash run series of bash commands to achieve
# some larger goal. You should mostly be able to complete this section by copy-
# pasting answers from earlier sections (into new files). There is a lot more
# detail on the topic of scripting in TLCL Ch. 24, if you want more info.
#
# In this section you'll make some scripts that abstract away from the work
# we've already done. To start, you'll make a new text file in this same
# directory called 'clean_text.sh'. The first line should be exactly like the
# first line of this file, like so:
#    #!/bin/bash
#
# Now write out your commands from above that produced clean_shakes.txt in 5.e.
#
# An important note is that positional arguments can be referred to in scripts
# with "$N", where N is a number showing its position. So if we have a script
# that is run like:
#    my_script.sh filename.txt
# Inside the script, if we use "$1" this will refer to filename.txt. So if in
# your original command you started with `cat shakes.txt`, here you can do:
#    cat "$1" | etc etc
#
# Save the output of the script to a file called clean_"$1". This again will
# substitute the argument name, so if you pass it 'shakes.txt', it will save to
# 'clean_shakes.txt'.
#
# Lastly, you have to make the file executable. Once it's written, exit your
# text editor and run:
#    chmod +x clean_text.sh
# This allows you to run the command by doing './clean_text.sh'.
echo "7.a. Create and run the file clean_text.sh."
# When you've made your script, remove the leading hash below.
# ./clean_text.sh shakes.txt
echo ''


# Now make another script called 'word_counts.sh', that replicates what you did
# in problem 6.d., taking in clean_shakes.txt and saving the sorted wordlist
# with counts to 'word_counts.txt'.
echo "7.b. Create and run the file word_counts.sh."
# When you've made your script, remove the leading hash below.
# ./word_counts.sh clean_shakes.txt
echo ''


# Finally, make a new script called 'process_text.sh' that *uses your previous
# scripts* to do all this processing in one go.
echo "7.c. Create and run the file process_text.sh."
# When you've made your script, remove the leading hash below.
# ./process_text.sh shakes.txt
echo ''


# When you run this file, it should reproduce the entire pipeline, re-generating
# clean_shakes.txt and word_counts.txt.


# Good job, you finished the core exercises! Remember that this file is itself
# a script. So let's do one last thing. Run this entire script, and save the
# output to a file called assignment_output.txt.
echo "7.d. Run your a2.sh file and save its output to assignment_output.txt"
# Don't put this command here - just run the necessary command in your shell.


######################
# Extra Exercise (8)
######################

echo -e '\n'
echo '#### 8. Unix for Poets'
echo ''

# Ken Church's "Unix for Poets" is linked on the course website under this
# week's. In it, he provides an alternative way to extract words, and then some
# additional commands that allow you to extract bigrams and trigrams (two- and
# three-word phrases). Use his techniques to do this problem. This will require
# multiple steps and saving intermediate files.
echo "8.a. Save a list of the most common bigrams and trigrams in Shakespeare to bigram_counts.txt and trigram_counts.txt, respectively."
# >>> YOUR ANSWER HERE

# >>> END YOUR ANSWER
echo ''
