import BD
# import info_user

nb_tentatives = 5

def login():

    #Instaurer une limite de tentatives
    if nb_tentatives == 0:
        print("Nombre de tentatives dépassé. Veuillez réessayer plus tard.")
        return False
    
    #Recuperer infos user
    # infos = info_user.demander_infos()
    infos = {"pseudonyme": "bb@bb.com", "email": "bb@bb.com", "mot_de_passe": "maoma"}
    print(infos)

    #Chercher si l'utilisateur existe    
    for user in BD.BD_sys_auth:
        if infos['pseudonyme'] == user['pseudonyme'] or infos['email'] == user['email']:
            user_infos = user
            print("Utilisateur trouvé :", user_infos)
            break
    else: 
        print("Aucun utilisateur trouvé avec ces informations.")
        return False
            
    #Tester si le mot de passe est bon
    if infos["mot_de_passe"] == user_infos['pwd']:
        print("Connexion réussie !")
        return True 
    else:
        print("Mot de passe incorrect.")
        nb_tentatives -= 1
        return False

print(login())