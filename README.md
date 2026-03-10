README — Régression linéaire et Quartet d’Anscombe

1. Objectif
Ce projet illustre les notions suivantes :
- Fonction de prédiction en régression linéaire
- Calcul des paramètres a et b
- Fonction de coût MSE
- Importance de la visualisation des données
- Analyse du quartet d’Anscombe

L’objectif principal est de montrer que des statistiques identiques peuvent correspondre à des jeux de données très différents.

2. Fonction de prédiction
En régression linéaire simple, on modélise la relation entre x et y par :

ŷ = a·x + b

où :

a est la pente

b est l’ordonnée à l’origine

ŷ est la valeur prédite

Cette fonction est dite paramétrée car son comportement dépend des paramètres a et b.

3. Calcul des paramètres a et b
Les paramètres sont obtenus par les formules suivantes :

a = [n Σ(xy) − (Σx)(Σy)] / [n Σ(x²) − (Σx)²]
b = [Σy − a Σx] / n

Ces formules proviennent de la méthode des moindres carrés.

4. Fonction de coût : MSE
Le MSE (Mean Squared Error) mesure l’erreur moyenne entre les valeurs réelles et les valeurs prédites :

MSE = (1/n) Σ (ŷi − yi)²

Interprétation :

MSE faible : bonne qualité de prédiction

MSE élevé : mauvaise qualité de prédiction

5. Quartet d’Anscombe
Les quatre jeux de données d’Anscombe ont :

la même moyenne de X

la même moyenne de Y

la même variance

la même corrélation

la même droite de régression

le même MSE

Cependant, leurs graphiques sont très différents.

Conclusion : les statistiques seules ne suffisent pas ; la visualisation est indispensable.

6. Code utilisé
Le code fourni :

calcule les paramètres a et b

calcule le MSE

trace les quatre jeux de données

affiche la droite de régression pour chacun

Il permet d’observer que des jeux de données très différents peuvent partager les mêmes indicateurs statistiques.

7. Conclusion
Ce travail montre que :

La régression linéaire repose sur une fonction de prédiction simple.

Les paramètres a et b se calculent directement à partir des données.

Le MSE permet d’évaluer la qualité d’un modèle.

Le quartet d’Anscombe démontre l’importance de visualiser les données.