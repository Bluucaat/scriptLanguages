def compare(s1, s2):
    dict1 = anagram(s1)
    dict2 = anagram(s2)
    count = 0

    if dict1 == dict2:
        return True
    else:
        return False


def anagram(s):
    dictionary = {}

    for char in s:
        if char not in dictionary.keys():
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    return dictionary


def normalize(s):
    s = s.lower().strip()
    s = s.replace(" ", "")

    return s


def main():
    s1 = "alma"
    s2 = "la ma  "
    if compare(normalize(s1), normalize(s2)):
        print("A ket szo anagramma!")
    else:
        print("A ket szo nem anagramma!")

    szo1 = list(normalize(s1))
    szo2 = list(normalize(s2))
    szo1.sort()
    szo2.sort()
    if szo1 == szo2:
        print("A ket szo anagramma!")
    else:
        print("A ket szo nem anagramma!")


if __name__ == '__main__':
    main()
