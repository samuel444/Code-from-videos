import matplotlib.pyplot as plt
resultTop = []
resultBottom = []
n = 6
t = 10
first = True
f = lambda cl,z: ((z-12*n) / (2*cl)) + 0.5 + t/102
for cl in range(1,52*n):
    result = f(cl, (52*n-cl)*3/13)
    resultBottom.append(result)
    if result > 0 and first:
        number = cl
        first = False

#z = 12 * n
#f = lambda cl: ((z-12*n) / (2*cl)) + 0.5 + t/102 
#resultTop = [f(cl) for _ in range(52*n - number - 1)]

#first = True
x = list(range(len(resultBottom)))
plt.scatter(x,resultBottom)
#plt.scatter(x,resultTop)
plt.xlabel("Cards Left")
plt.ylabel("Probability of high card")
plt.title("For true count " + str(t))
plt.show()