
db = input()
cantidad = input()


db = open(db, "r")
rangos = dict()

for line in db:
    data = line.split(",")
    if(data[0].split(".")[0] in rangos.keys()):
        rangos[data[0].split(".")[0]].append(data[0])
    else:
        rangos[data[0].split(".")[0]] = [(data[0])]


#Fixed from http://stackoverflow.com/a/29950808/2213659
def ipToInt(ip):
    o = list(map(int, ip.split('.')))
    res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
    return res

def isIpInSubnet(ip, ipNetwork, maskLength):
    ipInt = ipToInt(ip)#my test ip, in int form

    maskLengthFromRight = 32 - int(maskLength)

    ipNetworkInt = ipToInt(ipNetwork) #convert the ip network into integer form
    binString = "{0:b}".format(ipNetworkInt) #convert that into into binary (string format)

    chopAmount = 0 #find out how much of that int I need to cut off
    for i in range(maskLengthFromRight):
        if i < len(binString):
            chopAmount += int(binString[len(binString)-1-i]) * 2**i

    minVal = ipNetworkInt-chopAmount
    maxVal = minVal+2**maskLengthFromRight -1

    return minVal <= ipInt and ipInt <= maxVal

for i in range(int(cantidad)):
    ip = input()
    flag = False
    if (ip.split(".")[0] in rangos.keys()):
        for cidr in rangos[ip.split(".")[0]]:
            data = cidr.split("/")
            if isIpInSubnet(ip,data[0],data[1]):
                print("Yes")
                flag = True
                break
        if not flag:
            print("No")
    else:
        print("No")
db.close()
