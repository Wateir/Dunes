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
        if len(coordonnee) < 2 or len(coordonnee) > 3:
            print("La coordonnée doit contenir une lettre suivie d'un ou deux chiffres.")
            continue
        colonne = coordonnee[0].upper()
        ligne = coordonnee[1:]
        if colonne < 'A' or colonne > 'J' or not ligne.isdigit() or int(ligne) < 0 or int(ligne) > 9:
            print("Coordonnée invalide. La lettre doit être comprise entre A et J, et le chiffre entre 0 et 9.")
            continue
        return coordonnee


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

test_scenario()