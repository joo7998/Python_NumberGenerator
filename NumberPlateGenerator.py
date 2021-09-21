# 2 upper + 2 num + SPACE + 3 upper

import random

upper1 = chr(random.randint(65, 90))
upper2 = chr(random.randint(65, 90))

number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))

upper3 = chr(random.randint(65, 90))
upper4 = chr(random.randint(65, 90))
upper5 = chr(random.randint(65, 90))

plate = upper1 + upper2 + number1 + number2 + ' ' + upper3 + upper4 + upper5

print(plate)