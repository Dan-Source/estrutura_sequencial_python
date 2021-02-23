def dividir_medida_por_litros(medida):
    litros = medida // 3
    resto = litros % 3
    if resto == 0:
        return litros
    litros= litros+1
    return litros


def calcular_quantidade_de_latas(litros):
    latas = litros // 18
    resto = litros % 18
    if resto == 0:
        return latas
    latas = latas + 1
    return latas


def calcular_preco_da_tinta(preco, latas):
    valor = preco * latas
    return valor

preco = 80

medida = float(input("Insira o quantidade de metros: "))

litros = dividir_medida_por_litros(medida)

latas = calcular_quantidade_de_latas(litros)

valor = calcular_preco_da_tinta(preco, latas)

print("A quantidade de latas: {:.2f}".format(latas))
print("Valor da lata: {:.2f}".format(preco))
print("Preço da tinta: {:.2f}".format(valor))