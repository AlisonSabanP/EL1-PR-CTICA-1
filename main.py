from validacion import Validacion
from validar_expresiones import Validar_expresiones
from generar_tabla import Hacer_tabla

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

                    expresiones = input("Ingrese las expresiones lógicas: ")

                    #identifica una sola expresión de 3 caracteres sin comas y la convierte en una lista de un elemento.
                    if len(expresiones) == 3 and ',' not in expresiones:
                        lista_expresiones = [expresiones]
                    
                    #maneja cualquier otra entrada, dividiéndola por comas y limpiando espacios
                    else:
                        lista_expresiones = [expr.strip() for expr in expresiones.split(",")]

                    # validamos las expresiones con su clase y método 
                    validador_expresiones = Validar_expresiones(lista_expresiones, lista_variables)
                    expresiones_validas = validador_expresiones.validar_expresiones()

                    #en caso de haber errores los imprimimos
                    if validador_expresiones.expresiones_invalidas:
                        validador_expresiones.print_errores()
                    
                    #se imprimen las expresiones válidas y se genera la tabla 
                    if expresiones_validas: 
                        print('\nvariables validas:',','.join(expresiones_validas))

                        Generador_tabla = Hacer_tabla(lista_variables, expresiones_validas)
                        Generador_tabla.hacer_tabla()

                    else:
                        print('No se ha ingresado ninguna expresión válida')


                else:
                    print('No se ha ingresado ninguna variable válida')

            # si la opción es la no.2 se sale del programa 
            elif entry == 2:
                print('Saliendo del programa...')
                break 

            # en caso de no ingresar opción 1 o 2
            else:
                print('Opción inválida. Intenta de nuevo')
            
        # en caso de ingresar algo que no sea un int 

        except ValueError:
            print('Error: Debes ingresar un número válido')
