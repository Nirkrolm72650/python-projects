'''
Le jeu du Plus ou Moins

1 - Générer aléatoirement un nombre entre 0 et 100 inclus
2 - Demander à l'utilisateur d'entrer un nombre
3 - Vérifier si le nombre est bien un nombre et non une lettre ou un caractère spécial => demander de recommencer la saisie
3 - Vérifier si le nombre est compris entre l'interval
4 - Vérifier l'égalité entre le nombre généré et le nombre entré ( En cas de réussite = GAGNÉ )
5 - Sinon recommencer jusqu'à trouver le bon nombre

'''

import random

nombreAleatoire = random.randint(0,100)

nombreSaisie = int(input("Entrez un nombre : "))

while nombreSaisie != nombreAleatoire:
    if nombreSaisie > nombreAleatoire:
        print("C'est moins")
    elif nombreSaisie < nombreAleatoire:
        print("C'est plus")

    nombreSaisie = int(input("Entrez un nombre : "))

print(f"Vous avez trouvé le nombre. Le nombre était bien {nombreAleatoire}")


