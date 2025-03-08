class Generar_comb:
    def __init__(self, n):
        self.n = n 

    def generar_combinaciones(self):
        if self.n == 1:
            return [[False], [True]]
        else:
            generador_previo = Generar_comb(self.n - 1)
            combinaciones_previas = generador_previo.generar_combinaciones()
            resultado = []
            for comb in combinaciones_previas:
                resultado.append(comb + [False] )
                resultado.append(comb + [True])
            return resultado
