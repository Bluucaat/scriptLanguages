import sys


def cat(fname: str) -> None:
    try:
        f = open('fname', 'r')
        content = f.read()
        print("---", fname)
        print(content)
        f.close()
    except FileNotFoundError:
        print("I/O Error:", fname)


print("cat fgv vege.")


def main() -> None:
    args = sys.argv[1]
    for arg in args:
        cat(arg)


if __name__ == "__main__":
    main()
