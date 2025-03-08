from validacion import Validacion
from generar_comb import Generar_comb

def MostrarMenu():
    print('MENÚ'.center(16,'*'))
    print('1. Generar Tabla de verdad \n2. Salir')

if __name__ == "__main__":
    while True:
        try:
            #mostrar menú y entrada
            MostrarMenu()
            entry = int(input('Elija una opción: '))
            
            #opción 1
            if entry == 1:
                variables = input('Ingrese las variables a utilizar separadas por comas: ')

                #utilizamos la clase de validación
                validador = Validacion(variables)

                #utilizamos el médtodo validar_variables que valida caracter por caracter si es una letra, la combierte en minuscula y valida si está en la lista
                lista_variables = validador.validar_variables()

                #utilizamos es método validar_N_varialbes que valida el tamaño
                if validador.validar_N_variables():
                    print("Variables válidas:", ", ".join(lista_variables))

                #utilizamos la clase generar_comb y junto al método generar_combinaciones genera las combinaciones de cada una de las variables 

                if lista_variables:



                    print('No se ha ingresado ninguna variable válida.')
            elif entry == 2:
                print('Saliendo del programa...')
                break 

            else:
                print('Opción inválida. Intenta de nuevo.')

        except ValueError:
            print('Error: Debes ingresar un número válido.')
