print("Esse programa irá inverter o valor de duas variáveis")
print("----------------------------------------------------")
A = input("Digite o valor da variável 1: ")
B = input("Digite o valor da variável 2: ")
troca = A
A = B
B = troca
print("Agora a variável 1 vale {} e a variável 2 vale {}".format(A, B))
#Lembrete: não é necessário colocar o ".format" após cada chave, posso colocar em ordem dentro de um unico, como esta acima.
