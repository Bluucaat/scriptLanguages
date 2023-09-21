def listaszorzat(lista):
    szorzat = 1;
    for i in range(0, len(lista)):
        szorzat *= lista[i]
    return szorzat


def main():
    l1 = [2, 3, 4, 5, 6]
    l2 = []
    print(listaszorzat(l2))

if __name__ == '__main__':
    main()
