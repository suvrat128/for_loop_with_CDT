#wpt find the sum of even digit present in given string

s = input('enter the string:')

summ = 0
for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 == 0:
           summ+=k

print(summ)

'''
# process
1. took main string as input
# input string = '12@ha'
2. asuming that there is no digit present in the string so that  summ = 0
3. by using for loop:
    iteration 1:
        it will fetch first element '1' so i is '1'
        check '1'== 'digit' true:
            type cast the i and store in new variable
            check 1%2 == 0 false so summ stil 0
    iteration 2:
        it will fetch first element '2' so i is '2'
        check '2'== 'digit' true:
            type cast the i and store in new variable
            check 2%2 == 0 true:
                so summ = 0+2= 2
    iteration 3:
        it will fetch first element '@' so i is '@'
        check '@'== 'digit' false so summ still 2
    iteration 4:
        it will fetch first element 'h' so i is 'h'
        check 'h'== 'digit' false so summ still 2
    iteration 5:
        it will fetch first element 'a' so i is 'a'
        check 'a'== 'digit' false so summ still 2
       
5.at last after complete iteration of loop printing summ value
'''
