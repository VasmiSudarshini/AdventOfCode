with open('t.ini','r') as f:
    for line in f:
        print(line)
input_2 = open("/Users/vasmi/OneDrive/Desktop/input_Day2.txt", 'r')
lines = input_2.readlines()
lines[0:3]
print(lines)

#Convert the above list lines into string
str_lines = str(lines)
type(str_lines)
str_lines[0:3]

#Splitting the strings based on space
str_lines = str_lines.split()
str_lines

list_lines = list(str_lines)
list_lines[0:3]

Total_points = []

for line in list_lines:
    Total_points = 0
    if (A==X) or (B==Y) or (C==Z):
        Total_points = Total_points + 3
    elif (A==Y) or (B==Z) or (C==X):
        Total_points = Total_points + 6
    else:
        Total_points = 0


