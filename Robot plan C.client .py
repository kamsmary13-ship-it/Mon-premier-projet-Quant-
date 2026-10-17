# ROBOT DE MARY - PLAN C - VERSION CLIENT
print("=== ROBOT CACAO DE MARY - CONSEILLER PRO ===")

# 1. Tes prix à toi (tu changes ici chaque jour)
prix = [1800, 1820, 1810, 1850, 1840, 1860, 1890, 1900, 1920, 1950]
somme = 0
for i in range(9):
    somme = somme + (prix[i+1] - prix[i])
moyenne = somme / 9

prix_demain = int(prix[-1] + moyenne)
prix_semaine = int(prix[-1] + moyenne * 7)
prix_mois = int(prix[-1] + moyenne * 30)

# 2. Le robot demande au client
print(f"Aujourd'hui le cacao est à {prix[-1]} F")
print("")
nom = input("Quel est le nom du client ? ")
kilos = int(input(f"{nom}, tu as combien de kilos de cacao ? "))

# 3. Le robot calcule son gain
gain_semaine = (prix_semaine - prix[-1]) * kilos
gain_mois = (prix_mois - prix[-1]) * kilos

print("")
print(f"--- RÉSULTAT POUR {nom.upper()} ---")
print(f"Si tu vends aujourd'hui: {prix[-1] * kilos} F")
print(f"Si tu attends 7 jours: {prix_semaine * kilos} F (tu gagnes +{gain_semaine} F)")
print(f"Si tu attends 30 jours: {prix_mois * kilos} F (tu gagnes +{gain_mois} F)")
print("")
print(f"CONSEIL FINAL POUR {nom}: Attends 30 jours !")
print(f"Tu vas gagner {gain_mois} F de plus avec ton cacao !")
