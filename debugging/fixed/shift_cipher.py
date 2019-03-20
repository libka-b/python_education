import re


VALID_WORD = re.compile("^[a-z]+$")
VALID_INT = re.compile("^\\d+$")
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_valid_word(word: str) -> bool:
    return VALID_WORD.search(word) is not None


def is_valid_int(word: str) -> bool:
    return VALID_INT.search(word) is not None


def encrypt(shift: int, word: str) -> str:
    fully_encrypted = ""
    for char in word:
        number = ALPHABET.find(char)
        shift_num = number + shift
        fully_encrypted += ALPHABET[shift_num % 26]
    print(fully_encrypted)
    return fully_encrypted


def num_shift() -> int:
    word = input('How many numbers do you want to shift?\n')
    while not is_valid_int(word):
        word = input('Please insert a valid number.\n')
    return int(word) % 26


def our_word() -> str:
    word = input('Please enter your sentence (only a-z)\n')
    while not is_valid_word(word):
        word = input('Please try again \n')
    return word


def main():
    word = our_word()
    shift = num_shift()
    encrypt(shift, word)


if __name__ == "__main__":
    main()
