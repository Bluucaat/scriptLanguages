def duplaz(n):
    # TODO
    pass


# opc par fgv
# def greet(name, greetings="Hello"):
#     print(f"{greetings} {name}!")
#
# def hello(name, repeat=1, postfix = ''):
#     for i in range(repeat):
#         print(name + postfix)

def valid(text, chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    ans = ""
    charlist = []
    print(charlist)
    for char in text:
        charlist.append(char)
        for j in charlist:
            if j == char:
                ans.join(j)
    return ans


def main():

    valid("barking")

if __name__ == "__main__":
    main()