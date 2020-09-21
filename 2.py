class Quadrado:
  def __init__(self, tamanho):
    self.tamanho = tamanho
  def mudarValorTamanho(self, newTamanho):
    self.tamanho = newTamanho
  def retornarValorTamanho(self):
    return self.tamanho
  def calcularArea(self):
    return self.tamanho * self.tamanho

quadrado1 = Quadrado(5)

quadrado1.mudarValorTamanho(3)
print(quadrado1.calcularArea())