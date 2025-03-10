from generar_comb import Generar_comb
from expresiones import Expresiones
# IMPORTAMOS LAS GENERACIONES DE COMBINACIÓN Y la evaluacion de expresiones 
# la tabla tiene los parametros de las variablse y las expresiones 

class Hacer_tabla():
    def __init__(self,variables, expresiones):
        self.variables = variables
        self.expresiones = expresiones

    def hacer_tabla(self):
        #primero nos muestra los encabezados, uniendo las variables y las expresiones 
        print("\nSe ha generado la siguiente tabla de verdad\n")
        encabezado = " |  ".join(self.variables + self.expresiones)
        print(encabezado)
        print("-" * len(encabezado))
        
        #se crea un generador para las combinaciones y se le da el parametro de el no. de variables 
        # se utiliza el metodo de generar combinaciones para obtener los valores 
        generador_combinaciones = Generar_comb(len(self.variables))
        combinaciones = generador_combinaciones.generar_combinaciones()

        #se itera en los valores y se les convierte a valores numéricos (0, 1)

        for comb in combinaciones:  
            valores = [int(v) for v in comb]
            resultados = []

            # se itera en las expresiones y se instancia en la clase de Expresiones(expresión, variables, valores) y se utiliza el método de evaluar_expresion 
            for expr in self.expresiones:
                generador_resultado = Expresiones(expr, self.variables, comb)
                resultado = generador_resultado.evaluar_expresion()
                # a la lista de resultados se les agrega el resultado de cada una de las operaciones 
                resultados.append(int(resultado))

            #luego se imprime cada una de los valores + los resultados de las operaciones por fila 
            fila = " |  ".join(map(str, valores + resultados))
            print(fila)


