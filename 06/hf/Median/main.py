def getmedian(l):
    list = sorted(l)
    median = 0
    if len(list) % 2 == 0:
        median = (list[(len(list)-1) // 2] + list[(len(list)-1) // 2 + 1]) /2
    else:
        median = list[len(list) // 2]
    return median


def main():

    l = [1, 2, 3, 4, 5]
    print(getmedian(l))

    print(getmedian([1, 300, 2, 200, 1]))

    l = [3, 6, 20, 99, 10, 15]
    print(getmedian(l))





if __name__ == '__main__':
    main()