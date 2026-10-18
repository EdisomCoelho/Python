## Classe mensagem
class mensagem:
    def exibi_saudacao(self):
        print("Olá! Bem-vindo ao mundo de POO em Python")

minha_mensagem = mensagem()
minha_mensagem.exibi_saudacao()

## Constructor Init
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

usuario = Pessoa("Carlos", "Silva")
print(f"Nome do usuário: {usuario.nome} {usuario.sobrenome}")
##* O método init é o construtor da classe, roda automaticamente ao criarmos o objeto
##* O escopo self fixa as variáveis recebidas como atributos permanentes da instância

##Método com parametros
class Calculadora:
    def somar(self, numero1, numero2):
        return numero1 + numero2

calc = Calculadora()
resultado = calc.somar(15,25)
print(f"Resultado da somA: {resultado}")

## Alterando atributos através de métodos
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.quilometragem = 0

    def dirigir(self, distancia):
        self.quilometragem +- distancia

meu_carro = Carro("Sedan")
meu_carro.dirigir(50)
meu_carro.dirigir(32)

# Objeto interagindo com outro objeto
class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, oponente):
        oponente.vida -= 10

heroi = Jogador("Guerreiro", 100)
monstro = Jogador("Orc", 50)
heroi.atacar(monstro)

## Atributos privados
class contaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def exibir_saldo(self):
        return f"Saldo: R${self._saldo:.2f}"

conta = contaBancaria("Ana", 1000)
##* __ Ativa o Name Mangling no python, o que impede a modificação direta  da variável por fora da classe

## Métodos Getters e Setters tradicionais
class Ventilador:
    def __init__(self):
        self.__velocidade = 0
    def get_Velocidade(self):
        return self.__velocidade
    def set_velocidade(self,nova_v):
        if 0 <= nova_v <= 3: self.__velocidade = nova_v
##* Os métodos get e set atuam como filtros de segurança. A condicional restringe a alteração da velocidade ao intervalo válido

## Usando o decorador @property
class Pet:
    def __init__(self, nome, idade):
        self.__idade = idade
    @property
    def idade(self):
        return self.__idade

meu_pet = Pet("T-Rex", 4)
print(meu_pet.idade)
##* O decorador @property converte um método em uma propriedade de leitura

## Propriedades com Setter decorado
class Produto:
    def __init__(self, nome, preco):
        self.preco = preco
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, v):
        self.__preco = 0 if v < 0 else v
##* associado o @preco.setter, barramos valores inconsistentes, se uma tentativa de inserção negativa for reliazada, o sistema redefine o preço para 0

## Métodos privados
class Cofre:
    def __init__(self, senha):
        self.__senha = senha
    def __validar(self, senha):
        return senha == self.__senha
    def abrir(self, senha):
        if self.__validar(senha) : print("Aberto")

## Herança simples
class Animal:
    def __init__(self, nome) : self.nome = nome
    def emitir_som(self): print("som")
class Cachorro(Animal):
    def latir(self): print(f"{self.nome}: auauauaua")

## A função super()
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
class Gerente(Funcionario):
    def __init__(self, nome, salario, dept):
        super().__init__(nome, salario)
        self.dept = dept

##* A dirtiva super().__init__ invoca o construtor da superclasse, que executa o mapeamento padrão de dados da mão e libera a filha a ter parametros unicos

## Sobrescrita de método (Override)
class Ave:
    def voar(self):print("Voando alto")
class Pinguim(Ave):
    def voar(self):print("Não voa :()")

p = Pinguim()
p.voar()

## Herança múltipla
class Relogio:
    def hora(self):print("14:00h")
class Calendario:
    def data(self):print("25/12")
class Smartwatch(Relogio, Calendario):
    pass

##* Python aceita a derivação de multiplas classes ao mesmo tempo, a classe smartwatch agrega o catálogo completo de funções pertencentes a ambas as bases

## Verificação de tipos
class Veiculo: pass
class Moto(Veiculo): pass
biz = Moto()
print(isinstance(biz, Veiculo))
print(issubclass(Moto, Veiculo))

##* O comando isinstance valida se um objeto pertence ou descende de um molde
##* O comando issubclass checa a árvore genealógica de herança das classes textualmente

## Polimorfismo com funções
class Circulo:
    def desenhar(self):print("Circulo")
class Quadrado:
    def desenhar(self):print("Quadrado")
def render(forma):
    forma.desenhar()

render(Circulo())
##* A função render executa  a assinatura .desenhar() sem se importar com o tipo do objeto passado, permitindo comportamentos múltiplos sob a mesma chamada

## Polimorfismo em listas
class Aviao:
    def mover(self):print("Voando")
class Navio:
    def mover(self):print("Navegando")

frota = [Aviao(), Navio()]
for v in frota: v.mover()

## Classes abstratas conceituais
class NotaFiscal:
    def cacular_imposto(self):
        raise NotImplementedError("Obirgatório implementar")
class NotaServico:
    def calcular_imposto(self):return 15.0
##* Lançar NotImplementedError cria um bloqueio conceitual que notifica os desenvolvedores de que a reescrita do método é obrigatória nas subclasses

## O módulo ABC
from abc import ABC, abstractmethod
class Controle(ABC):
    @abstractmethod
    def ligar(self):pass
class TV(Controle):
    def ligar(self):print("Ligada")
##* Herdando de ABC e marcando rotinas com @abstractmethod, o sistema proíbe a instanciação direta da classe base

## Sobrecarga de operadores
class Vetor:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)
##* O método Add altera o comportamento padrão do operador aritmético + quando posicionado entre instâncias da classe personalizada, unindo suas propriedades

## O método STR
class Livro:
    def __init__(self, t, a):self.t, self.a = t,a
    def __str__(self):
        return(f"'{self.t}' por '{self.a}'")
print(Livro("Dom Casmurro", "Machado"))
##* O método STR intercepta requisições de conversão textual. Em vez de exibir o ponteiro de memória hexadecimal do objeto, retorna a string amigável configurada

## O método Len
class Playlist:
    def __init__(self, m):self.m = m
    def __len__(self):
        return len(self.m)

print(len(Playlist(["Música A", "Música B"])))
##* O método Len conecta o objeto diretamente à função global integrada len, repassando o resultado da contagem de dados da lista encapsulada

## Atributos de classe (Variáveis estáticas)
class Estudante:
    total = 0
    def __init__(self, nome):
        self.nome = nome
        Estudante.total += 1
##* A variável total reside diretamente no corpo da classe, e não nas instancias

## Métodos de classe (@classmethod)
class Data:
    def __init__(self, d, m, a): self.d, self.m, self.a = d, m, a
    @classmethod
    def de_string(cls, texto):
        d, m, a = map(int, texto.split("-"))
        return cls(d, m, a)
##* Métodos decorados com @classmethod recebem a classe em si(cls) em vez da instancia

## Métodos estáticos (@staticmethod)
class Validador:
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
##* Métodos anotados com @staticmethod operam como funções lógicas comuns acopladas ao bloco

## Associação simples
class Paciente:pass
class Medico:
    def __init__(self):
        self.paciente_atual = None
d = Medico
p = Paciente
d.paciente_atual = p
##* Associação ocorre quando duas entidades mantém ciclos de vida independentes, porém guardam uma referência temporária ou permanente de conexão em outro sistema

## Agregação
class Produto:pass
class Carrinho:
    def __init__(self):self.produtos = []
    def add(self, p):self.produtos.append(p)

c = Carrinho()
c.add(Produto())
##* O objeto container agrupa as partes contruidas externamente. Caso a instancia de Carrinho seja apaga os objetos de Produto continuam na memoria

## Composição
class Sala:pass
class Predio:
    def __init__(self):
        self.salas = [Sala(), Sala()]

meu_predio = Predio()
##* As instancias de Sala são geradas diretamente no construtor de prédio, excluindo o prédio as salas deixariam de existir

## Sistema de login com permissões
class Usuario:
    def __init__(self, user, senha):
        self.user = user
        self.__senha = senha
    def login(self, u, s):
        return self.user == u and self.__senha == s
class Admin(Usuario):
    def reset(self):print("Servidores reiniciados")


## Folha de pagamento completa
from abc import ABC, abstractmethod
class Colaborador(ABC):
    @abstractmethod
    def ganhos(self):pass
class Horista(Colaborador):
    def ganhos(self):return 160*25
class Folha:
    @staticmethod
    def rodar(lista):
        return sum(c.ganhos() for c in lista)
##* Centraliza uma classe abstrata de controle, ramifica cálculos polimórficos de salário e consolida o processamento via estático do salário