print("BEM VINDO(A) AO NOSSO SISTEMA!")
print("POR FAVOR, INFORME AS INFORMAÇÕES SOLICITADAS PARA ACESSAR.")
print("--------------------------------------------------------------")
nivel_acesso = input("Por favor, digite seu nível de acesso: ").upper()
if nivel_acesso == "ADM" or nivel_acesso == "USR":
    genero = input("Qual seu gênero? ").upper()
    if nivel_acesso == "ADM":
        if genero == "FEMININO":
            print("Olá, administradora!")
        else:
            print("Olá, administrador!")
    else:
        if genero == "FEMININO":
            print("Olá, usuária!")
        else:
            print("Olá, usuário!")
elif nivel_acesso == "GUEST":
    print("Olá, visitante!")
else:
    print("Olá, desconhecido(a)!")
