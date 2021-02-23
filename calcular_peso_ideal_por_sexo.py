def calcular_peso_ideal_homem(altura):
    peso_ideal = (72.7*altura) - 58
    return peso_ideal

def calcular_peso_ideal_mulher(altura):
    peso_ideal = (72.7*altura) - 44.7
    return peso_ideal


primeira_entrada = "Qual a sua altura: "

altura = float(input(primeira_entrada))


print("Se você for homem seu peso ideal seria: {:.2f}"
    .format(calcular_peso_ideal_homem(altura))
    )

print("Se você for mulher seu peso ideal seria: {:.2f}"
.format(calcular_peso_ideal_homem(altura))
)