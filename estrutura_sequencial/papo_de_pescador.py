def calcular_limite_peso(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        msg = "Multa: {:.2f} | Excesso: {:.2f}".format(multa, excesso)
        return msg
    return "Aproveite sua pesca, você não será taxado!"


peso_peixe = float(input("Quantos kg você pescou hoje: "))

msg = calcular_limite_peso(peso_peixe)

print(msg)
