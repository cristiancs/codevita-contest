from operator import itemgetter

filea = input("")
fileb = input("")


filea = open(filea,"r")
fileb = open(fileb,"r")


tabla1 = list()
for line in filea:
    tabla1.append(line.split(","))

tabla2 = dict()

for line in fileb:
    datos = line.split(",")
    tabla2[datos[0]] = datos[1]

tabla1 = sorted(tabla1, key=itemgetter(2,6))

for lista in tabla1:
    if(lista[2] in tabla2.keys()):
        print(lista[2]+","+tabla2[lista[2]]+","+lista[1]+","+lista[5]+","+lista[3]+","+lista[4]+","+lista[6])