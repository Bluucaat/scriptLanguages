def forditas(binary_str):
    binary_values = binary_str.split()
    valasz = ""

    for binary_value in binary_values:
        decimal_value = int(binary_value, 2)
        character = chr(decimal_value)
        valasz += character

    return valasz


bemenet = "01111001 01101111 01110101 01110100 01110101 00101110 01100010 01100101 00101111 01100100 01010001 01110111 00110100 01110111 00111001 01010111 01100111 01011000 01100011 01010001"
print(bemenet)
print(forditas(bemenet))
print("Rick Astley - Never Gonna Give You Up")
