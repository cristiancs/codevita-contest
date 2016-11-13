def sum(matrix, group, apply):
    dic = dict()
    for linea in matrix:
        argument = linea[group-1]
        total = linea[apply-1]
        dic.setdefault(argument, 0)
        dic[argument] += float(total)
    for key in sorted(dic):
        value = dic[key]
        if (value != int(value)):
            value = int(value)+1
        print(key+' '+str(value))

def count(matrix, group, apply):
    dic1 = dict()
    dic2 = dict()
    for linea in matrix:
        argument = linea[group-1]
        total = linea[apply-1]
        dic1.setdefault(argument, dict())
        dic1[argument] = total
        dic2.setdefault(total, 0)
        dic2[total] += 1
    for key in sorted(dic1):
        value = dic1[key]
        count = dic2[value]
        print(key+' '+str(count))

def avg(matrix, group, apply):
    dic = dict()
    for linea in matrix:
        argument = linea[group-1]
        total = linea[apply-1]
        dic.setdefault(argument, [0, 0])
        dic[argument][0] += 1
        dic[argument][1] += float(total)
    for key in sorted(dic):
        value = dic[key]
        value = value[1]/value[0]
        if (value != int(value)):
            value = int(value)+1
        print(key+' '+str(value))

def inv(matrix, group, apply):
    dic = dict()
    i = 0
    for linea in matrix:
        argument = linea[group - 1]
        column = linea[apply - 1]
        dic.setdefault(argument, [])
        dic[argument].append(column)
        i += 1
    k = 0
    for key in sorted(dic):
        values = dic[key]
        print(key, end=" ")
        if (len(values) <= (i - k)):
            hashes(k, i, values)
            k += 1
        else:
            hashes(0, i, values)
        print(end='\n')

def hashes(pos, quant, arg):
    assigned = False
    if (quant != 0):
        if (quant == (quant - pos) and (arg != [])):
            print(arg[0], end=" ")
            assigned = True

        if (assigned):
            hashes(pos, quant - 1, arg[1:])
        else:
            print('# ', end=" ")
            hashes(pos-1, quant - 1, arg)





n_funcs = int(input())
i = 0
while (i < n_funcs):
    function = input()
    group = int(input())
    apply = int(input())
    matrix = []
    line = input().strip()
    while (line != '-1'):
        line = line.split()
        matrix.append(line)
        line = input().strip()
    if (function == 'Sum'):
        sum(matrix, group, apply)
    elif (function == 'Count'):
        count(matrix, group, apply)
    elif (function == 'Average'):
        avg(matrix, group, apply)
    else:
        inv(matrix, group, apply)
    i += 1
