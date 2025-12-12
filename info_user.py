
sys_auth = []


# pseudonyme = input("Pseudonyme: ")
# email = input("Adresse couriel: ")
# mot_de_passe = input("Mot de passe: ")

def DemandeInfo(pseudonyme, email, mot_de_passe):
    sys_auth.append({"pseudonyme": pseudonyme,"email": email,"mot_de_passe": mot_de_passe})


DemandeInfo(input("Pseudonyme: "), input("Email: "), input("Mot de passe: "))
print(sys_auth)