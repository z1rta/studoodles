print("Checagem de IMC")
print("--------------------------------")

massa = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))
imc = float(massa) / float(altura ** 2)

print("Seu IMC é: {:.2f}".format(imc))
if imc <= 16:
    print("Baixo peso Grau III. Consulte seu médico!")
elif 16 <= imc <= 16.99:
    print("Baixo peso Grau II.")
elif 17 <= imc <= 18.49:
    print("Baixo peso Grau I.")
elif 18.50 <= imc <= 24.99:
    print("Peso ideal!")
elif 25 <= imc <= 29.99:
    print("Sobrepeso.")
elif 30 <= imc <= 34.99:
    print("Obesidade Grau I.")
elif 35 <= imc <= 39.99:
    print("Obesidade Grau II.")
elif imc >= 40:
    print("Obesidade Grau III. Consulte seu médico!")

print("Finalizando programa....")
