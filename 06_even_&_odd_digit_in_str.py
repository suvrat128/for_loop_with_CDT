#wpt count how many even digits and odd digits are present in given string

s = input('enter the string:')

even = 0
odd = 0

for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 == 0:
           even+=1
        else:
            odd+=1

print(even)
print(odd)
'''
# process

1. took main string as input
# input string = '91234'
2. asuming that there is no even nu present in the string so that even = 0
3. asuming that there is no odd nu present in the string so that odd = 0
4. by using for loop:
    iteration 1:
        it will fetch first element '9' so i is '9'
        check '9'== 'digit' true:
            type cast the i and store in new variable
            check 9%2 == 0 false :
                so odd+=1 = 1
    iteration 2:
        it will fetch first element '1' so i is '1'
        check '1'== 'digit' true:
            type cast the i and store in new variable
            check 1%2 == 0 false :
                so odd 1+=1 = 2
    iteration 3:
        it will fetch first element '2' so i is '2'
        check '2'== 'digit' true:
            type cast the i and store in new variable
            check 2%2 == 0 true :
                so even+=1 = 1
    iteration 4:
        it will fetch first element '3' so i is '3'
        check '3'== 'digit' true:
            type cast the i and store in new variable
            check 2%2 == 0 false :
                so odd 2+=1 = 3
    iteration 5:
        it will fetch first element '4' so i is '4'
        check '4'== 'digit' true:
            type cast the i and store in new variable
            check 4%2 == 0 true :
                so even 1+=1 = 2
5.at last after complete iteration of loop printing even and odd value
    
'''
