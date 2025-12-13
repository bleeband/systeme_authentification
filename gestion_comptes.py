#-Faire une fonction creer_compte OK!
# -Faire une fonction reset_mdp OK!
# -Faire une fonction delete_compte 
# -Utiliser la fonction infos_user.demander_infos()

import BD

#création d'un compte
#présentement aucune vérification avec la base de données
def creer_compte():
    pseudonyme = input("Entrez un nom d'utilisateur : ")
    while True:                                                                              #compléter une sécurité pour avoir un @ dans le courriel  MAD
        email = input("Entrez une adresse courriel : ")
        if "@" in email:
            break
        print("Adresse courriel invalide, doit contenir un @ ")
    while True:                                                                              #compléter la sécurité à 8 caracteres  MAD
        mot_de_passe = input("Entrez un mot de passe contenant au moins 8 caractères : ")
        if len(mot_de_passe) >= 8:
            break
        print("Mot de passe doit contenir un min de 8 caractères")
    prenom = input("Entrez votre prénom : ")
    nom = input("Entrez votre nom : ")
    return pseudonyme, email, mot_de_passe, prenom, nom

def ajout_compte_BD():
    pseudonyme, email, mot_de_passe, prenom, nom = creer_compte()   
    BD.BD_sys_auth.append({f"nom": nom, "prenom": prenom, "email": email, "pseudonyme": pseudonyme, "mot_de_passe": mot_de_passe})  #retrait des {} MAD
        

# #----test creer_compte et ajouteur_compte_BD:
# ajout_compte_BD()
# print(BD.BD_sys_auth)


# #-----test des valeurs après creer_compte 
# print(pseudonyme)
# print(email)
# print(mot_de_passe)

def reset_mdp():
    compte_a_reinitialiser = input("Entrez le nom d'utilisateur du compte à réinitialiser: ")
    
    #si un compte existe avec le nom spécifié, on remplace son mdp par le nouveau mdp spécifié
    for compte in BD.BD_sys_auth:
        if compte_a_reinitialiser == compte["pseudonyme"]:
            nouveau_mot_de_passe = input("Entrez un nouveau mot de passe: ")        #deplacer le input apres avoir verifier si le compte existe  MAD
            if len(nouveau_mot_de_passe) < 8:                                       #verification du nombre de caractere minimun de 8  MAD
                print("Mot de passe trop court (min 8 caractères).")
                return
            compte["mot_de_passe"] = nouveau_mot_de_passe
            return nouveau_mot_de_passe
        #break          ##commenter le break pour regler conflit MAD

    print("\nCompte introuvable.\n")

# #-----test de la fonction reset_mdp
# reset_mdp()
# print(BD.BD_sys_auth)


def delete_compte():
    #chercher un compte avec son nom d'user, si le compte existe, effacer son index.
    compte_a_supprimer = input("Entrez le nom d'utilisateur du compte à supprimer: ")
    for i in range(len(BD.BD_sys_auth)):
        if BD.BD_sys_auth[i]["pseudonyme"] == compte_a_supprimer:
            del BD.BD_sys_auth[i]
            print(f"Le compte \"{compte_a_supprimer}\" a été effacé!")
            break
    else:
        print("Ce compte n'existe pas, aucun compte effacé.")

#-----test de la fonction delete_compte
# delete_compte()
# print(BD.BD_sys_auth)

        
