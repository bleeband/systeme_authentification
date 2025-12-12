#-Faire une fonction creer_compte OK!
# -Faire une fonction reset_mdp
# -Faire une fonction delete_compte
# -Utiliser la fonction infos_user.demander_infos()

import BD

#création d'un compte
#présentement aucune vérification avec la base de données
def creer_compte():

    pseudonyme = input("Entrez un nom d'utilisateur: ")
    email = input("Entrez une adresse courriel: ")
    mot_de_passe = input("Entrez un mot de passe contenant au moins 8 caractères: ")
    prenom = input("Entrez votre prénom: ")
    nom = input("Entrez votre nom: ")
    return pseudonyme, email, mot_de_passe, prenom, nom

def ajout_compte_BD():
        
    BD.BD_sys_auth.append({f"nom": {nom}, "prenom": {prenom}, "email": {email}, "username": {pseudonyme}, "pwd": {mot_de_passe}})
        

# #test creer_compte et ajouteur_compte_BD:
# pseudonyme, email, mot_de_passe, prenom, nom = creer_compte()
# ajout_compte_BD()
# print(BD.BD_sys_auth)


# #test des valeurs après creer_compte 
# print(pseudonyme)
# print(email)
# print(mot_de_passe)


def reset_mdp():
    pass


def delete_compte():
    pass


def reset_mdp():
    pass