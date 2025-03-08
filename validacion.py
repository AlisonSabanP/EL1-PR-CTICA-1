class Validacion():
    def __init__(self, variables ):
        self.variables = variables
        self.lista_variables = []

    def validar_variables(self):
        for variable in self.variables:
            if variable.isalpha():
                variable = variable.lower()
                if variable not in self.lista_variables:
                    self.lista_variables.append(variable)
                else: 
                    print(f'la variable «{variable}» ya se encuentra en la lista, se omitirá')
        return self.lista_variables

    def validar_N_variables(self):
        tamanio = len(self.lista_variables)

        if tamanio > 3:
            print('Las variables deben ser 3 o menos.')
            self.lista_variables = []  # Reiniciar la lista si hay más de 3 variables
            return False
        elif tamanio == 0:
            print('Debe ingresar al menos una variable válida')
        return True

    def validar_expresiones(expresiones, variables):
        for expr in expresiones:
            for char in expr:
                if char.isalpha() and char not in variables:
                    print(f"Error: La expresión '{expr}' contiene una variable no declarada ('{char}').")
                    return False
        return True
