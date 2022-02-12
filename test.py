from enum import Enum


class test(Enum):
    hello = 1


def main():
    woop = test(1)

    print(woop == test.hello)
    print(woop == 1)


if __name__ == '__main__':
    main()
