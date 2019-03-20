def foo(a, methods=[]):
    for i in range(3):
        methods.append(lambda x: x + i)

    sum_methods = 0
    for method in methods:
        sum_methods += method(a)
    return sum_methods


if __name__ == "__main__":
    print(foo(0))
    print(foo(1))
