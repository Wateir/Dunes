def afficher_tableau(matrice):
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

def convertir_coordonnees(coordonnee):
    colonne = ord(coordonnee[0].upper()) - ord('A')
    ligne = int(coordonnee[1])
    return ligne, colonne

# Exemple d'utilisation
coordonnee = "J9"
ligne, colonne = convertir_coordonnees(coordonnee)
print(f"Coordonnées transformées : ({ligne}, {colonne})")

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

def convertir_en_coordonnee_alpha(coordonnee):
    colonne_alpha = chr(coordonnee[1] + ord('A'))
    ligne = coordonnee[0]
    coord_alpha = colonne_alpha + str(ligne)
    return coord_alpha

def est_bien_un_pion_joueur(matrice, coordonnee):
    ligne, colonne = coordonnee
    if ligne < 0 or ligne >= len(matrice) or colonne < 0 or colonne >= len(matrice[0]):
        print("Coordonnée en dehors des limites de la matrice.")
        return False
    if matrice[ligne][colonne] == '●':
        coord_alpha = convertir_en_coordonnee_alpha((ligne, colonne))
        print("Le caractère à la coordonnée", coord_alpha, "est bien '●'.")
        return True
    else:
        coord_alpha = convertir_en_coordonnee_alpha((ligne, colonne))
        print("Le caractère à la coordonnée", coord_alpha, "n'est pas '●'.")
        return False


def deplacements_possibles(coordonnee):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Haut, Bas, Droite, Gauche
    deplacements = []
    ligne, colonne = coordonnee
    for direction in directions:
        nouvelle_ligne = ligne + direction[0]
        nouvelle_colonne = colonne + direction[1]
        if 0 <= nouvelle_ligne < 10 and 0 <= nouvelle_colonne < 10:
            deplacements.append((nouvelle_ligne, nouvelle_colonne))
    return deplacements

def marquer_positions(matrice, positions):
    for position in positions:
        ligne, colonne = position
        if 0 <= ligne < len(matrice) and 0 <= colonne < len(matrice[0]):
            matrice[ligne][colonne] = "X"
    return matrice

# Exemple d'utilisation
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

positions_a_marquer = [(1, 1), (3, 3), (5, 5)]  # Exemple de liste de positions à marquer
matrice_marquee = marquer_positions(matrice, positions_a_marquer)

# Affichage de la matrice marquée
for ligne in matrice_marquee:
    print(ligne)