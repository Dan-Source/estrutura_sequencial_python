def area_circulo(r):
    pi = 3.14
    area = pi * (r**2)
    return area


raio = int(input("Informe o raio de circulo: "))

area = area_circulo(raio)

print("A area do ciruclo é: {}".format(area))
