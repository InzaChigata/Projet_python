from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Structure des données attendues pour un utilisateur
class ModeleUtilisateur(BaseModel):
    pseudo: str
    email: str

# 2. Une fausse base de données (une simple liste pour apprendre)
base_de_donnees = []

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API !"}

# 3. Route pour VOIR tous les utilisateurs
@app.get("/utilisateurs")
def recuperer_les_utilisateurs():
    return {"utilisateurs_enregistres": base_de_donnees}

# 4. Route pour CREER un nouvel utilisateur
@app.post("/utilisateurs")
def creer_utilisateur(compte: ModeleUtilisateur):
    # On ajoute les données envoyées dans notre fausse base de données
    base_de_donnees.append({"pseudo": compte.pseudo, "email": compte.email})
    return {"status": "Succès", "message": f"Le compte de {compte.pseudo} a été créé !"}

