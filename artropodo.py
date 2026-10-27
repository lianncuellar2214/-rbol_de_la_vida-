from invertebrados import Invertebrado

class Artropodo(Invertebrado):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tiene_exoesqueleto,
                 numero_patas, tiene_alas, numero_antenas):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tiene_exoesqueleto,
                         numero_patas)

        self.tiene_alas = tiene_alas
        self.numero_antenas = numero_antenas

    def mudar_exoesqueleto(self):
        print("Desecha la coraza vieja para crecer.")
        self.energia -= 20