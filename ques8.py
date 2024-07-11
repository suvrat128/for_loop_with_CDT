#wpt find the absulate difference betwween even digit sum and odd digit sum

s = input('enter the string:')

even = 0
odd = 0

for i in s:
    if i.isdigit():
        k = int(i)
        if k%2 == 0:
           even+=k
        else:
            odd+=k
if even > odd:
    print(even - odd)
else:
    print(odd - even)

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
                so odd+=9 = 9
    iteration 2:
        it will fetch first element '1' so i is '1'
        check '1'== 'digit' true:
            type cast the i and store in new variable
            check 1%2 == 0 false :
                so odd 9+=1 = 10
    iteration 3:
        it will fetch first element '2' so i is '2'
        check '2'== 'digit' true:
            type cast the i and store in new variable
            check 2%2 == 0 true :
                so even+=2 = 2
    iteration 4:
        it will fetch first element '3' so i is '3'
        check '3'== 'digit' true:
            type cast the i and store in new variable
            check 2%2 == 0 false :
                so odd 10+=3 = 13
    iteration 5:
        it will fetch first element '4' so i is '4'
        check '4'== 'digit' true:
            type cast the i and store in new variable
            check 4%2 == 0 true :
                so even 2+=4 = 6
5. check even > odd 6> 13 false:
                    so we go for else :
                        print the 13-6 = 7

'''
