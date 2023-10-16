
def main():
    a = str(2**1000)
    sum = 0
    for n in a:
        sum += int(n)
    print(sum)

if __name__ == '__main__':
    main()