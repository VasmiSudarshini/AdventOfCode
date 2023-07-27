fh = open("/Users/vasmi/AdventOfCode/input_Day6.txt",'r')
line = fh.readline()

# marker = []

for i in range(len(line)-4):
    parts = line[i:i+4]
    if parts[0] == parts[1] or parts[0] == parts[2] or parts[0] == parts[3] or parts[1] == parts[2] or parts[1] == parts[3] or parts[2] == parts[3]:
        continue
    else:
        print(i+4)
        break
        #marker.append(parts)

# position = marker[0]
# print(line.find(position)+1 +3)
