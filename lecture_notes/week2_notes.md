# Notes 1/12

### Commands:

- tree
    - prints structure of dir 
- wc
    - word, char, line count, etc

### Notes from HW1:

- Use the specific naming conventions from assignment
    - no spaces, etc
- answer between `>>> start` and `>>> end` 
- wc returns the number of `<newline>` chars, aka `\n`
    - this is how it counts lines
    - try `-S` and `-N` flags on `less`
- Dotfiles (.bashrc and .nanorc)
    - Save us from doing repetivtive tasks 
    - bash/nano
    - good to store hidden files (config, persistant mem)
- Errors
    - are good; gives useful information
    - `rm: cannot remove 'this': Is a directory`
        - Each part (seperated by :) tell what/where it went wrong
- Tab completion (use it)
    - Can be used for finishing **command** or **argument**
- Vim vs Emacs vs Nano
- Undo button on terminal?
    - nope; if you `rm`, everything's gone
    - he explained filesystem allocation a little bit (file name is allocating a section of vmem)
- Emacs backup (if you used emacs)
    - Emacs stores backup files when you create them
    - Vims doesn't do this.
    - [Emacs manual](https://emacsredux.com/blog/2013/05/09/keep-backup-and-auto-save-files-out-of-the-way/)
###
    assignment 1.txt   # real file
    assignment 1.txt~  # backup
    #assignment 1.txt#   # auto-save file

- Text editors vs GUI (VsCode)
    - Editors are stable, time saving, ubiquitous, permanent, remote-able, lightweight, open-source
- Experience Levels
    - Check out links for extra practice
        - [Bash Tutorial Website (YSAP)](https://ysap.sh/)
- AI Policy
    - Use duckduck go 


### Week 2 Concepts

#### Unix:

- Unix operates line by line
    - We're creating a pipeline where order matters (command order)
    - Class Clay Example:
        - We want a random line with at least one num and uppercase letter
        - **Prof Strat**: Carve away at original body of data (clay)
            1. We remove all the lines that don't contain what we're looking for 
    - Unix Philosophy:
        - One program does one thing:
            - Write 
- Abstractions
- Decomposition


