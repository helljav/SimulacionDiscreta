"""
*****************************************************************************************************

                                        UNIVERSIDAD AUTONOMA METROPOLITANA


            ALUMNO: CARRILLO PACHECO FRANCISCO JAVIER
            MATRICULA: 2143008102
            PRACTICA 2, Simulacion de un banco con una sola caja version2.0


******************************************************************************************************
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import math

prueba = [10,20,40,80,160,320,640,1280,2560,10000,15000,20000,25000,30000]#numero de simulaciones
promClientes = [0]*len(prueba)
promEspera = [0]*len(prueba)



def Simulacion(cont):
    """
        Como condiciones iniciales (en tiempo = 0 ), no hay ninngun cliente, entonces generamos una hora de llegada y despues iniciamos el ciclo
        Paara generar horas de salida debe de haber clientes y no haya registro una hora de salida 

    """
    rA = np.random.uniform(0.0,1.0)
    time = 0
    clientes = []
    tLlegada = []
    horaLlegada = [(math.log(1-rA)/-3)*60]
    horaSalida = []
    contadorClientes = 0
    horaCierre = 480
    tEspera = []
    nt = 0

    while time<=horaCierre:
        #print("Soy el tiempo :", time)
        """Checo si hay una hora llegada y una hora salida para comparar, si no, significa que no hay una hora salida programada"""
        if len(horaSalida)>0 and len(horaLlegada)>0:

            """Si la llegada es mas pronta que la salida se atiende primero"""
            if(horaLlegada[0]<horaSalida[0]):
                #print("llego un cliente a la hora: ", horaLlegada)
                time +=  horaLlegada.pop(0)
                clientes.append(1)
                nt +=1
                tLlegada.append(time)
                """Siempre se genera una nueva hora de entrada cuando ocurre uuna llegada"""
                rA = np.random.uniform(0.0,1.0)
                nuevaHoraLlegada = (math.log(1-rA)/-3)*60
                horaLlegada.append(nuevaHoraLlegada + time)
                #print("se genero una nueva Llegada",horaLlegada)

                """ Checamos si se puede generar una hora de salida"""
                if(len(clientes)>0 and len(horaSalida) ==0):
                    rD = np.random.uniform(0.0,1.0)
                    nuevaHoraSalida = (math.log(1-rD)/-5)*60
                    horaSalida.append(nuevaHoraSalida + time)
                    #print("se genero una nueva Salida",horaSalida)

            else:

                """Este caso se hace cuando la hora de salida es mas pequeña de la de llegada"""
                #print("Salio un cliente a la hora: ", horaSalida)
                time += horaSalida.pop(0)
                clientes.pop(0)
                nt -=1
                tEspera.append((time-tLlegada.pop(0))/60)
                contadorClientes +=1

                if(len(clientes)>0):
                    """Si hay mas clientes generamos una nueva salida"""
                    rD = np.random.uniform(0.0,1.0)
                    nuevaHoraSalida = (math.log(1-rD)/-5)*60
                    horaSalida.append(nuevaHoraSalida + time)
                    #print("se genero una nueva Salida",horaSalida)

        elif(len(horaSalida)==0):
            #print("llego un cliente a la hora: ", horaLlegada)
            time +=  horaLlegada.pop(0)
            clientes.append(1)
            nt +=1
            tLlegada.append(time)
            
            """Siempre se genera una nueva hora de entrada cuando ocurre uuna llegada"""
            rA = np.random.uniform(0.0,1.0)
            nuevaHoraLlegada = (math.log(1-rA)/-3)*60
            horaLlegada.append(nuevaHoraLlegada + time)
            #print("se genero una nueva Llegada",horaLlegada)

            """ En este caso siempre generamos una salida"""           
            rD = np.random.uniform(0.0,1.0)
            nuevaHoraSalida = (math.log(1-rD)/-5)*60
            horaSalida.append(nuevaHoraSalida + time)
            #print("se genero una nueva Salida",horaSalida)

    #print(contadorClientes)
    #print(len(tEspera))
    #print(tEspera) 
    #SACAMOS EL PROMEDIO DE ESPERA DE TODOS LOS CLIENTES EN ESTA SIMULACION
    PromedioEspera = sum(tEspera)/contadorClientes
    ##print(numeroIntervalos)
    promEspera[cont] = promEspera[cont] + PromedioEspera



def main():
    #Simulacion()
    contador = 0
    for prueb in prueba:
        for i in range(0,prueb):
            Simulacion(contador)            
        contador = contador +1

    
    for i in range(0,len(prueba)):
        # varAux = promClientes[i]/prueba[i]
        # promClientes[i] = varAux
        varAux = promEspera[i]/prueba[i]
        promEspera[i] = varAux

    plt.xlabel("Número de juegos")
    plt.ylabel("Número promedio de espera")
    plt.plot(prueba,promEspera)
    plt.show()


main()
