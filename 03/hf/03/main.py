# iterativ fgv
def iterativPalindrom(n):
    return n == n[::-1]


def rekurzivPalindrom(n):
    if len(n) < 2: return True
    if n[0] != n[-1]: return False
    return rekurzivPalindrom(n[1:-1])


def main():
    print(iterativPalindrom("121"))
    print(rekurzivPalindrom("122321"))


if __name__ == '__main__':
    main()
