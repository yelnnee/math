#EXO 01 :
# # Définition de la matrice A (2x2)
# A = [
#     [1, 2],
#     [3, 4]
# ]

# # Définition du vecteur x (2x1)
# x = [5, 6]

# # Calcul du produit Ax :
# # Pour chaque ligne i de la matrice A,
# # on calcule : A[i][0] * x[0] + A[i][1] * x[1]
# Ax = [
#     A[i][0] * x[0] + A[i][1] * x[1]
#     for i in range(len(A))
# ]

# # Affichage du résultat
# print(Ax)  # Résultat attendu : [17, 39]

#EXO 02 :

# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# x = [2, 4, 6]
# Ax = [sum([A[i][j] * x[j] for j in range(len(x))]) for i in range(len(A))]

# print (Ax)

