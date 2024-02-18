class CalculadoraArea:
    def calcular_area(self, formas):
        areas = []
        for forma in formas:
            if isinstance(forma, Quadrado):
                areas.append(forma.lado ** 2)
            elif isinstance(forma, Circulo):
                areas.append(3.14 * (forma.raio ** 2))
        return sum(areas)

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

class Circulo:
    def __init__(self, raio):
        self.raio = raio
