def main():
    a = input("Adja meg az elso szamot: ")
    b = input("Adja meg a masodik szamot: ")

    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        print(a + b)
    else:
        print("hibas input!")


if __name__ == '__main__':
    main()
