import json
import csv
from models.student import Student


def read_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def add_new_line(file_path, new_data):
    try:
        # Lire les données existantes dans le fichier JSON
        with open(file_path, "r") as file:
            data = json.load(file)
        print("Données lues depuis le fichier :", data)
    except FileNotFoundError:
        # Si le fichier n'existe pas, on crée une liste vide
        print(f"Le fichier {file_path} n'existe pas, création d'un fichier vide.")
        data = []
    except json.JSONDecodeError:
        # Si le fichier existe mais est mal formé
        print(f"Erreur: le fichier {file_path} contient un JSON invalide.")
        return None
    
    
    # si new_data est un objet student, on le convertit en dictionnaire
    if isinstance(new_data, Student):
        new_data = new_data.to_dict()
    # Ajouter la nouvelle ligne aux données existantes
    data.append(new_data)
    print("Données après ajout de la nouvelle ligne :", data)
    
    # Réécrire le fichier avec les nouvelles données
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    
    # Retourner les données mises à jour
    return data

def convert_csv_to_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            key = row['id']
            data[key] = row

        add_new_line(jsonFilePath, data)

        return data


