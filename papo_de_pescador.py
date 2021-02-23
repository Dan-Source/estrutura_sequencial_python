def calcular_limite_peso(peso):
    if peso <= 50:
        print("Aproveite sua pesca, você não será taxado!")
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print("""
                Você ecedeu o limite de 50 kg.
                Ecesso: {:.2f} kg.
                Multa: {:.2f}.
            """
        .format(excesso, multa))


peso_peixe = float(input("Quantos kg você pescou hoje: "))

calcular_limite_peso(peso_peixe)