
db = input()
cantidad = input()


db = open(db, "r")
rangos = list()

for line in db:
    data = line.split(",")
    rangos.append(data[0])


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
    for cidr in rangos:
        data = cidr.split("/")
        if isIpInSubnet(ip,data[0],data[1]):
            print("Yes")
            flag = True
            break
    if not flag:
        print("No")
db.close()
