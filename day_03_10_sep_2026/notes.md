# List
- written in '[]' 
- it stores different types of data (heterogenous)
- it is mutable
- indexing is allowed
- slicing allowed
- allowed duplicates
- dynamic in nature
- ordered (according to indexing)

```python
    l = []
    print(type(l))

    l1 = list()
    print(type(l1))

    l2 = [1, "hello", 1.3, [1,2], {2,3,4}, True, False, None, (4,5)]
    print(l2)

    l3 = [1, 2, 3]
    l3.append(56)
    print(l3)

```

## List Comprehension

- methods to solve the problem in the shortest way and most optimal way possible

---

# Questions:
1. Diff between array and list
2. Diff between array arraylist and list
3. static and dynamic array ?

---

# Tuples

- Collection of diff types of data
- represented by '()'
- immutable in nature
- ordered in nature
- slicing and indexing is allowed
- duplicates is allowed
- faster than List because speed depends on the data structure used in the particular situation and tuple is immutable and hence operations are faster due to new memory allocation for every operation (freshly)

---

# Set

- represented by '{}'
- unordered in nature
- indexing is not allowed
- slicing is not allowed
- dynamic in nature
- mutable in nature
- not allowed duplicated
- collection of diff types except dict, list and set

---

# Dictionary

- represented by '{}'
- represented in key : value pair
- any type of data is stored
- key is immutable and unique
- value is mutable and can be repeated

---

# String

- Collection of characters
- Immutable in nature
- represented by "" or '' or """
- Negative indexing is supported
- Slicing is supported