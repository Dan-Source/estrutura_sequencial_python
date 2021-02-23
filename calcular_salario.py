def calcular_salario(hora, valor):
    return hora * valor

primeira_entrada = "Quanto você ganha por hora: "
segunda_entrada = "Quanto você trabalhou por hora: "

valor = float(input(primeira_entrada))
hora = int(input(segunda_entrada))

print("Seu salario neste mês foi: R$ {:.2f}"
    .format(calcular_salario(valor, hora))
    )
