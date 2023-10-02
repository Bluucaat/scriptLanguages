MELY_MGHK = ['a', 'á', 'o', 'ó', 'u', 'ú']
MAGAS_MGHK = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']


def findWordType(words):
    for word in words:
        mely = False
        magas = False

        for char in word:
            if char in MELY_MGHK:
                mely = True
            if char in MAGAS_MGHK:
                magas = True
        if mely and magas:
            print("a " + word + " szo vegyes.")
        elif mely and not magas:
            print("a " + word + " szo mely.")
        elif magas and not mely:
            print("a " + word + " szo magas.")
        else:
            print("a " + word + " szo semmilyen.")


def main():
    szavak = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    findWordType(szavak)


if __name__ == '__main__':
    main()
