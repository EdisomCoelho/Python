# Exercício 1: Olá, Mundo! Personalizado 
# Crie um programa que peça o nome do usuário e exiba uma mensagem de boas-vindas 
# personalizada, por exemplo: "Olá, [Nome]! Seja bem-vindo ao curso de 
# Python!". 

nome = input("Insira o nome do usuário: ")
print(f"Olá, {nome}! Seja bem vindo ao curso de Python")
print("\n")
# Exercício 2: Calculadora de Idade em Dias 
# Escreva um programa que solicite a idade do usuário em anos e calcule a quantidade 
# aproximada de dias que ele já viveu (considere cada ano com 365 dias). 
idAno = int(input("Insira a idade do usuário: "))
idDia = idAno * 365
print(f"Sua idade em dias é de aproximadamente {idDia} dias")

print("\n")
# Exercício 3: Verificador de Par ou Ímpar 
# Peça ao usuário para digitar um número inteiro. O programa deve verificar e exibir se o 
# número digitado é par ou ímpar. 
num1 = int(input("Insira um número inteiro: "))
if num1 % 2 == 0:
    print(f"O número {num1}, é par")
elif num1 % 2 != 0:
    print(f"O número {num1}, é ímpar")

print("\n")
# Exercício 4: Média Escolar e Situação 
# Crie um programa que receba 3 notas de um aluno, calcule a média aritmética e informe 
# a situação: 
# • Média maior ou igual a 7.0: Aprovado 
# • Média entre 5.0 e 6.9: Recuperação 
# • Média menor que 5.0: Reprovado 
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
elif media <5:
    print("Reprovado")

print("\n")
# Exercício 5: Tabuada Interativa 
# Peça um número inteiro ao usuário e exiba a tabuada desse número (de 1 a 10) usando 
# um laço de repetição. 
num2 = int(input("Insira um número inteiro: "))
i = 1

while i<=10:
    print(num2*i)
    i = i+1

# Exercício 6: Contador Regressivo 
# Faça um programa que peça um número inteiro positivo ao usuário e faça uma 
# contagem regressiva a partir desse número até 0, exibindo "Fim!" ao final. 
num3 = int(input("Insira um número inteiro positivo: "))
while num3>=0:
    print(num3)
    num3 = num3 - 1

print("\n")
# Exercício 7: Lista de Compras 
# Crie um programa que permita ao usuário cadastrar 5 itens em uma lista de compras. Ao 
# final, o programa deve exibir todos os itens digitados em ordem alfabética. 
item1 = input("Insira um produto: ")
item2 = input("Insira um produto: ")
item3 = input("Insira um produto: ")
item4 = input("Insira um produto: ")
item5 = input("Insira um produto: ")

listaItens = [item1, item2, item3, item4, item5]
listaItens.sort() # Ativa ordem alfabética
print(listaItens)

print("\n")
# Exercício 8: Análise de Números (Maior, Menor e Soma) 
# Escreva um programa que receba 5 números inteiros do usuário, armazene-os em uma 
# lista e depois exiba: 
# 1. O maior número digitado. 
# 2. O menor número digitado. 
# 3. A soma de todos os números. 
num01 = float(input("Insira um número: "))
num02 = float(input("Insira um número: "))
num03 = float(input("Insira um número: "))
num04 = float(input("Insira um número: "))
num05 = float(input("Insira um número: "))

listaNum = [num01, num02, num03, num04, num05]
listaNum.sort() # Ordena em ordem numerica
print(listaNum[0]) #primeiro numero
print(listaNum[4]) #ultimo numero
print(sum(listaNum)) #Soma de todos os numeros da lista

print("\n")
# Exercício 9: Dicionário de Produtos e Preços 
# Crie um programa com um dicionário pré-cadastrado contendo 4 produtos e seus 
# respectivos preços. O programa deve solicitar ao usuário o nome de um produto e exibir 
# o preço correspondente. Caso o produto não exista, exiba a mensagem "Produto não 
# encontrado". 
prod1 = "SilverWolf"
prod2 = "Fuxuan"
prod3 = "Qingque"
prod4 = "Sparkle"

listaProd = [prod1, prod2, prod3, prod4]
pesq = input("Insira o nome de um produto: ")
print(pesq in listaProd)

print("\n")
# Exercício 10: Calculadora Simples com Função 
# Crie um programa que defina uma função chamada calcular(num1, num2, 
# operacao). A função deve aceitar dois números e um caractere representando a 
# operação (+, -, *, /) e retornar o resultado do cálculo. No programa principal, solicite os 
# valores ao usuário e chame a função.

num001 = float(input("Insira o primeiro numero: "))
num002 = float(input("Insira o segundo numero: "))
op =  input("Insira o operador aritmético: ")

def calcular(num001, num002, op):
    if op == "+":
        print(num001 + num002)
    elif op == "-":
        print(num001 - num002)
    elif op == "*":
        print(num001 * num002)
    elif op == "/":
        print(num001 / num002)

calcular(num001, num002, op)


    