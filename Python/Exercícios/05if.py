print("---------------------")
print("Inscrição -----------")
rm = input("Insira seu RM: ")
idade = input("Qual sua idade? ")

if int(idade) >= 18:
    print("Você está apto a se inscrever!")
    print("Os próximos passos serão enviados para o e-mail do aluno de RM {}".format(rm))
else:
    autorizado = input("Você possui autorização dos responsáveis para participar? [S/N] ")
    if str(autorizado) == "S":
        print("Você está apto a se inscrever!")
        print("Os próximos passos serão enviados para o e-mail do aluno de RM {}".format(rm))
    else:
        print("Sua participação não foi autorizada (Motivo: menor de idade sem autorização).")
