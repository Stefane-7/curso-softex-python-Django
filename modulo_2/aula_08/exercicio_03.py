"""3. Nível Médio/Avançado: Hierarquia de Formas Geométricas

Crie uma classe base FormaGeometrica com um construtor para cor e um método
calcular_area() que não faz nada.

Crie uma classe Retangulo que herda de FormaGeometrica e tem atributos para largura e
altura. A classe deve sobrescrever o método calcular_area().

Crie uma classe Quadrado que herda de Retangulo. 
O construtor deve receber apenas o lado e passar esse mesmo valor para largura e altura da classe pai. O encapsulamento deve ser
aplicado aos atributos de dimensão.

No script principal, crie uma tupla com um objeto de Retangulo e um objeto de Quadrado.

Crie uma função chamada calcular_soma_areas() que recebe essa tupla, itera sobre ela e
soma a área de todas as formas. A função deve chamar o método calcular_area() de forma
polimórfica para cada objeto, exibindo a soma total no final."""

class FormaGeometrica:
    def __init__(self, cor: str):
        self.cor = cor

    def calcular_area(self):
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses.")


class Retangulo(FormaGeometrica):
    def __init__(self, largura: float, altura: float, cor: str):
        super().__init__(cor)
        self.__largura = largura
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    def calcular_area(self):
        return self.__largura * self.__altura


class Quadrado(Retangulo):
    def __init__(self, lado: float, cor: str):
        super().__init__(lado, lado, cor)


def calcular_soma_areas(formas: tuple):
    soma = 0
    for forma in formas:
        soma += forma.calcular_area()  # chamada polimórfica
    print(f"Soma total das áreas: {soma}")


# Script principal
ret = Retangulo(5, 10, "azul")
quad = Quadrado(4, "vermelho")

formas = (ret, quad)
calcular_soma_areas(formas)

    
  