import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

# Script Python : perceptron from scratch fonctionnel sur AND / OR
def step(s):
    return 1 if s >= 0 else 0

def perceptron_train(X, y, eta=0.1, epochs=20):
    w = np.zeros(X.shape[1])
    b = 0.0
    history = []

    for _ in range(epochs):
        for xi, yi in zip(X, y):
            s = np.dot(w, xi) + b
            y_pred = step(s)
            error = yi - y_pred
            w += eta * error * xi
            b += eta * error
            history.append((w.copy(), b))

    return w, b, history

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([0,0,0,1])
y_or  = np.array([0,1,1,1])
y_xor = np.array([0,1,1,0])

w_and, b_and, hist_and = perceptron_train(X, y_and)
w_or,  b_or,  hist_or  = perceptron_train(X, y_or)
w_xor, b_xor, hist_xor = perceptron_train(X, y_xor)

print("From scratch")
print("AND :", w_and, b_and)
print("OR  :", w_or,  b_or)
print("XOR :", w_xor, b_xor)

# Graphique : frontière de décision animée sur N itérations
def plot_decision_boundary(X, y, w, b, title):
    xx, yy = np.meshgrid(
        np.linspace(-0.5, 1.5, 200),
        np.linspace(-0.5, 1.5, 200)
    )

    Z = np.array([step(w[0]*x + w[1]*y_ + b)
                  for x, y_ in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
    plt.scatter(X[:,0], X[:,1], c=y, s=100, edgecolors='k')
    plt.title(title)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()

def animate_boundary(X, y, history, title):
    xx, yy = np.meshgrid(
        np.linspace(-0.5, 1.5, 200),
        np.linspace(-0.5, 1.5, 200)
    )

    for w, b in history:
        Z = np.array([step(w[0]*x + w[1]*y_ + b)
                      for x, y_ in zip(xx.ravel(), yy.ravel())])
        Z = Z.reshape(xx.shape)

        plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
        plt.scatter(X[:,0], X[:,1], c=y, s=100, edgecolors='k')
        plt.title(title)
        plt.pause(0.05)
        plt.clf()

plot_decision_boundary(X, y_and, w_and, b_and, "Perceptron from scratch – AND")
plot_decision_boundary(X, y_or,  w_or,  b_or,  "Perceptron from scratch – OR")
plot_decision_boundary(X, y_xor, w_xor, b_xor, "Perceptron from scratch – XOR (échec)")

# Analyse comparative perceptron manuel vs sklearn
clf_and = Perceptron(max_iter=20, eta0=0.1)
clf_or  = Perceptron(max_iter=20, eta0=0.1)
clf_xor = Perceptron(max_iter=20, eta0=0.1)

clf_and.fit(X, y_and)
clf_or.fit(X, y_or)
clf_xor.fit(X, y_xor)

print("\nSklearn")
print("AND :", clf_and.coef_, clf_and.intercept_)
print("OR  :", clf_or.coef_,  clf_or.intercept_)
print("XOR :", clf_xor.coef_, clf_xor.intercept_)

plot_decision_boundary(X, y_and, clf_and.coef_[0], clf_and.intercept_[0], "Sklearn – AND")
plot_decision_boundary(X, y_or,  clf_or.coef_[0],  clf_or.intercept_[0],  "Sklearn – OR")
plot_decision_boundary(X, y_xor, clf_xor.coef_[0], clf_xor.intercept_[0], "Sklearn – XOR (échec)")

# Note écrite : explication de la limite XOR et solution envisagée
# XOR n'est pas linéairement séparable, donc aucune droite ne peut séparer correctement les classes.
# Un perceptron simple échoue forcément, même avec sklearn.
# La solution est d'utiliser un perceptron multicouche (MLP) avec une couche cachée.
