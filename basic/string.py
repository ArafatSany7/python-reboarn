str1 = "this is a string"
str2 = "  also a string \n this is new line"
print(str1)
print(str2)


print(str1 + str2)
print(len(str2))

ch = str2[7]
print(ch)

print(str1[0:4])
print(str2[30 : len(str2)])

print(str1.endswith("ing"))
print(str1.endswith("xyz"))

print(str1.replace("string", "String"))
print(str1.find("s"))
