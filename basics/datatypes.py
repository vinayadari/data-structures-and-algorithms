from math import floor
import math
import time
# isinstance
st = time.perf_counter()
pizza = str("Pepprioni")
print(isinstance(pizza, int))
# concatination
first = "vinay"
last = "adari"
fullname = first + " " + last
print(fullname)
# adding at the end
fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))

statement = "I love rock music from the " + decade + "s."

print(statement)

# multiple lines
multiline = '''
Hey, how are you?

I was just checking in.


                All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work \t Hey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first)
print(first.upper())
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "ok"))

print(len(multiline))
multiline += "                                                "
multiline = "                       "+multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffe".ljust(16, "."), "$1".rjust(4))
print("muffin".ljust(16, "."), "$2".rjust(4))
print("muffin".ljust(16, "."), "$4".rjust(4))

# string index values
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("V"))
print(first.endswith("y"))

# Boolean data type

myvalue = True
mynewvalue = False
secondvalue = None

print(myvalue, mynewvalue, secondvalue)

# numeric data type
price = 80
new = 80
print(type(price+new))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built in function
print(abs(comp_value))
print(abs(comp_value * -1))

print(round(abs(comp_value)))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(9.76))  # ceils to the next number
print(floor(9.76))  # just remove the deciaml

# casting to string
zipcode = "10001"
zip_code = int(10001)
print(type(zip_code))
# incorrect conversion cant be converted
end = time.perf_counter()
print(end-st)
