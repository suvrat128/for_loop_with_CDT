# wpt print how many time each and every element is present CDT

cdt = eval(input())

d = {}.fromkeys(cdt,0)

for i in cdt:
    d[i]=d[i]+1
print(d)

#or

cdt = eval(input())
d={}
for i in cdt:
    d[i]=cdt.count(i)
print(d)

#or

cdt = eval(input())
d={}

for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
'''
#process
1. took list as input
#list = [9,9,2,12,12]
2. take one empty dictionar as d
3. by using for loop:
    iteration 1:
       it will fetch element '9' so i is '9'
       check wether '9' is not in dictionary == true:
           so it wil store the key as 9 and value =1
    iteration 2:
       it will fetch element '9' so i is '9'
       check wether '9' is not in dictionary == false:
           so the value of '9' will get incriment 1 to 2
    iteration 3:
       it will fetch element '2' so i is '2'
       check wether '2' is not in dictionary == true:
           so it wil store the key as 2 and value =1
    iteration 4:
       it will fetch element '12' so i is '12'
       check wether '12' is not in dictionary == true:
           so it wil store the key as 12 and value =1
    iteration 5:
       it will fetch element '12' so i is '12'
       check wether '12'is not in dictionary == false:
           so the value of '12' will get incriment 1 to 2
4.at last after complition of for loop we will print the d       
       
'''
