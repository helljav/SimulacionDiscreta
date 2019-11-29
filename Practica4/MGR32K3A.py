seed1 = [411040508, 544377427, 2887694751]
seed2 = [702892456, 758163486, 2462939166]
a1 = 1403580
a2 = 810728 
a3 = 527612
a4 = 1370589
mod1 = 2**32 - 209 
mod2 = 2**32 - 22853

def MGR():
    global a1,a2,a3,a4,mod1,mod2
    """ Z1 """
    z1n = ((a1 * seed1[1]) - (a2 * seed1[0])) % mod1
    seed1[0] = seed1[1]
    seed1[1] = seed1[2]
    seed1[2] = z1n

    """ Z2 """
    z2n = ((a3 * seed2[2]) - (a4 * seed2[0])) % mod2
    seed2[0] = seed2[1]
    seed2[1] = seed2[2]
    seed2[2] = z2n
    y = (z1n - z2n) % mod1
    return y/mod1

def main():
    for i in range(1,16):
         print(i," Numero aleatorio generado ", MGR())

main()





   



