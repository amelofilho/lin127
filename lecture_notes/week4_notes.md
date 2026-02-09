# Lecture notes: 2/2

## a3 feedback 

### Reading files in python:

for line in open(f) vs
- reads in place
text = open(f).read()
- Uses memory; not efficient 

### guard clause
- the if line ignores all cases in words we dont care ab

    words = [.., .., ...]
    stopword = [.., .., ...]
    for word in words:
        if word in stopwords: continue

### meaningful variable names...
- be aware of clashing names with keywords, etc...

    def mean(vals):
        mean = 0 # same name as func
        for val in vals:
            mean += val
        return mean/len(vals)

### dont overload built in functions

Be careful using keywords like sum() mean() as python doesn't prevent you from rewriting built in functions/libs


### sets intro:
- unordered collection of *unique* elements

**Set Methods:**
- set()
- s.add()
- s.remove()
- &, -
- issubset(), issuperset(), union(), intersection()
- len()

### dictionary intro:
- key-value mappings
- keys must
    - be immutable (cannot be modified)
    - appear only once

**Dict methods:**
- 


### random built in module
- `random.random()` w/ nested conditionals
- probability ranges:
    - randval example
