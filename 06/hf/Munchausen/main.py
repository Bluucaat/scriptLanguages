while True:
    a = input("Legyszi add mar meg a 2+2 eredmenyet ")
    if int(a) == 4:
        print("Helyes valasz")
        break
    print("helytelen valasz")

joValasz = False
while not joValasz:
    a = input("Mennyi a 2+2 eredmenye?")
    if int(a) == 4:
        print("Helyes valasz")
        joValasz = True
    else:
        print("Helytelen valasz")
