def calculo_letra_a(a, b):
    r = (a*2)+(b/2)
    print("O produto do dobro do primeiro com metade do segundo: {:.2f}"
    .format(r))

def calculo_letra_b(a, c):
    r = (a*3)+c
    print("A soma do triplo do primeiro com o terceiro: {:.2f}"
    .format(r))

def calculo_letra_c(c):
    from math import pow
    r = pow(c, 3)
    print("O terceiro elevado ao cubo: {:.2f}"
    .format(r))

a = int(input("Informe um número A: "))
b = int(input("Informe um número B: "))
c = float(input("Informe um número C: "))

calculo_letra_a(a, b)
calculo_letra_b(a, c)
calculo_letra_c(c)