# EN LA Clase validación se recibe el parametro de la entrada de variables 
class Validacion():
    def __init__(self, variables):
        self.variables = variables
        self.lista_variables = []

# en el método de validar_variables se itera en la cadena de texto y caracter por caracter  se valida si:
#1. es una letra usando el método .isalpha()
#2. se convierte en minúscula utilizando el método .lower()
#3. si está en la lista de variables válidas 
# si pasa los filtros nos retorna la lista de varialbes válidas
    def validar_variables(self):
        self.variables = self.variables.replace(' ','')
        for variable in self.variables:
            if variable.isalpha():
                variable = variable.lower()
                if variable not in self.lista_variables:
                    self.lista_variables.append(variable)
                else: 
                    print(f'la variable «{variable}» ya se encuentra en la lista, se omitirá')
            else:
                if variable != ',': 
                    print(f'la variable «{variable}» no es válida, se omitirá')
        return self.lista_variables

# en el método validar_N_variables, validamos el número de variables válidas que tenemos
# si son más de 3 entonces devuelve la lísta vacía 
# y si sonn 0 nos muestra un mensaje de añadir variables válidas
    def validar_N_variables(self):
        tamanio = len(self.lista_variables)

        if tamanio > 3:
            print('Las variables deben ser 3 o menos.')
            self.lista_variables = []  
            return False
        elif tamanio == 0:
            print('Debe ingresar al menos una variable válida')
            return False
        return True 

