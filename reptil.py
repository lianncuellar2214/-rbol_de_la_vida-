from vertebrados import Vertebrado

class Anfibio(Vertebrado):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto, fase_vida):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tipo_esqueleto)

        self.fase_vida = fase_vida

    def respirar(self):
        if self.fase_vida == "Renacuajo":
            print("Respira por branquias")
        else:
            print("Respira por pulmones")  