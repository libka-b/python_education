# Cycles for and while

Used for iterating over lists, or for conditioned looping

## for loop

### Syntax

```python
for <iterating_variable> in <some_list>:
    do_something()
else:
    do_something_else()
```

every time you use a for loop, iterating_variable becomes an element in the list. If the element is of primitive 
type, it can be changed only by assigning new value to the list of that index. If the element type is an object
it can be modified.

## while loop

### Syntax

```python
while <condition>:
    do_something()
```

While loops are commonly used to do something until the condition is met.

## controlling loops

Loops can be controlled using keywords `continue` and `break`. 

`continue` keyword jumps to the next iterable

`break` ends the looping
