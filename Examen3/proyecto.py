import math
from scipy.stats import expon
import numpy as np

#S=40 #Limite superior del inventario
#=20 #Limite inferior del inventario
PromInvPos=[]
PromInvNeg=[]
PromCostoPedido=[]
def inventario(s,S):
    I=60 #Inventario
    n=120 #tiempo en meses
    tiempo=0 #tiempo del sistema
    tiempoaux=0
    Z = 0 #articulos ordenados al mes
    llegada = 0
    #tiempo en el que el proveedor llegara para sutir el producto
    surtido = 0
    #Arreglo que guarda los pedidos pendientes
    demandas = []
    cantidadProductos = 0
    flag=True
    costoPedido=0
    InvPosMes=[]
    InvNegMes=[]
    CostoPedidoMes=[]
    while  tiempo < n :
        #print("Tiempo actual ", tiempo)
        #Si el inventario no tiene suficientes productos
        if(I-cantidadProductos) < 0 :
                
                #I -= cantidadProductos 
                demandas.append(cantidadProductos)
                #Se almacena en el arreglo de demandas para surtirla a principio de mes
                #print(demandas)
        else : 
            I -= cantidadProductos
            #productos restantes en el inventario
            #print("Inventario ", I)
                    
        if(tiempo == surtido):
            #Condicion para ver si el evento es el surtido de producto
            #print("Surtido")
            
            demandas.sort()
            #print(demandas)
            #print("Surtido")
            for i in range (len(demandas)):
                X= demandas.pop()
                if(Z>0 and (Z-X) >= 0 ):
                    Z -= X
                    #I += X
                else:
                    demandas.append(X)
                    break
            #Se actualiza el inventario
            I += Z - sum(demandas)
            #print("Inventario actualizado", I)
                                
                                
        rA=np.random.uniform(0.0,1.0)
        #llegada=expon.pdf(0.1)
        #tiempo de distribucion exponencial
        llegada =- (math.log(1-rA))*(0.1)
        #llegada = ((math.log(1-rA))/-0.1)
        #cantidad de productos que pide un cliente
        prob=np.random.uniform(0.0,1.0) 
        if(prob <= (1/6)):
            cantidadProductos=1
        elif(1/6 < prob and prob <= 1/2):
            cantidadProductos = 2
        elif(1/2 < prob and prob <= 5/6):
            cantidadProductos = 3
        elif(5/6 < prob and prob <= 1):
            cantidadProductos = 4
    
        #Calculo de productos a pedir a principio de mes
        if math.floor(tiempo) != math.floor(tiempoaux): 
            #print("principio de mes")
            if (I > 0):
                InvPosMes.append(I)
            else:
                InvNegMes.append(I)
                
            if(I < s):
                Z = S - I                
                rB=np.random.uniform(0.5,1.0)
                surtido = tiempo+rB
                costoPedido= 32+3*Z
                
            CostoPedidoMes.append(costoPedido)
        #Pra el manejo deinicio de mes
        tiempoaux = tiempo 
        #Condicion para ver si hay que hacer un surtido o una venta
        print(tiempo,"|",I,"|",cantidadProductos,"|",llegada,"|",surtido,"|",Z)
        if((tiempo+llegada) > surtido and flag):
            tiempo += llegada #Acumulacion de tiempo en meses
        else : 
            flag = False
            #print ("tiempo ",tiempo+llegada)
            if (tiempo+llegada) > surtido:
                tiempo = surtido
                #print("soy tiempoactual",tiempo)
                #print("soy surtidorico",surtido)
                flag = True
            else: 
                tiempo += llegada
    PromInvPos.append(sum(InvPosMes)/n)
    PromInvNeg.append(((abs(sum(InvNegMes)))/n)*5)
    PromCostoPedido.append(sum(CostoPedidoMes)/n)
    
inf=[20,20,20,20,40,40,40,60,60]
sup=[40,60,80,100,60,80,100,80,100]
#inf=[20]
#sup=[40]
for i in range (len(inf)):
    inventario(inf[i],sup[i])

costototal=[]
for j in range(len(inf)):
    costototal.append((PromInvPos[j]+PromInvNeg[j]+PromCostoPedido[j])/3)

print("(s  ,S) |   Ct   |   Co    |   Cm  |  Ce")
for k in range (len(sup)):
    print(inf[k],"|",sup[k],"|",round(costototal[k],3),"|",round(PromCostoPedido[k],3),"|",round(PromInvPos[k],3),"|",round(PromInvNeg[k],3))
   