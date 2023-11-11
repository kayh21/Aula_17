#A classe é o incio de tudo e dela nasce o objeto 
#toda classe tem a primeira letra maiúscula
#classes guardam características, atributos ou métodos 
#self significa seu próprio
# identação vai seguir a ordem classe > função > condição 
#Exemplo o bolo seria um objeto, a recita seria a classe e o leite,ovos e tals seriam atributos da classe em forma de função
#atributos, caracteristicas ou métodos são variáveis
#Exemplo: 
# - **OBJETO É O FILHO DA CLASSE, PODE SER CONSIDERADO UM FILHOTE  -  OBJETOS**
# - **FILHOTES HERDAM CARACTERISTICAS DE SUAS MÃES  -  ATRIBUTOS**
# - **EXISTEM CORES E CARACTERISTICAS QUE NÃO SERÃO HERDADAS, OU VISUALIZADA  - ENCAPSULAMENTO**
# - **EXISTEM RAÇAS DE CACHORROS MAIS RAPIDAS, MAIS INTELIGENTES E MAIS QUIETAS - POLIFORMISMO**
# - **TODOS OS CACHORROS LATEM , ANDAM , MORDEM  -  MÉTODO**S

class Carro:
    def __init__(self, cor, km):
      self.cor = cor
      self.km = km
      
carro = Carro("preto", 250)

print(carro) #não imprimi
print(carro.cor)
print(carro.km)

class Casa:
    def __init__(self, color, length):
      self.color = color
      self.length = length
      
   

# EXERCÍCIO01 -  Crie uma classe chamada Cachorro com um atributo nome e um método latir que imprima "Woof!" quando chamado. Em seguida, crie um objeto da
#  classe Cachorro e chame o método latir.


class Dog:
    def __init__(self, nome, latir):
      self.nome = nome
      self.latir = latir

cachorro = Dog("Lili", "Woof!")
print(cachorro.latir)

# EXERCÍCIO02 - Crie uma classe chamada Retangulo com atributos largura e altura. Adicione um método chamado calcular_area que retorna a área do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
      self.largura = largura
      self.altura = altura

    def area(self):
        print(self.largura * self.altura)

rectagle = Retangulo (100, 100)
print(rectagle)
rectagle.area()

# EXERCÍCIO03 - Crie uma classe chamada Carro com um atributo chamado velocidade (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta 
# a velocidade em 5 unidades a cada vez que é chamado.

class Carro:
    def __init__(self, velocidade):
      self.velocidade = 0
      
    def aumentar(self):
        for v in range(self.velocidade,100,+5):
            print(v)
        
vel = float(input("Digite a velocidade inicial:\n"))
carro = Carro(vel)
carro.aumentar()

# DESAFIO - Crie uma classe chamada Conta_bancaria com um atributo saldo inicializado com 0. 
# Em seguida, crie métodos deposito e saque que atualizem o saldo. Crie um objeto da classe ContaBancaria, faça um depósito e um saque, e imprima o saldo resultante.
