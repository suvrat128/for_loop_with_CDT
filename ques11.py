#wppt how many alphanumric values are present in given sting


s = input()
count = 0

for i in s:
    if i.isalnum():
        count+=1 
print(count)


'''
#process

1. took main string as input
#string = 'ha912'
2. asuming that there is no alphanumeric  present in the string so that count = 0
4. by using for loop:
    iteration 1:
       it will fetch first element 'h' so i is 'h'
       check wheter 'h' is a alphanum == true:
             SO count+=1 = 1
    iteration 2:
       it will fetch element 'a' so i is 'a'
       check wheter 'a' is a alphanum == true:
             SO count+=1 = 2
    iteration 3:
       it will fetch element '9' so i is '9'
       check wheter '9' is a alphanum == true:
             SO count+=1 = 3
    iteration 4:
       it will fetch element '1' so i is '1'
       check wheter '1' is a alphanum == true:
             SO count+=1 = 4
    iteration 5:
       it will fetch element '2' so i is '2'
       check wheter '2' is a alphanum == true:
             SO count+=1 = 5
    iteration 6:
       it will fetch element '@' so i is '@'
       check wheter '@' is a alphanum == false:SO count still 5
5. at last we will print the value of count =5

'''
