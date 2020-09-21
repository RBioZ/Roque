class Retangulo:
  def __init__(self, ladoA, ladoB):
    self.ladoA = ladoA
    self.ladoB = ladoB
  def mudarValorLados(self,  ladoA, ladoB):
    self.ladoA = ladoA
    self.ladoB = ladoB
  def retornarValorTamanho(self):
    return(self.ladoA,self.ladoB)
  def calcularArea(self):
    return self.ladoA * self.ladoB
  def calcularPerimetro(self):
    return self.ladoA + self.ladoB

altura = 0;
largura = 0;

print('[INFORME A MEDIDA DO LOCAL]')
altura = int(input('ALTURA: '))
largura = int(input('LARGURA: '))


retangulo1 = Retangulo(altura,largura)

print('\n\n[AREA] : ',retangulo1.calcularArea())
print('[PERIMETRO] : ',retangulo1.calcularPerimetro())