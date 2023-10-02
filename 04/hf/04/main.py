def main():

    str1 = "hi"
    str2 = None

    if (bool(str1) and not bool(str2)) or (bool(str2) and not bool(str1)):
        print("True")
    else:
        print("False")




if __name__ == '__main__':
    main()
