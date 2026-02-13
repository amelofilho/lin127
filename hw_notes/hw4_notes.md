# HW4 Notes

## Commands

TODO
### [`strip()`](https://www.w3schools.com/python/ref_string_strip.asp)

The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.

You can specify which character(s) to remove, if not, any whitespaces will be removed.

**Syntax:**
    
    string.strip(characters)

**Parameter Values**
|Parameter |Description|
|:-|:-|
|characters	|Optional. A set of characters to remove as leading/trailing characters|

**Example 1:**

Remove spaces at the beginning and at the end of the string:

    txt = "     banana     "
    x = txt.strip()
    print("of all fruits", x, "is my favorite")

**Output 1**:

    "of all fruits banana is my favorite"

---

**Example 2:**

Remove the leading and trailing characters:

    txt = ",,,,,rrttgg.....banana....rrr"

    x = txt.strip(",.grt")

    print(x)

**Output 2**:

    banana

TODO
### [`split()`](https://www.w3schools.com/python/ref_string_split.asp)

The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.

> Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

**Syntax:**
    
    string.split(separator, maxsplit)

**Parameter Values**
|Parameter |Description|
|:-|:-|
|separator	|Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator|
|maxsplit	|Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"|


**Example 1:**

Split a string into a list where each word is a list item:

    txt = "welcome to the jungle"

    x = txt.split()

    print(x)

**Output 1**:

    ['welcome', 'to', 'the', 'jungle']

---

**Example 2:**

Split the string, using comma, followed by a space, as a separator:

    txt = "hello, my name is Peter, I am 26 years old"

    x = txt.split(", ")

    print(x)
**Output 2**:

    ['hello', 'my name is Peter', 'I am 26 years old']

---

**Example 3:**

    txt = "apple#banana#cherry#orange"

    x = txt.split("#")

    print(x)
**Output 4:**
    
    ['apple', 'banana', 'cherry', 'orange']

---
**Example 4:**
Split the string into a list with max 2 items:

    txt = "apple#banana#cherry#orange"

    # setting the maxsplit parameter to 1, will return a list with 2 elements!
    x = txt.split("#", 1)

    print(x)
**Output 4:**

    ['apple', 'banana#cherry#orange']
---

TODO
### String Module: 
List of availabile: 
- **whitespace** -- a string containing all ASCII whitespace
- **ascii_lowercase** -- a string containing all ASCII lowercase letters
- **ascii_uppercase** -- a string containing all ASCII uppercase letters
- **ascii_letters** -- a string containing all ASCII letters
- **digits** -- a string containing all ASCII decimal digits
- **hexdigits** -- a string containing all ASCII hexadecimal digits
- **octdigits** -- a string containing all ASCII octal digits
- **punctuation** -- a string containing all ASCII punctuation characters
- **printable** -- a string containing all ASCII characters considered printable

---
### [Sets](https://www.geeksforgeeks.org/python/set-add-python/)
The set.add() method in Python adds a new element to a set while ensuring uniqueness. 
- It prevents duplicates automatically and only allows immutable types like numbers, strings, or tuples. 
- If the element already exists, the set remains unchanged, while mutable types like lists or dictionaries cannot be added due to their unhashable nature. 

**Example:**

    a = set()
    a.add('s')
    print(a)
    ​
    # adding 'e' again
    a.add('e')
    print(a)
    ​
    # adding 's' again
    a.add('s')
    print(a)

**Output:**

    {'s'}
    {'s', 'e'}
    {'s', 'e'}

---

### [Set add() Syntax](https://www.geeksforgeeks.org/python/set-add-python/)

`set.add( elem )`

- Parameter: elem is the element to be added to the set.
- Returns: It does not return anything (None).

**Ex 1:**

In this example, we have a set of characters and we use the add() method to insert a new element. 
Since sets only store unique values, adding the same element multiple times has no effect.

    a = {'g', 'e', 'k'}
    ​
    # adding 's'
    a.add('s')
    print(a)
    ​
    # adding 's' again
    a.add('s')
    print(a)

**Output**

    {'g', 's', 'e', 'k'}
    {'g', 's', 'e', 'k'}

---

**Ex 2:**

In this example, we have a set of characters and use the add() method to insert a tuple, while the update() method is used to add elements from a list. Since sets only store unique values, duplicates are ignored.

    s = {'g', 'e', 'e', 'k', 's'}
    t = ('f', 'o')
    l = ['a', 'e']
    ​
    # adding tuple t to set s.
    s.add(t)
    ​
    # adding list l to set s.
    s.update(l)
    print(s)

**Output**
    {'a', 'g', 'e', 'k', 's', ('f', 'o')}

---

**Ex 3:**
In this example, we have a set of numbers and we use the add() method to insert a new element. Since sets only store unique values, adding the same element multiple times has no effect.

    a = {6, 0, 4}
    ​
    # adding 1
    a.add(1)
    print(a)
    ​
    # adding 0
    a.add(0)
    print(a)

**Output:**

    {0, 1, 4, 6}
    {0, 1, 4, 6}
---