from vertebrados import Vertebrado

class Pez(Vertebrado):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto, tipo_agua):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tipo_esqueleto)

        self.tipo_agua = tipo_agua

    def desplazarse(self):
        print("Nadando rápidamente")

    def respirar(self):
        print("Filtrando oxígeno por branquias")