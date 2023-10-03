MELY_MGHK = ['a', 'á', 'o', 'ó', 'u', 'ú']
MAGAS_MGHK = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']


def findWordType(word):
        mely = False
        magas = False

        for char in word:
            if char in MELY_MGHK:
                mely = True
            if char in MAGAS_MGHK:
                magas = True
        if mely and magas:
            return "vegyes"
        elif mely and not magas:
            return "mely"
        elif magas and not mely:
            return "magas"
        else:
            return "semmilyen"


def main():
    szavak = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    for el in szavak:
     print("a(z) " + el + " szo " + findWordType(el))


if __name__ == '__main__':
    main()
