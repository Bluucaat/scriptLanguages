import sys


def main():
    a = [4, 6, 8]
    type(a)
    a.append(10)
    b = []
    b.append(5)

    c = [1, 2] + [6 + 7]
    print(c[:2])

    b = a[:]
    b.append(1)
    print(a == b)

    for i in c:
        print(i)

        print("hello", True, 2, sep="---")

    print("OK")
    # print("Hiba!", file=sys.stderr)
    a = [1, 2, 7, 4, 9]
    a.append(10)

    x = a.pop(2)
    a.pop()
    print(a)
    a.extend(b)
    a = [8, 5, 4, 3]
    sorted(a)
    # a metodus kap listat, csinal masolatot, lerendezi, es azt adja vissza.
    sorted(a, reverse=True)
    a = [8, 5, 4, 3]
    a.sort()
    #a lista.sort a listat helyben rendezi, nem ad vissza semmit
    a.sort(reverse=True)


if __name__ == '__main__':
    main()