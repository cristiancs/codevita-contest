entrada = "3k4/8/8/2P1P3/3B4/2R1R3/8/4K3 w - - 0 1"

entrada = entrada.split("/")
turno = entrada[7].split(" ")[1]
entrada[7] = entrada[7].split(" ")[0]
tablero = {0: [], 1: [],2: [], 3: [],4: [], 5: [],6: [], 7: []}


for linea in range(len(entrada)):
    contador = 0
    pos = 0
    while contador < 8:
        if entrada[linea][pos].isdigit():
            for i in range(int(entrada[linea][pos])):
                tablero[linea].append(0)
                contador+=1
        else:
            tablero[linea].append(entrada[linea][pos])
            contador += 1
        pos+=1

posibles = []

for x,val in tablero.items():
    y = 0
    for item in val:
        if item=="B":
            newx = x-1
            newy = y
            # + , +
            while newx  <= 7 and newy <= 7:
                print(str(newx) + str(newy) + str(x) + str(y))
                if(tablero[newx][newy] == 0):

                    posibles.append(chr(96+x)+str(y+1)+chr(96+newx)+str(newy+1))
                newx += 1
                newy += 1
            newy = x
            newx = y
            # -, -

        y += 1

print(posibles)