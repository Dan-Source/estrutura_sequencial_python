def calcular_salario(hora, valor):
    return hora * valor

def calcular_imposto_renda(salario):
    return (11/100)*salario

def calcular_inss(salario):
    return (8/100)*salario

def calcular_sindicato(salario):
    return (5/100)*salario

def calcular_salario_liquido(salario, desc_IR, desc_inss, desc_sindicato):
    descontos = desc_IR  + desc_inss + desc_sindicato
    return salario - descontos


def imprimir_descontos(salario):
    desc_IR = calcular_imposto_renda(salario)
    desc_inss =  calcular_inss(salario)
    desc_sindicato = calcular_sindicato(salario)
    salario_liquido = calcular_salario_liquido(
        salario, desc_IR, desc_inss, desc_sindicato
    )
    print(

    '''
        + Salário Bruto : R$ {:.2f}
        - IR (11%) : R$ {:.2f}
        - INSS (8%) : R$ {:.2f}
        - Sindicato ( 5%) : R$ {:.2f}
        = Salário Liquido : R$ {:.2f}
    '''
    .format(
        salario,
        desc_IR,
        desc_inss,
        desc_sindicato,
        salario_liquido
        )
    )
   


primeira_entrada = "Quanto você ganha por hora: "
segunda_entrada = "Quanto você trabalhou por hora: "

valor = float(input(primeira_entrada))
hora = int(input(segunda_entrada))

salario = calcular_salario(valor, hora)

imprimir_descontos(salario)
