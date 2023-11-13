def get_nyero_szamok():
    for a in range(1, 46):
        for b in range(1, 46):
            for c in range(1, 46):
                for d in range(1, 46):
                    for e in range(1, 46):
                        f = 90 - (a + b + c + d + e)
                        product = a * b * c * d * e * f


                        if product == 996300 and all(int(digit) % 3 == 0 for digit in str(product) if digit != '0'):
                            print(f)
                            return [a, b, c, d, e, f]



nyeroszamok = get_nyero_szamok()
print("A nyero szamok:", nyeroszamok)







