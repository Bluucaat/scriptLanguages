import sys
import random as r

UPTO = 100


def main():
    for i in range(1, UPTO+1):
        print(r.randint(0, 9), end="")
        if(i % 10 == 0):
            print()
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()