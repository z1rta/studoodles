#Esse programa recebe a distância e o tempo e calcula a velocidade de média.
#Primeiro vamos pedir a distância e o tempo

print("Calculador de velocidade média")
print("------------------------------")

distancia = input("Digite a distância percorrida: ")
tempo = input("Digiteo tempo percorrido: ")
#realizando o cálculo
veloc_media = float(distancia) / float(tempo)

#exibindo o resultado
print("A velocidade média calculada foi de {:.2f}km/h. ".format(veloc_media))
#para exibir o nº de casa decimais desejado foi adicionado dentro das chaves ":.2f". o 2 significa o número de casas e
# o f significa o tipo da variável, que no caso é float.
