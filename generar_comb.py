# la clase Generar_comb, tiene como parámetro n, donde n es igual a la cantidad de variables a las cuales se les generarán combinaciones 


class Generar_comb:
    def __init__(self, n):
        self.n = n 
    
    # este metodo devuelve una matriz en donde cada elemento representa una combinación de valores booleanos 

    def generar_combinaciones(self):
        # si self.n nos devuele una lisa en donde tenemos solo los 2 valores (verdadero y falso)
        if self.n == 1:
            return [[False], [True]]
        
        # si self.n es diferente a 1 entonces entra en una recursión donde se manda a llamar al método de generar combinaciones 
        # en donde n = 1 es el tope e inicia con los valores F  T
        # Luego el valor es de n = 2 y se le suma a la combinación previa de F  T 
            #continua como [F F] [F  T]  [T F] [ T T]
        # y al solo aceptarse 3 variables 3 es el valor final de n 
        else:
            generador_previo = Generar_comb(self.n - 1)
            combinaciones_previas = generador_previo.generar_combinaciones()
            resultado = []
            for comb in combinaciones_previas:
                resultado.append(comb + [False] )
                resultado.append(comb + [True])
            return resultado
