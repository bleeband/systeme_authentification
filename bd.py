# BASE DE DONNÉES (format DICT)      *** SysAuth - STOCKAGE ***
# nom, prenom, email, username, mot_de_passe

bd_sys_auth = [
    {"nom": "NOM", "prenom": "PRENOM", "email": "  EMAIL  ", "pseudonyme": "PSEUDONYME", "mot_de_passe": "MOT DE PASSE"},
    {"nom": "Default", "prenom": "User", "email": "default@mail.com", "pseudonyme": "Pseudo", "mot_de_passe": "pseudo1234"},
    {"nom": "Dufour", "prenom": "Marc", "email": "bleeband@gmail.com", "pseudonyme": "bleeband@gmail.com", "mot_de_passe": "12345678"},
    {"nom": "M.", "prenom": "Pascale", "email": "Mercierp@outlook.com", "pseudonyme": "Mercierp@outlook.com", "mot_de_passe": "12345678"},
    {"nom": "G.", "prenom": "Mathieu", "email": "math.gosselin@gmail.com", "pseudonyme": "Grindy", "mot_de_passe": "12345678"},
    {"nom": "L.", "prenom": "Clément", "email": "bb@bb.com", "pseudonyme": "bb@bb.com", "mot_de_passe": "12345678"},
    {"nom": "test", "prenom": "test", "email": "test", "pseudonyme": "test", "mot_de_passe": "12345678"},
]


def afficher_bd():

    for user in list(bd_sys_auth):
        champs_cache = ["mot_de_passe"]
        safe_user = {}
        for key, value in user.items():
            if key in champs_cache:
                safe_user[key] = "****"  # cacher le vrai mot de passe
            else:
                safe_user[key] = value
        print("•", user["nom"], user["prenom"],", ", user["email"], "--> ", user["pseudonyme"],"PWD =", safe_user["mot_de_passe"])


def sauvegarder_bd():
    with open("bd.py", "r", encoding="utf-8") as f:
        lignes = f.readlines()

    nouveau_bloc = []
    nouveau_bloc.append("bd_sys_auth = [\n")

    for compte in bd_sys_auth:
        ligne = (
            "    {"
            f"\"nom\": \"{compte['nom']}\", "
            f"\"prenom\": \"{compte['prenom']}\", "
            f"\"email\": \"{compte['email']}\", "
            f"\"pseudonyme\": \"{compte['pseudonyme']}\", "
            f"\"mot_de_passe\": \"{compte['mot_de_passe']}\""
            "},\n"
        )
        nouveau_bloc.append(ligne)

    nouveau_bloc.append("]\n")

    nouveau_fichier = []
    dans_bloc = False

    for ligne in lignes:
        if ligne.strip().startswith("bd_sys_auth = ["):
            nouveau_fichier.extend(nouveau_bloc)
            dans_bloc = True
            continue

        if dans_bloc:
            if ligne.strip() == "]":
                dans_bloc = False
            continue

        nouveau_fichier.append(ligne)

    with open("bd.py", "w", encoding="utf-8") as f:
        f.writelines(nouveau_fichier)

    print("bd_sys_auth sauvegardée sans toucher au reste du fichier.")