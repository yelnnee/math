import numpy as np
import matplotlib.pyplot as plt

# choix dataset 01
X = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
Y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])


X_matrix = np.column_stack((np.ones(len(X)), X))

# Calcul analytique:
theta = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ Y

b = theta[0]
a = theta[1]

print("pente a =", a)
print("biais b =", b)

# Prédictions
Y_pred = a * X + b

# MSE
mse = np.mean((Y - Y_pred)**2)
print("MSE =", mse)

# Visualisation
plt.scatter(X, Y, color="blue", label="Données")
plt.plot(X, Y_pred, color="red", label="Droite de régression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
