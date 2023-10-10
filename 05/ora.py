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

# 9


def duplaz(n):
    # TODO
    pass


# opc par fgv
def greet(name, greetings="Hello"):
    print(f"{greetings} {name}!")

def hello(name, repeat=1, postfix = ''):
    for i in range(repeat):
        print(name + postfix)

def main():

    li = ["alfa", "beta", "gamma"]
    idx = 0
    for idx, e in enumerate(li, start=1):
        print(idx, e)
    greet("Krisz")
    greet("Krisz", greetings="Bonjour")
    hello("Krisz", repeat=3)
    hello("Krisz", postfix="!")

if __name__ == "__main__":
    main()