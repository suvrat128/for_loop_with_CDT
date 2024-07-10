# wpt check how many elements present in given CDT

cdt = eval(input('enter a CDT:'))
c=0
for i in cdt:
    c+=1
print(c)


'''
# process
1. took CDT as input
2. By assuming given CDT is empty assigning c =0
3. by using for loop fetching each and every element of CDT
4. adding 1 to c fro every element of CDT
5. at last after complete iteration of loop printiong c value 
'''

#wpt print how many times given substring is present given string

MS = input('enter the string:')
SS = input('enter the sub string:')

c = 0
for el in MS:
    if el == SS:
        c+=1
print(c)

'''
# process
1. took main string as input
2. took substring as input
3. by assuming given substring is not present in mainstring c=0
4. by using for loop
    iteration1:
        it will fetch 'h' so el= 'h'
        check 'h' == 'o' false so still c=0
    iteration2:
        it will fetch 'e' so el= 'e'
        check 'e' == 'o' false so still c=0
    iteration3:
        it will fetch 'l' so el= 'l'
        check 'l' == 'o' false so still c=0
    iteration4:
        it will fetch 'l' so el= 'l'
        check 'l' == 'o' false so still c=0
    iteration1:
        it will fetch 'o' so el= 'o'
        check 'o' == 'o' true
                    so incerment c from 0 to 1
5.at last after complete iteration of loop printing c value'''
