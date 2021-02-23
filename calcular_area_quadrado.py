def calcular_area(b, h):
    area = b * h
    dobro_da_area = area * 2
    return area, dobro_da_area
    

b = int(input("Informe a base: "))
h = int(input("Informe a altura: "))

area, dobro_da_area = calcular_area(b, h)

print("A area do quadrado é: {}".format(area))
print("Dobro da area do quadrado é: {}".format(dobro_da_area))