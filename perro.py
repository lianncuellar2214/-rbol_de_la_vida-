from mamifero import Mamifero

class Perro(Mamifero):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto,
                 tipo_pelaje, meses_gestacion, raza, nivel_lealtad):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tipo_esqueleto,
                         tipo_pelaje, meses_gestacion)

        self.raza = raza
        self.nivel_lealtad = nivel_lealtad

    def ladrar(self):
        print("¡Guau, guau! El perro está defendiendo su territorio.")