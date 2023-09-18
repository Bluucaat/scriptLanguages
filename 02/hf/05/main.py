def szamMegforditas(n):
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num


def szamMegforditas2(n):
    n = str(n)[::-1]
    n = int(n)
    return n


def main():
    print(szamMegforditas(1977))
    print(szamMegforditas2(1977))


if __name__ == '__main__':
    main()
