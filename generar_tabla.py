from generar_comb import Generar_comb
from expresiones import Expresiones

class Hacer_tabla():
    def __init__(self,variables, expresiones):
        self.variables = variables
        self.expresiones = expresiones 
    def hacer_tabla(self):
        print("\nSe ha generado la siguiente tabla de verdad\n")
        # Encabezado
        encabezado = " | ".join(self.variables + self.expresiones)
        print(encabezado)
        print("-" * len(encabezado))
        
        # Generar combinaciones
        generador_combinaciones = Generar_comb(len(self.variables))
        combinaciones = generador_combinaciones.generar_combinaciones()
        
        for comb in combinaciones:  
            valores = [int(v) for v in comb]
            resultados = []
            for expr in self.expresiones:
                generador_resultado = Expresiones(expr, self.variables, comb)
                resultado = generador_resultado.evaluar_expresion()
                resultados.append(int(resultado))
            fila = " |  ".join(map(str, valores + resultados))
            print(fila)


