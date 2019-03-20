def average(xs):
    length = len(xs)
    acc = 0
    for i in range(1, length):
        acc = acc + xs[i]
    return acc/length


if __name__ == "__main__":
    print(average([1, 2, 3]))
