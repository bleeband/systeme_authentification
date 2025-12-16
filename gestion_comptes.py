import bd
import info_user

#création d'un compte
def creer_compte():
    pseudonyme, email, mot_de_passe = info_user.demande_info()                       #les vérifications d'entrées sont déménagées dans demande_info() MG
    prenom = "Telesphore"                                                           #en attendant qu'on demande l'info dans info_user MG
    nom = "Tremblay"                                                                #en attendant qu'on demande l'info dans info_user MG
    return pseudonyme, email, mot_de_passe, prenom, nom

def ajout_compte_bd():
    pseudonyme, email, mot_de_passe, prenom, nom = creer_compte()   
    bd.bd_sys_auth.append({f"nom": nom, "prenom": prenom, "email": email, "pseudonyme": pseudonyme, "mot_de_passe": mot_de_passe})  #retrait des {} MAD


# #----test creer_compte et ajouteur_compte_bd:
# ajout_compte_bd()
# # print(bd.bd_sys_auth)


# #-----test des valeurs après creer_compte, affiche le dernier élément ajouté à la liste de la bd.
# print(bd.bd_sys_auth.pop())

def reset_mdp():
    compte_a_reinitialiser = input("Entrez le nom d'utilisateur du compte à réinitialiser: ")
    
    #si un compte existe avec le nom spécifié, on remplace son mdp par le nouveau mdp spécifié
    for compte in bd.bd_sys_auth:
        if compte_a_reinitialiser == compte["pseudonyme"]:
            while True:
                nouveau_mot_de_passe = input("Entrez un nouveau mot de passe: ")            #deplacer le input apres avoir verifier si le compte existe  MAD
                if len(nouveau_mot_de_passe) >= 8:                                          #verification du nombre de caractere minimun de 8  MAD
                    compte["mot_de_passe"] = nouveau_mot_de_passe
                    print("Mot de passe réinitilisé!")
                    return
                else:
                    print("Mot de passe trop court (min 8 caractères).")

    print("\nCompte introuvable.\n")

# #-----test de la fonction reset_mdp
# reset_mdp()
# print(bd.bd_sys_auth)


def delete_compte():
    #chercher un compte avec son nom d'user, si le compte existe, effacer son index.
    compte_a_supprimer = input("Entrez le nom d'utilisateur du compte à supprimer: ")
    for i in range(len(bd.bd_sys_auth)):
        if bd.bd_sys_auth[i]["pseudonyme"] == compte_a_supprimer:
            del bd.bd_sys_auth[i]
            print(f"Le compte \"{compte_a_supprimer}\" a été effacé!")
            break
    else:
        print("Ce compte n'existe pas, aucun compte effacé.")

# #-----test de la fonction delete_compte
# delete_compte()
# print(bd.bd_sys_auth)