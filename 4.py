class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
  def envelhecer(self, anos):
    if(self.idade <= 21 ):
      self.crescer(anos)
    self.idade += anos
    return self.idade

  def engordar(self, peso):
    self.peso += peso
    return self.peso

  def emagrecer(self, peso):
    self.peso -= peso
    return self.peso

  def crescer(self, anos):
    self.altura = anos * 0.5
    return self.altura

pessoa1 = Pessoa("Pedro", 5, 20, 70)

pessoa1.envelhecer(5)
print(pessoa1.altura)