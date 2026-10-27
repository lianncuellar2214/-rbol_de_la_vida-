from animal import Animal
class Invertebrado(Animal):

    def __init__(self, nombre_cientifico, adn, dieta, habitat,
                 exoesqueleto, numero_patas, edad=0, energia=0):

        super().__init__(
            nombre_cientifico, adn, dieta, habitat, edad, energia
        )

        self.exoesqueleto = exoesqueleto
        self.numero_patas = numero_patas