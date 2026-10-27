class SerVivo:
    def __init__(self, nombre_cientifico, adn, edad,altura):
        self.nombre_cientifico = nombre_cientifico
        self.edad = edad
        self.altura = altura
        self.__adn = adn

    def obtener_adn(self):
        return self.__adn

    def nacer(self):
        self.altura = 1.70
        print(f"{self.nombre_cientifico} ha nacido.")

    def morir(self):
        self.energia = 0
        print(f"{self.nombre_cientifico} ha fallecido.")

    def alimentarse(self):
        pass