#Clase validar expresiones, tiene como parámetros la lista de expresiones y lista de variables 
# tambien tiene una lista con todos los operadores que son operables, en las expresiones invalidas agregamos todas las expresiones no procesadas 
# y en las válidas se agregan las expresiones que son operables para nuestro programa 
class Validar_expresiones:
    def __init__(self, expresiones, variables):
        self.variables = variables 
        self.operadores_validos = ['^', 'v', '⊕', '→', '↔']
        self.expresiones = expresiones 
        self.expresiones_invalidas = []
        self.expresiones_validas = []  

    #en este método validamos si son menos de 3 expresiones 
    #sí es así, entonces se reemplazan los espacios vacíos y parentesis si hubieran, Tambien se hace mínuscula 
    #asignamos los valores a diferentes variables para poder comparar individualmente. Si:
    # 1. alguna de las dos variables no está dentro de las ingresadas
    # 2. si el operador no es válido
    # la expresión no es valida y la agrega a las expresiones por mostrar como invalidas 
    #si todo esta bíen devuelve las expresiones válidas


    def validar_expresiones(self):
        self.expresiones_invalidas = []
        self.expresiones_validas = []


        if len(self.expresiones) > 3:
            self.expresiones_invalidas.append('Máximo 3 expresiones')
            return self.expresiones_validas 


        for expr in self.expresiones:
            expr = expr.replace(' ','')
            expr = expr.replace('(','')
            expr = expr.replace(')','')
            expr = expr.lower()
            es_valida = True  

            if len(expr) == 3:  
                var1, op, var2 = expr[0], expr[1], expr[2]

                if var1 not in self.variables or var2 not in self.variables:
                    self.expresiones_invalidas.append(f'Expresión «{expr}» usa variables no ingresadas.')
                    es_valida = False

                if op not in self.operadores_validos:
                    self.expresiones_invalidas.append(f'Operador «{op}» no válido.')
                    es_valida = False

            else:
                self.expresiones_invalidas.append(f'Expresión «{expr}» no válida.')
                es_valida = False

            if es_valida:
                self.expresiones_validas.append(expr)

        return self.expresiones_validas 
    
    #imprime las expresiones invalidas o errores
    
    def print_errores(self):
        for message in self.expresiones_invalidas:
            print(message)

