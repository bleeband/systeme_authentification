import BD
import info_user

BD.BD_sys_auth

def login():

    #Recuperer infos user
    infos = info_user.demander_infos()
    

    if info_user.pseudonyme or info_user.email not in BD.BD_sysauth:
        print("Il n'y a aucun compte qui correspond à ces informations.")
        return False
    #Tester si le mot de passe est bon
    if infos["mot_de_passe"] == BD.BD_sysauth[info_user.pseudonyme or info_user.email]["mot_de_passe"]:
        print("Connexion réussie !")
        return True 

   