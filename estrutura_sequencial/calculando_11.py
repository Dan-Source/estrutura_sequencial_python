def calculo_letra_a(a, b):
    r = (a*2)+(b/2)
    return r


def calculo_letra_b(a, c):
    r =(a*3)+c
    return r


def calculo_letra_c(c):
    r = c**3
    return r


a = int(input("Informe um número A: "))
b = int(input("Informe um número B: "))
c = float(input("Informe um número C: "))

x = calculo_letra_a(a, b)
y = calculo_letra_b(a, c)
z = calculo_letra_c(c)

print(
    "O produto do dobro do primeiro com metade do segundo: {:.2f}".format(x)
)
print(
    "A soma do triplo do primeiro com o terceiro: {:.2f}".format(y)
)

print(
    "O terceiro elevado ao cubo: {:.2f}".format(z)
)
