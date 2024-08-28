s1=int(input("Enter the first side"))
s2=int(input("Enter the second side"))
s3=int(input("Enter the third side"))

if (s1*s1)+(s2*s2)==(s3*s3) or (s2*s2)+(s2*s2)==(s1*s1) or (s1*s1)+(s3*s3)==(s2*s2):
    print("It is right triangle!")
else:
    print("It is not right triangle!")

