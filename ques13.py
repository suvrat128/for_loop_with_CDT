#wpt to print the sum of digits present in list:

l = eval(input())

summ = 0

for i in l:
    if type(i) == int: # or if isinstance(i,int):
        summ+=i
print(summ)

'''
#process

1. took list as input
#list = [9,1,2,'suvrat']
2. asuming that there is no digit  present in the list so that summ = 0
3. by using for loop:
    iteration 1:
       it will fetch element '9' so i is '9'
       check wheter type(9) is integer == true:
           so summ+=9 = 9
    iteration 2:
       it will fetch element '1' so i is '1'
       check wheter type(1) is integer == true:
           so summ+=1 = 10
    iteration 3:
       it will fetch element '2' so i is '2'
       check wheter type(2) is integer == true:
           so summ+=2 = 12
    iteration 4:
       it will fetch element 'suvrat' so i is 'suvrat'
       check wheter type('suvrat') is integer == false:
           so summ still 12
4. at last we print the value of summ = 12
  
'''
