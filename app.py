
# for i in range(10):
#     print(i+1)


# count = 1
# while count < 5:
#     print(count)
#     count += 1

#
# square = []
# for i in range(10):
#     square.append(i*i)
# print(square)


# # in python arrray is called lists don't forgot ?
# square = [i*i for i in range(10)]
# print(square)

# while loop :
# num = []
# x = 5
# while x < 10:
#     num.append(x)
#     x += 1

# print(num)

# Date structure :
# lists :
# Numbers = [2, 1, 4, 5]
# print(Numbers[0])

# # sets  :
# Num = {2, 4, 6, 6}
# print(Num)


# function :
# def add(a, b=10):
#     result = a * b
#     print(result)


# add(2, 5)


# modules :

# import math
# import abdibasid
# from datetime import date

# print(abdibasid.adder(4, 5))

# print(math.ceil(2.5))

# print(date.today())

# person = {
#     "name": "abdibasid Mohamed Aden",
#     "age": 20,
#     "department": "Software Engineering"
# }

# print(person["department"])


# # variable and Data types :

# x = 5
# y = 6

# print(x)
# print(y)

# with open("abdibasid.py", "r") as file:
#     readingFile = file.read()
#     print(readingFile)


try:
    number = int(input("Enter a number:"))

    print(f"you entered {number}")

except ValueError:
    print("you entered a invalid Num!:")
