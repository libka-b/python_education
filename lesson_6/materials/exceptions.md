# Exceptions

In large projects we need to handle unexpected inputs in order to avoid program crash in middle of its 
execution

Several trivial examples:

TypeError
```python
>>> a = 5
>>> for i in a:
...     a += 1
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

KeyError
```python
>>> my_dict = {}
>>> a = my_dict["awesome_key"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'awesome_key'
```

ValueError
```python
>>> b = [1, 2, 3]
>>> b.index(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 5 is not in list
```

[Documentation](https://docs.python.org/3/tutorial/errors.html)

## Exception handling

syntax:

```python
try:
    block of critical code
except MyAwesomeError as e:
    do something when the code raise an exception
else:
    do something when the code didn't raise an exception'
finally:
    something that will always be done
```

Some examples how to fix previous code

## Exception raising

```python
class MyAwesomeError(Exception):
    pass
```

usage:
```python
def sort_array(array: list):
    if not isinstance(array, list):
        raise MyAwesomeError("Input array must be of type list!")
        
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
```
