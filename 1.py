class Bola:
  def __init__(self, cor, circ, material):
    self.cor = cor
    self.circ = circ
    self.material = material
  def trocarCor(self,cor):
    self.cor = cor
  def mostrarCor(self):
    return self.cor

bola1 = Bola("Azul", 3, "Borracha")

bola1.trocarCor("Vermelho")
print(bola1.mostrarCor())