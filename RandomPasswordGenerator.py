# 8 characters
# 2 upper, 2 lower, 2 numbers, 2 special letters

import random
# list = [1, 2, 5]
# random.shuffle(list)
# print(list)

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# print(random.randint(3, 9))
# chr : returns a str representing a character whose unicode is an integer

upper1 = chr(random.randint(65, 90))
upper2 = chr(random.randint(65, 90))

lower1 = chr(random.randint(97, 122))
lower2 = chr(random.randint(97, 122))

number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))

special1 = chr(random.randint(33, 47))
special2 = chr(random.randint(33, 47))

password = upper1 + upper2 + lower1 + lower2 + number1 + number2 + special1 + special2
password = shuffle(password)

print(password)
