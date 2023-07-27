with open('/Users/vasmi/OneDrive/Desktop/input_Day2.txt','r') as f:
    Total_points = 0
    for line in f:
        split_line = line.split()
        print(split_line[0])

        if split_line[0]== 'A' and split_line[1] == 'Y': 
            Total_points = Total_points + 6
        elif split_line[0] == 'B' and split_line[1] == 'Z':
            Total_points = Total_points + 6
        elif split_line[0] == 'C' and split_line[1] =='X':
            Total_points = Total_points + 6
        elif split_line[0] == 'A' and split_line[1]== 'X':
            Total_points = Total_points + 3
        elif split_line[0] == 'B' and split_line[1] == 'Y':
            Total_points = Total_points + 3
        elif split_line[0] == 'C' and split_line[1] =='Z':
            Total_points = Total_points + 3

        if split_line[1] == 'X':
            Total_points = Total_points + 1
        elif split_line[1] == 'Y':
            Total_points = Total_points + 2
        elif split_line[1] == 'Z':
            Total_points = Total_points + 3

    print(Total_points)

with open('/Users/vasmi/OneDrive/Desktop/input_Day2.txt','r') as file:
    Win_points = 0
    for line in file:
        split_line = line.split()
        print(split_line[0])

        if split_line[0]== 'A'and split_line[1] == 'X': 
            Win_points = Win_points + 3
        elif split_line[0]== 'A'and split_line[1] == 'Y': 
            Win_points = Win_points + 1 
        elif split_line[0]== 'A'and split_line[1] == 'Z': 
            Win_points = Win_points + 2
        elif split_line[0] == 'B' and split_line[1] == 'X':
            Win_points = Win_points + 1
        elif split_line[0] == 'B' and split_line[1] == 'Y':
            Win_points = Win_points + 2
        elif split_line[0] == 'B' and split_line[1] == 'Z':
            Win_points = Win_points + 3
        elif split_line[0] == 'C' and split_line[1] =='X':
            Win_points = Win_points + 2
        elif split_line[0] == 'C' and split_line[1] =='Y':
            Win_points = Win_points + 3
        elif split_line[0] == 'C' and split_line[1] =='Z':
            Win_points = Win_points + 1

        if split_line[1] == 'X':
            Win_points = Win_points + 0
        elif split_line[1] == 'Y':
            Win_points = Win_points + 3
        elif split_line[1] == 'Z':
            Win_points = Win_points + 6

    print(Win_points)   



