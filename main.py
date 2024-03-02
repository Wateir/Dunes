nombre_pion_blanc = 10
nombre_pion_noir = 10



def initialisation_plateau():
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

    return matrice

def convertir_coordonnees(coordonnee):
    colonne = ord(coordonnee[0].upper()) - ord('A')
    ligne = int(coordonnee[1])
    return ligne, colonne

def convertir_en_coordonnee_alpha(coordonnee):
    colonne_alpha = chr(coordonnee[1] + ord('A'))
    ligne = coordonnee[0]
    coord_alpha = colonne_alpha + str(ligne)
    return coord_alpha


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

def est_bien_un_pion_joueur(matrice, coordonnee, couleur_joueur):
    ligne, colonne = coordonnee
    
    # Vérifier si la coordonnée est dans les limites de la matrice
    if ligne < 0 or ligne >= len(matrice) or colonne < 0 or colonne >= len(matrice[0]):
        print("Coordonnée en dehors des limites de la matrice.")
        return False
    
    # Vérifier la couleur du pion et la couleur du joueur
    pion = matrice[ligne][colonne]
    if couleur_joueur == "blanc":
        if pion != "●":
            print("Vous ne pouvez déplacer que les pions blancs.")
            return False
    elif couleur_joueur == "noir":
        if pion != "○":
            print("Vous ne pouvez déplacer que les pions noirs.")
            return False
    
    return True


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

    # Exemple de grille vide que renvoie cette fonction si une matrice vide est donné en parametre
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------
    ##|   |   |   |   |   |   |   |   |   |   |
    ##-----------------------------------------

def afficher_grille_avec_deplacements(matrice, deplacements):
    grille_affichage = [ligne[:] for ligne in matrice]  # Création d'une copie de la grille
    
    # Marquer les déplacements possibles avec des 'X'
    for deplacement in deplacements:
        ligne, colonne = deplacement
        grille_affichage[ligne][colonne] = 'X'
    
    # Afficher la grille avec les déplacements possibles
    afficher_grille(grille_affichage)

def deplacements_possibles(matrice, coordonnee):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Haut, Bas, Droite, Gauche
    deplacements = []
    ligne, colonne = coordonnee
    for direction in directions:
        nouvelle_ligne = ligne + direction[0]
        nouvelle_colonne = colonne + direction[1]
        
        # Vérifier si la nouvelle ligne est dans les limites de la matrice
        ligne_valide = 0 <= nouvelle_ligne < 10
        
        # Vérifier si la nouvelle colonne est dans les limites de la matrice
        colonne_valide = 0 <= nouvelle_colonne < 10
        
        # Vérifier si la case correspondante est vide
        case_vide = matrice[nouvelle_ligne][nouvelle_colonne] == " "
        
        # Ajouter le déplacement à la liste s'il est valide
        if ligne_valide and colonne_valide and case_vide:
            deplacements.append((nouvelle_ligne, nouvelle_colonne))
    
    return deplacements

def demander_destination_possible(deplacements):
    while True:
        destination = input("Entrez la destination souhaitée (sous la forme A0) : ")
        ligne_dest, colonne_dest = convertir_coordonnees(destination)
        
        if (ligne_dest, colonne_dest) in deplacements:
            return ligne_dest, colonne_dest
        else:
            print("La destination n'est pas valide. Veuillez choisir parmi les déplacements possibles.")

def deplacer_pion(matrice, origine, destination):
    ligne_origine, colonne_origine = origine
    ligne_dest, colonne_dest = destination
    
    # Déplacer le pion de l'origine vers la destination
    matrice[ligne_dest][colonne_dest] = matrice[ligne_origine][colonne_origine]
    matrice[ligne_origine][colonne_origine] = " "
    return matrice

def verifier_et_supprimer_pion_capture(matrice, destination, couleur_joueur):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Haut, Bas, Droite, Gauche
    pion_capture = False
    ligne_dest, colonne_dest = destination
    pion_adverse = '○' if couleur_joueur == "noir" else '●'
    pion_joueur = '●' if couleur_joueur == "noir" else '○'

    for direction in directions:
        ligne_adjacente = ligne_dest + direction[0]
        colonne_adjacente = colonne_dest + direction[1]

        # Vérifier les bords du plateau comme "pion allié"
        if ligne_adjacente < 0 or ligne_adjacente >= 10 or colonne_adjacente < 0 or colonne_adjacente >= 10:
            continue  # Passe à la direction suivante si on est au bord du plateau

        if matrice[ligne_adjacente][colonne_adjacente] == pion_adverse:
            ligne_opposee = ligne_adjacente + direction[0]
            colonne_opposee = colonne_adjacente + direction[1]

            # Vérifier si le pion opposé est un pion joueur ou si on est au bord du plateau
            if (ligne_opposee < 0 or ligne_opposee >= 10 or colonne_opposee < 0 or colonne_opposee >= 10) or (matrice[ligne_opposee][colonne_opposee] == pion_joueur):
                matrice[ligne_adjacente][colonne_adjacente] = " "
                pion_capture = True
                print(f"Un pion {pion_adverse} a été capturé à la position {convertir_en_coordonnee_alpha((ligne_adjacente, colonne_adjacente))}.")

    return matrice, pion_capture


def est_partie_finis():
    if nombre_pion_blanc or nombre_pion_noir == 0:
        return True
    else:
        return False


def bouger_pion(matrice, joueur):
    couleur_joueur = "blanc" if joueur == "blanc" else "noir"
    
    print(f"C'est au tour du joueur {couleur_joueur}.")

    coordonnee = demander_coordonnee()
    ligne, colonne = convertir_coordonnees(coordonnee)
    
    while not est_bien_un_pion_joueur(matrice, (ligne, colonne), couleur_joueur):
        print("Position invalide. Veuillez réessayer.")
        coordonnee = demander_coordonnee()
        ligne, colonne = convertir_coordonnees(coordonnee)
    
    deplacements = deplacements_possibles(matrice, (ligne, colonne))
    afficher_grille_avec_deplacements(matrice, deplacements)
    
    destination = demander_destination_possible(deplacements)
    matrice = deplacer_pion(matrice, (ligne, colonne), destination)
    afficher_grille(matrice)
    
    # Vérifier si un pion adverse est mangé
    matrice, pion_capture = verifier_et_supprimer_pion_capture(matrice, destination, couleur_joueur)
    
    if pion_capture:
        if joueur == "blanc":
            global nombre_pion_noir
            nombre_pion_noir -= 1
            print("Un pion noir a été capturé!")
            afficher_grille(matrice)
            if nombre_pion_noir == 0:
                print("Il n'y a plus de pions noirs. Blanc a gagné!")
                return True
        else:
            global nombre_pion_blanc
            nombre_pion_blanc -= 1
            print("Un pion blanc a été capturé!")
            afficher_grille(matrice)
            if nombre_pion_blanc == 0:
                print("Il n'y a plus de pions blancs. Noir a gagné!")
                return True
    
    return False

def jouer_partie():
    plateau_de_jeu = initialisation_plateau()
    afficher_grille(plateau_de_jeu)
    
    while True:
        if bouger_pion(plateau_de_jeu, "blanc"):
            break
        if bouger_pion(plateau_de_jeu, "noir"):
            break

jouer_partie()