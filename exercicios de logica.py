# 1 - Verificação de ímpar ou par

numero = int(input("Digite um numero inteiro: "));

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 2 - Verificação de maioridade
idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#3 - Positivo, negativo ou zero
numero = float(input("Digite um número"))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é 0")

#4 - Maior entre dois números
n1 = int(input("Digite um número"))
n2 = int(input("Digite outro número"))

if n1 > n2:
    print(f"O maior número é {n1}")
elif n1 < n2:
    print(f"O maior número é {n2}")
else:
    print("Os números são iguais")

#5 - Aprovação escolar média simples
nota1 = float(input("Digite a primeira nota"))
nota2= float(input("Digite a segunda nota"))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f"Média {media:.1f}: Aprovado")
elif media >= 5.0:
    print(f"Média {media:.1f}: Recuperação")
else:
    print(f"Média {media:.1f}: Reprovado")

#6 - Votação obrigatória
idade = int(input("Informe sua idade"))

if idade < 18:
    print("Não eleitor (não pode votar)")
elif (idade >=16 and idade <18) or idade >= 70:
    print("Voto facultativo")
else:
    print("Voto obrigatório")

#7 - Calculadora de turno de estudo
turno = input("Digite seu turno [M - Matutino | V - Vespertino | N - Noturno]: ").upper()

if turno == "M":
    print("Seja bem-vindo ao turno matutino")
elif turno == "V":
    print("Seja bem-vindo ao turno vespertino")
elif turno == "N":
    print("Seja bem vindo ao turno noturno")
else:
    print("Insira um turno válido")

#8 - Verificador de ano bissexto
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 == 0) or (ano % 400 == 0):
    print("O ano é bissexto") 
else:
    print("O ano não é bissexto")

#9 - Maior de três números
a = float(input("Digite um número"))
b = float(input("Digite outro número"))
c = float(input("Digite algum outro número"))

if a >= b and a >= c:
    maior = a
if b >= a and b >= c:
    maior = b
else:
    maior = c

print(f"O maior número é {maior}")

#10 - Desconto por quantidade de compras
valor = float(input("Valor total da compra, R$ "))

if valor > 300.0:
    desconto = valor * 0.15
elif valor >100.0:
    desconto = valor * 0.10
else:
    desconto = 0.00

total = valor - desconto
print(f"Total a pagar: R$ {total:.2f}")

#11 - Cálculo de IMC
peso = float(input("Digite o peso em kg"))
altura = float(input("Digite a altura em metros"))

imc = peso/(altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Peso Normal"
elif imc < 30.00:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"IMC {imc:.2f} - Classificação: {classificacao}")

#12 - Classificação de triângulos
a = float(input("Lado A:"))
b = float(input("Lado B:"))
c = float(input("Lado C:"))

    #Validação de existencia
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        tipo = "Equilátero (3 lados iguais)"
    elif a == b or a == c or b == c:
        tipo = "Isósceles (2 lados iguais)"
    else: 
        tipo = "Escaleno (3 lados diferentes)"
    print(f"Os lados formam um triângulo {tipo}")
else:
    print("Os segmentos informados não formam um triângulo")

#13 - Conversor de temperatura Celsius / Fahrenheit
print("1 - Celsius para fahrenheit")
print("2 - Fahrenheit para celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    c = float(input("Temperatura em celsius: "))
    f = (c * 9/5) + 32
    print(f"{c} Celsius equivale a {f:.2f} fahrenheit")
elif opcao == 2:
    f = float(input("Temperatura em fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f} Fahrenheit equivale a {c:.2f} celsius")

print("Opção inválida")

#14 - Calculadora de reajuste salarial 
salario = float(input("Digite o salário atual: R$ "))

if salario <= 2500.0:
    percentual = 15
elif salario <= 5000.0:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual/100)
novo_salario = aumento + salario

print(f"Percentual de aumento: {percentual}%")
print(f"Valor do aumento: {aumento:.2f}")
print(f"Novo salário {novo_salario:.2f}")

#15 - Verificação de múltiplos
n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))

if n2 == 0:
    print("Não é possível verificar divisão por zero")
elif n1 % n2 == 0:
    print(f"{n1} é multiplo de {n2}")
else:
    print(f"{n2} é multiplo de {n1}")

#16 - Calculadora simples de 4 operações
num1 = float(input("Primeiro número: "))
operador = input("Operação (+, -, *, /)")
num2 = float(input("Segundo número: "))

if operador == "+":
    res = num1 + num2
elif operador == "-":
    res = num1 - num2
elif operador == "*":
    res = num1 * num2
elif operador == "/":
    if(num2 == 0):
        res = "Erro: Divisão por zero"
    else:
        res = num1 / num2
else:
    print("Operador inválido")

print(f"Resultado {res}")

#17 - Verificação de triângulo de angulação
a1 = float(input("Ãngulo 1: "))
a2 = float(input("Ãngulo 2: "))
a3 = float(input("Ãngulo 3: "))

if (a1 + a2 + a3) == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    if a1 == 90 or a2 == 90 or a3 == 90:
        tipo = "Retângulo (posui um angulo de 90 graus)"
    elif a1 > 90 or a2 > 90 or a3 > 90:
        tipo = "Obtsângulo (Possui um ângulo maior que 90 graus)"
    else:
        tipo = "Acutângulo (Todos os ângulos menores que 90 graus)"
else:
    print("Os ângulos fornecidos  não formam um triângulo válido")

#18 - Validador de data (dia e mês)
dia = int(input("Dia: "))
mes = int(input("Mês: "))

if mes < 1 or mes > 12:
    print("Data inválida: mês inexistente")
elif mes in [1, 3, 5, 7, 8, 10, 12] and (1 <= dia <= 31):
    print("Data válida")
elif mes in [4, 6, 9, 11] and (1 <= dia <= 31):
    print("Data válida")
elif mes == 2 and (1 <= dia <= 28):
    print("Data válida")
else:
    print("Data inválida: dia fora do intervalo do mês")

#19 - Ordenação de dois números
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

if a <= b:
    print(f"Ordem crescente: {a}, {b}")
else:
    print(f"Ordem crescente: {b}, {a}")

#20 - Identificador do século
ano = int(input("Digite o ano (positivo): "))
if ano <= 0:
    print("Ano inválido")
else:
    seculo = (ano - 1) //100 + 1
    print(f"O ano {ano} pertence ao século {seculo}")

#21 - Simulador de crédito imobiliário
valor_casa = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Anos para pagar: "))

meses = anos * 12
parcela = valor_casa / meses
limite = salario * 0.30

print(f"Prestação mensal: R$ {parcela:.2f}")
if parcela <= limite:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado, parcela excede 30% do salário")

#22 - Cálculo de posto de combustível
tipo = input("Tipo de combustível (A - Álcool / G - Gasolina)").upper()
litros = float(input("Quantidade de litros: "))

if tipo == 'A':
    preco = 3.90
    if litros <= 20:
        desc = 0.03
    else:
        desc = 0.05
    total = litros * preco * (1 - desc)
    print(f"Total a pagar pelo álcool: R$ {total:.2f}")
elif tipo == 'G':
    preco = 5.50
    if litros <= 20:
        desc = 0.04
    else:
        desc = 0.06
    total = litros * preco * (1 - desc)
    print(f"Total a pagar pela gasolina: R$ {total:.2f}")
else:
    print("Tipo de combustível inválido")

#23 - Tabela imposto de renda (IRRF)
salario = float(input("Salário bruto: R$ "))

if salario <= 2259.20:
    aliquota = 0.0
elif salario <= 2826.65:
    aliquota = 7.5
elif salario <= 3751.05:
    aliquota = 15.0
elif salario <= 4664.68:
    aliquota = 22.5
else:
    aliquota = 27.5

imposto = salario * (aliquota/100)
print(f"Aliquota aplicada: {aliquota}% | Imposto estimado: R$ {imposto:.2f}")

#24 - Cálculo de frete por ditancia e peso
distancia = float(input("Distância em km: "))
peso = float(input("Peso em kg: "))
custo_base = 20.00

if distancia <= 100:
    custo_km = distancia * 1.50
else:
    custo_km = (100 * 1.50) + ((distancia - 100) * 1.00)

taxa_peso = 15.0 if peso > 10 else 0.0

total_frete = custo_base + custo_km + taxa_peso
print(f"Custo total do frete: R$ {total_frete:.2f}")

#25 - Forma de pagamento em loja
preco = float(input("Preço do produto: R$ "))
print("1 - À vista Dinheiro/PIX")
print("2 - À vista cartão")
print("3 - Em até 2x no cartão")
print("4 - 3x ou mais no cartão")
opcao = int(input("Escolha a opção de pagamento: "))

if opcao == 1:
    final = preco * 0.90
elif opcao == 2:
    final = preco * 0.95
elif opcao == 3:
    final = preco
    parcela = final / 2
    print(f"2 Parcelas de R$ {parcela:.2f}")
elif opcao == 4:
    final = preco * 1.20
    tot_parc = int(input("Quantas parcelas ? "))
    if tot_parc >= 3:
        parcela = final / tot_parc
        print(f"{tot_parc} parcelas de R$ {parcela:.2f}")
    else:
        print("Quantidade de parcelas inválida para esta opção")
else:
    final = preco
    print("Opção inválida")

print(f"Valor final a pagar: R$ {final:.2f}")

#26 - Sistema de comissão de vendas
meta = 10000.0
vendas = float(input("Total  vendido pelo funcionário: R$"))

percentual_meta = (vendas / meta) * 100

if percentual_meta < 80:
    comissao = 0.0
elif percentual_meta < 100:
    comissao = vendas * 0.03
elif percentual_meta <= 120:
    comissao = vendas * 0.05
else:
    comissao = vendas * 0.08

print(f"Meta atingida: {percentual_meta:.1f}% | Comissão a receber: R$ {comissao:.2f}")

#27 - Calculadora de diário de hotel
dias = int(input("Quantidade de dias hospedado"))
if dias < 5:
    taxa = 15.00
elif dias == 5:
    taxa = 10.00
else:
    taxa = 5.0

total = dias * (150.0 + taxa)
print(f"Valor total da hospedagem ({dias} dias: R$ {total:.2f})")

#28 - Análise de lucro de produto
custo = float(input("Valor de custo do produto: R$"))

if custo < 50.0:
    margem = 0.45
elif custo <= 100.0:
    margem = 0.35
else:
    margem = 0.25

venda = custo * (1 + margem)
print(f"Margem aplicada: {margem*100:.0f}% | Preço sugerido de venda: R$ {venda:.2f}")

#29 - Cálculo de horas extras trabalhadas
salario_base = float(input("Salário mensal básico: R$ "))
horas_trabalhadas = float(input("Total de horas trabalhadas no mês: "))
valor_hora = salario_base / 160.0

if horas_trabalhadas <= 160:
    extra = 0.0
elif horas_trabalhadas <=180:
    horas_extras = horas_trabalhadas - 160
    extra = horas_extras * (valor_hora * 1.5)
else:
    horas_50 = 20
    horas_100 = horas_trabalhadas - 180
    extra = (horas_50 * valor_hora * 1.5) + (horas_100 * valor_hora * 2.0)

salario_total = salario_base + extra
print(f"Valor adicional de horas extras: R$ {extra:.2f}")
print(f"Salário final a receber: R$ {salario_total:.2f}")

#30 - Verificador de eligibilidade para desconto de estudante
estudante = input("Possui carteira de estudante? (s/n):").lower() == "s"
idade = int(input("Informa sua idade: "))
pcd = input("É pessoa com deficiência ? (s/n)").lower() == "s"

if estudante or idade >= 60 or pcd:
    print("Benefício concedido: direito á meia-entrada")
else:
    print("Ingresso inteiro (sem descont aplicável)")

#31 - Categorização de atletas por idade
idade = int(input("Digite a idade do atleta: "))

if idade < 5:
    categoria = "Não tem idade minima para competir"
elif idade <= 7:
    categoria = "Infantil A"
elif idade <= 10:
    categoria = "Infantil B"
elif idade <= 13:
    categoria = "Juvenil A"
elif idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"

print(f"Categoria do atleta: {categoria}")

#32 - Classificação conceitual de notas
nota = float(input("Digite a nota (de 0 a 10)"))

if nota < 0 or nota > 10:
    conceito = "Nota inválida"
elif nota >= 9.0:
    conceito = "A"
elif nota >= 7.5:
    conceito = "B"
elif nota >= 6.0:
    conceito = "C"
elif nota >= 4.0:
    conceito = "D"
else:
    conceito = "F"

print(f"Conceito final obtido: {conceito}")

#33 - Verificação de triangulo retangulo (pitágoras)
lados = [float(input("Lado 1: ")), float(input("Lado 2: ")), float(input("Lado 3: "))]
lados.sort() #Garante que o maior fique por ultimo

cat1, cat2, hip = lados[0], lados[1], lados[2]

if abs((cat1**2 + cat2**2) - (hip**2)) < 1e-5:
    print("Os lados formam um triangulo retangulo perfeito")
else:
    print("Os lados não formam um triangulo retangulo")

#34 - Identificador de estação de dano no hemisfério sul
dia = int(input("Dia do mês: "))
mes = int(input("Mês (1 a 12): "))

if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20):
    estacao = "Verão"
elif (mes == 3 and dia >= 20) or mes in [4, 5] or (mes == 6 and dia < 21):
    estacao = "Outono"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 23):
    estacao = "Inverno"
else:
    estacao = "Primavera"

print(f"Estação do ano aproximada: {estacao}")

#35 - Validador de força de senha
senha = input("Crie uma senha: ")

tem_num = any(char.isdigit() for char in senha)
tem_especial = any(char in "!@#$%%¨&*" for char in senha)

if(len(senha) >= 8 and tem_num and tem_especial):
    print("Senha forte e aprovada")
elif len(senha) >= 8 and tem_num and tem_especial:
    print("senha média, adicione simbolos especiais para melhorá-la")
else:
    print("Senha fraca, requisitos: pelo menos 8 caracteres, 1 numero e 1 simbolo")

#36 - Classificação da pressão arterial
sistolica = int(input("Pressão sistolica (maxima) : "))
diastolica = int(input("Pressão diastólica (mínima) : "))

if sistolica < 120 and diastolica < 80:
    status = "Pressão normal"
elif (120 <= sistolica <= 139) or (80 <= diastolica <= 89):
    status = "Pré-hipertensão"
elif (140 <= sistolica <= 159) or (90 <= diastolica <= 99):
    status = "Hipertensão etágio 1"
else:
    status = "Hipertensão estágio 2 | Crise"

print(f"Diagnóstico preliminar: {status}")

#37 - Sistema de controle de estoque
estoque_atual = int(input("Quantidade atual em estoque: "))
estoque_minimo = int(input("Quantidade mínima de segurança: "))

if estoque_atual <= 0:
    print("Alerta crítico: Estoque zerado")
elif estoque_atual < estoque_minimo:
    print("Alerta, estoque abaixo do mínimo")
elif estoque_atual == estoque_minimo:
    print("Atenção, estoque na marca de segurança")
else:
    print("Estoque em nível regular")

#38 - Validador de triângulos por ângulos
a1 = float(input("Ângulo 1:"))
a2 = float(input("Ângulo 2:"))
a3 = float(input("Ângulo 3:"))

    #Validação de existencia
if (a1 + a2 + a3) == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    if a1 == a2 == a3:
        print("Triângulo equiângulo")
    elif a1 == a2 or a2 == a3 or a1 == a3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Ângulos inválidos pra um triângulo")

#39 - Calculadora de consumo de energia elétrica
consumo = float(input("Consumo em kwh no mês: "))

if consumo <= 100:
    tarifa = 0.50
elif consumo <= 300:
    tarifa = 0.75
else: 
    tarifa = 1.00

valor_energia = consumo * tarifa
taxa_iluminacao = 15.00
total = valor_energia + taxa_iluminacao

print(f"Valor da energia: R$ {valor_energia:.2f}")
print(f"Total da contacom iluminação pública: R$ {total:.2f}")

#40 - Verificação de quadrante no plano cartesiano
x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))

if x == 0 and y == 0:
    print("O ponto está na origem (0, 0)")
elif x == 0:
    print("O ponto está sobre o Eixo Y.")
elif y == 0:
    print("O ponto está sobre o Eixo X.")
elif x > 0 and y > 0:
    print("Quadrante 1 (Q1)")
elif x < 0 and y > 0:
    print("Quadrante 2 (Q2)")
elif x < 0 and y < 0:
    print("Quadrante 3 (Q3)")
else:
    print("Quadrante 4 (Q4)")

#41 - Jodo pedra, papel e tesoura
import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)

print("Opções: [0] Pedra | [1] Papel | [2] Tesoura")
jogador = int(input("Qual a sua jogada ?"))

if jogador not in [0, 1, 2]:
    print("Jogada inválida")
else:
    print(f"Computador jogou: {itens[computador]}")
    print(f"Você jogou: {itens[jogador]}")

    if computador == jogador:
        print("Empate")
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print("Você venceu !")
    else:
        print("Computador venceu")

#42 - Calculadora de radar de velocidade e multa
velocidade = float(input("Velocidade registrada no veícul (km/h): "))
limite = 80.0

if velocidade <= limite:
    print("Velocidade dentro do limite permitido")
else:
    excesso_percentual = ((velocidade - limite) / limite) * 100
    if excesso_percentual <= 20:
        multa = 130.16
        infracao = "Média (+4 pontos na CNH)"
    elif excesso_percentual <= 50:
        multa = 195.23
        infracao = "Grave (+5 pontos na CNH)"
    else:
        multa = 880.41
        infracao = "Gravíssima (+7 pontos e suspensão da CNH)"

print(f"Excesso: {excesso_percentual:.1f}")
print(f"Infração: {infracao} | Valor da multa: R$ {multa:.2f}")

#43 - Simulador de login com bloqueio de tentativas
usuario_correto = "admin"
senha_correta = "123"

usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso concedido")
elif usuario != usuario_correto and senha == senha_correta:
    print("Usuário não cadastrado")
elif usuario == usuario_correto and senha != senha_correta:
    print("Senha incorreta")
else:
    print("Erro: usuário e senha inválidos")

#44 - Simulador de caixa eletrônico
saque = int(input("Valor do saque (Apenas múltiplos de 10): R$ "))
if saque <= 0 or saque % 10 != 0:
    print("Valor de saque inválido! O caixa só possui notas de R$ 50, R$ 20 e R$ 10.")
else:
    notas50 = saque // 50
    resto = saque % 50
    notas20 = resto // 20
    resto = resto % 20
    notas10 = resto // 10
    print("Distribuição de notas:")
    if notas50 > 0: print(f"- {notas50} nota(s) de R$ 50,00")
    if notas20 > 0: print(f"- {notas20} nota(s) de R$ 20,00")
    if notas10 > 0: print(f"- {notas10} nota(s) de R$ 10,00")

#45 - Verificador de palíndromo
texto = input("Digite uma palavra ou frase: ")
# Limpeza: remove espaços e coloca em minúsculas
texto_limpo = texto.replace(" ", "").lower()
texto_invertido = texto_limpo[::-1]
if texto_limpo == texto_invertido:
    print(f"'{texto}' é um palíndromo!")
else:
    print(f"'{texto}' não é um palíndromo.")

#46 - Conversor de moedas dinâmico
brl = float(input("Valor em Reais (R$): "))
print("Moedas disponíveis: [1] Dólar (USD) | [2] Euro (EUR) | [3] Libra (GBP)")
moeda = int(input("Converter para: "))

cot_dolar = 5.20
cot_euro = 5.60
cot_libra = 6.50

if moeda == 1:
    convertido = brl / cot_dolar
    print(f"R$ {brl:.2f} = US$ {convertido:.2f}")
elif moeda == 2:
    convertido = brl / cot_euro
    print(f"R$ {brl:.2f} = € {convertido:.2f}")
elif moeda == 3:
    convertido = brl / cot_libra
    print(f"R$ {brl:.2f} = £ {convertido:.2f}")
else:
    print("Moeda inválida!")

#47 - Sistema de triagem de pronto socorro
print("Triagem Médica:")
dor_intensa = input("Paciente apresenta dor no peito ou falta de ar grave? (s/n):").lower() == 's'
sangramento = input("Apresenta sangramento ativo moderado/grave? (s/n): ").lower() == 's'
febre_alta = input("Febre acima de 39°C? (s/n): ").lower() == 's'

if dor_intensa:
    prioridade = "VERMELHO - Atendimento Imediato (Emergência)"
elif sangramento or febre_alta:
    prioridade = "AMARELO - Atendimento Urgente (Até 60 min)"
else:
    prioridade = "VERDE - Pouco Urgente (Atendimento por ordem)"

    print(f"Classificação de Risco: {prioridade}")

#48 - Validados de equação de segundo grau
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

if a == 0:
    print("Não é uma equação do 2o grau (a deve ser diferente de 0).")
else:
    delta = (b ** 2) - (4 * a * c)
    print(f"Valor de Delta: {delta:.2f}")
if delta > 0:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f"Possui duas raízes reais distintas: x1 = {x1:.2f} e x2 = {x2:.2f}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Possui apenas uma raiz real (raízes duplas): x = {x:.2f}")
else:
    print("Não possui raízes reais no conjunto dos Números Reais (Delta negativo).")


#49 - Calculadora de Desconto de Ingressos por Idade e Horário
preco_base = 40.0
hora = int(input("Horário da sessão (hora inteira 0-23): "))
idade = int(input("Idade do cliente: "))
desconto = 0.0

# Desconto de horário
if hora < 17:
    desconto += 0.20

    # Desconto por faixa etária
if idade < 12 or idade >= 60:
    desconto += 0.30
else:
    estudante = input("É estudante? (s/n): ").lower() == 's'
if estudante:
    desconto += 0.15

preco_final = preco_base * (1 - desconto)
print(f"Desconto total acumulado: {desconto * 100:.0f}%")
print(f"Preço do ingresso: R$ {preco_final:.2f}")




#50 - Avaliador de Perfil do Cliente para Investimentos
print("--- Questionário de Perfil de Investidor ---")
print("1 - Prefiro total segurança, mesmo rendendo pouco.")
print("2 - Aceito pequenos riscos para render um pouco mais.")
print("3 - Aceito oscilações e riscos para buscar alta rentabilidade.")
p1 = int(input("Escolha sua postura diante do mercado (1-3): "))

print("\nSe seus investimentos caírem 20% no mês, você:")
print("1 - Resgata tudo imediatamente.")
print("2 - Aguarda a recuperação sem movimentar.")
print("3 - Aproveita para investir mais dinheiro barato.")
p2 = int(input("Sua reação (1-3): "))

pontos = p1 + p2

if pontos <= 2:
    perfil = "CONSERVADOR (Foco em Renda Fixa e Tesouro Direto)"
elif pontos <= 4:
    perfil = "MODERADO (Mistura de Renda Fixa e Fundos Imobiliários)"
else:
    perfil = "ARROJADO (Foco em Ações, Criptoativos e Renda Variável)"
    print(f"\nSua Pontuação Total: {pontos}")