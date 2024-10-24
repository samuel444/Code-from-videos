# The basic if statement
if True:
    print ('Hello')

# Using a condition and it is false
var = 1
if var == 0:
    print ('Hello')

# Using a condition and it is true
var = 0
if var == 0:
    print ('Hello')

# First if else statement, this shall print hello
var = 0
if var == 0:
    print ('Hello')
else:
    print ('Bye')

# This will print bye
var = 2
if var == 0:
    print ('Hello')
else:
    print ('Bye')

# Elif Statements with an else
if var == 1:
    print ('1')
elif var == 2:
    print ('2')
elif var == 3:
    print ('3')
elif var == 4:
    print ('4')
else:
    print ('5')

# Without an else
if var == 1:
    print ('1')
elif var == 2:
    print ('2')
elif var == 3:
    print ('3')
elif var == 4:
    print ('4')

# Nested if statements
var = 1
if var == 1:
    var2 = 10
    if var2 == 10:
        print ('Nest')

# Will not print anything as first if is not true
var = 2
if var == 1:
    var2 = 10
    if var2 == 10:
        print ('Nest')

# Will not print anything as nested if is not true
var = 1
if var == 1:
    var2 = 9
    if var2 == 10:
        print ('Nest')

# While loop, this will loop forever
while True:
    print ('Hello')

# Will repeat until var equals 5
var = 0
while var != 5:
    var += 1
    print (var)

# First for loops, colour will go through every element in the list, colours
colours = ['blue','green','yellow']
for colour in colours:
    print (colour)

# Range will create a list of numbers up to 5
for i in range(5):
    print (i)

# Add a starting element to the range
for i in range(2,7):
    print (i)

# Adding a step
for i in range(2,7,2):
    print (i)

# Will go through every character in the string
string = 'hello'
for i in string:
    print (i)

# Using continue to go onto the next iteration
for i in range(1,8):
    if i == 5:
        continue
    print (i)

# Stopping the for loop with break
for i in range(1,8):
    if i == 5:
        break
    print (i)
