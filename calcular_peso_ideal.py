def calcular_peso_ideal(altura):
    peso_ideal = (72.7*altura) - 58
    return peso_ideal

primeira_entrada = "Qual a sua altura: "

altura = float(input(primeira_entrada))

print("Seu peso ideal seria: {:.2f}"
    .format(calcular_peso_ideal(altura))
    )