# >>> int(100*(101)/2)
# 5050
# >>>

def szamSzamjegyeinekOsszege(n):
    a = list(str(n))
    sum = 0
    for num in a:
        if num.isdigit():
            sum += int(num)
    return sum


def main():
    print(szamSzamjegyeinekOsszege(12023))


if __name__ == "__main__":
    main()