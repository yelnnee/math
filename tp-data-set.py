import matplotlib.pyplot as plt

# Fonction pour calculer a et b
def regression_coeffs(X, Y):
    n = len(X)
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_xy = sum(x*y for x, y in zip(X, Y))
    sum_x2 = sum(x*x for x in X)

    denom = (n * sum_x2 - sum_x**2)
    if denom == 0:
        return 0, sum_y / n  # Cas où tous les X sont identiques

    a = (n * sum_xy - sum_x * sum_y) / denom
    b = (sum_y - a * sum_x) / n
    return a, b

# Fonction MSE
def mse(X, Y, a, b):
    return sum((a*x + b - y)**2 for x, y in zip(X, Y)) / len(X)

# Datasets d'Anscombe
datasets = [
    ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
     [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),

    ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
     [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 7.26, 7.26, 4.74]),

    ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
     [7.46, 6.77, 12.74, 7.11, 8.81, 8.84, 6.08, 5.39, 8.15, 6.40, 5.73]),

    ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
     [6.58, 5.76, 5.76, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])
]

plt.figure(figsize=(12, 10))

for i, (X, Y) in enumerate(datasets, start=1):
    a, b = regression_coeffs(X, Y)
    m = mse(X, Y, a, b)

    plt.subplot(2, 2, i)
    plt.scatter(X, Y, color="blue", label="Données")

    # Tracer la droite de régression
    x_range = [2, 20]
    y_range = [a * x + b for x in x_range]
    plt.plot(x_range, y_range, color="red", label=f"y = {a:.2f}x + {b:.2f}")

    plt.xlim(2, 20)
    plt.ylim(2, 14)
    plt.title(f"Dataset {i} — a={a:.2f}, b={b:.2f}, MSE={m:.2f}")
    plt.legend()

plt.tight_layout()
plt.show()
