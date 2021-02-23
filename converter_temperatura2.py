def converter_temperatura_celsius_fahrenheit(c):
    t = (c *(9/5))+32
    print("Temperatura em Fahrenheit: {:.2f}°"
        .format(t))

c = float(input("Insira uma temperatura celsius:"))

converter_temperatura_celsius_fahrenheit(c)