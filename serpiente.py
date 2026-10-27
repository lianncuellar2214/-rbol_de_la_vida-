from reptil import Reptil

class Serpiente(Reptil):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto,
                 es_venenoso, tipo_escamas,
                 longitud, es_constrictora):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tipo_esqueleto,
                         es_venenoso, tipo_escamas)

        self.longitud = longitud
        self.es_constrictora = es_constrictora

    def atacar(self):
        if self.es_venenoso:
            print("La serpiente da una mordida venenosa.")
        elif self.es_constrictora:
            print("La serpiente se enrolla alrededor de su presa.")
        else:
            print("La serpiente se defiende.")

    def desplazarse(self):
        print("Deslizándose en zig-zag")