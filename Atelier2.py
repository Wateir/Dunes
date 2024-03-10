# -*- coding: utf-8 -*-

def initialisation_plateau(scenario):
    if scenario == "debut":
        matrice = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ['○', '○', '○', '○', '○', '○', '○', '○', '○', '○'],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ['●', '●', '●', '●', '●', '●', '●', '●', '●', '●'],    
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ['○', '○', '○', '○', '○', '○', '○', '○', '○', '○'],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ]
    elif scenario == "milieu":
        matrice = [
    [" ", "●", " ", " ", "○", " ", "●", " ", "○", " "],
    ["○", " ", "○", "●", " ", "○", " ", "●", " ", "○"],
    [" ", " ", "●", " ", " ", " ", "●", " ", " ", " "],
    ["●", " ", " ", " ", "○", " ", " ", " ", "●", " "],
    [" ", "●", " ", "●", " ", "○", " ", "○", " ", " "],
    [" ", " ", "○", " ", "●", " ", " ", " ", "○", " "],
    [" ", "○", " ", " ", " ", "●", " ", " ", " ", "●"],
    [" ", " ", " ", "○", " ", " ", " ", "●", " ", " "],
    ["○", " ", "●", " ", "○", " ", "●", " ", "○", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ]
    else:
        matrice = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", "●", " ", " ", " ", " ", " "],
    [" ", " ", "●", " ", " ", " ", "●", " ", " ", " "],
    [" ", " ", " ", " ", " ", "○", " ", " ", " ", " "],
    [" ", "○", " ", " ", " ", " ", " ", " ", "○", " "],
    [" ", " ", " ", "○", " ", "●", " ", "○", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ]
    return matrice

def convertir_coordonnees(coordonnee):
    colonne = ord(coordonnee[0].upper()) - ord('A')
    ligne = int(coordonnee[1])
    return ligne, colonne


def demander_coordonnee():
    while True:
        coordonnee = input("Entrez une coordonnée (sous la forme A0) : ")
        if est_au_bon_format(coordonnee) and est_dans_grille(coordonnee):
            return coordonnee
        else:
            print("Coordonnée invalide, veuillez réessayer.")

def est_au_bon_format(coordonnee):
    if len(coordonnee) >= 2 and len(coordonnee) <= 3:
        return True
    else:
        print("La coordonnée doit contenir une lettre suivie d'un ou deux chiffres.")
        return False

def est_dans_grille(coordonnee):
    colonne = coordonnee[0].upper()
    ligne = coordonnee[1:]
    if (colonne >= 'A' and colonne <= 'J') and ligne.isdigit() and (0 <= int(ligne) <= 9):
        return True
    else:
        print("Coordonnée invalide. La lettre doit être comprise entre A et J, et le chiffre entre 0 et 9.")
        return False



def afficher_grille(matrice):
    print("    A   B   C   D   E   F   G   H   I   J  ")
    print("  -----------------------------------------")
    coordonnée_vertical = -1
    for ligne in matrice:
        ligne_final = "|"
        coordonnée_vertical += 1
        for valeur in ligne:
            ligne_final += f" {valeur} |"
        print(coordonnée_vertical, ligne_final)
        print("  -----------------------------------------")

def placer_X_sur_coordonnee(matrice, coordonnee):
    ligne, colonne = convertir_coordonnees(coordonnee)
    nouvelle_matrice = [ligne[:] for ligne in matrice]  # Création d'une copie de la matrice
    
    nouvelle_matrice[ligne][colonne] = 'X'
    
    return nouvelle_matrice

def test_scenario():
    while True:
        choix_scenario = input("Quel scénario voulez-vous tester ? (debut/milieu/fin) : ")
        plateau_jeu = initialisation_plateau(choix_scenario)

        afficher_grille(plateau_jeu)

        coordonnee = demander_coordonnee()  # Appel de la fonction demander_coordonnee
        afficher_grille(placer_X_sur_coordonnee(plateau_jeu, coordonnee))  # Appel de la fonction placer_X_sur_coordonnee avec la coordonnée obtenue

        continuer = input("Voulez-vous tester un autre pion joueur ? (Oui/Non) : ")
        if continuer.lower() != 'oui':
            break

def test_est_au_bon_format():
    # Cas valides
    assert est_au_bon_format("A1"), "A1 devrait être un format valide"
    assert est_au_bon_format("J10"), "J10 devrait être un format valide"
    # Cas invalides
    assert not est_au_bon_format("K1"), "K1 devrait être un format invalide (lettre hors grille)"
    assert not est_au_bon_format("A11"), "A11 devrait être un format invalide (numéro hors grille)"
    assert not est_au_bon_format("1A"), "1A devrait être un format invalide (format incorrect)"
    assert not est_au_bon_format("AB"), "AB devrait être un format invalide (manque de chiffre)"
    print("test_est_au_bon_format: tous les tests passent")

def test_est_dans_grille():
    # Cas valides
    assert est_dans_grille("A1"), "A1 devrait être dans la grille"
    assert est_dans_grille("J10"), "J10 devrait être dans la grille"
    # Cas invalides
    assert not est_dans_grille("A0"), "A0 ne devrait pas être dans la grille (numéro hors grille)"
    assert not est_dans_grille("K1"), "K1 ne devrait pas être dans la grille (lettre hors grille)"
    assert not est_dans_grille("J11"), "J11 ne devrait pas être dans la grille (numéro hors grille)"
    print("test_est_dans_grille: tous les tests passent")

test_est_au_bon_format()
test_est_dans_grille()

test_scenario()