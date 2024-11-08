import json

class Livre:
    def __init__(self, titre, auteur, annee, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible

    def __str__(self):
        return f"'{self.titre}' par {self.auteur} ({self.annee}) - {'Disponible' if self.disponible else 'Non disponible'}"


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        print(f"Livres disponibles à la bibliothèque '{self.nom}':")
        for livre in self.livres:
            print(livre)

    def emprunter_livre(self, utilisateur, titre):
        livre = self.trouver_livre(titre)
        if livre and livre.disponible:
            livre.disponible = False
            utilisateur.emprunter_livre(livre)
            print(f"{utilisateur.nom} a emprunté '{livre.titre}'.")
        elif livre:
            print(f"Le livre '{livre.titre}' n'est pas disponible pour le moment.")
        else:
            print(f"Le livre '{titre}' n'existe pas dans notre bibliothèque.")

    def retourner_livre(self, utilisateur, titre):
        livre = utilisateur.retourner_livre(titre)
        if livre:
            livre.disponible = True
            print(f"{utilisateur.nom} a retourné '{livre.titre}'.")
        else:
            print(f"{utilisateur.nom} n'a pas emprunté
