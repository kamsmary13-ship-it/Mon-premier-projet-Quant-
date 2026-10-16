# Projet 2 - Probabilités Quant pour le cacao
jours_hausse = 7
jours_total = 10

# Formule de proba : cas favorables / cas total
probabilite = (jours_hausse / jours_total) * 100

print(f"Sur {jours_total} jours, le cacao est monté {jours_hausse} fois")
print(f"Probabilité qu'il monte demain : {probabilite}%")

if probabilite > 60:
    print("-> Signal QUANT : On ACHETE")
else:
    print("-> Signal QUANT : On attend")
