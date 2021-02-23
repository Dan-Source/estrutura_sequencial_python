def calcular_peso_ideal(altura):
    peso_ideal_homem = (72.7*altura) - 58
    peso_ideal_mulher = (72.7*altura) - 44.7
    return peso_ideal_homem, peso_ideal_mulher


primeira_entrada = "Qual a sua altura: "
altura = float(input(primeira_entrada))
homem, mulher = calcular_peso_ideal(altura)

print(
    "Se você for homem seu peso ideal seria: {:.2f}".format(homem)
)
print(
    "Se você for mulher seu peso ideal seria: {:.2f}".format(mulher)
)
