class Carro:
  def __init__(self, modelo):
    self.modelo = modelo

  def ExibirModelodesteCarro(self):
    print('Modelo: BMW')
  def Carro(self):
    print('Carro: 320I M Sport 2.0')
  def Ano(self):
    print('Ano: 2022')
  def Valor(self):
    print('Valor atual: R$336.950')
  def Combustivel(self):
    print('Combustível: Flex(álcool/gasolina)')
  def Lugares(self):
    print('Lugares: 5')
  def Configuração(self):
    print('Configuração: Sedã')

carro1 = Carro('Modelo')
carro1.ExibirModelodesteCarro()
carro1.Carro()
carro1.Ano()
carro1.Valor()
carro1.Combustivel()
carro1.Lugares()
carro1.Configuração()
