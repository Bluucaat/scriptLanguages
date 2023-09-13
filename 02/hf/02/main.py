def palindromE1():
    checkedString = input("adjon meg egy String-et, és a program megmondja hogy palindróm-e!")

    if checkedString == checkedString[::-1]:
        print("Az adott String palindróm")
    else:
        print("Az adott String nem palindróm")


def main():
    palindromE1()


if __name__ == '__main__':
    main()
