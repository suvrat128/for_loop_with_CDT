#wpt print how many nubers are in given string

s = input('enter the string:')

count=0
for i in s:
    if i.isdigit():
        count+=1
print(count)

'''
# process
1. took main string as input
# 'happy14'
2. asuming that there is no digit present in the string so that  count = 0
3. by using for loop:
    iteration 1:
        it will fetch first element 'h' so i is 'h'
        check 'h' == 'digit' false so count stil 0
    iteration 2:
        it will fetch  element 'a' so i is 'a'
        check 'a' == 'digit' false so count stil 0
    iteration 3:
        it will fetch  element 'p' so i is 'p'
        check 'p' == 'digit' false so count stil 0
    iteration 4:
        it will fetch  element 'p' so i is 'p'
        check '' == 'digit' false so count still 0
    iteration 5:
        it will fetch element 'y' so i is 'y'
        check 'h' == 'digit' false so count stil 0
    iteration 6:
        it will fetch  element '1' so i is '1'
        check '' == 'digit' true
            so count get increment from 0 to 1
    iteration 7:
        it will fetch element '4' so i is '4'
        check 'h' == 'digit' true
             so count get increment from 1 to 2
5.at last after complete iteration of loop printing count value
'''
