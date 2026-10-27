from serVivo import SerVivo
class Planta (SerVivo):

    def __init__(self, nombre_cientifico, adn, tipo_hoja,
                 necesita_sombra, edad=0, energia=0):

        super().__init__(nombre_cientifico, adn, edad, energia)

        self.tipo_hoja = tipo_hoja
        self.necesita_sombra = necesita_sombra

    def alimentarse(self):
        self.cambiar_energia(10)
        print("La planta realiza la fotosíntesis gracias a la luz del sol.")