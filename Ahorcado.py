import random #Libreria de python que en este caso me permitira escoger una palabra random de mi lista de palabras
import os #Libreria de python que me permitira limpiar la consola
def menu():#Es un menu del juego donde elegiras entre jugar o salir del programa en cuestion
    print("------------------------MENU---------------------------")
    #Para jugar solo tendras que elegir entre este menu de opcion 1 o 2, 1 para jugar
    print("1.Jugador contra la maquina") #Se toma la palabra de un archivo aleatorio
    print("2.Salir")

def obtener_palabra():

    palabras = ["hola", "adios", "Complacer", "Coma", "Espumoso", "Mama", "Nuclear", "lugar",
                "Pesca", "Implicar", "Optimista", "Cero", "Pezuñas", "Desvanecimiento", "Cobre", "Explicación",
                "Retirar", "Zoom", "Innecesario", "Plano", "Desayuno", "Componer", "Problema", "Bovino",
                "Arcilla", "Cualquier", "momento", "Seda", "Raro", "Primero", "Minuto", "Equivocado", "Probado",
                "Diagonal", "Moneda", "Blanda", "Negro", "Estación", "Respaldar", "Lineal", "Examinador"]
    palabra = random.choice(palabras).lower() #Utilizo el random para que sea aleatorio y choice para elegir la palabra, lower para que sea minuscula
    return palabra

def ahorcado(cantVida):
    #Funcion para definir el ascii del ahorcado
    dibujo = [
        '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========'''
    ]

    print(dibujo[cantVida])



def juego():
    os.system('cls') #Limpio la consola al iniciar el juego
    jugar = True
    while jugar == True:
        print("------------Este es el juego de el ahorcado------------")
        menu()
        op = int(input("\nIngrese la opcion a elegir:\n-> "))
        #apartir de aqui comienza el juego, tendras que adivinar una palabra aleatoria, ingresando letra por letra o en su defecto 
        #ingresar la palabra "adivinar" si estas muy seguro de saber que palabra es , 
        #con cada intento si es incorrecta la letra te resta una vida, si es la palabra completa perdes toda tus vidas.
        os.system('cls')#Limpio la consola mientras mis vidas sean > 0
        if op == 1:
            palabra = obtener_palabra()
            vidas = 6 #int(vida(palabra))
            adivinada = ''
            letras_equivocada = [] #Lista donde se guardaran las letras ingresadas y que son incorrectas      
            letras_repetidas = [] #Lista donde se guardaran las letras ingresadas repetidas
            while vidas > 0:
               
                print(f"\nTienes {vidas} vidas")
                ahorcado(vidas)
                letras_advinidas = 0
                for letra in palabra:
                    if letra in adivinada:
                        print(letra, end="")
                    else:
                        print("_ ", end="")
                        letras_advinidas +=1               
                
                print(f"\nQuedan {letras_advinidas} letras")    
                           
                if letras_advinidas == 0:
                    print("\n┌(ㆆ㉨ㆆ)ʃ¡Ganaste! lograste adivinar la palabra┌(ㆆ㉨ㆆ)ʃ")               
                    print(f"\nLetras incorrectas: {', '.join(letras_equivocada)}")
                    break 

                if letras_advinidas == 2 and vidas > 1 :
                    opc = input("\nQuiere arriesgar la palabra completa? y/n: ").lower()
                    if opc == "y":
                        palabra_intentada = input("\nIngresa la palabra completa: ").lower()                        
                        if palabra_intentada == palabra:
                            print("\n┌(ㆆ㉨ㆆ)ʃ¡Ganaste adivinando la palabra completa!┌(ㆆ㉨ㆆ)ʃ")
                            if letras_equivocada == []:
                                print("\nNo te equivocaste en ninguna letra :D")
                            else:
                                print(f"\nLetras equivocadas: {', '.join(letras_equivocada)}")
                            break    
                        else:
                            print("\n Palabra incorrecta. Pierdes todas las vidas (╯°□°）╯︵ ┻━┻")
                            if letras_equivocada == []:
                                print("\nNo te equivocaste en ninguna letra :D")
                            else:
                                print(f"\nLetras equivocadas: {', '.join(letras_equivocada)}")
                            vidas = 0   
                
                letrain = input("\nIntroduce una letra: ").lower()

                if len(letrain) != 1 or not letrain.isalpha(): #.isalpha debuelve tru si los caracteres ingresado son letras
                    print('\nEl caracter ingresado no es una letra o es mas de una letra,Ingrese nuevamente una letra')
                    continue
                               
                letra_ingresada = letrain  #Le asigno el intento que seria la letra ingresada
                
                if letra_ingresada in letras_repetidas:  #Si la letra que ingreso es la misma que la ingresada anteriormente entonces le pide que ingrese otra
                    print("\n ''⌐(ಠ۾ಠ)¬''' Ya has ingresado esa letra, intenta con una diferente.")
                    continue  # Vuelve al inicio del bucle sin restar vidas
                    
                letras_repetidas.append(letra_ingresada) 
                adivinada += letra_ingresada
                                
                if letra_ingresada not in palabra: 
                        vidas -= 1 #Resto uno a la vida si la letra que ingreso no esta en la palabra tomada de la lista
                        letras_equivocada.append(letra_ingresada)   
                        print(f"Letra equivocada . Te quedan {vidas} vidas restantes.") 

                #Si la vida del jugador es  0 entonces este perdio el juego, es decir no adivno la palabra
                if vidas == 0:
                    print(f"\nPerdiste!, La palabra era: {palabra} (╯°□°）╯︵ ┻━┻")
                    if letras_equivocada == []:
                        print("\nNo te equivocaste en ninguna letra :D")
                    else:
                        print(f"\nLetras equivocadas: {', '.join(letras_equivocada)}")

                   
            juego = input("\nDeseas jugar otra vez y/n: ").lower()
            if juego == 'n':
                jugar = False
                os.system('cls')#Limpio la consola mientras mis vidas sean > 0
                print("---Gracias por jugar!---")
            else:
                continue
        else:
            exit()

juego()


