import re

def cleanWhitespaces(s):
    s = s.replace("\n", "")
    s = s.replace(" ", "")
    return s


def main():
    print(cleanWhitespaces("192 .20.246.138:\n8080"))



if __name__ == '__main__':
    main()
