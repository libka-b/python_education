# if - elif - else statement

## Syntax

if-elif-else is used for program execution branching based on state of a program.
The syntax is simple:

```python
if <condition0>:
    do_something()
elif <condition1>:
    do_something_elif1()
elif <condition2>:
    do_something_elif2()
else:
    do_something_else()
```

`elif` and `else` are optional.

In this case, if <condition0> is evaluated to `True`, then `do_something()` is 
executed and the code is skipped right after the else. If it is evaluated to `False`, 
program continues to first elif and evaluates the second condition. And it does the 
same as in `if` part.

If program gets to the `else` part, no condition is checked and everything following 
`else` part is executed.

## Conditions

Conditions are important for branching program execution and it is crucial to 
understand them well. Conditions are always evaluated to `True` or `False` using 
comparison operators (they can be ommited in some cases).

### Operators

Number comparison operators are:

- `a < b` operator lesser than
- `a > b` operator greater than
- `a >= b` operator greater or equal to
- `a <= b` operator lesser or equal to

Equality comparison operators:

- `a == b` operator equals to
- `a != b` operator not equal to

Object equality comparison operators:

- `a is b` 
- `a is not b`

Member checking operators:

- `a in some_list`
- `a not in some_list`

Chaining conditions:

- `a == b and c < d` logical operator and
- `a == b or c > d` logical operator or

More on operators on the lesson.

[Documentation on if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
