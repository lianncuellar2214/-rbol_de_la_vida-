from plantavascular import PlantaVascular

class Arbol(PlantaVascular):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_hoja, necesita_sombra, tiene_flor,
                 tipo_tallo, da_frutos, altura):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_hoja, necesita_sombra,
                         tiene_flor, tipo_tallo)

        self.da_frutos = da_frutos
        self.altura = altura

    def mudar_hojas(self):
        if self.tipo_hoja == "Caduca":
            print("El árbol deja caer sus hojas.")
        else:
            print("El árbol mantiene sus hojas.")