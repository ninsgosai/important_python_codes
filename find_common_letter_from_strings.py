str1 = input("Enter 1st string:")
str2 = input("Enter 2nd string:")


# Method 1
match = ""
for i in str1:
    if i in str2 and i not in match:
        match = match + i
for i in str2:
    if i in str1 and i not in match:
        match = match + i
print("Matched chars are :", match.replace(" ", ""))


# Method 2
str2 = set(str2)
str1 = set(str1)
print("Matched chars are :", "".join(str2 & str1).replace(" ", ""))
