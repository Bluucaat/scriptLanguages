def main():
    diakok = [('Krisz', 3, 4.5), ('Adam', 2, 4.1),
              ('Anita', 1, 4.7), ('Zalan', 3, 2)]

    print("{0:<12} {1:^16} {2:>16}".format("Nev", "Szemeszter", "Atlag"))
    print("-"*30)
    for element in diakok:
        print("{0:12} {1:^16} {2:16}".format(element[0], element[1], element[2]))

    if __name__ == '__main__':
        main()
