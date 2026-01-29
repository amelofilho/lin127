# HW3 Notes


### Introduced Python Functions:

`dir()`
- lists all attributes and methods in specified module
###
    dir(string)

---
`help()`
- gives you documentation about the module, including descriptions of what each attribute contains.
###
    help(string)


---
`.upper()/.lower()`
- convers char/string types to upper/lowercase version

###
    string = 'shoe'
    string.upper()
    # out = 'SHOE'

---
`split()`
- split a string into a list where each word is a list item: `string.split(separator, maxsplit)`
- you can specify the separator; default separator is any whitespace.
    
###
    s = "hello world today"
    s.split()  # returns ['hello', 'world', 'today']`

---
`join()`

- takes all items in an iterable and joins them into one string: `string.join(iterable)`
- using **list comprehension**, we can filter characters from a list into a string
    - [expression `for` item `in` iterable `if` condition]
        - `for` item `in` iterable - loop through each item
        - `if` condition - optional filter (only include items that pass)
        - **expression** - what to put in the resulting list for each item
   

###
    string.join(iterable)

    # List Comprehension
    s = 'som4e string3'
    s_clean = ''.join([char.lower() for char in s if (char.isalpha())])
    # print(s_clean) = somestring

---
`open()`

- 
   

###
    open(/user/adriano/desktop/lin127/hw3.py)


---
`enumerate()`

- Useful for when you want to iterate using with a counter
- It does two things:
    - `i` = auto counter
    - `digit` = actual item from the list
- Without enumerate we'd have to manually create a counter before the loop (like a while loop)
- 

###
    for i, digit in enumerate(num_list):
