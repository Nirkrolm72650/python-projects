from models.student import Student
from services.utils import add_new_line, read_file

import uuid
import json
import pprint


def add_student(id, firstname, lastname, email):
    
    """
    Ajoute un étudiant dans un fichier JSON.

    Paramètres:
    id (int) : id de l'étudiant (généré via la fonction uuid)
    firstname (str) : prénom de l'étudiant
    lastname (str) : nom de famille de l'étudiant
    email (str) : adresse mail de l'étudiant

    """
    new_student = Student(id, lastname, firstname, email)
    

    student = read_file("data/students.json")
    
    student.append(new_student.to_dict())
    
    
    add_new_line("data/students.json", new_student)
    
    if student:
        print(f"L'étudiant {new_student.firstname} a bien été ajouté dans la base")
    else:
        print("Un problème est survenu...")
    

    
def delete_student(file_path, student_id):
    
    """
    Supprime un étudiant dans un fichier JSON.

    Paramètres:
    file_path (str) : chemin vers le fichier JSON
    student_id (int) : id de l'étudiant
    
    Renvoie:
    dict : un dictionnaire contenant les informations de l'étudiant

    """
    try:
         data = read_file("data/students.json")
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas")
        return None
    except json.JSONDecodeError:
        print("fErreur: le fichier {file_path} contient un JSON invalide")
        
    # Chercher et supprimer l'élément avec l'id correspondant
    remove_student = None
    for student in data:
        if student.get('id') == student_id:
            remove_student = student
            break
    
    if remove_student:
        data.remove(remove_student) # Supprime l'étudiant trouvé
        print(f"Étudiant avec l'ID {student_id} supprimé")
    else:
        print(f"Aucun étudiant trouvé avec l'ID {student_id}")
        return None
    
    # On réécrit les données mises à jour dans le fichier JSON
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        
    return data

def search_student(file_path, name_student):
    
    """
    Recherche un étudiant dans un fichier JSON.

    Paramètres:
    file_path (str) : chemin vers le fichier JSON
    student_name (str) : nom de famille de l'étudiant

    Renvoie:
    dict : dictionnaire contenant les informations de l'étudiant recherchée
    """
    try:
         data = read_file("data/students.json")
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas")
        return []
    except json.JSONDecodeError:
        print("fErreur: le fichier {file_path} contient un JSON invalide")
        return []
    
    # Liste permettant de stocker les résultats de la recherche
    result_data = []
    
    for student_name in data:
        if name_student.lower() in student_name.get("lastname", "").lower():
            result_data.append(student_name)
            
    # Affiche les résultats après la vérification
    if result_data:
        pprint.pprint(f"Étudiants trouvées avec le nom '{name_student}':", result_data)
    else:
        print(f"Aucun étudiant trouvé avec le nom '{name_student}'")
        
    return result_data
        
    
    
    