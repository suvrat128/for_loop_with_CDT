# wpt print lengthiest word in given string

s = input()
st = s.split()
c = 0
lw=''

for i in st:
    if len(i)>c:
        c= len(i)
        lw=i
print(lw)

or
s = input()
st = s.split()
print(max(st,key=len))

'''
#process
1. took string as input
# string=='hello happys bye happy '
2. split the string with space and store in variable st
3. take a variable with empty string
4. asume that the string is empty so c =0
5. by using for loop:
    iteration 1:
        it will fetch element 'hello' so i is 'hello'
        check len(hello) is greator than 0 == true:
            lw = 'hello'
            and c = 5
    iteration 2:
        it will fetch element 'happys' so i is 'happys'
        check len(happys) is greator than 5 == true:
            lw = 'happys'
            and c = 6
    iteration 3:
        it will fetch element 'hai' so i is 'hai'
        check len(hai) is greator than 6 == false: so still c = 6, lw = 'happys'
    iteration 4:
        it will fetch element 'happy' so i is 'happy'
        check len(happy) is greator than 6== false: so still c = 6, lw = 'happys'
6. after complition of for loop we print lw = 'happys'
'''
