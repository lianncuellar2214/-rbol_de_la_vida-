from vertebrados import Vertebrado

class Mamifero(Vertebrado):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto,
                 tipo_pelaje, meses_gestacion):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tipo_esqueleto)

        self.tipo_pelaje = tipo_pelaje
        self.meses_gestacion = meses_gestacion

    def amamantar(self):
        print("El mamífero está amamantando a sus crías.")
        self.energia += 10

    def desplazarse(self):
        print("Corriendo en 4 patas")
        self.energia -= 10