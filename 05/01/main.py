# list comprehesion / listak eloallitasa egy kompakt modja

nums = [1, 2, 3, 4]
squares = [n * n for n in nums if n <= 100]

vehicles = ["auto", "villamos", "metro"]
out = [s.upper() + "!" for s in vehicles]
print(out)

nevek = ['aladar', 'bela', 'cecil']
out2 = [nev.capitalize() for nev in nevek]
print(out2)

uresszamok = [(n * 0) for n in range(10)]
print(uresszamok)

kettesSzorzas = [n * 2 for n in range(1, 10 + 1)]
# vagy list(range(2,20+1,2))
print(kettesSzorzas)

sztringszamok = [str(n) for n in range(1, 10 + 1)]
eredmenyszamok = [int(n) for n in sztringszamok]
print(eredmenyszamok)

sztring1 = "1234567"
szetbontott = [int(char) for char in sztring1]
print(szetbontott)

sztring2 = "The quick brown fox jumps over the lazy dog"
szavakhossza = [len(szo) for szo in sztring2.split()]
print(szavakhossza)

# 8
sztring = "python is an awesome language"
szavakElsoBetuje = [szo[0] for szo in sztring.split()]
print(szavakElsoBetuje)

##ora

# 9sztring
sztring = "The quick brown fox jumps over the lazy dog"
szoEsAHossza = ["('" + szo + "'," + str(len(szo)) + ")" for szo in sztring.split()]
print(szoEsAHossza)

elKissebbParos = [n for n in range(10) if n % 2 == 0]
print(elKissebbParos)

husznalkissebb = [n*n for n in range(20) if n*n%2==0]
print(husznalkissebb)

alphabet = []
for i in range(65, 90):
    alphabet.append(chr(i))

szo = "".join(alphabet)
print(szo)

sztring = [' apple ', ' banana ', ' kiwi']
ujsztring = [elem.strip() for elem in sztring]
print(ujsztring)

szamok = [1, 0, 1, 1, 0, 1, 0, 0]
rendesszam = [str(szam) for szam in szamok]
print("".join(rendesszam))