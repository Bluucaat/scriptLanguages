def main():
    # f = open("input.txt", "r")
    #
    # sorok = ""
    # for line in f:
    #     line = line.rstrip("\n")
    #     print(line)
    #
    # sorok = f.read().splitlines()
    # print(sorok)
    #
    # for line in f:
    #     if line.endswith("line."):
    #         print(line)
    #
    # f.close()
    #
    # f = open("out.txt", "w")
    # print("sznia", file = f)
    # print(True, 3.14, "hi", file=f)
    # f.close()
    # f.write("aa\n")

    with open("input.txt", "w") as f:
        f.write("helo\n")

    with open("input.txt", "r") as f1, open("out.txt", "w") as f2:
        for line in f1:
            f2.write(line)

    #regivel
    f = open("input.txt", "r")
    f2 = open("out.txt", "w")
    for line in f:
        f2.write(line)
    f.close()
    f2.close()

if __name__ == '__main__':
    main()