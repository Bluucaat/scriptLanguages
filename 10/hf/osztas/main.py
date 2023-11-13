
def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print("Az osztas eredmenye: {0:2f}".format(result))
        except ZeroDivisionError:
            print("a 0-val valo osztas lehetetlen.")
        except ValueError:
            print("A megadott ertek helytelen.")
        except KeyboardInterrupt:
            print("A program meg lett szakitva.")
            exit()


while __name__ == "__main__":
    main()
