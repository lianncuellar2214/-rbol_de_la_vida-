from serVivo import SerVivo

class Animal(SerVivo):

    def __init__(self, nombre_cientifico, edad, energia, adn,
                 tipo_dieta, habitat):

        super().__init__(nombre_cientifico, edad, energia, adn)

        self.tipo_dieta = tipo_dieta
        self.habitat = habitat

    def desplazarse(self):
        print(f"El animal se mueve por su hábitat: {self.habitat}")
        self.energia -= 5

    def alimentarse(self):
        if self.tipo_dieta == "Carnívoro":
            print("Cazando presa")
        elif self.tipo_dieta == "Herbívoro":
            print("Comiendo plantas")
        else:
            print("Comiendo alimentos variados")

        self.energia += 20