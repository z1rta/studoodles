print("** O ALGORITMO DA SORTE DE FIBONNACI **")
i = int(input("Digite um valor inteiro: "))
n1 = 0
n2 = 1
print(n2)
n3 = int(0)

while n3 < i:
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

if i == n3:
    print("Ação bem sucedida!")
else:
    print("Falhou!")
