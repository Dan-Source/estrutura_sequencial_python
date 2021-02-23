def area_quadrado(b, h):
    area = b * h
    print("A area do quadrado é: {}".format(area))
    dobro_da_area = area * 2
    print("Dobro da area do quadrado é: {}".format(dobro_da_area))
    

b = int(input("Informe a base: "))
h = int(input("Informe a altura: "))

area_quadrado(b, h)