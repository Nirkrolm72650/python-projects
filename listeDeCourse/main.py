choix = 0
liste_de_course = []
def menu():
    print("\n")
    print("1: Ajouter un élément")
    print("2: Afficher la liste de course")
    print("3: Supprimer un élément")
    print("4: Vider la liste de course")
    print("5: Quitter")
    print("\n")
    print("----------------------------------------")
def ajouterElement(liste):
    element = input("Entrez l'élement à ajouter : ")
    liste.append(element)
    print(f"L'élément {element} a bien été ajouter à la liste de course")

def afficherListe(liste):
    if not liste:
        print("Il n'y a pas d'élément dans la liste")

    for i in range(len(liste)):
        print(f"{i}. {liste[i]}")

def supprimerElement(liste):
    afficherListe(liste)

    element = input("Entrez l'élément à supprimer : ")
    liste.remove(element)
    print(f"L'élément {element} a bien été supprimé")

def viderListe(liste):
    for _ in liste:
        liste.clear()
    print("La liste a bien été vidée")

while choix != 5:
    menu()
    choix = int(input("Entrez votre choix : "))

    if choix == 1:
        ajouterElement(liste_de_course)
    elif choix == 2:
        afficherListe(liste_de_course)
    elif choix == 3:
        supprimerElement(liste_de_course)
    elif choix == 4:
        viderListe(liste_de_course)
    elif choix == 5:
        print("A bientôt !")
        break
