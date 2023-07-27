fh = open('/Users/vasmi/AdventOfCode/input_Day5.txt', 'r')
input_rack = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

def crate(x,y, line): #x = line index, y = input_rack keys
    if line[x] != " ":
        input_rack[y].append(line[x])

for line in fh:
    if line[1] == "1":
        break
    crate(1,1,line)
    crate(5,2, line)
    crate(9,3, line)
    crate(13,4, line)
    crate(17,5, line)
    crate(21,6, line)
    crate(25,7, line)
    crate(29,8, line)
    crate(33,9, line)

instruc = []
for line in fh:
    if line.startswith('move'):
        instruc.append(line)

for i in instruc:
    splt = i.split()
    crate_trans = input_rack[int(splt[3])][0:int(splt[1])]
    input_rack[int(splt[3])] = input_rack[int(splt[3])][int(splt[1]):]
    input_rack[int(splt[5])] = crate_trans+ input_rack[int(splt[5])]

print([i[0] for i in input_rack.values()])

    

