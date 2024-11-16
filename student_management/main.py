from console.menu import display_menu  
from services.student_service import add_student, delete_student, search_student

import uuid
import pprint

def main():
    
    
    while True:
        # Afficher le menu et récupérer le choix de l'utilisateur
        choice = display_menu()
        
        # Gestion des choix
        if choice == "1":
            id = uuid.uuid4().int
            lastname = input("Entrez un nom de famille : ")
            firstname = input("Entrez un prénom : ")
            email = input("Entrez une adresse email : ")
            add_student(id, firstname, lastname, email)  # Appel de la fonction pour ajouter un étudiant
            input
        elif choice == "2":
            name_search = input("Entrez un nom pour rechercher : ")
            results = search_student("data/students.json",name_search) # Appel de la fonction pour rechercher un étudiant
            input()
        elif choice == "3":
            delete_by_id = int(input("Entrez l'id de l'étudiant : "))
            valeur = delete_student("data/students.json", delete_by_id)  # Appel de la fonction pour supprimer un étudiant
            type(valeur)
            input()
        elif choice == "4":
            pass  # Appel de la fonction pour afficher tous les étudiants
        elif choice == "5":
            print("Merci d'avoir utilisé le système de gestion des étudiants. Au revoir!")
            break  # Sortir de la boucle et terminer le programme
        else:
            print("Option invalide, veuillez réessayer.")

# Lancer le programme principal
if __name__ == "__main__":
    main()