fh = open("/Users/vasmi/AdventOfCode/input_Day6.txt",'r')
line = fh.readline()
# print(line)

# marker = []
for i in range(len(line)-14):
    parts = line[i:i+14]
    # print(parts[0] in parts[1:])
    if parts[0] not in parts[1:] and parts[1] not in parts[2:] and parts[2] not in parts[3:] and parts[3] not in parts[4:] and parts[4] not in parts[5:] and parts[5] not in parts[6:] and parts[6] not in parts[7:] and parts[7] not in parts[8:] and parts[8] not in parts[9:] and parts[9] not in parts[10:] and parts[10] not in parts[11:] and parts[11] not in parts[12:] and parts[12] not in parts[13:]:
        print(i+14)
        break
        # marker.append(parts)

# print(marker)
# print(line.find(marker[0]) +1+13)