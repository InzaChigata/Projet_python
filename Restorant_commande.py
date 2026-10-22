import csv
from datetime import datetime

# =================================================
# 1. ACCUEIL ET VÉRIFICATION DU CLIENT
# =================================================
print("=== BIENVENUE chez Inza Chigata ===")

nom = ""
while True:
    nom = input("Entrez votre nom: ").strip()
    if nom != "":
        break
    print("Le nom ne doit pas être vide.")

while True:
    try:
        age = int(input("Entrez votre age: "))
        break
    except ValueError:
        print("Reprends la saisie. Veuillez entrer un nombre valide.")

# Condition d'accès au menu
if 14 < age < 100:
    print(f"\nBonjour {nom}, Vous  pouvez passer votre commande !")
else:
    print("Désolé, vous ne pouvez  pas passer de commande.") 
    exit()

# ==========================================
# 2. BASE DE DONNÉES ET AFFICHAGE DU MENU
# ==========================================
def affiche_menu(nourriture):
    print("\n" + "="*30)
    print("          MENU DU JOUR          ")
    print("="*30)
    for element in nourriture:
        print(f"[{element['id']}] {element['nom']} : {element['prix']} FCFA")
    print("="*30)

Plats = [
    {"id": 0, "nom": "Alloco Oeuf", "prix": 2700},
    {"id": 1, "nom": "Attiéké poisson braisé", "prix": 2500},
    {"id": 2, "nom": "Garba", "prix": 1000},
    {"id": 3, "nom": "Sauce arachide avec riz", "prix": 2000},
    {"id": 4, "nom": "Kedjenou de poulet", "prix": 3000},
    {"id": 5, "nom": "Placali sauce graine", "prix": 1500},
    {"id": 6, "nom": "Foutou banane sauce arachide", "prix": 2500},
    {"id": 7, "nom": "Alloco poulet frit", "prix": 1800},
    {"id": 8, "nom": "Soupe de poisson", "prix": 2200},
    {"id": 9, "nom": "Riz gras au poulet", "prix": 2000},
    {"id": 10, "nom": "Brochettes d’agneau", "prix": 2700}
]

# Affichage des plats disponibles
affiche_menu(Plats)

# ==========================================
# 3. LA GRANDE BOUCLE DE COMMANDE MULTIPLE
# ==========================================
Commande = []

print("Entrez 'q' lorsque vous avez fini de choisir vos plats.")

while True:
    # 1. Demander la saisie (en texte d'abord)
    choix = input("\nEntrez le numéro du plat (ou 'q' pour terminer) : ").strip().lower()
            
    # CONDITION DE SORTIE : Si le client tape 'q', on arrête la boucle globale
    if choix == 'q':
        print("\nFin de la prise de commande. Passage à la caisse...")
        break

    # Conversion en entier s
    try:
        commande_intermediaire = int(choix)
    except ValueError:
        print("Saisie invalide. Veuillez entrer un numéro de plat valide ou 'q' pour quitter.")
        continue 

    # 2. Vérifier si le plat existe
    plat_trouve = None
    for plat in Plats:
        if plat["id"] == commande_intermediaire:
            plat_trouve = plat
            break
            
    if plat_trouve is None:
        print("Ce numéro de plat n'existe pas. Veuillez réessayer.")
        continue

    # 3. Demander la quantité
    while True:
        try:
            quantite = int(input(f"Entrez la quantité de {plat_trouve['nom']} : "))
            if quantite <= 0:
                print("La quantité doit être supérieure à 0.")
                continue
            break
        except ValueError:
            print("Reprends la saisie. Veuillez entrer un nombre entier.")

    # 4. Ajouter à la commande
    Commande.append({
        "id": plat_trouve["id"],
        "nom": plat_trouve["nom"],
        "prix_unitaire": plat_trouve["prix"],
        "quantite": quantite
    })
    print(f"-> {quantite} x {plat_trouve['nom']} ont été ajoutés à votre commande.")


# ==========================================
# 4. LA CAISSE & LE TICKET DE CAISSE
# ==========================================
print("\n" + "="*60)
print(f"      VOTRE TICKET DE CAISSE - {nom.upper()}      ")
print("="*60)

total_general = 0
frais_livraison = 1000  # Frais de base (si achat < 5000 F CFA)
reduction = 0

if not Commande:
    print("Vous n'avez rien commandé. À bientôt !")
else:
    # 1. Calcul et affichage du détail des plats
    for produit in Commande:
        prix_total_plat = produit["quantite"] * produit["prix_unitaire"]
        total_general += prix_total_plat
        print(f"- {produit['nom']}")
        print(f"  Quantité : {produit['quantite']} x {produit['prix_unitaire']} F CFA | Total : {prix_total_plat} F CFA")
        print("-" * 40)

    # 2. Application des règles selon le montant du panier
    if total_general >= 15000:
        frais_livraison = 0              # Livraison gratuite
        reduction = total_general * 0.01  # Réduction de 1%
        print("🎉 Super Offre (Achat >= 15 000 F CFA) :")
        print("  -> Livraison GRATUITE !")
        print(f"  -> Remise de 1% accordée : -{reduction:.0f} F CFA")
        print("-" * 60)
        
    elif total_general >= 5000:
        frais_livraison = 0              # Livraison gratuite
        reduction = 0                     
        print("🎉 Offre Spéciale (Achat >= 5000 F CFA) :")
        print("  -> Livraison GRATUITE !")
        print("-" * 60)
        
    else:
        print(f"Frais de livraison standard : {frais_livraison} F CFA")
        print("-" * 60)

    # 3. Calcul du montant final net à payer
    montant_final = total_general - reduction + frais_livraison

    # 4. Affichage du résumé financier
    print(f"Sous-total plats   : {total_general} F CFA")
    print(f"Frais de livraison : {frais_livraison} F CFA")
    print(f"Réduction          : -{reduction:.0f} F CFA")
    print(f"\n NET À PAYER       : {montant_final:.0f} F CFA")
    print("="*60)

    # ==========================================
    # 5. SAUVEGARDE DE LA COMMANDE CLIENT (CSV)
    # ==========================================
    nom_fichier_sauv = "historique_ventes.csv"
    try:
        # Vérifier si le fichier existe déjà pour savoir s'il faut écrire l'entête
        import os
        fichier_existe = os.path.exists(nom_fichier_sauv)

        with open(nom_fichier_sauv, mode="a", newline="", encoding="utf-8") as fichier:
            createur_csv = csv.writer(fichier, delimiter=";")
            date_actuelle = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            
            # Si le fichier est tout neuf, on écrit l'entête UNE SEULE FOIS
            if not fichier_existe:
                createur_csv.writerow(["Date et Heure", "Nom Client", "Nom du Plat", "Quantite", "Prix Unitaire (FCFA)", "Total Plat (FCFA)"])
            
            # Enregistrement ligne par ligne
            for produit in Commande:
                total_plat = produit["quantite"] * produit["prix_unitaire"]
                createur_csv.writerow([
                    date_actuelle,
                    nom,
                    produit["nom"], 
                    produit["quantite"], 
                    produit["prix_unitaire"], 
                    total_plat
                ])
    except IOError:
        print("\n[Erreur Système] Impossible d'archiver la commande sur le disque.")

