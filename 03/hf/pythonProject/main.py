
TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb""".strip()

DECODEDICT = {
    "k": "m",
    "k": "q",
    "e": "g"
}

def solve(s):
    ans = """"""
    for i in range(len(TEXT)):
        if TEXT[i].lower() in DECODEDICT.keys():
            ans += DECODEDICT.get(TEXT[i])
        else:
            ans += TEXT[i]

    return ans


def main():
    print(solve(TEXT))


if __name__ == '__main__':
    main()