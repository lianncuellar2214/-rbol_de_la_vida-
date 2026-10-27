from animal import Animal

class Vertebrado(Animal):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat)

        self.tiene_columna = True
        self.tipo_esqueleto = tipo_esqueleto