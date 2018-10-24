# Data Types

## Primitive data types

### Integer

Represent whole numbers from negative infinity to positive infinity. Any number like 1, 5,
-8, etc.

### Float

[Floating point number](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
represents any number using with some limited precision as defined in IEEE 754 standard.
Such numbers like 1.5, 1.11097, -0.981, etc.

### String

Strings are sequences of any printable characters, enclosed in single or double (not 
mixed) quotes. Anything like `"Hello world"`, `'12345'`, `"a"`, etc.

[Documentation](https://docs.python.org/3/library/stdtypes.html#str)

### NoneType

None type represents "nothing". Every variable needs to be initialized on creation,
but often you don't know the value in advance, that's where it is appropriate to choose 
None.

[Documentation](https://docs.python.org/3.2/library/constants.html)

### Boolean

Boolean is a two valued type, with values `True` and `False`. When evaluating objects 
by Booleans, 0's, False's, empty strings, empty collections and None's evaluate to False.
Non-empty, non-zero objects evaluate to True.


## Collections

We will mention only major types of collections here, as there are many more.

### List

List is an array of python objects (anything already mentioned and anything that will 
follow). It can be indexed and iterated. Elements can be inserted and removed.

[Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Tuple
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
The main difference between the tuples and the lists is that the tuples 
cannot be changed unlike lists.

[Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

### Set

Set is a collection of unique, unordered and hashable elements. Sets like in mathematics
can be intercepted, differentiated and unificated.

[Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)

### Dictionary

Dictionary is a key - value mapping.

[Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)