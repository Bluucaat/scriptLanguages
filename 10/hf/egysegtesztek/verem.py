class Verem:
    def __init__(self):
        self.items = []

    def betesz(self, elem):
        self.items.append(elem)

    def kivesz(self):
        if not self.ures():
            return self.items.pop()
        else:
            print("A verem üres.")
            return None

    def ures(self):
        return len(self.items) == 0

    def meret(self):
        return len(self.items)

    def __str__(self):
        return "[" + " ".join(map(str, self.items)) + "]"



v = Verem()
print(v)         # []
print(v.ures())  # True

v.betesz(1)
v.betesz(4)
v.betesz(5)

print(v)         # [1 4 5]
print(v.meret()) # 3
print(v.ures())  # False

x = v.kivesz()
print(x)         # 5
print(v)         # [1 4]

v.kivesz()
v.kivesz()       # mar ures.
x = v.kivesz()
print(x)         # None
