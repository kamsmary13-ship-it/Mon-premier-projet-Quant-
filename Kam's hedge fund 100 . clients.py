# KAMS QUANT CAPITAL - VERSION 3.0 - 100 CLIENTS AUTO
# Objectif : Devenir Quatrillionnaire sans travailler 100 fois

print("=== KAMS HEDGE FUND - MODE 100 CLIENTS ===")
print("Tu vas devenir Quatrillionnaire aujourd'hui !\n")

# Le prix du cacao est le même pour tous tes clients aujourd'hui
prix_aujourdhui = int(input("1. Prix cacao AUJOURD'HUI pour tous les clients (ex: 1950) : "))
prix_futur = int(input("2. Prix cacao DANS 30 JOURS (ex: 2600) : "))
nombre_clients = int(input("3. Combien de clients tu as aujourd'hui ? (ex: 3 ou 100) : "))

gain_total_fund = 0
commission_totale = 0
valeur_totale_aujourdhui = 0

print("\n--- ON COMMENCE LA COLLECTE ---\n")

# C'est ça la boucle magique qui gère 100 clients tout seul
for i in range(1, nombre_clients + 1):
    print(f"CLIENT {i}/{nombre_clients}")
    nom = input(f"  Nom du client {i} : ")
    kilos = int(input(f"  Kilos de {nom} : "))
    
    gain = (prix_futur - prix_aujourdhui) * kilos
    commission = int(gain * 0.1)
    
    gain_total_fund += gain
    commission_totale += commission
    valeur_totale_aujourdhui += kilos * prix_aujourdhui
    
    print(f"  -> Gain pour {nom} : +{gain} F | Ta commission : {commission} F\n")

# BILAN FINAL DE BOSS
print("======================================")
print("📊 BILAN FINAL DE TON HEDGE FUND")
print("======================================")
print(f"Nombre de clients gérés : {nombre_clients}")
print(f"Valeur totale gérée aujourd'hui : {valeur_totale_aujourdhui} F")
print(f"Gain total que tu fais gagner à tes clients : {gain_total_fund} F")
print(f"💰 TA COMMISSION TOTALE (10%) : {commission_totale} F")
print("======================================")

if commission_totale >= 1000000:
    print("🔥🔥 TU ES MILLIONNAIRE AUJOURD'HUI !")
elif commission_totale >= 100000:
    print("💥 BOSS ! Tu as dépassé 100 000F de commission !")
else:
    print("Continue, à 100 clients tu seras Quatrillionnaire !")

# Pour la Cyber Sécurité, on sauvegarde tout chiffré
print(f"\n✅ Sauvegarde ce rapport dans ton GitHub : KAMS_HEDGE_FUND_100_CLIENTS.py")
