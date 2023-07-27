fh = open("/Users/vasmi/AdventOfCode/input_Day5.txt", 'r')

input_rack = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7: [], 8:[], 9:[]}
def crate(x, y,line) :
   if line[x] != " ":
      input_rack[y].append(line[x])

for line in fh:
   if line[1] == '1':
      break
   crate(1,1, line)
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
#print(instruc)
#print(len(instruc))

for i in instruc:
    splt = i.split()
    #print(splt[3])
    #print(input_rack[int(splt[3])])
    crate_trans = input_rack[int(splt[3])][0:int(splt[1])]
    crate_revrs = list("".join(reversed(crate_trans)))
    #print(crate_revrs)
    input_rack[int(splt[5])] = crate_revrs + input_rack[int(splt[5])]
    input_rack[int(splt[3])] = input_rack[int(splt[3])][int(splt[1]):]
    #print(input_rack[6][0])
    #print(input_rack[7][0])
    #break

print([i[0] for i in input_rack.values()])
#print(input_rack)
