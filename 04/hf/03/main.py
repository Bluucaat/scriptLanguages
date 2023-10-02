def diamond(n):
    for i in range(n // 2 + 1):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for j in range((n // 2), 0, -1):
        print(' ' * (n - j) + '* ' * j)


def simpleDiamond(n):
    if not (n % 2 == 0):
        for i in range(1, n //2 +2):
            line = ('*' * (i + (i - 1)))
            print(line.center(n, ' '))

        for j in range(n//2, 0, -1):
            print(("*"*(j+j-1)).center(n, ' '))
    else:
        print("Csak paratlan szamra lehet rajzolni!")


def main():
    simpleDiamond(5)
#   diamond(9)


if __name__ == '__main__':
    main()
