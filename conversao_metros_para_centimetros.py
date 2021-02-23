def converter(m):
    cm = m * 100
    return cm

m = int(input("Insira uma valor em metros: "))

print("A o valor em centimetros é: {}".format(converter(m)))