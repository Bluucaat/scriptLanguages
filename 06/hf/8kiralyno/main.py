def convertTable(table):
    cols = 8
    rows = 8
    tableMatrix = [[0 for i in range(cols)] for j in range(rows)]
    for col in reversed(range(cols)):
        for row in reversed(range(rows)):
            if row == table[col]:
                tableMatrix[row][col] = "Q"
            else:
                tableMatrix[row][col] = "."
    print("+", ("-" * 38), "+")
    for row in reversed(range(rows)):
        print("|", end="")
        for col in range(cols):
            print(" ", tableMatrix[row][col], " ", end="")
        print("|", end="")
        print()

    print("+", ("-" * 38), "+")


def drawTable():
    pass


def main():
    table = [0,4,7,5,2,6,1,3]
    convertTable(table)


if __name__ == '__main__':
    main()
