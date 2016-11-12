import copy
archivo = input("")
archivo = open(archivo,"r")
data = archivo.read().splitlines()
archivo.close()
linea = 0

def guardarEstacionamiento(estacionamientos,datos):
    key, val = 0, ""
    flag = False
    for key, val in estacionamientos[datos[1]][datos[2]].items():
        if val == "":
            estacionamientos[datos[1]][datos[2]][key] = datos[3]
            flag = True
            break
    if not flag:
        estacionamientos[datos[1]][datos[2]][key+1] = datos[3]
    return key
def removeEstacionamiento(estacionamientos,datos):
    key, val = 0, ""
    flag = False
    for key, val in estacionamientos[datos[1]][datos[2]].items():
        if val == datos[3]:
            estacionamientos[datos[1]][datos[2]][key] = ""
            flag = True
            break
    if not flag:
        estacionamientos[datos[1]][datos[2]][key+1] = datos[3]
    return key
for i in range(int(data[0])):
    linea += 1
    ciudad = list(map(int, data[linea].split(" ")))
    #Creamos lista de estacionamientos
    nesta = 0
    estacionamientos = dict()

    estacionamientosporx = 0
    for x in range(ciudad[0]+1):
        if x%ciudad[2] == 0:
            estacionamientosporx+=1
            nesta+=1
    estacionamientospory = 0


    estacionamientos = dict()
    tempdict = dict()
    for x in range(ciudad[1]+1):
        if x % ciudad[2] == 0:
            tempdict[estacionamientospory*ciudad[2]] = dict()
            estacionamientospory+=1

    for x in range(ciudad[2]+1):
        estacionamientos[x*ciudad[2]] = copy.deepcopy(tempdict)
    nesta *= estacionamientospory

    print(nesta)
    linea+=1
    for x in range(int(data[linea])):
        linea+=1
        datos = data[linea].split(" ")
        if datos[0] == "P":
            datos[1] = int(datos[1])
            datos[2] = int(datos[2])
            posicion = 0
            if datos[1] % ciudad[2] == 0 and datos[2] % ciudad[3] == 0:
                guardarEstacionamiento(estacionamientos,datos)
            elif datos[1] % ciudad[2] == 0:
                ycorrecto = datos[2]
                while ycorrecto % ciudad[3] != 0:
                    ycorrecto -=1
                datos[2] = ycorrecto
                posicion = guardarEstacionamiento(estacionamientos, datos)
                #Estoy en el mismo eje x que un estacionamiento
            elif datos[2] % ciudad[3] == 0:
                xcorrecto = datos[1]
                while xcorrecto % ciudad[3] != 0:
                    xcorrecto -= 1
                datos[1] = xcorrecto
                posicion = guardarEstacionamiento(estacionamientos, datos)
                #Estoy en el mismo eje y que un estacionamiento
            else:
                # Debo buscar en alguna parte
                ycorrecto = datos[2]
                while ycorrecto % ciudad[3] != 0:
                    ycorrecto -= 1
                datos[2] = ycorrecto
                xcorrecto = datos[1]
                while xcorrecto % ciudad[3] != 0:
                    xcorrecto -= 1
                datos[1] = xcorrecto
                posicion = guardarEstacionamiento(estacionamientos, datos)
            #print(str(datos[1])+" "+str(datos[2])+" "+str(int(posicion/ ciudad[3]))+" "+str(posicion % ciudad[3] +1))
        else:
            #Buscamos el auto
            matricula = datos[1]
            stop = False
            for x,val in estacionamientos.items():
                for y,v1 in val.items():
                    for posicion, mat in v1.items():
                        if mat == matricula:
                            removeEstacionamiento(estacionamientos, [0,x,y,matricula])
                            if posicion <= ciudad[3]:
                                print(str(x) + " " + str(y) + " 0 " + str(
                                    posicion))
                            else:
                                print(str(x) + " " + str(y) + " " + str(int(posicion / ciudad[3])) + " " + str(
                                    posicion % ciudad[3]))
                            stop = True
                            break
                    if stop:
                        break
                if stop:
                    break
