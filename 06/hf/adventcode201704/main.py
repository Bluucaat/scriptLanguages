def elfogadhatoJelmondat(passphrase):
    words = passphrase.split()
    word_count = {}

    for word in words:
        if word in word_count:
            return False
        word_count[word] = 1

    return True

def jelmondatokSzama(jelmondatok):
    count = 0
    for jelmondat in jelmondatok:
        if elfogadhatoJelmondat(jelmondat):
            count += 1
    return count


# Read the input from a file (assuming input.txt contains your list of passphrases)
with open("input.txt", "r") as file:
    jelmondatok = [line.strip() for line in file.readlines()]

elfogadott_jelmondat = jelmondatokSzama(jelmondatok)
print(elfogadott_jelmondat)