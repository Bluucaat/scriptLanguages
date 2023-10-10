# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    lista = [n for n in range(1000) if n % 3 == 0 or n % 5 == 0]
    print(sum(lista))

if __name__ == '__main__':
    main()