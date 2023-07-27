#Reading the text file and assigning it to a variable
input_1 = open("/Users/vasmi/OneDrive/Desktop/input_Day2.txt",'r')
#Reading each line
lines = input_1.readlines()
lines

calorie_list = []
a = 0

for line in lines:
    #print(int(line))
   
    if line =='\n':
        calorie_list.append(a)
        a=0
    else:
        a = a + int(line)
print(calorie_list)

max(calorie_list)

#part 2
calorie_list.sort(reverse=True)
calorie_list

first_three = calorie_list[0:3]
first_three

sum(first_three)
