from plantas import Planta

class PlantaVascular(Planta):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_hoja, necesita_sombra, tiene_flor, tipo_tallo):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_hoja, necesita_sombra)

        self.tiene_flor = tiene_flor
        self.tipo_tallo = tipo_tallo

    def transportar_savia(self):
        print("La planta transporta nutrientes por la savia.")
        self.energia += 5