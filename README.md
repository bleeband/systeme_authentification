Exercice Final : Projet Libre
Consignes

1.	Choix du projet : Utilitaire d’authentification
2.	Planification : Découpage en 4 parties égales
3.	Implémentation : 1h de code synchronisé
4.	Intégration : 30 min de merge et tests
5.	Rétrospective : 15 min de discussion

Critères de Succès
•	Tous les membres ont commit au moins 2 fois
•	Pas de code cassé après merge
•	README.md complet
•	Projet fonctionnel

Template README.md Collaboratif

# [Nom du Projet]

## Equipe

- [Marc]  - Git Manager
- [Membre 2] - Rôle/Fonctionnalité
- [Membre 3] - Rôle/Fonctionnalité
- [Membre 4] - Rôle/Fonctionnalité

## Installation
1. git clone [url]
2. cd [projet]
3. python main.py

## Fonctionnalités
Système d'authentification
 
1. Définir les variables : nom d'utilisateur, mot de passe et protection 
2. Vérifier que les données de l'utilisateur matchent avec la base de données
3. Créer un nouveau compte
4. Réinitialiser le mot de passe
 
## Leçons Apprises

- Comment résoudre les conflits Git
- L'importance de la communication
- etc.

Bonus : Script d'Initialisation pour l'Equipe

# setup_team.py - À exécuter par le chef de projet

def initialiser_projet():

    print("=== INITIALISATION DU PROJET ===")

    print("1. Créer dépôt GitHub")

    print("2. Cloner sur toutes les machines")

    print("3. Créer branches :")

    print("   - git checkout -b feature-membre1")

    print("   - git checkout -b feature-membre2")

    print("   - git checkout -b feature-membre3")

    print("   - git checkout -b feature-membre4")

    print("4. Commencer à coder !")

if __name__ == "__main__":
    initialiser_projet()
