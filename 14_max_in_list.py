# wpt find max number in given list

l = eval(input())

max =l[0]
for i in l:
    if i > max:
        max= i
print(max)

'''
#procees
1. took list as input
#list = [9,1,2,12,5]
2. asuming that first element as max so max = l[0]
3. by using for loop:
    iteration 1:
       it will fetch element '9' so i is '9'
       check wheter '9'  is greator than max false:
           so max still 9
    iteration 2:
       it will fetch element '1' so i is '1'
       check wheter '1'  is greator than max false:
           so max still 9
    iteration 3:
       it will fetch element '2' so i is '2'
       check wheter '2'  is greator than max false:
           so max still 9
    iteration 4:
       it will fetch element '12' so i is '12'
       check wheter '12'  is greator than max == true:
           so max will become 12
    iteration 5:
       it will fetch element '5' so i is '5'
       check wheter '5'  is greator than max false:
           so max still 12
4. at last we wil print the value of max = 12
    
'''
