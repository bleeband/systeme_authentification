
def demande_info():

    pseudonyme=  input("Pseudonyme: ")

    #demande un email, si @ n'est pas présent, on redemande le email.
    while True:
        email = input("Email: ")
        if "@" in email:                                    #ajout de la verif @ demande info MG
            break
        print("Adresse courriel invalide, doit contenir un @.")

    #demande un mot de passe d'au moins 8 caractères, sinon on redemande.
    while True:
        mot_de_passe = input("Mot de passe: ")
        if len(mot_de_passe) >= 8:                          #ajout de la verif 8 caracteres dans demande info MG
            break
        print("Mot de passe doit contenir un min de 8 caractères")

    return pseudonyme, email, mot_de_passe

def demande_prenom_nom():
    
    prenom = input("Prénom: ")
    nom = input("Nom: ")
    return prenom, nom

# #-----test de demande_info
# demande_info()