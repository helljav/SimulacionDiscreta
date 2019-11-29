"""
*****************************************************************************************************

                                UNIVERSIDAD AUTONOMA METROPOLITANA
    ALUMNO: CARRILLO PACHECO FRANCISCO JAVIER
    MATRICULA: 2143008102
    PRACTICA 1, SIMULADOR DE UN JUEGO DE AZAR 

Considere un juego de lanzamiento de monedas con las siguientes reglas:
1. En cada juego se lanza una moneda no alterada en repetidas ocasiones, hasta que la
diferencia entre el número de caras y cruces que han aparecido sea tres.
2. Si desea participar debe pagar un peso cada vez que se lanza la moneda y no puede
abandonar el juego hasta que éste termine.
3. Al final de cada juego usted recibe 8 pesos independientemente del número de lanzamientos.

Se simulo este juego, se obtuvieron los datos al repetir el juego un determinado numero de veces
(prueba = [10,20,40,80,160,320,640,1280,2560]) y base a estos datos se grafico el promedio de lanzamientos
por cada conjunto de prueba y tambien se grafico el promedio de  ganancias o pérdidas por juego.
Base a estos resultados se concluyo que existe un peromedio de  9 lanzamientos por juego, por lo tanto el 
promedio de ganancias o perdidas es igual a -1 




******************************************************************************************************
"""





import random
import matplotlib.pyplot as plt
import numpy as np

cara = 0
cruz = 0
prueba = [10,20,40,80,160,320,640,1280,2560]#numero de juegos
pesitosPrueba = [0,0,0,0,0,0,0,0,0] #Representa cuantas veces fue lanzada la moneda por cada juego
arrjuegosGP = [0,0,0,0,0,0,0,0,0] #Representa cuantas veces gano por juegos

def main():

    contador = 0
    varAux = 0
    for prueb in prueba:
        for i in range(0,prueb):
            juego(pesitosPrueba, contador, cara, cruz, arrjuegosGP)            
        contador = contador +1

    #Posteriormente sacamos el promedio de lanzamientos/cojunto de los juegos
    for i in range(0,len(pesitosPrueba)):

        varAux2 = (8*prueba[i]) - pesitosPrueba[i]
        arrjuegosGP[i] = varAux2/prueba[i] 

        varAux = pesitosPrueba[i]/prueba[i]
        pesitosPrueba[i] = varAux



    print(pesitosPrueba)
    plt.xlabel("Número de juegos")
    plt.ylabel("Número promedio de lanzamientos")
    plt.plot(prueba,pesitosPrueba)
    plt.show()

    print(arrjuegosGP)
    plt.xlabel("Número de juegos")
    plt.ylabel("Número promedio de juegos ganados o perdidos")
    plt.plot(prueba,arrjuegosGP)
    plt.show()


def juego(pesitosPrueba, cont,cara,cruz,arrjuegosGP):
    while True:
        pesitosPrueba[cont] +=1
        num = np.random.uniform(0.0,1.0)
        if num <0.5:
            cara = cara +1        
        else:
            cruz = cruz + 1       

        if(cara-cruz) == 3 or (cruz -  cara ) == 3:
            break
    
    
   

main()
