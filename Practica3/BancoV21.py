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

prueba = [10]#numero de simulaciones
promClientes = [0]*len(prueba)
promEspera = [0]*len(prueba)



def Simulacion(cont,cientes):
    """
        Como condiciones iniciales (en tiempo = 0 ), no hay ninngun cliente, entonces generamos una hora de llegada y despues iniciamos el ciclo
        Paara generar horas de salida debe de haber clientes y no haya registro una hora de salida 

    """
    rA = np.random.uniform(0.0,1.0)
    rD = 0
    time = 0
    clientes = []
    tLlegada = []
    deltaAT = (math.log(1-rA)/-3)*60
    deltaTD = 0
    horaLlegada = [deltaAT]
    horaSalida = []
    contadorClientes = 0
    tEspera = []
    nt = 0
    clientesintervalo = []
    
    print("tiempo\t\t\tnt\t\t\tra\t\tdeltaTA\t\t\trd\t\t\tdeltaTD\t\tHorallegada\t\tHoraSalida")
    print(time,"\t","\t",nt,"\t","\t",rA,"\t","\t",deltaAT,"\t","\t",rD,"\t","\t",deltaTD,horaLlegada,horaSalida)
    while contadorClientes<=cientes:
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
                clientesintervalo.append(nt)

                """Siempre se genera una nueva hora de entrada cuando ocurre uuna llegada"""
                rA = np.random.uniform(0.0,1.0)
                deltaAT = (math.log(1-rA)/-3)*60
                horaLlegada.append(deltaAT + time)
                #print("se genero una nueva Llegada",horaLlegada)

                """ Checamos si se puede generar una hora de salida"""
                if(len(clientes)>0 and len(horaSalida) ==0):
                    rD = np.random.uniform(0.0,1.0)
                    deltaTD = (math.log(1-rD)/-5)*60
                    horaSalida.append(deltaTD + time)
                    #print("se genero una nueva Salida",horaSalida)

            elif(horaSalida[0]<horaLlegada[0]):

                """Este caso se hace cuando la hora de salida es mas pequeña de la de llegada"""
                #print("Salio un cliente a la hora: ", horaSalida)
                time += horaSalida.pop(0)
                clientes.pop(0)
                nt -=1
                tEspera.append((time-tLlegada.pop(0))/60)
                contadorClientes +=1
                clientesintervalo.append(nt)

                if(len(horaLlegada)==0):
                    rA = np.random.uniform(0.0,1.0)
                    deltaAT = (math.log(1-rA)/-3)*60
                    horaLlegada.append(deltaAT + time)


                if(len(clientes)>0 and len(horaSalida)==0):
                    """Si hay mas clientes generamos una nueva salida"""
                    rD = np.random.uniform(0.0,1.0)
                    deltaTD = (math.log(1-rD)/-5)*60
                    horaSalida.append(deltaTD + time)
                    #print("se genero una nueva Salida",horaSalida)

        elif(len(horaSalida)==0  and len(horaLlegada)>0):
            #print("llego un cliente a la hora: ", horaLlegada)
            time +=  horaLlegada.pop(0)
            clientes.append(1)
            nt +=1
            tLlegada.append(time)
            clientesintervalo.append(nt)
            """Siempre se genera una nueva hora de entrada cuando ocurre uuna llegada"""
            rA = np.random.uniform(0.0,1.0)
            deltaAT = (math.log(1-rA)/-3)*60
            horaLlegada.append(deltaAT + time)
            #print("se genero una nueva Llegada",horaLlegada)

            if(len(clientes)>0 and len(horaSalida)==0):
                """ En este caso siempre generamos una salida"""           
                rD = np.random.uniform(0.0,1.0)
                deltaTD = (math.log(1-rD)/-5)*60
                horaSalida.append(deltaTD + time)

        elif(len(horaSalida)==0 and len(horaSalida)>0):
            time += horaSalida.pop(0)
            clientes.pop(0)
            nt -=1
            tEspera.append((time-tLlegada.pop(0))/60)            
            contadorClientes +=1
            clientesintervalo.append(nt)

            if(len(horaLlegada)==0):
                rA = np.random.uniform(0.0,1.0)
                deltaAT = (math.log(1-rA)/-3)*60
                horaLlegada.append(deltaAT + time)


            if(len(clientes)>0 and len(horaSalida)==0):
                """Si hay mas clientes generamos una nueva salida"""
                rD = np.random.uniform(0.0,1.0)
                deltaTD = (math.log(1-rD)/-5)*60
                horaSalida.append(deltaTD + time)
                #print("se genero una nueva Salida",horaSalida)
        print(time,"\t",nt,"\t",rA,"\t",deltaAT,"\t",rD,"\t",deltaTD,horaLlegada,horaSalida)
            #print("se genero una nueva Salida",horaSalida)
    

    #print(contadorClientes)
    #print(len(tEspera))
    #print(tEspera) 
    #SACAMOS EL PROMEDIO DE ESPERA DE TODOS LOS CLIENTES EN ESTA SIMULACION
    PromedioEspera = sum(tEspera)/contadorClientes
    ##print(numeroIntervalos)
    promEspera[cont] = PromedioEspera

    promCliet = sum(clientesintervalo)

    promClientes[cont] = promCliet/(time/8)



def main():
    #Simulacion()
    contador = 0
    for prueb in prueba:
        Simulacion(contador,prueb)            
        contador = contador +1
    #print(promEspera)

    
    # for i in range(0,len(prueba)):
    #     # varAux = promClientes[i]/prueba[i]
    #     # promClientes[i] = varAux
    #     varAux = promEspera[i]/prueba[i]
    #     promEspera[i] = varAux

    # plt.xlabel("Número de juegos")
    # plt.ylabel("Número promedio de espera")
    # plt.plot(prueba,promEspera)
    # plt.show()

    # #print(promClientes)
    # plt.xlabel("Número de juegos")
    # plt.ylabel("Número promedio de clientes")
    # plt.plot(prueba,promClientes)
    # plt.show()


main()
























# """
# Vazquez Ruiz Celso Esteban

# Simulacion que nos permite obtener
# el promedio de tiempo de espera de un banco
# y el numero promedio de clientes en el sistema (en la fila)
# Enuenciado del ejemplo
# Banco con una soloa fila en la caja
# Suponga que un sistema con una sola cola (fila) y un servidor (caja)..
# Cuando los clientes llegan se unen a la fila donde esperan a ser servidos
# y cuando son se van.
# """

# import numpy as np
# import random
# import matplotlib.pyplot as plt
# import math
# def main():
    
#     #intervalo de 9:00 a 17:00, tiempo total 8 horas de servicio
#     #480 minutos equivale a un dia
#     ListOfDays=[480,960 , 2400, 9600, 14400, 33600,38400,50000,70000,80000,100000,160000,200000,300000]
#     #ListOfDays=[480]
#     listaPromedioEspera=[]
#     listaPromedioClientes=[]   

#     for interval in ListOfDays:
#         customers = 0
#         totalCustomers = 0			
#         timeEvent = 0
#         timeArrival = 0
#         timeExit = 0
#         flag = True
#         timeArrivalList=[]
#         waitTime=[]
#         listEventsArrival=[]
#         listEventsExit=[]
#         timeArrivalList=[]
#         waitTime=[]
#         customersByInterval=0
#         waitingSum=0 #suma de espera
#         customersList=[] #en cada posicion guarda los clientes que hay en la fila por intervalo 
#     ########################################
#     # Transcurso de servicio durante el dia #   
#     ########################################
#         while(timeEvent < interval):
            
#             if customers > 0 or flag == False:
#                 if  timeEvent == listEventsArrival[0]:
#                     listEventsArrival.pop(0)
#                     totalCustomers += 1					
#                     customers += 1
#                     timeArrivalList.append(timeEvent)
#                     rA = np.random.uniform(0.0,1.0)
#                     deltaTa = ((math.log(1-rA))/-3)*60
#                     #eventoActual = timeEvent para mantener el evento en esa iteracion
#                     #timeEvent += deltaTa  suma el delta a la tiempo total para general el proximo evento
#                     #nos permite definir que si se ejecuta el evento
#                     timeArrival = timeEvent + deltaTa 
#                     listEventsArrival.append(timeArrival)  #LISTA DE EVENTOS DE ENTRADA Y SALIDA
#                     if len(listEventsExit) == 0:
#                         rD = np.random.uniform(0.0,1.0)     
#                         deltaTd = ((math.log(1-rD))/-5)*60
#                         timeExit = timeEvent + deltaTd
#                         listEventsExit.append(timeExit)                    
                    
#                     if timeExit < timeArrival:
#                         timeEvent = timeExit                        
#                         #listEvents.append(timeExit)
#                     else:
#                         timeEvent = timeArrival
#                 elif timeEvent == listEventsExit[0]:
#                     listEventsExit.pop(0)
#                     customers -= 1
#                     waitTime.append(timeEvent-timeArrivalList.pop(0))
#                     if len(listEventsArrival) == 0:
#                         rA = np.random.uniform(0.0,1.0)
#                         deltaTa = ((math.log(1-rA))/-3)*60
#                         #para mantener el evento en esa iteracion
#                         eventoActual = timeEvent 
#                         timeEvent += deltaTa  #suma el delta a la tiempo total para general el proximo evento
#                         timeArrival = timeEvent #nos permite definir que si se ejecuta el evento
#                     if customers > 0:
#                         rD = np.random.uniform(0.0,1.0)     
#                         deltaTd = ((math.log(1-rD))/-5)*60
#                         timeExit = timeEvent + deltaTd
#                         listEventsExit.append(timeExit)  
                    
#                         if timeExit < timeArrival:
#                             timeEvent = timeExit
#                         else:
#                             timeEvent = timeArrival					
#                     else:
#                         timeEvent = listEventsArrival[0]
#             #Permite generar el primer evento del dia
#             if  customers == 0 and flag == True: #Caso base al abrir el banco para general el evento de llegada
#                 rA = np.random.uniform(0.0,1.0)
#                 deltaTa = ((math.log(1-rA))/-3)*60
#                 timeArrival = timeEvent + deltaTa  #suma el delta a la tiempo total para general el proximo evento
#                 timeEvent = timeArrival  #nos permite definir que si se ejecuta el evento
#                 listEventsArrival.append(timeArrival) #LISTA DE EVENTOS DE ENTRADA
#                 flag = False
        
#             customersList.append(customers)
#             #Fin ciclo while
#         print ("total de cliente: ",totalCustomers)
#         print ("clientes dentro del banco: ",customers)
#         print ("Tamaño del arreglo: ", len(timeArrivalList))

#         while customers > 0:
#             rD = np.random.uniform(0.0,1.0)     
#             deltaTd = ((math.log(1-rD))/-5)*60
#             timeExit = timeEvent + deltaTd
#             timeEvent = timeExit
#             waitTime.append(timeEvent -timeArrivalList.pop(0))
#             customers -= 1

#         print ("clientes dentro del banco: ",customers)  
        
#         ########################################################## 	
#         ###### Calculamos el promedio de espera por intervalo ####	
#         ##########################################################
#         for i in range(0,len(waitTime)):
#             waitingSum +=  (waitTime[i]/60)
        
#         #inserta en cada posicion la promedio de intervalo entre el total de clientes 
#         listaPromedioEspera.append(waitingSum/totalCustomers)

#         ############################################################ 	
#         ###### Calculamos el promedio de clientes en el sistema,####
#         ######             es decir en la fila                 #####	
#         ############################################################
        
#         for i in range(0,len(customersList)):
#         customersByInterval +=  customersList[i]

#         #promedio de clientes en el sistema (en la fila) 
#         #Se considera la suma de clientes en cada intervalo de "tiempo"
#         #y se divide entre el dia completo represetado por numero de intervalos	
        
#         listaPromedioClientes.append(customersByInterval/(timeEvent/8)) 
#         #fin ciclo for
#     print ("intervalos",ListOfDays)
#     print(listaPromedioEspera)
#     plt.xlabel("Numero de intervalos")
#     plt.ylabel("Numero promedio de espera")    
#     plt.plot(ListOfDays,listaPromedioEspera)
#     plt.show()
#     plt.xlabel("Numero de intervalos")
#     plt.ylabel("Numero promedio de clientes en cada evento")    
#     plt.plot(ListOfDays,listaPromedioClientes)
#     plt.show()
# main()