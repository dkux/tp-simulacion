class GeneradorNumeros:

    def __init__(self, incremento=None, multiplicador=None, modulo=None):
        if incremento is None:
            self._incremento = 1664525
        else:
            self._incremento = incremento
        if multiplicador is None:
            self._multiplicador = 1013904223
        else:
            self._multiplicador = multiplicador
        if modulo is None:
            self._modulo = 2 ** 32
        else:
            self._modulo = modulo

    def _generar_numero_random(self, x):
        valor = (self._multiplicador * x + self._incremento) % self._modulo
        return valor

    def generar_numeros(self, semilla, cantidad, normalizado=False):
        valores = [0] * cantidad
        for i in range(cantidad):
            if i == 0:
                valores[i] = semilla
            else:
                valores[i] = self._generar_numero_random(valores[i - 1])
        if normalizado:
            for i, val in enumerate(valores):
                valores[i] = val / (self._modulo * 1.0)
        return valores

    def imprimir(self, array):
        for value in array:
            print value
