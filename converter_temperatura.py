def converter_temperatura_fahrenheit_celsius(f):
    temp = 5*((f-32)/9)
    return temp
    
f = float(input("Insira uma temperatura fahrenheit: "))

temp = converter_temperatura_fahrenheit_celsius(f)

print(
    "Temperatura em Celsius: {:.2f}°".format(temp)
)
