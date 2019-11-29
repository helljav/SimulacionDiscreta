import math
arreglo = []
def GCL1(a,xi1, modulo):
    xdes =  (a*xi1) % modulo
    ri = xdes / modulo
    arreglo.append(ri)
    return xdes

def GCL2(a,xi1, modulo):
    xdes =  (a*xi1) % modulo
    ri = xdes / modulo
    entero = int(ri/(1/128))
    return entero, xdes

def GC2C(xant):
    a = 40692
    modulo = 2147483399
    indice,xant = GCL2(a,xant,modulo)
    return indice,xant


def GC1C():
    a = 40014
    xant =  123457
    modulo = 2147483563
    for i in range(128):
        xant = GCL1(a,xant,modulo)
    return xant
def GC11C(xant,indice):
    a = 40014
    modulo = 2147483563
    xdes =  (a*xant) % modulo
    ri = xdes / modulo
    arreglo[indice] = ri
    return xdes

def main():
    xantGc2 =  7531
    xantGc1 = GC1C()
    arregloIndice = []
    numerosAleatorios = []

    print("Primeros 15 numeros GCL1")
    for i in range(15):
        print(arreglo[i])
    
    print("\n")
    
    print("Primeros 128 GCL!")
    print(arreglo)
    print("\n")

    
    """Generando los numeros aleatorios"""
    for i in range(1,128):
        indice,xantGc2 = GC2C(xantGc2)
        arregloIndice.append(indice)
        numerosAleatorios.append(arreglo[indice])
        xantGc1 = GC11C(xantGc1,indice)

    print("Arreglo GCL2")
    for i in range(15):
        print(arregloIndice[i])
    print("\n")

    print("Primeros 15 GCLC")
    for i in range(15):
        print(numerosAleatorios[i])
    print("\n")

    print("Primeros 128 GCLC")
    print(numerosAleatorios)
    print("")

    print("arreglo despues del GCLC")
    print(arreglo)

   
    


main()
