def mostrar_menu():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Ver los resultados guardados hasta ahora')
    print('3: Finalizar')
    return input()

def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdigit():  # Verifica si es un número
            point = int(point)
            
            if point < 1 or point > 5:
                print('La puntuación debe estar entre 1 y 5.')
            else:
                print('Por favor, introduzca un comentario:')
                comment = input()
                post = f'Puntuación: {point}, Comentario: {comment}'
                
                file_pc = open("resultados.txt", 'a')  # Abre el archivo en modo 'añadir'
                file_pc.write(post + '\n')       # Guarda la puntuación y el comentario
                file_pc.close()                  # Cierra el archivo
                
                print("Puntuación y comentario guardados.")
                break
        else:
            print('Por favor, introduzca la puntuación como un número.')

def ver_resultados():
    try:
        file = open("resultados.txt", "r")  # Intenta abrir el archivo
        contenido = file.read()       # Lee el contenido del archivo
        file.close()                  # Cierra el archivo
        
        if contenido:                 # Verifica si hay algo en el archivo
            print("Resultados hasta ahora:")
            print(contenido)
        else:
            print("No hay resultados guardados.")
    except FileNotFoundError:         # Si el archivo no existe
        print("No hay resultados guardados.")

def ejecutar_programa():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            ingresar_puntuacion_y_comentario()
        elif opcion == '2':
            ver_resultados()
        elif opcion == '3':
            print('Finalizando...')
            break
        else:
            print('Por favor, selecciona una opción válida (1, 2 o 3).')

# Ejecutar el programa
ejecutar_programa()