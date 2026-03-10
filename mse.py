Y = [100, 140, 180]      # valeurs observées
Y_hat = [100, 140, 180]  # valeurs prédites identiques

mse = sum((Yi - Yhi)**2 for Yi, Yhi in zip(Y, Y_hat)) / len(Y)

print(mse)  
