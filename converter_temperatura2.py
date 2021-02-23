def converter_temperatura_celsius_fahrenheit(c):
    temp = (c *(9/5))+32
    return temp
    

c = float(input("Insira uma temperatura celsius:"))

temp = converter_temperatura_celsius_fahrenheit(c)

print(
    "Temperatura em Fahrenheit: {:.2f}°".format(temp)
)