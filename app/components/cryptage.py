import random

def generer_cle_cesar():
    """
    Génère une clé de décalage aléatoire pour un chiffrement de type César.
    Returns:
        int: Clé de décalage (entre 1 et 25)
    """
    return random.randint(1, 25)

def chiffrer_cesar(texte, cle):
    """
    Chiffre un texte en utilisant le chiffre de César avec une clé donnée.

    Args:
        texte (str): Le texte à chiffrer.
        cle (int): La clé de décalage.

    Returns:
        str: Le texte chiffré.
    """
    texte_chiffre = []
    for char in texte:
        if char.isalpha():
            # Déterminer la base (majuscules ou minuscules)
            base = ord('A') if char.isupper() else ord('a')
            # Calculer le nouveau caractère décalé
            texte_chiffre.append(chr((ord(char) - base + cle) % 26 + base))
        else:
            texte_chiffre.append(char)  # Garder les ponctuations intacts

    return ''.join(texte_chiffre)

def dechiffrer_cesar(texte, cle):
    """
    Déchiffre un texte chiffré avec le chiffre de César en utilisant la clé de décalage.

    Args:
        texte (str): Le texte chiffré.
        cle (int): La clé de décalage.

    Returns:
        str: Le texte déchiffré.
    """
    return chiffrer_cesar(texte, -cle)
