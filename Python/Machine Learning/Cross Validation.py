import numpy as np
from matplotlib import pyplot as plt

car_data = np.loadtxt("car_data.txt")
np.random.shuffle(car_data)

chunks = 5
car_data_chunks = np.array_split(car_data, chunks)

losses = []

for i in range(chunks):
    D_test = car_data_chunks[i]
    D_train = np.array([x for x in car_data if not x in D_test])

    X_test = D_test[:,0]
    y_test = D_test[:, 1]

    X_train = D_train[:,0]
    y_train = D_train[:, 1]


    x_vandermonde = np.vander(X_train, 4)

    A = (x_vandermonde.T) @ x_vandermonde
    b = (x_vandermonde.T) @ y_train
    theta_star = (np.linalg.solve(A,b))

    X_test_vandermonde = np.vander(X_test, 4)
    predict_matrix = theta_star * (X_test_vandermonde)
    y_test_prediction = [np.sum(i) for i in predict_matrix]
    
    plt.scatter(X_test, y_test, label="Test Statistics", s=20)
    plt.scatter(X_train, y_train, label="Train Statistics", s=7)
    plt.scatter(X_test, y_test_prediction, label="Predicted Test Statistics", s=20)

    plt.xlabel("Engine Size (L)")
    plt.ylabel("Fuel Efficiency (MPG)")
    plt.title("Engine Size vs Fuel Usage, Chunk "+str(i+1))
    plt.legend()
    plt.show()

    losses.append(np.mean((y_test_prediction - y_test)**2))

print (losses)
cross_validation_loss = np.mean(losses)
print (cross_validation_loss)



