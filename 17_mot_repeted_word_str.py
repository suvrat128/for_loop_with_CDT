# wpt most repeted word in given string

s = input()
st = s.split()
mrc= ''
c = 0
for i in st:
    if st.count(i)>c:
        c=st.count(i)
        mrc=i
print(mrc)

'''
#process
1. took string as input
# string=='hello happy bye happy'
2. split the string with space and store in variable st
3. take a variable with empty string
4. asume that the string is empty so c =0
5. by using for loop:
    iteration 1:
        it will fetch element 'hello' so i is 'hello'
        check count(hello)in st is greator than 0 == true:
            mrc = 'hello'
            and c = 1
    iteration 2:
        it will fetch element 'happy' so i is 'happy'
        check count(happy)in st is greator than 0 == true:
            mrc = 'happy'
            and c = 2
    iteration 3:
        it will fetch element 'hai' so i is 'hai'
        check count(hai)in st is greator than 2 == false: so still c = 2, mrc = 'happy'
    iteration 4:
        it will fetch element 'happy' so i is 'happy'
        check count(happy)in s is greator than 2 == false: so still c = 2, mrc = 'happy'
6. after complition of for loop we print mrc = 'happy'
        

  
'''
