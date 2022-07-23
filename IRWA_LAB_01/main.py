# 1). Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Answer = ['My', 'name', 'is', 'Kelly']


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]

print(list3)

print(tuple(zip(list1,list2)))

#output
['My', 'name', 'is', 'Kelly']
(('M', 'y'), ('na', 'me'), ('i', 's'), ('Ke', 'lly'))



# 2). Given a Python list. Turn every item of a list into its square
# List1 = [1, 2, 3, 4, 5, 6, 7]
# Answer = [1, 4, 9, 16, 25, 36, 49]



List1 = [1, 2, 3, 4, 5, 6, 7]

for i in List1:
    x = i*i
    print(x)
    answer = [n*n for n in List1]
print(answer)





# 3). Given a two Python list. Iterate both lists simultaneously such that list1 should display item in
# original order and list2 in reverse order
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Answer = 10 400
#          20 300
#          30 200
#          40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2 = list2[::-1]
print(list2)    #reverse the list

for x,y in zip(list1,list2):
    print(x,y)



# 4). Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look
# like the following list
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
# Answer = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

#extending exist list
list1[2][1][2].extend(sub_list)
print(list1)

#adding as a separate list
list1[2][1][2].append(sub_list)
print(list1)





# 5). Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Answer = [5, 15, 25, 50]











# 6). Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Answer = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# 01 method----------------------------------------------
answer = dict(zip(keys, values))
print(answer)



# 02 method----------------------------------------------
# print("Original key list is : " + str(keys))
# print("Original value list is : " + str(values))
#
# res = {}
# for key in keys:
#     for value in values:
#         res[key] = value
#         values.remove(value)
#         break
# print ("Resultant dictionary is : " +str(res))




# 7). Merge following two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Answer = {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 01 method--------------------------------------------------
dict3 = {**dict1, **dict2}
print(dict3)

# 02 method--------------------------------------------------
dict3 = dict1 | dict2
print(dict3)




# 8). Rename key city to location in the following dictionary
# sampleDict = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "city": "New york"
# }
# Answer = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "location": "New york"
# }

sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
}

print(sampleDict)
sampleDict['location']= sampleDict.pop('city')
print(sampleDict)



# 9). Delete set of keys from Python Dictionary
#
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# keysToRemove = ["name", "salary"]
# Answer = {'city': 'New york', 'age': 25}

sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
}

#method 01
sampleDict.pop('name')
sampleDict.pop('salary')

print(sampleDict)

#method 02
keysToRemove = ["name", "salary"]

for i in keysToRemove:
    del sampleDict[i]

print(sampleDict)










# 10). Create a new dictionary by extracting the following keys from a given dictionary
# Given Dictionary
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# Keys to extract
# keys = ["name", "salary"]
# Answer = {'name': 'Kelly', 'salary': 8000}


sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# use for loop
# add to dictionary

# keys = ["name", "salary"]
#
#
# newDict = dict()
#
# for i in sampleDict.keys() and keys:       #at the same time get keys from sampleDict and add them to newDict
#     newDict[i] = sampleDict[i]
# print(newDict)


# output
# {'name': 'Kelly', 'salary': 8000}







# 11). Given a list iterate it and display numbers which are divisible by 5 and if you find number
# greater than 150 stop the loop iteration
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# Answer =
# 15
# 55
# 75
# 150

# %5 = 0
# break if equal to 150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i > 150:
        break
    if i % 5 == 0:
        print(i)


# output
# 15
# 55
# 75
# 150







# 12). Generate a Python list of all the even numbers between 4 to 30
# Answer = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# method 1 printing numbers as normal
for num in range(4,30,2):
    print(num)

# output
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28

# method 2 printing numbers as a list
list1 = []

for num in range(4,30):
    if num % 2 ==0 :
        list1.append(num)
print(list1)

# output
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


# 13). Count all lower case, upper case, digits, and special symbols from a given string
# input_str = "P@#yn26at^&i5ve"
# Total counts of chars, digits,and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

input_str = "P@#yn26at^&i5ve"
lccount = 0
upcount = 0
digcount = 0
symbol = 0
for x in input_str:
    if x.islower():
        lccount += 1
    elif x.isupper():
        upcount += 1
    elif x.isdigit():
        digcount += 1
    else:
        symbol+= 1

print("lower case count: ", lccount, "upper case count: ", upcount, "digit count: ", digcount, "symbol: ", symbol)

# output
# lower case count:  7 upper case count:  1 digit count:  3 symbol:  4








# 14). Given an input string, count occurrences of all characters within a string
# count("pynativepynvepynative") = {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, 'v': 3, 'e': 3}


# the output is like dictionary format

input_str = "pynativepynvepynative"

newDict = dict()


for i in input_str:
    count = input_str.count(i)
    newDict[i] = count

print(newDict)

# output
# {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, 'v': 3, 'e': 3}








# 15). Roll dice in such a way that every time you get the same number
# Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do
# this 5 times

# number of times = 5

import random

dice = [1,2,3,4,5,6]
for i in range(5):
    random.seed(34)         #this function is used to get same output for each loop iteration
    print(random.choice(dice))



















































