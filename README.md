 # 📋 Système d'authentification

Système d'authentification développé pour l'exercice final du TP Git de Concepts de Programmation 1.

## 🚀 Installation

```bash
git clone https://github.com/bleeband/systeme_authentification.git
cd systeme_authentification
```

## 📖 Utilisation

Lancer à partir de main.py

Pour votre première connexion, utilisez le compte suivant:

Username: Pseudo
Email: default@mail.com
Mot de passe: pseudo1234

(Cette information ne serait pas présente si on déployait pour de vrai là!)

## 📁 Structure du projet

```
system_authentification/
├── __pycache__
├── README.md
├── .gitignore
├── bd.py                   # Base de données
├── gestion_comptes.py      # Gestion des opérations au comptes (modifications, création, déletion)
├── info_user.py            # Gestion des demandes d'informations de l'usager
├── login.py                # Gestion du login
└── main.py                 # Fichier de fonctionnement principal
```

## ✨ Fonctionnalités

- ✅ Login dans le système et gestion du succès / échec.
- ✅ Interface de menu fonctionnelle.
- ✅ Création de comptes et ajout à la base de données.
- ✅ Demande d'informations à l'usager lors de la création du compte et règles de validation pour le email et le mot de passe.
- ✅ Suppression de comptes et retrait de la base de données.
- ✅ Affichage de la liste des comptes avec leur mot de passe caché.
- ✅ Changement de mot de passe.
- ✅ Sauvegarde de la base de données à la sortie.

## 👨‍💻 Auteurs

Mathieu Gosselin
Clément Laflamme
Pascale Mercier
Marc-André Dufour

## 📄 Licence

Ce projet est sous licence MIT.