with open("/Users/vasmi/OneDrive/Desktop/input_Day3.txt", 'r') as f:
    priority = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
            'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
            'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
            'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F': 32, 'G':33, 'H':34, 'I':35, 'J':36,
            'K':37, 'L':38, 'M':39, 'N': 40, 'O':41, 'P':42, 'Q':43, 'R': 44, 'S':45, 'T':46,
            'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
    Total = 0
    for line in f:
        l = len(line)
        #print(l)
        if l != 0:
            str_1 = line[0:l//2]
            str_2 = line[l//2:]
            #print(str_1)
            common = ''.join(set.intersection(set(str_1), set(str_2)))
            #common = print(set.intersection(set(str_1), set(str_2)))
            #common = list(common)
            #print(common)

        points = priority.get(common)
        print(points)
        Total = Total + points
    print(Total)

with open("/Users/vasmi/OneDrive/Desktop/input_Day3.txt", 'r') as f:
    priority = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
            'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
            'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
            'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F': 32, 'G':33, 'H':34, 'I':35, 'J':36,
            'K':37, 'L':38, 'M':39, 'N': 40, 'O':41, 'P':42, 'Q':43, 'R': 44, 'S':45, 'T':46,
            'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
    total = 0
    count = 0
    common = []
    
    for line in f:
        count = count+1 
        if count%3 == 1:
            common = set(line.strip())
        if count%3 == 2:
            common = set(line.strip()).intersection(common)
        if count%3 == 0:
            common = ''.join(set(line.strip()).intersection(common))
            #common = list(common)
            print(common)
    
            points = priority.get(common)
            print(points)
            total = total + points
    print(total)


    
            
            
            

