import json
import csv
import time
from rich.progress import Progress
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

    # Calcul du nombre de ligne pour la barre de progression
    with open(csvFilePath, encoding="utf-8") as csvf:
        total_lines = sum(1 for _ in csvf) - 1 # -1 permet d'exclure l'en-tête

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        with Progress() as progress:
            task = progress.add_task("[cyan]Conversion en JSON...", total=total_lines)

            for row in csvReader:
                key = row['id']
                data[key] = row
                progress.advance(task)
                time.sleep(0.1)

        add_new_line(jsonFilePath, data)

        return data


