# # Données
# x = [50, 70, 90]
# y = [100, 140, 180]

# # Moyennes
# xm = sum(x) / len(x)
# ym = sum(y) / len(y)

# # Coefficient a
# a = sum((xi - xm) * (yi - ym) for xi, yi in zip(x, y)) / \
#     sum((xi - xm) ** 2 for xi in x)

# # Intercept b
# b = ym - a * xm

# print(a, b)

# Valeurs observées
Y = [100, 140, 180]

# Valeurs prédites (exemple)
Y_hat = [110, 130, 175]

# Calcul de la MSE
mse = sum((Yi - Yhi)**2 for Yi, Yhi in zip(Y, Y_hat)) / len(Y)

print(mse)

