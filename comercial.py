name_company = input("Insira o nome da empresa: ")
print (f'O nome da empresa é: {name_company}')

class carro :
    def __init__(self, marca, modelo, ano) :
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def informacoes (self) :
        print(f"marca: [{self.marca}], modelo: [{self.modelo}], ano: [{self.ano}]")
carro1 = carro ("chevrolet", "onix", "2024")
carro2 = carro ("peugot","208","2024")
carro1.informacoes()
carro2.informacoes()

class banco :
    def __init__(self, titular, saldo) :
        self.tiluar = titular
        self.saldo = saldo
    def depositar(self, valor) :
        self.saldo += valor
        print (f"valor do depósito: {valor}")
    def sacar (self, valor) : 
        self.saldo -= valor
        print (f"valor do saque: {valor}")
    def extrato (self) :
        return self.saldo
conta = banco("Maria Eduarda", 5000)
conta.depositar (3582)  
conta.sacar(2000)
print (f"saldo atual: R${conta.extrato()}")

class animal:
    def falar (self):
        return "O animal faz um barulho."
class cachorro(animal):
    def falar (self):
        return "O cachorro late"
class gato(animal):
    def falar (self):
        return "O gato mia"
cachorro1 = cachorro ()   
gato1 = gato ()
print (cachorro1.falar())
print (gato1.falar())

frutas = ["maça", "banana", "laranja", "uva", "morango"]
print ("lista inicial: ", frutas)
frutas.append ("abacaxi")
print ("após adicionar 'abacaxi': ", frutas)
frutas.insert(0, "morango")
print ("após inserir 'morango' no início: ", frutas)
print (len(frutas))
print (frutas.sort())
if "melancia" in frutas:
  print("melancia está na lista")
else:
    frutas.append("melancia")
print ("lista:", frutas)

estoque_frutas = {
  "maçã": 10,
  "banana": 25,
  "laranja": 15,
  "uva": 12,
  "manga": 8
}
estoque_frutas ["abacaxi"] = 20
estoque_frutas ["banana"] = 30
estoque_frutas.pop("laranja")
print ("quantidades de maçãs:", estoque_frutas["maçã"])
if "melancia" in estoque_frutas:
  print("melancia está na biblioteca")
else:
    estoque_frutas ["melancia"] = 5
frutas_dispoiveis = estoque_frutas.keys()
print ("biblioteca:", estoque_frutas)

def calcular_divisão():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        resultado = numerador/denominador
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except ValueError:
        print("Erro: só é aceito valores númericos.")
    else:
        print ("Resultado:", resultado)
    finally:
        print("Operação finalizada!")
calcular_divisão()