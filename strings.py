## Exercício 1 – Criando uma String
nome = "Maria";
print(nome);

nome = "Joãozinho";
print(nome);

nome = "Marley";
print(nome);

print("\n")

    #! Exercício 2 – Descobrindo o tipo
print(type("python"))

print(type(67.67))

print(type(248))

print("\n")

    #! Exercício 3 – Quantidade de caracteres
palavra = "Computador"
print(len(palavra))

palavra = "Pneumoultramicroscopicosilicovulcanoconiótico"
print(len(palavra))

palavra = "The same type of stand as star platinum"
print(len(palavra))

print("\n")

    #! Exercício 4 – Primeira letra
palavra = "Python"
print(palavra[0])

palavra = "Yggdrasil"
print(palavra[0])

palavra = "Ragnarok"
print(palavra[0])

print("\n")

    #! Exercício 5 – Última letra
palavra = "Python"
print(palavra[-1])

palavra = "Yggdrasil"
print(palavra[-1])

palavra = "Ragnarok"
print(palavra[-1])

print("\n")

    #! Exercício 6 – Três primeiras letras
palavra = "Computador"
print(palavra[:3])

palavra = "América"
print(palavra[:3])

palavra = "Asadelta"
print(palavra[:3])

print("\n")

    #! Exercício 7 – Três últimas letras
palavra = "Computador"
print(palavra[:-3])

palavra = "América"
print(palavra[:-3])

palavra = "Asadelta"
print(palavra[:-3])

print("\n")

    #! Exercício 8 – Letras maiúsculas
print("python".upper())

print("i dont know anymore".upper())

print("what".upper())

print("\n")

    #! Exercício 9 – Letras minúsculas
print("PYTHON".lower())

print("I DONT KNOW ANYMORE".lower())

print("WHAT".lower())

print("\n")

    #! Exercício 10 – Primeira letra maiúscula
print("python".capitalize())

print("i dont know anymore".capitalize())

print("what".capitalize())

print("\n")

    #! Exercício 11 – Remover espaços
texto = " Olá "
print(texto.strip())

texto = " What could have been rings through the night "
print(texto.strip())

texto = " lost love echoes in the single pale moonlight "
print(texto.strip())

print("\n")

    #! Exercício 12 – Substituir texto
cor = "azul"
print(cor.replace("azul","verde"))

cor = "roxo"
print(cor.replace("roxo","azul"))

cor = "amarelo"
print(cor.replace("amarelo","vermelho"))

print("\n")

    #! Exercício 13 – Verificar palavra
print("Py" in "Python")

print("sky" in "Let the sky fall")

print("crumble" in "When it crumbles")

print("\n")

    #! Exercício 14 – Encontrar posição
print("Python".find("t"))

print("We will stand tall".find("w"))

print("Face it all together".find("l"))

print("\n")

    #! Exercício 15 – Repetir texto
print("Oi"*3)

print("For Spartha"*3)

print("We fight"*3)

print("\n")

    #! Exercício 16 – Concatenar strings
print("Bom "+"dia")

print("I have "+"my mother's dream")

print("And i have my "+"father's eyes")

print("\n")

    #! Exercício 17 – Contar letras
print("banana".count("a"))

print("you cant take that from me".count("a"))

print("just go ahead and try".count("a"))

print("\n")

    #! Exercício 18 – Começa com
print("Python".startswith("Py"))

print("Help is".startswith("He"))

print("on the way".startswith("on"))

print("\n")

    #! Exercício 19 – Termina com
print("Python".endswith("on"))

print("they say".endswith("ay"))

print("help is on the way".endswith("ay"))

print("\n")

    #! Exercício 20 – Dividir texto
frutas = "maçâ, banana, uva"
print(frutas.split(","))

frutas = "coco, tomate, laranja"
print(frutas.split(","))

frutas = "kiwi, mexerica, pera"
print(frutas.split(","))

print("\n")

    #! Exercício 21 – Juntar lista
palavras = ["Python ", "é ", "legal"]

palavras = ["Wake ", "me ", "up inside"]

palavras = ["I dont ", "want ", " to hear"]

print("\n")

    #! Exercício 22 – Inverter texto
print("Python"[::-1])

print("Caos"[::-1])

print("Tragédia"[::-1])

print("\n")

    #! Exercício 23 – Entrada do usuário
nome = input("Digite seu nome: ")
print("Olá: ",nome)

cep = input("Digite seu CEP: ")
print("CEP: ",cep)

cpf = input("Digite seu CPF: ")
print("CPF: ",cpf)

print("\n")

    #! Exercício 24 – F-String
nome = "João"
print(f"Bem-vindo,{nome}!")

nome = "joseph joestar"
print(f"Bem-vindo,{nome}!")

nome = "yoshikage kira"
print(f"Bem-vindo,{nome}!")

print("\n")

    #! Exercício 25 – Somente números?
print("12345".isdigit())

print("25702".isdigit())

print("ami?".isdigit())

print("\n")

    #! Exercício 26 – Somente letras?
print("Python".isalpha())

print("StarPlatinum".isalpha())

print("WonderOfU".isalpha())

print("\n")

    #! Exercício 27 – Letras e números
print("Python123".isalpha())

print("matemátic4".isalpha())

print("sc1ence".isalpha())

print("\n")

    #! Exercício 28 – Primeira letra maiúscula de cada palavra
print("curso de python".title())

print("i am just the boy".title())

print("inside the man".title())

print("\n")

    #! Exercício 29 – Centralizar texto
print("Python".center(20))

print("not exactly".center(25))

print("who you think i am".center(30))

print("\n")

    #! Exercício 30 – Formatar nome completo
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
print((nome + " " + sobrenome).upper())