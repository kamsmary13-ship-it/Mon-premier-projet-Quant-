# robot_semaine.py - Mary - Collège Privé Les Floriane - 2025/2026
# Le robot qui prédit pour la semaine prochaine

# Les prix du cacao des 7 derniers jours à Abidjan (en FCFA)
# Toi tu changeras ces chiffres avec les vrais prix de Google
prix_7_jours = [2700, 2750, 2720, 2800, 2850, 2820, 2880]

# ETAPE 1 : Le robot calcule la moyenne
moyenne = sum(prix_7_jours) / len(prix_7_jours)
print(f"Moyenne des 7 derniers jours: {moyenne} FCFA")

# ETAPE 2 : Il regarde si ça monte ou descend
dernier_prix = prix_7_jours[-1]
premier_prix = prix_7_jours[0]

if dernier_prix > premier_prix:
    tendance = "MONTE"
    proba = 75
    prix_prevu_semaine_prochaine = dernier_prix + 400
else:
    tendance = "DESCEND"
    proba = 65
    prix_prevu_semaine_prochaine = dernier_prix - 300

print(f"Tendance: {tendance}")
print(f"Mon robot prédit pour la semaine prochaine: {proba}% de chance que le cacao soit à {prix_prevu_semaine_prochaine} FCFA")

# ETAPE 3 : Il sauvegarde la preuve pour ta vidéo
from datetime import datetime
date = datetime.now().strftime("%d-%m-%Y")
with open("journal_preuves.txt", "a") as f:
    f.write(f"{date} | Prevision SEMAINE: {proba}% -> {prix_prevu_semaine_prochaine} FCFA (actuel {dernier_prix})\n")

print("Preuve semaine sauvegardée !")
