from vertebrados import Vertebrado

class Ave(Vertebrado):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat, tipo_esqueleto,
                 envergadura_alas, puede_volar):

        super().__init__(nombre_cientifico, edad, energia, adn,
                         tipo_dieta, habitat, tipo_esqueleto)

        self.envergadura_alas = envergadura_alas
        self.puede_volar = puede_volar
   
    def desplazarse(self):
        if self.puede_volar:
            print("Volando en el cielo")
        else:
            print("Caminando rápido")

        self.energia -= 15