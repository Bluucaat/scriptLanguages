def precompute_powers():
    powers = [i ** i for i in range(10)]
    return powers

def munchausen(n, powers):
    n_str = str(n)
    num2 = sum(powers[int(digit)] for digit in n_str if digit != '0')
    if n == num2:
        return n
    return -1

def main():
    powers = precompute_powers()

    for i in range(10000):
        result = munchausen(i, powers)
        if result != -1:
            print(result)


    for i in range(10000, 440000000):
        result = munchausen(i, powers)
        if result != -1:
            print(result)

if __name__ == '__main__':
    main()