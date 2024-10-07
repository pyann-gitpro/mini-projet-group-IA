import logging
import re

# Configuration de la journalisation
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def inverser_mot(mot):
    """
    Inverse les lettres d'un mot tout en conservant les majuscules et la ponctuation.
    
    Args:
        mot (str): Le mot à inverser.

    Returns:
        str: Le mot inversé avec majuscules et ponctuation préservées.
    """
    # On sépare les lettres et la ponctuation en utilisant une regex
    lettres = re.findall(r'[A-Za-z]', mot)
    inverse_lettres = lettres[::-1]  # Inverser les lettres

    # Reconstruire le mot en respectant la ponctuation et la majuscule
    nouveau_mot = []
    lettre_index = 0
    for char in mot:
        if char.isalpha():
            nouvelle_lettre = inverse_lettres[lettre_index]
            # Garde la majuscule à la bonne place
            if char.isupper():
                nouveau_mot.append(nouvelle_lettre.upper())
            else:
                nouveau_mot.append(nouvelle_lettre.lower())
            lettre_index += 1
        else:
            # Si c'est un caractère de ponctuation, on le garde tel quel
            nouveau_mot.append(char)

    mot_inverse = ''.join(nouveau_mot)
    logging.info(f"Mot inversé: {mot} -> {mot_inverse}")
    return mot_inverse


def inverser_phrase(phrase):
    """
    Inverse chaque mot d'une phrase en respectant l'ordre des mots et la ponctuation.

    Args:
        phrase (str): La phrase à inverser.

    Returns:
        str: La phrase avec chaque mot inversé.
    """
    mots = phrase.split(' ')  # Séparer les mots par les espaces
    mots_inverses = [inverser_mot(mot) for mot in mots]  # Inverser chaque mot
    phrase_inversee = ' '.join(mots_inverses)  # Recomposer la phrase
    logging.info(f"Phrase inversée: {phrase} -> {phrase_inversee}")
    return phrase_inversee


if __name__ == "__main__":
    # Exemple d'utilisation
    phrase = input("Entrez une phrase en Zorglangue : ")
    phrase_inversee = inverser_phrase(phrase)
    print(f"Phrase en Zorglangue : {phrase_inversee}")
