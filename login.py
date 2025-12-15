import bd
import info_user



def login() -> bool:
  
    """
    Tente d'authentifier un utilisateur.

    Comportement :
    - Demande les informations de connexion via `info_user.DemandeInfo()`.
    - Recherche l'utilisateur dans `bd.bd_sys_auth`.
    - Vérifie le mot de passe fourni.
    - Décrémente `nb_tentatives` en cas d'échec et bloque après épuisement.

    Affichage :
    Cette fonction utilise `print()` pour indiquer son état (console).

    Returns:
        bool: `True` si la connexion réussit, `False` sinon.
    """

    nb_tentatives = 5

    #Instaurer une limite de tentatives
    while True:
        if nb_tentatives == 0:
            print("Nombre de tentatives dépassé. Veuillez réessayer plus tard.")
            return False
        
        #Recuperer infos user
        pseudonyme, email, mot_de_passe = info_user.DemandeInfo()               #-DemandeInfo() retourne des variables au lieu d'un dictionnaire, changé en conséquences dans login() MG

        #Chercher si l'utilisateur existe    
        for user in bd.bd_sys_auth:
            if pseudonyme == user['pseudonyme'] and email == user['email']:     #-Changé infos["user"] et ["email"] par les variables. MG
                user_infos = user
                break
        else: 
            print("Aucun utilisateur trouvé avec ces informations.")
            return False
                
        #Tester si le mot de passe est bon
        if mot_de_passe == user_infos["mot_de_passe"]:                          #-Changé infos["mpt_de_passe"] par la variable. MG
            print("Connexion réussie !")
            return True 
        else:
            nb_tentatives -= 1
            print(f"Mot de passe incorrect. {nb_tentatives} essais restants.")
            continue

