import sys


def main():
    a = sys.argv[1]
    b = sys.argv[2]

    if a.lstrip("-").isdigit() and b.lstrip("-").isdigit():
        a = int(a)
        b = int(b)
        print(a + b)
    else:
        print("hibas input!")


if __name__ == '__main__':
    main()
