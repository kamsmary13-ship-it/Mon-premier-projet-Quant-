# CYBER SECURITE - KAMS QUANT CAPITAL
# Protège les clients du Hedge Fund

def securiser_client(nom, mot_de_passe):
    # Vérifie si le mot de passe est assez fort pour un Quatrillionnaire
    if len(mot_de_passe) < 8:
        return f"⛔ ACCES REFUSE pour {nom} : Mot de passe trop faible ! Hacker peut voler tes milliards !"
    
    if mot_de_passe.isdigit():
        return f"⛔ ACCES REFUSE pour {nom} : Ne mets pas que des chiffres !"
    
    # Chiffrement simple (comme les vrais hedge funds)
    code_secret = ""
    for lettre in nom:
        code_secret += str(ord(lettre))
    
    return f"✅ ACCES AUTORISE pour {nom} | Coffre-fort sécurisé | Code client : {code_secret[:8]} | Statut : PROTÉGÉ CONTRE LES HACKERS"

# Test de sécurité
print("=== TEST CYBER SECURITE HEDGE FUND ===")
print(securiser_client("Koffi", "123"))
print(securiser_client("Mary", "Kams@2026!Quatrillion"))
print(securiser_client("Client VIP", "AbidjanQuant!"))
