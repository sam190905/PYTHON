print("Select the conversion operation:")
print("1.celsius to Fahrenheit\n2.Fahrenheit to celsius")
a=int(input())
if a==1:
    temp=float(input("Enter the temp in celsius:"))
    print((temp/5)-(32/9),"deg fahrenheit")
elif a==2:
    temp=float(input("Enter the temp in Fahrenheit:"))
    print((temp-(32/9))*5," deg celsius")