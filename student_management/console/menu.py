from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
import sys

console = Console()

def display_menu():
    console.clear()
    
    # Titre du menu
    console.print(Panel("[bold cyan]Système de Gestion des Étudiants[/bold cyan]", expand=False))
    
    # Création de la table pour afficher les options du menu
    table = Table(title="Menu Principal", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="bold green")
    table.add_column("Description", style="yellow")

    # Ajout des options du menu
    table.add_row("1", "Ajouter un étudiant")
    table.add_row("2", "Rechercher un étudiant")
    table.add_row("3", "Supprimer un étudiant")
    table.add_row("4", "Afficher la liste des étudiants")
    table.add_row("5", "Quitter")

    try:
        # Affichage du tableau
        console.print(table)
        
        # Demande du choix à l'utilisateur
        choice = Prompt.ask("\n[bold cyan]Choisissez une option[/bold cyan]", 
                          choices=["1", "2", "3", "4", "5"])
        return choice
        
    except KeyboardInterrupt:
        console.print("\n[bold red]Programme interrompu. Voulez-vous quitter ? (o/n)[/bold red]")
        quit_response = input()
        if quit_response.lower() == "o":
            console.print("\n[bold cyan]Au revoir ![/bold cyan]")
            print("Appuez sur une touche pour continuer...")
            input()
            console.clear()
            sys.exit()
        else:
            return display_menu()
    return choice