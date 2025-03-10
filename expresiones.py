#la clase Expresiones nos sirve para devolver los resultados de la expresión
#como parametros tiene expr(las expresiones) vars(las variables), valores(lo valores de las variables a operar )
class Expresiones():
    def __init__(self, expr, vars, valores):
        self.expr = expr
        self.vars = vars
        self.valores = valores

    #el método utiliza los atributos para calcular los resultados de la expresión
    def evaluar_expresion(self ):
        if len(self.expr) == 1:  
            return self.valores[self.vars.index(self.expr)]
        # si la expresión no es de una sola variable, entonces se descompone en lo siguiente:
        #var1(variable 1),op (operador), var2(variable 2), v1(valor 1), v2(valor 2)
        var1 = self.expr[0]
        op = self.expr[1]
        var2 = self.expr[2]
        v1 = self.valores[self.vars.index(var1)] 
        v2 = self.valores[self.vars.index(var2)]
        
        # el if identifica el tipo de operador que tenemos y le asigna su respectiva operación 
        if op == '^': 
            return v1 and v2
        elif op == 'v':  
            return v1 or v2
        elif op == '⊕':  
            return v1 != v2
        elif op == '→':  
            return (not v1) or v2
        elif op == '↔':  
            return v1 == v2
        

