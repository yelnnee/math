import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation

# Dataset 1 (Anscombe)
x = np.array([10,8,13,9,11,14,6,4,12,7,5])
y = np.array([8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68])

n = len(x)

# Paramètres initiaux
w = 0
b = 0
lr = 0.01
iterations = 100

loss_history = []
w_history = []
b_history = []

# Descente de gradient
for i in range(iterations):
    y_pred = w * x + b

    loss = np.mean((y - y_pred)**2)
    loss_history.append(loss)

    dw = (-2/n) * np.sum(x * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)

    w -= lr * dw
    b -= lr * db

    w_history.append(w)
    b_history.append(b)

print("Descente de gradient :")
print("w =", w)
print("b =", b)

# Courbe du MSE
plt.plot(loss_history)
plt.xlabel("Itérations")
plt.ylabel("MSE")
plt.title("Convergence de la descente de gradient")
plt.show()

# Animation de la droite
fig, ax = plt.subplots()
ax.scatter(x, y, color="blue")
line, = ax.plot([], [], 'r')

def update(i):
    y_pred = w_history[i] * x + b_history[i]
    line.set_data(x, y_pred)
    return line,

ani = FuncAnimation(fig, update, frames=len(w_history), interval=100)
plt.title("Évolution de la droite pendant l'entraînement")
plt.show()

# Comparaison avec scikit-learn
model = LinearRegression()
model.fit(x.reshape(-1,1), y)

print("\nScikit-learn :")
print("coef =", model.coef_[0])
print("intercept =", model.intercept_)
