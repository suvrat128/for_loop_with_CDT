#wpt most repeted charecter in given string

s = input()

mrc=''
c = 0
for i in s:
    if s.count(i)>c:
        mrc=i
        c = s.count(i)
print(mrc)

'''
#process
1. took string as input
# strint=='happy'
2. take a variable with empty string
3. asume that there is no character in the string so c =0
4. by using for loop
    iteration 1:
        it will fetch element 'h' so i is 'h'
        check count(h)in s is greator than 0 == true:
            mrc = 'h'
            and c = 1
    iteration 2:
        it will fetch element 'a' so i is 'a'
        check count(a)in s is greator than 1 == false: so still c = 1, mrc = 'h'
    iteration 3:
        it will fetch element 'p' so i is 'p'
        check count(p)in s is greator than 1 == true:
            mrc = 'p'
            and c = 2
    iteration 4:
        it will fetch element 'p' so i is 'p'
        check count(p)in s is greator than 2 == false: so still c = 2 ,mrc = 'p',
    iteration 5:
        it will fetch element 'y' so i is 'y'
        check count(y)in s is greator than 2 == false: so still c = 2, mrc = 'p'
5. after complition of for loop we will print mre = 'p'
    
'''
