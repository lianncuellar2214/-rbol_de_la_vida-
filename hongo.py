from serVivo import SerVivo
class Hongo(SerVivo):

    def __init__(self, nombre_cientifico, adn, venenoso,
                 edad=0, energia=0):

        super().__init__(nombre_cientifico, adn, edad, energia)

        self.venenoso = venenoso

    def alimentarse(self):
        print("El hongo absorbe nutrientes de materia orgánica en descomposición.")