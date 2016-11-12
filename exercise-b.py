import struct,socket

db = input()
cantidad = input()


db = open(db, "r")
rangos = list()

for line in db:
    data = line.split(",")
    rangos.append(data[0])


def addressInNetwork3(ip,net):
    '''This function allows you to check if on IP belogs to a Network'''
    ipaddr = struct.unpack('=L',socket.inet_aton(ip))[0]
    netaddr,bits = net.split('/')
    netmask = struct.unpack('=L',socket.inet_aton(calcDottedNetmask(int(bits))))[0]
    network = struct.unpack('=L',socket.inet_aton(netaddr))[0] & netmask
    return (ipaddr & netmask) == (network & netmask)

def calcDottedNetmask(mask):
    bits = 0
    for i in range(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

for i in range(int(cantidad)):
    ip = input()
    flag = False
    for cidr in rangos:
        if addressInNetwork3(ip,cidr):
            print("Yes")
            flag = True
            break
    if not flag:
        print("No")
db.close()
