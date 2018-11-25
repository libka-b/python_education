# Files

[documentation](https://docs.python.org/3/library/functions.html#open)

syntax:
`open(file, mode="r", encoding=None)`

open file for reading:

```python
file = open("exceptions.md", "r")
for line in file.readlines():
    print(line)
file.close()
```

open file for writing:

```python
file = open("newfile.txt", "w")
file.write("Hello, ")
file.write("World")
file.write("\n")
file.close()
```

for reading file in binary, add "b" to the mode

## Context manager

It is better to use context manager implemented on opening files rather than opening / closing them 
manually

`with` statement:

```python
with open("newfile.txt", "w") as f:
    f.write("Hello, ")
    f.write("World")
```

There is no need to close the file now. The context manager takes care of it and even if there was
an unhandled exception inside the `with` block, context manager still takes care of closing the file.
