def calcular_media(a, b, c, d):
    media = (a + b + c + d)/4
    return media
    

a = int(input("Informe uma nota A: "))
b = int(input("Informe uma nota B: "))
c = int(input("Informe uma nota C: "))
d = int(input("Informe uma nota D: "))

media = calcular_media(a, b, c, d)
print("O calculo da media é : {}".format(media))