#wpt to print how many special character are present in string

s = input()
count = 0
for i in s:
    if not i.isalnum():
        count+=1
print(count)
'''
#process

1. took main string as input
#string = 'ha912@'
2. asuming that there is no alphanumeric  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       it will fetch element 'h' so i is 'h'
       check wheter 'h' is not  alphanum == false, SO count =0
    iteration 2:
       it will fetch element 'a' so i is 'a'
       check wheter 'a' is not alphanum == false, SO count =0
    iteration 3:
       it will fetch element '9' so i is '9'
       check wheter '9' is not alphanum == false, SO count =0
    iteration 4:
       it will fetch element '1' so i is '1'
       check wheter '1' is not alphanum == false, SO count =0
    iteration 5:
       it will fetch element '2' so i is '2'
       check wheter '2' is not alphanum == false, SO count =0
    iteration 6:
       it will fetch element '@' so i is '@'
       check wheter '@' is not  alphanum == true:
           so count+=1 = 1
5. at last we will print the value of count =1
'''
