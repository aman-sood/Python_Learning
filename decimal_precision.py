

# Seen some example to fix decimal precision but they do with lot of mathematical
# computation. I felt it easier this way and it will be faster while execution. 
# Still welcome input if there are other better ways other than string conversions
# which will take less time to execute.


maxLimit = int(input('Max digits after decimal :'))

number = float(input('Number please :'))

numberWithPrecision = "%.{}f".format(maxLimit) % number

# Conversion to float if required 
floatNumber = float(numberWithPrecision)

print(numberWithPrecision)

# for using as a float value
print(floatNumber + 32.2)