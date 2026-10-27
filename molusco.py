from invertebrados import Invertebrado

class Molusco(Invertebrado):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tiene_exoesqueleto,
                 numero_patas, tiene_concha, produce_tinta):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tiene_exoesqueleto,
                         numero_patas)

        self.tiene_concha = tiene_concha
        self.produce_tinta = produce_tinta

    def defenderse(self):
        if self.produce_tinta:
            print("Expulsa una nube de tinta.")
        else:
            print("Se esconde en su concha.")