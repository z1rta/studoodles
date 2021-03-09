# studoodles
Registrando meu estudos

Algoritmos
São conjuntos de passos finitos e organizados que, quando executados, resolvem um determinado problema.
São passos a serem seguidos por um módulo processador e seus respectivos usuários que, quando executados na ordem correta, conseguem realizar determinada tarefa.

Módulo Processador: Tudo aquilo que pode efetuar processamento. Tudo aquilo que pode ser programável.
Usuários: Quem utiliza > client.
Realizar: Resolver um problema/necessidade (tarefa).

Algoritmos computacionais são rotinas realizadas por algum processador. 

Pseudocódigo ou "Portugol" - Lógica de Programação - é uma forma de representar a lógica do programa antes de passar para uma linguagem de programação.

_____________________________________________________________________________________________________________

  Variáveis
	- Tipo de dado armazenado no computador;
	- O valor contido na memória do computador varia com o tempo, ou seja, não é um valor fixo.
	- Ex: RAM- Armazena dados temporários.
	- Ao declarar uma variável em um programa, estamos definindo e reservando um espaço na memória para armazenar o valor que aquela variável conterá em determinado tempo de execução do programa.
	
  Contantes
	- Armazena valores únicos, que não mudará com o tempo de execução do programa.

_____________________________________________________________________________________________________________

Tipos
	- Tipo númerico -Int
Armazenamento de números, podendo ser utilizados para cálculos.

Podem ser classificados como inteiros e reais(Double-possuem casas decimais).

	- Tipo Caractere -Char

Sequencia de caracteres que contêm apenas letras. Não é possivel ter números ou simbolos especiais.

	- Tipo Alfanumerico -String

Letras, números, digitos ou simbolos especiais.

São delimitados com aspas.

	- Tipo Lógico -Bool

Representa dois únicos valores lógicos que são possíveis: o verdadeiro ou o falso / sim ou não / 1 ou 0 / true or false

_____________________________________________________________________________________________________________

Declaração
	-  o nome que será dado a variável ou constante;
	-  associar esse nome a um tipo de dado (numérico/caractere/string/lógico).

Exemplo:

Variável Idade Tipo Inteiro

Variável Velocidade Tipo Real

Operadores
igual: ==

diferente: !=

*exclamação antes do símbolo NEGA o que vem em seguida*

menor: <

maior: >

menor igual: <=

maior igual: >=

	- PARA (for): quando sabemos a quantidade de vezes que teremos que mostrar aquela informação (quantidade de repetições). 
ex:
for(var i = 0; i <= 10; i++)
{
        Console.WriteLine(i);
}
	- Repita / Enquanto (while): 
ex:
var cont = 0;

while (cont < 10)
{
        Console.WriteLine("Beatriz");
        cont++;
}
	- Repita até (do while): 
ex:
var cont = 0;

do
{
        Console.WriteLine("Beatriz");
        cont++;
}
while(cont < 5)

	- Para cada (foreach) - mais voltado para usar em vetores e matrizes.

{
     string[] nomes = new string { "Marcos", "Joaquim", "Amanda", "Marcela" }
    
     foreach(string nome in nomes)
     {
           Console.WriteLine(nome);
     }
 }
 
 Arrays
	- Vetores (Array Simples): Estrutura que permite armazenar informações de forma ordenada/sequenciada. Permite criar uma lista de variáveis do mesmo tipo. Uma dimensão.
ex:
{
string[] nomes= { "Maria", "Amanda", "Roberta", "Fernando" };

        Console.WriteLine(nomes[3]);
}
        A "resposta" seria: Fernando (a contagem começa do 0, 1, 2, 3).

ex usando laço for:
{
string[] nomes= { "Maria", "Amanda", "Roberta", "Fernando" };

for(int i = 0; i < nomes.Length; i++)
 {
        Console.WriteLine(nomes[i]);
 }
}
          Resposta: todos os nomes / "Length" mostra o comprimento, tudo o que consta dentro de "nomes".

	- Matrizes (Array Composto): Estrutura encadeada de vetores. Permite criar uma lista de vetores do mesmo tipo. Tridimensional. Uma matriz, fisicamente, se parece com uma tabela, os elementos são acessados através de coordenadas (X;Y).
ex:
string[,] nome: new string[3, 3];

for (int linha = 0; linha < 3; linha++)
{
      for (int coluna = 0; coluna < 3; coluna++)
      {
                 nome[linha, coluna] = Console.ReadLine();
      }
}
      
      Console.WriteLine();

for (int linha = 0; linha < 3; linha++)
{
      for (int coluna = 0; coluna < 3; coluna++)
      {
               Console.WriteLine(nome[linha, coluna] + " ");
      }
      Console.WriteLine();
}

_____________________________________________________________________________________________________________

Exercicios
Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número]. 
var numero = prompt("Digite um número")
    alert("Você digitou o número " + numero)

 Faça um Programa que converta metros para centímetros. (Dica: 1 metro = 100 centímetros)
var numerocen = prompt("Digite os centimetros")
var resultado = numerocen / 100
    alert("Resultado:" + resultado + " Metros")

Faça um Programa que converta centímetros para polegadas. (Dica: 1 centímetro = 0,393700787 polegadas) 
var centimetros = prompt("Digite os centimetros:")
var resultado = centimetros * 0.393700787
    alert("O resultado é = " + resultado + " polegadas")

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Fórmula: Area = pi * raio² 
var raioCirculo = prompt("Digite o raio do circulo")
var resultado = 3.14 * (raioCirculo * raioCirculo)
    alert("Resultado da área = " + resultado)

Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. Fórmula: Celsius = (5 * (Farenheit -32) / 9). 
var temperaturaF = prompt("Digite a temperatura em Farenheit")
var resultado = (5 * (temperaturaF -32) / 9)
    alert("Celsius" + resultado)

Faça um Programa que peça as 4 notas bimestrais e mostre a média.
var Nota1 = parseFloat(prompt("Digite a nota 1"))
var Nota2 = parseFloat(prompt("Digite a nota 2"))
var Nota3 = parseFloat(prompt("Digite a nota 3"))
var Nota4 = parseFloat(prompt("Digite a nota 4"))
resultado = (Nota1 + Nota2 + Nota3 + Nota4) / 4
    alert("Média = " + resultado)

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. Fórmula : Farenheit = Celsius × 1,8 + 32 
var temperaturaC = prompt("Digite os Graus Celsius")
var resultado = (temperaturaC * 1.8) + 32
    alert("F = " + resultado)

Faça um Programa que peça o valor da gasolina e do álcool de um posto e diga qual é o combustível mais vantajoso abastecer, sabendo que somente é vantagem abastecer álcool se o preço do mesmo é menor ou igual a 70% do valor da gasolina.
var gasolina = parseFloat(prompt("Preço da gasolina"))
var alcool = parseFloat(prompt("Preço do álcool"))
var resultado = (70 / 100) * gasolina

    if(alcool <= resultado) {
        alert("É mais vantajoso colocar álcool e não gasolina")

    }else {
        alert("É mais vantajoso colocar gasolina e não álcool")

    }
_____________________________________________________________________________________________________________

Exercícios - Curso em vídeo

4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles. 
Algoritmo "soma"
Var
       N1, N2, S: inteiro
Inicio
      Escreva("Digite um número: ")
      Leia(N1)
      Escreva("Digite outro número: ")
      Leia(N2)
      S <- N1 + N2
      Escreva("A soma entre ", N1," e ", N2," é igual a ", S)
Fimalgoritmo 

5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
Algoritmo "média"

Var
    N1, N2, M: real
Inicio
    Escreva("Digite a nota da P1: ")
    Leia(N1)
    Escreva("Digite a nota da P2: ")
    Leia(N2)
    M <- (N1 + N2)/2
    Escreva("A média do aluno é: ", M)

Fimalgoritmo

6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
Algoritmo "ante/suce"

Var
     N1, Ant, Suc: inteiro
Inicio
     Escreva("Digite um número: ")
     Leia(N1)
     Ant <- N1 - 1
     Suc <- N1 + 1
     Escreval("O antecessor de ", N1, " é: ", Ant)
     Escreva("O sucessor de ", N1, " é: ", Suc)

Fimalgoritmo

7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
Algoritmo "exerc7"

Var
    N1, D2, TP: real
Inicio
    Escreva("Digite um número: ")
    Leia(N1)
    D2 <- N1*2
    Escreval("O dobro de ", N1, " é", D2)
    TP <- N1/3
    Escreva("A terça parte de ", N1, " é", TP)

Fimalgoritmo

8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas. 
Ex:  Digite uma distância em metros: 185.72 
A distância de 85.7m corresponde a: 0.18572Km 1.8572Hm 18.572Dam 1857.2dm 18572.0cm 185720.0mm
Algoritmo "exerc8"

Var
   M, Km, In, Cm, Mm: real
Inicio
   Escreva("Digite uma distância em metros: ")
   Leia(M)
   Km <- M/1000
   In <- M*39.370
   Cm <- M/0.010000
   Mm <- M/0.0010000
   Escreva("A distância de ", M, " metros", " corresponde a:", Km, "Km,", In, " polegadas,", Cm, "cm,", Mm, "mm.")

Fimalgoritmo

9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5.56.
Algoritmo "exerc9"

Var
   dinCart, dinDolar: real
Inicio
   Escreva("Digite quantos reais você deseja converter para dolars: R$ ")
   Leia(dinCart)
   dinDolar <- dinCart/5.56
   Escreva("R$", dinCart:5:2, " é igual a US$", dinDolar:5:2)

Fimalgoritmo

10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
Algoritmo "exerc10"

Var
   altP, larP, areaP, tinta: real
Inicio
   Escreva("Qual a altura da parede: ")
   Leia(altP)
   Escreva("Qual a largura da parede: ")
   Leia(larP)
   areaP <- altP*larP
   tinta <- areaP/2
   Escreva("Para pintar as paredes, vocês usará ", tinta, " litros de tinta")

Fimalgoritmo

11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
resultado = b * 2 - 4 * a * c
Algoritmo "exerc8"

Var
   A, B, C, Delta: real
Inicio
   Escreva("Qual o valor de A: ")
   Leia(A)
   Escreva("Qual o valor de B: ")
   Leia(B)
   Escreva("Qual o valor de C: ")
   Leia(C)
   Delta <- B*2-4*A*C
   Escreva("O valor de Delta é: ", Delta)

Fimalgoritmo

12) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada
---
Aula 7 - Estruturas Condicionais 

Condicional Simples: Quando existe um bloco sendo executado caso uma expressão seja verdadeira.
Se (x) entao
          Escreval("y")
FimSe

Condicional Composta:Quando incorpora o "senao" na sintaxe.
Se (x) entao
          Escreval("y")
senao
	Escreval("z")
FimSe

Exercícios: 
algoritmo "QuantosAnos"
var
      Nasc, Atual, ID: inteiro
inicio
      Escreva("Em que ano estamos? ")
      Leia(Atual)
      Escreva("Em que ano eu nasci? ")
      Leia(Nasc)
      ID <- Atual - Nasc
      Escreva("Eu tenho", ID, " anos, ")
      Se (ID >= 21) entao
         Escreval("já posso beber nos USA!!")
      senao
         Escreval("não posso beber nos USA :(")
      FimSe
fimalgoritmo
---
algoritmo "ParOuImpar"
var
N1: Inteiro
R: Real
inicio
Escreval("------------------")
Escreval("---PAR OU IMPAR---")
Escreval("------------------")
Escreval("                  ")
Escreva("Digite um número: ")
Leia(N1)
Se (N1 % 2 = 0) entao
   Escreval("Par!")
senao
   Escreval("Impar!")
FimSe
fimalgoritmo
---
algoritmo "IMC"
var
M, A, IMC: Real
inicio
      Escreva("Digite sua massa (Kg): ")
      Leia(M)
      Escreva("Digite sua altura (m): ")
      Leia(A)
      IMC <- M / A ^ 2
      Escreval("Seu IMC é: ", IMC:5:2)
      Se (IMC >= 18.5) e (IMC < 25) entao
           Escreval("Parabéns, você está no seu peso ideal!")
      senao
           Escreval("Você não está no seu peso ideal.")
      FimSe
fimalgoritmo
---
algoritmo "AptoDirigir"
var
anoA, anoN, ID: inteiro
inicio
Escreval("-----------------------")
Escreval("-----ESCOLA RODAPÉ-----")
Escreval("-----------------------")
Escreval("                   ")
Escreval("-----------------------")
Escreva("Ano atual (yyyy): ")
Leia(anoA)
Escreva("Ano de nascimento (yyyy): ")
Leia(anoN)
ID <- anoA - anoN
Escreval("                   ")
Escreval("--------STATUS--------")
EscrevaL("IDADE: ", ID, " ANOS.")
Se (ID > 18) entao
   EscrevaL("APTO A TIRAR A CARTA.")
senao
   EscrevaL("INAPTO A TIRAR A CARTA.")
FimSe
Escreval("-----------------------")
fimalgoritmo
---
algoritmo "media"
var
nomeA: caractere
P1, P2, M: real
inicio
Escreval("-------------------------")
Escreval("-----ESCOLA RORAIMAR-----")
Escreval("-------------------------")
Escreval("                   ")
Escreval("-------------------------")
Escreva("Digite o nome do aluno: ")
Leia(nomeA)
Escreva("Digite a nota da P1 de ", nomeA, ": ")
Leia(P1)
Escreva("Digite a nota da P2 de ", nomeA, ": ")
Leia(P2)
M <- (P1+P2)/2
Escreval("                   ")
Escreval("-------------------------")
Escreval("MÉDIA: ", M)
Se (M >=7) entao
   Escreval(nomeA, ", ESTA APROVADX!")
senao
   Escreval(nomeA, ", ESTA REPROVADX!")
FimSe
Escreval("-------------------------")
fimalgoritmo
---
Aula 8 - Estruturas Condicionais 2

Condicional aninhada: Quando há uma estrutura dentro da outra.
Se (x) e (y) entao
       EscrevaL("z")
senao
          Se (a) entao
                  EscrevaL("b")
          senao
		(c)
          FimSe
FimSe

Escolha / Caso: Quando se utiliza "Caso" - Ideal para usar com variáveis inteiras (não serve para testar faixa de valores "x >= y" ).
Escolha D
        Caso 1
            Valor <- 10
        Caso 2
            Valor <- 25
        Caso 3
            Valor <- 50
        Caso 4
            Escreva("Qual o valor da doação? R$ ")
            Leia(Valor)
        Caso 5
            Valor <- 0
      FimEscolha

Exercícios: 
algoritmo "médiaescolar"
var
    N1, N2, N3, M: real
inicio
       Escreva("Digite sua nota da P1: ")
       Leia(N1)
       Escreva("Digite sua nota da P2: ")
       Leia(N2)
       Escreva("Digite sua nota do trabalho em grupo: ")
       Leia(N3)
       M <- (N1+N2+N3)/3
       Escreval("Sua média final é: ", M:3:2)
       Se (M>=7) entao
          Escreval("Você passou de ano!! Boas férias!")
       senao
            Se (M >= 5) e (M < 7) entao
               Escreval("Você está de recuperação.")
            senao
               Escreva("Você está reprovado.")
            fimse
       fimse
fimalgoritmo
---
algoritmo "médiaescolar"
var
N1, N2, M: Real
inicio
      Escreva("Digite a nota da P1: ")
      Leia(N1)
      Escreva("Digite a nota da P2: ")
      Leia(N2)
      M <- (N1 + N2)/2
       Se (M >= 7) entao
          Escreval("Aprovadx!")
       senao
            Se (M >=5)e (M < 7) entao
               Escreval  ("Recuperação!")
            senao
               Escreval("Reprovadx!")
            FimSe
       FimSe
fimalgoritmo
---
algoritmo "IMC2"
var
M, A, IMC: Real
inicio
      Escreva("Massa (Kg): ")
      Leia(M)
      Escreva("Altura (m): ")
      Leia(A)
      IMC <- M / (A^2)
      Escreval("IMC: ", IMC:5:2)
      Se (IMC < 17) entao
         Escreval("Muito abaixo do peso!")
      senao
           Se (IMC >= 17) e (IMC < 18.5) entao
              Escreval("Abaixo do peso!")
           senao
                Se (IMC >= 18.5) e (IMC < 25) entao
                   Escreval("Dentro do seu peso ideal!")
                senao
                     Se (IMC >= 25) e (IMC < 30) entao
                         Escreval("Sobrepeso!")
                     senao
                          Se (IMC >= 30) e (IMC < 35) entao
                             Escreval("Obesidade!")
                          senao
                               Se (IMC >= 35) e (IMC < 40) entao
                                  Escreval("Obesidade severa!")
                               senao
                                    Escreval("Obesidade mórbida!")
                               FimSe
                          FimSe
                     FimSe
                FimSe
           FimSe
      FimSe
fimalgoritmo
---
algoritmo "casoDoacao"
var
D: Inteiro
Valor: Real
inicio
      Escreval ("[1] para doar R$10")
      Escreval ("[2] para doar R$25")
      Escreval ("[3] para doar R$50")
      Escreval ("[4] para doar outros valores")
      Escreval ("[5] para cancelar")
      Leia(D)
      Escolha D
        Caso 1
            Valor <- 10
        Caso 2
            Valor <- 25
        Caso 3
            Valor <- 50
        Caso 4
            Escreva("Qual o valor da doação? R$ ")
            Leia(Valor)
        Caso 5
            Valor <- 0
      FimEscolha
      Escreval("Sua doação foi de R$ ", Valor:5:2)
fimalgoritmo
---
algoritmo "escolha"
var
     Nome: Caractere
     ASal, NSal: Real
     Dep: Inteiro
inicio
     Escreva("Digite o nome do funcionário: ")
     Leia(Nome)
     Escreva("Digite o salário atual do funcionário: R$ ")
     Leia(ASal)
     Escreva("Quantos dependentes este funcionário tem?")
     Leia(Dep)
     Escolha Dep
             Caso 0
                  NSal <- ASal + (ASal*5/100)
             Caso 1, 2, 3
                  NSal <- ASal + (ASal*10/100)
             Caso 4, 5, 6
                  NSal <- ASal + (ASal*15/100)
             OutroCaso
                  NSal <- ASal + (ASal*18/100)
     FimEscolha
     Escreva("O novo salário de ", Nome," é: ", NSal)
fimalgoritmo
---
algoritmo "Aproveitamento"
var
    N1, N2, M: Real
inicio
  EscrevaL("------------------------------------")
  EscrevaL("     E.E. MARIA IRACEMA MUNHOZ      ")
  EscrevaL("------------------------------------")
      
      Escreva("Nota da P1: ")
      Leia(N1)
      Escreva("Nota da P2: ")
      Leia(N2)
      M <- (N1+N2)/2
      EscrevaL("------------------------------------")
      EscrevaL("MÉDIA:", M)
      Se (M>=9) entao
         EscrevaL("APROVEITAMENTO: A")
      senao
           Se (M>=8) e (M<8.9) entao
              EscrevaL("APROVEITAMENTO: B")
           senao
                Se (M>=7) e (M<7.9) entao
                   EscrevaL("APROVEITAMENTO: C")
                senao
                     Se (M>=6) e (M<6.9) entao
                        EscrevaL("APROVEITAMENTO: D")
                     senao
                          Se (M>=5) e (M<5.9) entao
                             EscrevaL("APROVEITAMENTO: E")
                          senao
                               Se (M<5) entao
                                  EscrevaL("APROVEITAMENTO: F")
                               senao
                               FimSe
                          FimSe
                     FimSe
                FimSe
           FimSe
      FimSe
      EscrevaL("------------------------------------")
fimalgoritmo
---
algoritmo "Gols"
var
corn, sant, D: inteiro
inicio
Escreval("CORINTIA x SANTU")
Escreval("----------------")
Escreva("Quantos gols do CORINTIA? ")
Leia(corn)
Escreva("Quantos gols do SANTU? ")
Leia(sant)
Se (corn > sant) entao
   D <- corn - sant
senao
     Se (sant > corn) entao
        D <- sant - corn
     FimSe
FimSe
Escreval("DIFERENÇA: ", D)
Se (D > 0 ) e (D <= 4) entao
   Escreval("Partida normal!")
senao
     Se (D = 0) entao
        Escreval("Empate!")
     senao
          Se (D > 4) entao
             Escreva ("Goleada!")
          FimSe
     FimSe
FimSe
fimalgoritmo
---
Aula 9 - Estruturas de Repetição

algoritmo "contador"
var
    cont, N, S: inteiro
inicio
    cont <- 0
    Escreva("Quer contar até quanto? ")
    Leia(N)
    Escreva("Qual o valor do salto? ")
    Leia(S)
    Enquanto (cont <= N) faca
        EscrevaL(cont)
        cont <- cont + S
    FimEnquanto
fimalgoritmo

algoritmo "contador2"
var
    cont, N, S: inteiro
inicio
    cont <- 1
    S <- 0
    Enquanto (cont <= 5) faca
        Escreva("Digite o ", cont, "o. valor: ")
        Leia(N)
        S <- S + N
        cont <- cont + 1
    FimEnquanto
    Escreval("A soma de todos os valores é: ", S)
fimalgoritmo

algoritmo "contador"
var
    cont, N, S, maior, menor: inteiro
inicio
    cont <- 1
    S <- 0
    Enquanto (cont <= 5) faca
        Escreva("Digite o ", cont, "o. valor: ")
        Leia(N)
        Se (N > maior) entao
            maior <- N
         senao
           Se (0 <= menor) entao
              menor <- N
           senao
           FimSe
        FimSe
        S <- S + N
        cont <- cont + 1
    FimEnquanto
    Escreval("A soma de todos os valores é: ", S)
    Escreval("O maior número é: ", maior)
    Escreval("O menor número é: ", menor)
fimalgoritmo

algoritmo "conversor dólar"
var
    R, D: real
    C, Q: inteiro
inicio
    C <- 1
    Escreva("Quantas vezes você deseja converter? ")
    Leia(Q)
    Enquanto (C <= Q) faca
       Escreva("Qual o valor em R$? ")
       Leia(R)
       D <- R/5.16
       Escreval("Valor convertido em dólar: US$ ", D:5:2)
       C <- C + 1
    FimEnquanto
fimalgoritmo
