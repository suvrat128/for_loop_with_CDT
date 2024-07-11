# wpt to find the some of digit inside a string:

s = input('enter the string:')

summ = 0
for i in s:
    if i.isdigit():
       summ+=int(i)

print(summ)

'''
# process
1. took main string as input
# 'happy14'
2. asuming that there is no digit present in the string so that  summ = 0
3. by using for loop:
    iteration 1:
        it will fetch first element 'h' so i is 'h'
        check 'h' == 'digit' false so summ stil 0
    iteration 2:
        it will fetch  element 'a' so i is 'a'
        check 'a' == 'digit' false so summ stil 0
    iteration 3:
        it will fetch  element 'p' so i is 'p'
        check 'p' == 'digit' false so summ stil 0
    iteration 4:
        it will fetch  element 'p' so i is 'p'
        check '' == 'digit' false so summ still 0
    iteration 5:
        it will fetch element 'y' so i is 'y'
        check 'h' == 'digit' false so summ stil 0
    iteration 6:
        it will fetch  element '1' so i is '1'
        check '' == 'digit' true so summ = 0+1 = 1
    iteration 7:
        it will fetch element '4' so i is '4'
        check 'h' == 'digit' true so summ = 1+4 = 5
5.at last after complete iteration of loop printing summ value
'''
