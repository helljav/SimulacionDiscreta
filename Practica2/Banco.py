"""
*****************************************************************************************************

                                UNIVERSIDAD AUTONOMA METROPOLITANA
    ALUMNO: CARRILLO PACHECO FRANCISCO JAVIER
    MATRICULA: 2143008102
    PRACTICA 2, Simulacion de un banco con una sola caja 




******************************************************************************************************
"""

import random
import matplotlib.pyplot as plt
import numpy as np

prueba = [10,20,40,80,160,320,640,1280,2560,10000,15000,20000,25000,30000]#numero de juegos
promClientes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Representa cuantas veces fue lanzada la moneda por cada juego
promEspera = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Representa cuantas veces gano por juegos

def simulacion(cont):
    time  = 0.1
    clientes = []
    tLlegada = []
    tEspera = []
    clientesIntervalo = []
    EsperaTotal = 0
    ClientesTotalIntervalos = 0
    PromedioClientes = 0
    PromedioEspera = 0
    numeroIntervalos = -10  

    while True:
        time = time + 0.1
        rA = np.random.uniform(0.0,1.0)
        rD = np.random.uniform(0.0,1.0)
        if(len(clientes)>0 and rD<0.393):
            # Con el pop(0) simulamos la cola
            clientes.pop(0)
            tEsperaCliente = time - tLlegada.pop(0)
            tEspera.append(tEsperaCliente)
        if(rA<0.259):
            clientes.append(1)
            tLlegada.append(time)
        
        clientesIntervalo.append(len(clientes))
        numeroIntervalos = numeroIntervalos + 1
        if(time>8 and len(clientes) == 0):
            break
        
        
    
    # SACAMOS LA SUMA DE EL TIEMPO DE ESPERA DE CADA CLIENTE 
    EsperaTotal = sum(tEspera)
    #SACAMOS EL PROMEDIO DE ESPERA DE TODOS LOS CLIENTES EN ESTA SIMULACION
    PromedioEspera = EsperaTotal/len(tEspera)
    #print(numeroIntervalos)
    promEspera[cont] = promEspera[cont] + PromedioEspera

    #SACAMOS LA SUMA DE LOS CLIENTES QUE ESTUVIERON EN CADA INTERVALO
    ClientesTotalIntervalos = sum(clientesIntervalo)

    #SACAMOS EL PROMEDIO DE LOS CLIENTES QUE HAY EN CADA INTERVALO EN ESTA SIMULACION
    
    PromedioClientes = ClientesTotalIntervalos/numeroIntervalos

    promClientes[cont] = promClientes[cont] + PromedioClientes


def main():
    contador = 0
    for prueb in prueba:
        for i in range(0,prueb):
            simulacion(contador)            
        contador = contador +1

    #Posteriormente sacamos el promedio de lanzamientos/cojunto de los juegos
    for i in range(0,len(prueba)):
        varAux = promClientes[i]/prueba[i]
        promClientes[i] = varAux

        varAux = promEspera[i]/prueba[i]
        promEspera[i] = varAux


    plt.xlabel("Número de juegos")
    plt.ylabel("Número promedio de espera")
    plt.plot(prueba,promEspera)
    plt.show()



    plt.xlabel("Número de juegos")
    plt.ylabel("Número promedio de clientes")
    plt.plot(prueba,promClientes)
    plt.show()    



main()
