# main.py

from app.components.zorglangue import inverser_phrase

def afficher_menu():
    """
    Affiche le menu principal pour interagir avec l'application.
    """
    print("\n=== Bienvenue dans l'application Zorglangue ===")
    print("1. Inverser une phrase en Zorglangue")
    print("2. Quitter")
    print("===============================================")

def main():
    """
    Fonction principale pour exécuter le programme Zorglangue.
    """
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1 ou 2) : ")

        if choix == "1":
            phrase = input("Entrez une phrase à inverser : ")
            phrase_inversee = inverser_phrase(phrase)
            print(f"Phrase inversée : {phrase_inversee}")
        elif choix == "2":
            print("Merci d'avoir utilisé l'application Zorglangue !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
