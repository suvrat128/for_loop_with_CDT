#wpt how many consonant are present in string

s = input()

vol = 'aeiouAEIOU'
count = 0

for i in s:
    if i.isalpha():
        if i not in vol:
            count+=1
print(count)
'''
#process
1. took main string as input
#strint input = 'suvrat'
2. we define a veriable volvels inside we store 'aeiouAEIOU'
3. asuming that there is no vovels  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       it will fetch first element 's' so i is 's'
       check wheter 's' is a alpha == true:
           check 's' is not  present in variable vovels('aeiouAEIOU') TRUE
               SO count+=1 = 1
    iteration 2:
       it will fetch  element 'U' so i is 'U'
       check wheter 'U' is a alpha == true:
       check 'U' is NOT present in variable vovels('aeiouAEIOU') FALSE so count still =1
    iteration 3:
       it will fetch element 'v' so i is 'v'
       check wheter 'v' is a alpha == true:
           check 'v' is not  present in variable vovels('aeiouAEIOU') TRUE
               SO count+=1 = 2
    iteration 4:
       it will fetch element 'r' so i is 'r'
       check wheter 'r' is a alpha == true:
           check 'r' is not  present in variable vovels('aeiouAEIOU') TRUE
               SO count+=1 = 3
    iteration 5:
       it will fetch  element 'a' so i is 'a'
       check wheter 'a' is a alpha == true:
       check 'a' is NOT present in variable vovels('aeiouAEIOU') FALSE so count still =3
    iteration 6:
       it will fetch element 't' so i is 't'
       check wheter 't'is a alpha == true:
           check 't' is not  present in variable vovels('aeiouAEIOU') TRUE
               SO count+=1 = 4
5. at last we print the value of count = 4

'''
