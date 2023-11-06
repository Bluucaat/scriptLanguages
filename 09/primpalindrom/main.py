def prim(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def palindrom(num):
    return str(num) == str(num)[::-1]


def legkissebb_prim_palindrom(N):
    if N < 2:
        N = 2
    while True:
        if palindrom(N) and prim(N):
            return N
        N += 1


def main():
    number = 31
    result = legkissebb_prim_palindrom(1977)
    print(result)


if __name__ == "__main__":
    main()
