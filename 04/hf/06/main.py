def szamokkulonbsege(num):
    sum1 = 0
    for i in range(1, num+1):
        sum1 += i**2

    sum2 = (num*(num+1)/2)**2

    return int(sum2-sum1)


def main():
    print(szamokkulonbsege(100))






if __name__ == '__main__':
    main()
