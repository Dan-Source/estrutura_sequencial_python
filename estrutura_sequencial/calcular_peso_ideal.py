def calcular_peso_ideal(altura):
    peso_ideal = (72.7*altura) - 58
    return peso_ideal


altura = float(input("Qual a sua altura: "))
peso_ideal =  calcular_peso_ideal(altura)
print(
    "Seu peso ideal seria: {:.2f}".format(peso_ideal)
)