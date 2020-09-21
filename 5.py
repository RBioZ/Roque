class Conta:
  def __init__(self, numero, nome, saldo):
    self.numero = numero
    self.nome = nome
    self.saldo = saldo
  def trocarCor(self,cor):
    self.cor = cor
  def mostrarCor(self):
    return self.cor

bola1 = Bola("Azul", 3, "Borracha")

bola1.trocarCor("Vermelho")
print(bola1.mostrarCor())