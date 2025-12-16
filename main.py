import bd
import gestion_comptes
import login

# SYSTEME D'AUTHENTIFICATION

# LOGIN

print("\n*** Veuillez vous identifier ***")
if not login.login():
    exit()                                                   # TESTER ??? NE CALCUL PAS LES 5 ESSAIS  MAD

# GESTION

while True:
    print("\n1.AFFICHER  2.CREER  3.EFFACER  4.RESET PWD")
    choix = input("Veuiller faire un choix : ")

    if choix == "1":
        print("AFFICHER LA LISTE DES UTILISATEURS\n")
        bd.afficher_bd()                                         # TESTER OK  MAD

    elif choix == "2":
        print("CREER UN NOUVEAU COMPTE\n")
        gestion_comptes.ajout_compte_bd()                        # TESTER OK  MAD  (mais peux creer deux identiques)

    elif choix == "3":
        print("EFFACER UN COMPTE\n")
        gestion_comptes.delete_compte()                         # TESTER OK  MAD 

    elif choix == "4":
        print("REINITIALISER VOTRE MOT DE PASSE\n")
        gestion_comptes.reset_mdp()                             # TESTER OK MODIFICATION  MAD

    elif choix.lower() == "q":
        bd.sauvegarder_bd()
        break
    
    else:
        print("Choix invalide, recommencer svp")
        choix

