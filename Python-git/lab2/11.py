
test_string = "Geeksforgeeks is best Computer Science Portal"

print ("The original string is : " + test_string)

res = len(test_string.split())

print ("The number of words in string are : " + str(res))
a=0
b=0
for i in test_string:
    
    if i.isupper():
        a+=1
    elif i.islower():
        b+=1

        

print("The upper case letters :",a)
print("The upper case letters :",b)


