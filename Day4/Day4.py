with open("/Users/vasmi/AdventOfCode/input_Day4.txt", 'r') as f:
    count_1 = 0
    count_2 = 0

    for line in f:
        #print(line)
        split_line = line.split(',')
        first_section = split_line[0].split('-')
        second_section = split_line[1].split('-')
        one = int(first_section[0])
        two = int(first_section[1])
        three = int(second_section[0])
        four = int(second_section[1])
        if one >= three and two <= four:
            count_1 = count_1 + 1
        elif three >= one and four <= two:
            count_2 = count_2 + 1

    total_count = count_1 + count_2
    print(total_count)

with open("/Users/vasmi/AdventOfCode/input_Day4.txt", 'r') as f:
    count_1 = 0
    count_2 = 0

    for line in f:
        #print(line)
        split_line = line.split(',')
        first_section = split_line[0].split('-')
        second_section = split_line[1].split('-')
        one = int(first_section[0])
        two = int(first_section[1])
        three = int(second_section[0])
        four = int(second_section[1])
        if one in range(three, four):
            count_1 = count_1 + 1
        elif one == four:
            count_1 = count_1 +1
        elif three in range(one, two):
            count_2 = count_2 + 1
        elif three == two:
            count_2 = count_2 +1
        

    total_count = count_1 + count_2 
    print(total_count)

