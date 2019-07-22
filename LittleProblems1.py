print("\n// Problem 1: Convert 1024 to binary and hexadecimal representation\n")

num = 1024
print(f"The Binary number of {num} is " + bin(num))
print(f"The Hexadecimal number of {num} is " + hex(num))


print("\n// Problem 2: Round 5.23222 to two decimal places\n")

num = 5.23222
print(round(num,2))


print("\n// Problem 3: Check if every letter in the string s is lower case")
print("s = 'hello how are you Mary, are you feeling okay?'\n")

s = 'hello how are you Mary, are you feeling okay?'
if s.islower():
    print("Yes all letters are lower case")
else:
    print("No, not all letters are lower case")


print("\n// Problem 4: How many times does the letter 'w' show up in the string below?")
print("s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'\n")

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print("The letter 'w' appears " + str(s.count('w')) + " times.")


print("\n// Problem 5: Find the elements in set1 that are not in set2:")
print("set1 = {2,3,1,5,6,8}\nset2 = {3,1,7,5,6,8}\n")

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print("The elements that are not inside are: " + str(set1.difference(set2)))


print("\n// Problem 6: Find all elements that are in either set:\n")

print("The elements that are in either set are: " + str(set1.intersection(set2)))


print("\n// Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.\n")
res = {x:x**3 for x in range(5)}
print("{k:v**3 for k in range(5)}" + " --> " + str(res))


print("\n// Problem 8: Reverse the list below:")
print("list1 = [1,2,3,4]\n")
list1 = [1,2,3,4]
list1.reverse()
print("The reverse of [1,2,3,4] is " + str(list1))


print("\n// Problem 9: Sort the list below:")
print("list2 = [3,4,2,5,1]\n")
list2 = [3,4,2,5,1]
list2.sort()
print("The sorted list is: " + str(list2))




