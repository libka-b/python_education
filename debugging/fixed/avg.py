from typing import List


def average(xs: List[int]) -> float:
    return sum(xs) / len(xs)


if __name__ == "__main__":
    print(average([1, 2, 3]))
