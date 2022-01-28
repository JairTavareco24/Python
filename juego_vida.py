import random
print("Juego  escape de la prision\n"
       "---------------------------\n"
      "\n"
      "Tu y tu compañero de celda acaban de escapar de la celda, burlaron a los guardios y se \n"
      "dirigen hacia el exterior. Entran en una zona donde los guardias estan alertas, uno de los guardias\n"
      "ataca a tu compañero, se lo lleva pero tu pasas desarpecibido escondido en las sombras. El guardia se retira\n"
      "es tu posibilidad de escapar. Hacia donde te diriges?\n"
      "\n"
      "A la izquierda tienes una puerta semiabierta, a la derecha hay una escotilla en el suelo")

opcion = input("[OPCION (A) - Puerta semiabierta] | [OPCION (B) - Escotilla en el suelo]: ")

if opcion =="A":
    print("Entras en la puerta semiabierta y otro guardia te descubre, que haces?")
    opcion = input("[OPCION (A) - Te haces el muerto] | [OPCION (B) - Sales corriendo a toda velocidad]:")

    if opcion =="A":
        print("El guardia te atrapa y te manda al incinerador\n FIN")
    elif opcion =="B":
        print("Despues de correr un rato vez tirado un cuchillo, ¿lo tomas para conservarlo?")
        opcion = input("[OPCION (A) - SI] | [OPCION (B)-  NO]: ")

        if opcion == "A":
            print("Recoges el cuchillo y sIgues avanzando, al fondo hay dos pasillos, no ves final de ninguno "
                  "uno esta a la derecha y el otro a la izquierda, ¿Cual tomas?")
            opcion = input("[OPCION (A) - Derecha] | [OPCION (B)-  Izquierda]: ")

            if opcion =="A":
                print("La habitacion de hace cada vez mas oscura, ves tan poco que caes en un agujero en el suelo "
                      "con picos de metal, mueres al instante. \n FIN")
            elif opcion =="B":
                print("Encuentras la salida, en la puerta hay aparcado una moto, te subes y la enciendes"
                      "y huyes hacia el horizonte\n FIN")

elif opcion == "B":
    print("Caes en una zona innundada, el agua te llega hasta las rodillas, avanzas durante media hora y finalmente"
          " llegas a una zona abierta, seca y con luz, parecen unas alcantarillas\n\nEncuentras un palo largo, parece"
          " algo pesado, pero podria servir, ¿Lo tomas?")
    opcion = input("[OPCION (A) - SI] | [OPCION (B)-  NO]: ")

    palo_en_inventario = False
    if opcion == "A":
        print("Coges el palo contigo")
        palo_en_inventario = True
    elif opcion == "B":
        print("No coges el palo")
    else:
        print("no has elegido ninguna opcion vañida, por wey mueres")
        exit()
    numero_random_rata = random.randint(1, 100)
    print("Sigues adelante, encuentras un cholo, y el cholo te pregunta cuanto es 15 * {}).".format(
        numero_random_rata))
    opcion = int(input("¿Cual es el resultado? "))

    if opcion == 15 * numero_random_rata:
        print("La rata de asesina en el acto, resultaque no telera a los cerebritos.\nFIN")
    else:
        print("La rata abre una puerta delante de ti, parece un pasillo que lleva hasta la salida. Lo recoges, "
              "llegas al final, el tunel se derrumba detras de ti, no hay salida mas que un espacie de boca de  "
              "alcantarilla, pero esta lejos de tu alcance, ¿Que haces?")

        opcion = input("[OPCION (A) - Esperas a que alguien te rescate] | [OPCION (B)-  Intentas salir]:")

        if opcion == "A":
            print("Llegan un moton de guardias y te matan a macanazos, es tu fin\nFIN")
        elif opcion == "B" and palo_en_inventario == True:
            print("Usas el palo que cogiste antes para hacer un hoyo en la pared y salir de la carcel "
                  "En la puerta hay estacionado ferrari, te subes a el y es tu dia de suerte, las llaves estan ahi "
                  "huyes hacia el horizonte\nFIN")
        elif opcion == "B" and palo_en_inventario == False:
            print("No tienes como salir, si solo tuvieras un palo... pero no lo tienes ¿verdad? Asi que finalmente "
                   " te quedas atrapado.\nPasado un rato te quedas dormido y llegan los guardias y te matan.\nFIN")
else:
    print("No has elegido ninguna opcion valida, te mueres perro.")











