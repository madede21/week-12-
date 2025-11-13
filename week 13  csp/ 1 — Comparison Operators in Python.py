# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
# 10 > 5 true
# 7 == 2 * 3 + 1  true
# 8 != 8 false
# 4 <= 2 + 2 true

# Write 3 examples that result in True and 3 that result in False.

15 > 5
10 > 2
1 > 0

# Create a simple grade-checking condition:
# practice problem :
 
# Grade Checker

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


 
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
grade = int(input("enter your score: "))
if grade >= 60:
    print("you passed the test")
else: print("you failed the test :(")



password = input("Enter you password: ")
if len(password) >= 8 and any (char.isdigit() for char in password):
    print("password is valid.")
else:
    print("password is invalid. ")


