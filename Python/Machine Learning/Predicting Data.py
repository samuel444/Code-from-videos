import numpy as np
from matplotlib import pyplot as plt

car_data = np.loadtxt("car_data.txt")
X = car_data[:, 0]
y = car_data[:, 1]

predictions = []
for n in range(1,9):
    x_vandermonde = np.vander(X, n+1)
    A = (x_vandermonde.T) @ x_vandermonde
    b = (x_vandermonde.T) @ y
    theta_star = np.linalg.solve(A,b)
    
    pred_x = np.arange(0,16,0.1)
    pred_x_vandermonde = np.vander(pred_x, n+1)
    predict_matrix = theta_star * (pred_x_vandermonde)
    predict_matrix = [np.sum(i) for i in predict_matrix]

    plt.plot(pred_x,predict_matrix, label='Prediction Line')

    plt.scatter(X,y)

    plt.xlabel("Engine Size (L)")
    plt.ylabel("Fuel Efficiency (MPG)")
    plt.title("Engine Size vs Fuel Usage, N="+str(n))
    plt.legend()
    plt.show()
    
