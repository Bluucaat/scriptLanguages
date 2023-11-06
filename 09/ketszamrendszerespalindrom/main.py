def palindrom_e(s):
    return s == s[::-1]


def palindrom_e_kettes_szamrendszerben(n):
    binary_representation = bin(n)[2:]
    return palindrom_e(binary_representation)


def szamok_osszege(limit):
    total = 0
    for num in range(1, limit):
        decimal_str = str(num)
        if palindrom_e(decimal_str) and palindrom_e_kettes_szamrendszerben(num):
            total += num
    return total


def main():
    result = szamok_osszege(1000000)
    print(result)


if __name__ == '__main__':
    main()
