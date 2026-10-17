# HEDGE FUND KAMS QUANT CAPITAL - Gestion de 100 clients
# Objectif : 1 Quatrillion

# Base de données de ton Hedge Fund
clients = [
    {"nom": "Koffi", "kilos": 500, "capital": 1000000},
    {"nom": "Aya", "kilos": 1200, "capital": 2500000},
    {"nom": "Yao", "kilos": 800, "capital": 1800000},
]

# Prix du jour (ton ancien robot)
prix_aujourd_hui = 1950
prix_dans_30_jours = 2400

print("=== KAMS QUANT CAPITAL - RAPPORT HEDGE FUND ===")
print(f"Prix cacao aujourd'hui: {prix_aujourd_hui} F")
print(f"Prix dans 30 jours: {prix_dans_30_jours} F\n")

capital_total = 0
gain_total_fund = 0

for client in clients:
    gain_client = (prix_dans_30_jours - prix_aujourd_hui) * client["kilos"]
    capital_total += client["capital"]
    gain_total_fund += gain_client
    print(f"Client: {client['nom']} | Kilos: {client['kilos']} | Gain prévu: +{gain_client} F")

print("\n--- BILAN DU FUND ---")
print(f"Nombre de clients: {len(clients)}")
print(f"Capital total géré: {capital_total} F")
print(f"Gain total pour le Fund: {gain_total_fund} F")
print(f"Commission du Fund (10%): {int(gain_total_fund * 0.1)} F")
print("\nSi on passe de 3 clients à 100 clients, on devient Quatrillionnaire !")
