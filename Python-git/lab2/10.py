s=input("Enter the string:")
if s==s[::-1]:
    print("Yes")
else:
    print("No")
    print("No of occurences:")




all_freq = {}

for i in s:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "
	+ str(all_freq))
