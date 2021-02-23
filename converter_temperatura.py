def converter_temperatura_fahrenheit_celsius(f):
    t = 5*((f-32)/9)
    print("Temperatura em Celsius: {:.2f}°"
        .format(t))

f = float(input("Insira uma temperatura fahrenheit: "))

converter_temperatura_fahrenheit_celsius(f)
