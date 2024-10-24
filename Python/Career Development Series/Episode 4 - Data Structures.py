# Creating lists
colours = ['green', 'yellow', 'orange', 'pink']
ages = [21, 43, 64, 1, 54, 51]
randomList = ['orange', 42, True, 'Daniel']

# Getting the index from a list
colours = ['green', 'yellow', 'orange', 'pink']
print (colours[2])

# Getting multiple indices
colours = ['green', 'yellow', 'orange', 'pink']
print (colours[2:])


colours = ['green', 'yellow', 'orange', 'pink']
print (colours[:2])


colours = ['green', 'yellow', 'orange', 'pink']
print (colours[1:3])

# Adding elements into lists
colours = ['green', 'yellow', 'orange', 'pink']
colours[1] = 'purple'
print (colours)


colours = ['green', 'yellow', 'orange', 'pink']
colours.append('black')
print (colours)


colours = ['green', 'yellow', 'orange', 'pink']
colours.insert(1, 'purple')
print (colours)

# Other operations for lists
colours = ['green', 'yellow', 'orange', 'pink']
print (colours.count('green'))


colours = ['green', 'yellow', 'orange', 'pink']
print (colours.index('orange'))


colours = ['green', 'yellow', 'orange', 'pink']
colours.reverse()
print (colours)

# Removing elements from lists
colours = ['green', 'yellow', 'orange', 'pink']
colours.pop(2)
print (colours)


colours = ['green', 'yellow', 'orange', 'pink']
colours.remove('yellow')
print (colours)

# Looking into tuples
tupleExample = ('hello', 4, 'cheese', True)
print (tupleExample)

# Ordered so we can use indices
tupleExample = ('hello', 4, 'cheese', True)
print (tupleExample[2])

# Sets
setExample = {'hello', 'hi', 'hey', 5}

# Sets unique operations
setExample1 = {'hello', 5, 'hola', 'henry', 'chicken'}
setExample2 = {'yo', 'running', 'pickles', 42, 'chicken', 5, 'hola'}
print (setExample1.difference(setExample2))


setExample1 = {'hello', 5, 'hola', 'henry', 'chicken'}
setExample2 = {'yo', 'running', 'pickles', 42, 'chicken', 5, 'hola'}
print (setExample1.intersection(setExample2))


setExample1 = {'hello', 5, 'hola', 'henry', 'chicken'}
setExample2 = {'yo', 'running', 'pickles', 42, 'chicken', 5, 'hola'}
print (setExample1.union(setExample2))


setExample1 = {'hello', 5, 'hola', 'henry', 'chicken'}
setExample2 = {'yo', 'running', 'pickles', 42, 'chicken', 5, 'hola'}
print (setExample1.symmetric_difference(setExample2))

# Dictionaries, key:value format
opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}

opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
print (opposites['hello'])

opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
opposites['hello'] = 'goodbye'
print (opposites['hello'])

# Trying to print a value from a key that doesn't exists, this will cause an error
'''opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
print (opposites['stand'])'''

# Same thing, but this time using get() it will return 'None'
opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
print (opposites.get('stand'))

# Getting set like objects from these dictionary operations:
opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
print (opposites.items())


opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
print (opposites.keys())


opposites = {'hello':'bye', 'black':'white', 'up':'down','left':'right', 'girl':'boy'}
print (opposites.values())
