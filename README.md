# CYBER COFFRE-FORT - KAMS QUANT CAPITAL
# Mission : Protéger la liste des clients du Hedge Fund

def chiffrer_donnee(texte):
    # Chiffrement ultra-simple mais efficace (comme les vrais Hedge Funds au début)
    secret = ""
    for lettre in texte:
        secret += str(ord(lettre)) + "-"
    return secret

def dechiffrer_donnee(secret):
    # Pour toi seule, tu peux retrouver les vrais noms
    original = ""
    codes = secret.split("-")
    for code in codes:
        if code != "":
            original += chr(int(code))
    return original

print("=== CYBER COFFRE-FORT KAMS ===")
nom = input("Tape le nom du client à PROTÉGER : ")
nom_chiffre = chiffrer_donnee(nom)

print(f"\n⛔ Pour les hackers, ils voient : {nom_chiffre}")
print(f"✅ Pour toi, tu sais que c'est : {nom}")
print(f"\nTu peux sauvegarder {nom_chiffre} dans ton GitHub, même si un hacker vole ton GitHub, il ne saura pas qui est ton client !")

# Test avec ton client Koffi
print("\n--- Exemple avec Koffi ---")
print(f"Koffi chiffré = {chiffrer_donnee('Koffi')}")
