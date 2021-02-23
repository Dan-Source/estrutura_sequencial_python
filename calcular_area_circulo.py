from math import pow

def area_circulo(r):
    pi = 3.14
    area = pi * pow(r,2)
    print("A area do ciruclo é: {}".format(area))

raio = int(input("Informe o raio de circulo: "))

area_circulo(raio)
