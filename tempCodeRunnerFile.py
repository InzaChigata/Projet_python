# Liste de commande vide au départ
Commande = []
# GRANDE BOUCLE : Permet de commander plusieurs fois
while True:
    while True:
        try:
            commande_intermediaire = int(input("Entrez le numéro du plat (ou 0 pour terminer la commande) : "))
            break
        except ValueError:
            print("Reprends la saisie")
            
    # CONDITION DE SORTIE : Si le client tape 0, on arrête tout
    if commande_intermediaire == 0:
        print("Fin des achats !")
        break

    # --- Ton code de vérification du plat ---
    plat_trouve = None
    for plat in Plats:
        if plat["id"] == commande_intermediaire:
            plat_trouve = plat
            break
            
    # Si le plat n'existe pas, on passe au produit suivant sans bloquer
    if plat_trouve is None:
        print("Ce plat n'existe pas, choisis-en un autre.")
        continue # Repart au début de la grande boucle

    # --- Ton code pour demander la quantité ---
    if plat_trouve:
        while True:
            try:
                quantite = int(input(f"Entrez la quantité de {plat_trouve['nom']} : "))
                break
            except ValueError:
                print("Reprends la saisie")
                
        # --- Ton code pour ajouter à la liste ---
        Commande.append({
            "id": plat_trouve["id"],
            "nom": plat_trouve["nom"],
            "prix_unitaire": plat_trouve["prix"],
            "quantite": quantite
        })
        print(f"{quantite} x {plat_trouve['nom']} ont été ajoutés à votre commande.\n")

# À la fin de la boucle, la liste 'Commande' contient tous les produits ajoutés !
print("Voici le contenu final de votre commande :", Commande)
