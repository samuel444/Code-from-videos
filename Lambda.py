example1 = lambda : print ('Hello')
example1()
example2 = lambda x, y : x + y
print (example2(2,5))
example3 = lambda x, y, z: x + y - x
print (example3(y = 4, z = 2, x = 3))
example4 = lambda *args : sum(args)
print (example4(5, 2, 5, 7, 6))
list1 = [14, 1, 8, 3, 9, 12, 5, 2, 71]
example5 = list(map(lambda x : x+2, list1))
print (example5)
example6 = list(filter(lambda x : x>5, list1))
print (example6)
