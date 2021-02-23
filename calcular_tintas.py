def retornar_opcao(opcao):
    if opcao  == 1:
        return 18
    if opcao == 2:
        return 3.6
    if opcao == 3:
        return 'misto'
        
def dividir_metros_por_litros(metros):
    litros = metros // 6
    resultado = litros + (litros * 0.10)
    return resultado

def calcular_quantidade_de_latas(litros, tipo):
    latas = litros // 
    resto = litros % tipo
    if resto == 0:
            return latas
    elif resto > 0:
        return latas + 1

def calcular_quantidade_de_galoes(litros, tipo):
    latas = litros // tipo
    resto = litros % tipo
    if resto == 0:
            return latas
    elif resto > 0:
        return latas + 1

def calcular_preco_da_tinta_latas(preco, opcao):
    valor = preco * latas
    print("A quantidade de latas: {:.2f}".format(latas))
    print("Valor da lata: {:.2f}".format(preco))
    print("Preço da tinta: {:.2f}".format(valor))


def calcular_preco_da_tinta_galoes(preco, galoes):
    valor = preco * galoes
    print("A quantidade de galoes: {:.2f}".format(galoes))
    print("Valor da lata: {:.2f}".format(preco))
    print("Preço da tinta: {:.2f}".format(valor))


def calcular_preco_da_tinta_mista(preco, latas):
    valor = preco * latas
    print("A quantidade de latas: {:.2f}".format(latas))
    print("Valor da lata: {:.2f}".format(preco))
    print("Preço da tinta: {:.2f}".format(valor))
    

# medida = float(input("Insira o quantidade de metros: "))
# opcao = int(input(
#     '''
#     Escolha uma opção:
#         1 => Latas de 18 litros
#         2 => Galões de 3,6 litros
#         3 => Misturando Latas e Galões
#     '''
# ))
metros = 114





litros = dividir_metros_por_litros(metros)
print(litros)
# latas = calcular_quantidade_de_latas(litros, opcao)
# print(latas)
# opcao = 2
# galoes = calcular_quantidade_de_galoes(litros, opcao)
# print(galoes)

# calcular_preco_da_tinta_latas(80, latas)

# calcular_preco_da_tinta_galoes(80, galoes)
