def somar_numero(a, b):
    soma = a + b
    return soma


a = int(input("Informe um número A: "))
b = int(input("Informe um número B: "))

soma = somar_numero(a, b)
print("A soma do numéro A + B: {}".format(soma))
