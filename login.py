import BD
import info_user

nb_tentatives = 5

def login() -> bool:
  
    """
    Tente d'authentifier un utilisateur.

    Comportement :
    - Demande les informations de connexion via `info_user.DemandeInfo()`.
    - Recherche l'utilisateur dans `BD.BD_sys_auth`.
    - Vérifie le mot de passe fourni.
    - Décrémente `nb_tentatives` en cas d'échec et bloque après épuisement.

    Affichage :
    Cette fonction utilise `print()` pour indiquer son état (console).

    Returns:
        bool: `True` si la connexion réussit, `False` sinon.
    """

    global nb_tentatives

    #Instaurer une limite de tentatives
    if nb_tentatives == 0:
        print("Nombre de tentatives dépassé. Veuillez réessayer plus tard.")
        return False
    
    #Recuperer infos user
    infos = info_user.DemandeInfo()

    #Chercher si l'utilisateur existe    
    for user in BD.BD_sys_auth:
        if infos['pseudonyme'] == user['pseudonyme'] and infos['email'] == user['email']:
            user_infos = user
            break
    else: 
        print("Aucun utilisateur trouvé avec ces informations.")
        return False
            
    #Tester si le mot de passe est bon
    if infos["mot_de_passe"] == user_infos["mot_de_passe"]:
        print("Connexion réussie !")
        return True 
    else:
        print("Mot de passe incorrect.")
        nb_tentatives -= 1
        return False

