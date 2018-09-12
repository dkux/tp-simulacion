class GeneradorNumeros:

    def __init__(self, incremento=None, multiplicador=None, modulo=None):
        if incremento is None:
            self.incremento = 1664525
        else:
            self.incremento = incremento
        if multiplicador is None:
            self.multiplicador = 1013904223
        else:
            self.multiplicador = multiplicador
        if modulo is None:
            self.modulo = 2 ** 32
        else:
            self.modulo = modulo

    def _generar_numero_random(self, x):
        valor = (self.multiplicador * x + self.incremento) % self.modulo
        return valor

    def generar_numeros(self, semilla, cantidad, normalizado=False):
        valores = [0] * cantidad
        for i in range(cantidad):
            if i == 0:
                valores[i] = self._generar_numero_random(semilla)
            else:
                valores[i] = self._generar_numero_random(valores[i - 1])
        if normalizado:
            for i, val in enumerate(valores):
                valores[i] = val / (self.modulo * 1.0)
        return valores

    def imprimir(self, array):
        for value in array:
            print value
