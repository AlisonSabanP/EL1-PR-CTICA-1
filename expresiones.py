class Expresiones():
    def __init__(self, expr, vars, valores):
        self.expr = expr
        self.vars = vars
        self.valores = valores

    def evaluar_expresion(self ):
        if len(self.expr) == 1:  # Variable sola
            return self.valores[self.vars.index(self.expr)]
        
        var1 = self.expr[0]
        op = self.expr[1]
        var2 = self.expr[2]
        v1 = self.valores[self.vars.index(var1)]
        v2 = self.valores[self.vars.index(var2)]
        
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