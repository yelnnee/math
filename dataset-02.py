import numpy as np

# Nouveau dataset 
X = np.array([30, 45, 60, 75, 90])
Y = np.array([90, 130, 170, 210, 250])

# matrice X avec biais
X_matrix = np.column_stack((np.ones(len(X)), X))

# calcul analytique 
theta = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ Y

b = theta[0]   
a = theta[1]   

print("pente a =", a)
print("biais b =", b)
