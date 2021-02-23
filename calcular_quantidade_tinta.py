def dividir_medida_por_litros(medida):
    litros = medida // 3
    resto = litros % 3
    print(resto)
    if resto == 0:
        return litros
    if resto > 0:
        return litros + 1
def calcular_quantidade_de_latas(litros):
    latas = litros // 18
    resto = litros % 18
    if resto == 0:
            return latas
    elif resto > 0:
        return latas + 1

def calcular_preco_da_tinta(preco, latas):
    valor = preco * latas
    print("A quantidade de latas: {:.2f}".format(latas))
    print("Valor da lata: {:.2f}".format(preco))
    print("Preço da tinta: {:.2f}".format(valor))
    

medida = float(input("Insira o quantidade de metros: "))


litros = dividir_medida_por_litros(medida)

latas = calcular_quantidade_de_latas(litros)

calcular_preco_da_tinta(80, latas)
