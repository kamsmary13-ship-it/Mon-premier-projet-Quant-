# produit.py - Mary - Collège Privé Les Florians
# Etape 2 : Le Journal

import datetime

# --- 1. TOI TU CHANGES ICI SEULEMENT ---
nom_produit = "igname"   # mets cacao ou riz ou igname
prix_hier = 600
prix_aujourdhui = 650

# --- 2. LE ROBOT CALCULE DEMAIN ---
if prix_aujourdhui > prix_hier:
    prediction_demain = prix_aujourdhui + 50
    chance = 72
    conseil = "Attends demain pour vendre"
else:
    prediction_demain = prix_aujourdhui - 30
    chance = 68
    conseil = "Vends aujourd'hui"

# --- 3. ON AFFICHE ---
aujourdhui_date = datetime.date.today()
demain_date = aujourdhui_date + datetime.timedelta(days=1)

print("--- RESULTAT ---")
print(f"Produit: {nom_produit}")
print(f"Aujourd'hui ({aujourdhui_date}): {prix_aujourdhui} FCFA")
print(f"Prediction pour DEMAIN ({demain_date}): {prediction_demain} FCFA")
print(f"Chance: {chance}%")
print(f"Conseil: {conseil}")

# --- 4. LE JOURNAL - C'EST NOUVEAU ---
# Ca va ecrire tout seul dans un cahier qui s'appelle journal.txt
with open("journal.txt", "a") as cahier:
    cahier.write(f"{aujourdhui_date} | {nom_produit} | Aujourd'hui:{prix_aujourdhui} | Pred Demain:{prediction_demain} | Chance:{chance}%\n")

print("\nC'est bon ! J'ai ecrit dans ton journal.txt")
