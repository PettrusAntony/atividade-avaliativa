class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'O veiculo de modelo {self.marca} está acelerando')

    def frear(self):
        print(f"O veículo: {self.modelo} está freando")

class Carro(Veiculo):
    def __init__(self, cor, modelo, marca):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print('O carro está com a porta aberta')

class Moto(Veiculo):
    def __init__(self, cilindrada, empinar, marca, modelo):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
        self.empinar = empinar

    def cilindrada(self):
        print('A fan tem 160 cilindradas')

    def empinar(self):
        print('Um garoto está empinando sua Fan 160')

if __name__ == "__main__":
    motos = Moto("160","0", "Honda", "Fan")
    carros = Carro("Azul", "Corolla", "Toyota")

    print(carros.cor)
    print(carros.marca)
    print(motos.cilindrada)
