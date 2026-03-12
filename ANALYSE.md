## Analyse du TP — Perceptron et XOR

### Pourquoi le perceptron simple échoue sur XOR ?
- Le perceptron simple ne peut apprendre que des frontières de décision linéaires.
- Le problème XOR est non linéairement séparable : les classes sont disposées en diagonale.
- Aucune droite ne peut séparer correctement les sorties 0 et 1 du XOR.
- Le perceptron n’arrive donc jamais à converger, même avec plus d’itérations.

### Effet du nombre d’itérations et du taux d’apprentissage
- Augmenter le nombre d’epochs ne permet pas au perceptron de trouver une solution correcte.
- Modifier le learning rate change seulement la vitesse d’apprentissage, pas la capacité du modèle.
- Le problème vient de la structure du perceptron, pas de l’entraînement.

### Visualisation et frontière de décision
- En représentant les points du XOR dans le plan, on observe deux classes en diagonale.
- Une seule droite ne peut pas séparer ces deux groupes.
- La frontière nécessaire est non linéaire, ce qu’un perceptron simple ne peut pas produire.

### Comment une couche cachée permet de résoudre XOR ?
- Une couche cachée permet de combiner plusieurs frontières linéaires.
- Deux neurones cachés peuvent créer deux demi-plans différents.
- Le neurone de sortie combine ces informations pour produire une séparation non linéaire.
- C’est le principe des réseaux neuronaux multicouches (MLP), capables de résoudre XOR.
