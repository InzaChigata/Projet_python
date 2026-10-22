""" class Plat:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher(self):
        print(f"{self.nom} = {self.prix}")

garba = Plat("Garba", 1000)
garba.afficher() """
""" print(garba.nom)
print(garba.prix)
Alloco=Plat("Alloco",500)
print(f"{Alloco.nom}--------{Alloco.prix} FCFA") """

""" class Plats:
    def __init__(self, nom, prix):
        self.nom=nom
        self.prix=prix
    def prix_pour(self,quantite):
        return self.prix*quantite

Garba = Plats("Garba", 1000)
resultat=Garba.prix_pour(3)
print(resultat) """


class Plat:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def prix_pour(self, quantite):
        return self.prix * quantite


class Commande:
    def __init__(self, client):
        self.client = client
        self.lignes = []          # liste vide au départ

    def ajouter(self, plat, quantite):
        self.lignes.append((plat, quantite))

    def total(self):
        s=0
        for i in self.lignes:
            return s+i


garba = Plat("Garba", 1000)
alloco = Plat("Alloco", 500)

commande = Commande("Awa")
commande.ajouter(garba, 3)
commande.ajouter(alloco, 2)