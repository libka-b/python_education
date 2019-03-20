def foo(a, methods=None):
    if not methods:
        methods = []
    for i in range(3):
        methods.append(lambda x: x + i)
    return sum(method(a) for method in methods)


if __name__ == "__main__":
    print(foo(0))
    print(foo(1))
