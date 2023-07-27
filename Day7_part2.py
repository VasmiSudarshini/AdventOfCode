from typing import Iterable
fh = open("/Users/vasmi/AdventOfCode/input_Day7.txt", "r")

dir_dict = dict()
key_name = ""

# Populating the dictionary with key value pairs
for line in fh:
    line.rstrip('\n')
    # print(line)
    if line.startswith("$ cd") and line != "$ cd ..\n":
        #creating key names
        dir_name = line[5:-1] #-1 because removing empty space from the end of line
        key_name += dir_name + '/' 
        dir_dict.update({key_name : list()})
    
    elif line == "$ cd ..\n":
        # getting out of a directory 
        if len(dir_name) > 0:
            key_name = key_name.rsplit(dir_name, 1)
            key_name = key_name[0]
            dir_name = key_name.split('/')
            dir_name = dir_name[-2]
        else:
            key_name = '//'

    elif line.startswith("$ ls"):
        continue

    elif line[0].isdigit() or line.startswith("dir"):
        # finding the values and populating the dictionary
        item = line.split(" ")
        if item[0].isdigit():
            dir_dict[key_name].append(int(item[0]))
        if item[0] == 'dir':
            name = key_name + item[1][0:-1] + '/' # to match the alphabetical values to the key names
            str(dir_dict[key_name].append(name)) 

def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

def add_values(dicty): 
    # add numerical values in each value list
    for k, v in dicty.items():
        new_list = []
        sum = 0
        for i in v:
            if type(i) == int:
                sum += int(i)
            else:
                new_list.append(i)
        new_list.append(sum)
        dicty[k] = new_list
    return dicty

def reduce_to_size(dictionary):
    # finding the sizes of directories in the values and replacing those directories with its sizes
    for k, v in dictionary.items():
        new_list = []
        # sum = 0
        for i in v:
            if type(i) == int:
                new_list.append(i)
            elif i in dictionary.keys():
                new_list.append(dictionary[i])
        dictionary[k] = list(flatten(new_list)) # removing multiple lists
    return dictionary

for k,v in dir_dict.items():
    # looping through untill each key has a list if only one numerical value
    dir_dict = reduce_to_size(dir_dict)
    dir_dict = add_values(dir_dict)

# print(dir_dict)
total_space = 70000000
# used_space = dir_dict['//'].pop(0) #to remove the integer from the list
# dir_dict['//'].append(int(used_space)) #add the removed integer back into the list
used_space = dir_dict['//'][0] # 43598596
print("total size of disk:", total_space)
print("used space:", used_space)

# # Total space of disk is 70000000, occupied space is 48381165, available free space is 
avail_freespace = total_space - used_space
print("avaiable free space:", avail_freespace) # required free space is 30000000

req_freespace = 30000000
to_freeup = req_freespace - avail_freespace
print("space to be freed up by deleting directories:", to_freeup)

# # # print(dir_dict)

lst = []
for k,v in dir_dict.items():
    for i in v:
        if int(i) >= to_freeup:
            lst.append(i)

size_toremove = min(lst)
print(size_toremove)

k = []
for key, value in dir_dict.items():
        for i in value:
            if i == size_toremove:
                k.append(key)
            else:
                continue

print(k)