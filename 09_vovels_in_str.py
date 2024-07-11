#wpt how many voels are present in givem string

s = input()

vol = 'aeiouAEIOU'
count = 0

for i in s:
    if i in 'aeiouAEIOU':
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
       check 's' is present in variable vovels('aeiouAEIOU') FALSE so count still =0
    iteration 2:
       it will fetch element 'u' so i is 'u'
       check 'u' is present in variable vovels('aeiouAEIOU') TRUE:
               so count+=1 = 1
    iteration 3:
       it will fetch element 'v' so i is 'v'
       check 'v' is present in variable vovels('aeiouAEIOU') FALSE so count still =1
    iteration 4:
       it will fetch element 'r' so i is 'r'
       check 'r' is present in variable vovels('aeiouAEIOU') FALSE so count still =1
    iteration 5:
       it will fetch element 'a' so i is 'a'
       check 'a' is present in variable vovels('aeiouAEIOU') TRUE:
               so count+=1 = 2
    iteration 6:
       it will fetch element 't' so i is 't'
       check 't' is present in variable vovels('aeiouAEIOU') FALSE so count still =2
5. at last we print the value of count = 2
'''
