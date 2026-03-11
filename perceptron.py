import numpy as np
import matplotlib.pyplot as plt

# Fonction d'activation (seuil)
def seuil(s):
    return 1 if s >= 0 else 0

# Paramètres du perceptron
w1 = 0.7
w2 = 1.0
b = -1.1

# Fonction de prédiction
def perceptron(x1, x2):
    s = w1*x1 + w2*x2 + b
    return seuil(s)

# Données (toutes les combinaisons possibles)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
labels = ["Aucun critère", "Contact important", "Urgent", "Urgent + contact important"]

# Calcul des sorties
y = [perceptron(x1, x2) for x1, x2 in X]

# Affichage des résultats
for i in range(len(X)):
    print(labels[i], "-> sortie =", y[i])

# Graphe des points
plt.figure(figsize=(5,5))
for i in range(len(X)):
    x1, x2 = X[i]
    if y[i] == 1:
        plt.scatter(x1, x2, color="green")
    else:
        plt.scatter(x1, x2, color="red")
    plt.text(x1+0.02, x2+0.02, labels[i], fontsize=9)

plt.xlabel("x1 (urgent)")
plt.ylabel("x2 (contact important)")
plt.title("Décision du perceptron sur les emails")
plt.grid(True)
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.show()
