"# Perceptron simple pour classer les emails en fonction de leur urgence et de l'importance du contact"

# Fonction d'activation (seuil)
def seuil(s):
    if s >= 0:
        return 1
    else:
        return 0

# Perceptron avec les paramètres de l'exemple
w1 = 0.7
w2 = 1.0
b = -1.1

# Fonction de prédiction
def perceptron(x1, x2):
    s = w1*x1 + w2*x2 + b
    return seuil(s)

# Tests des différentes situations
tests = [
    (1, 1, "Email urgent + contact important"),
    (1, 0, "Email urgent seulement"),
    (0, 1, "Contact important seulement"),
    (0, 0, "Aucun des deux")
]

for x1, x2, description in tests:
    y = perceptron(x1, x2)
    print(description, "-> sortie =", y)
