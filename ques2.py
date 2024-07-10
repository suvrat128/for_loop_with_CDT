# wpt print how many times given substring is present in given string

s =input('enter the string')
ss = input('enter the sub string:')
count = 0
for i in s:
    if i == ss:
        count+=1
print(count)

'''
# process
1. took main string as input  # 'hello'
2. took substring as input  # 'o'
3. by assuming given substring is not present in mainstring c=0
4. by using for loop
    iteration1:
        it will fetch 'h' so i= 'h'
        check 'h' == 'o' false so still count=0
    iteration2:
        it will fetch 'e' so i= 'e'
        check 'e' == 'o' false so still count=0
    iteration3:
        it will fetch 'l' so i= 'l'
        check 'l' == 'o' false so still count=0
    iteration4:
        it will fetch 'l' so i= 'l'
        check 'l' == 'o' false so still count=0
    iteration1:
        it will fetch 'o' so i= 'o'
        check 'o' == 'o' true
                    so incerment count from 0 to 1
5.at last after complete iteration of loop printing count value
'''
