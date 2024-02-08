class Piece:
    def __init__(self, couleur):
        self.couleur = couleur

class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

class Fou(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

class Dame(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

class Plateau:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

    def initialiser_plateau(self):
        # Initialisation des pièces blanches
        self.board[0] = [Tour("blanc"), Cavalier("blanc"), Fou("blanc"), Dame("blanc"), Roi("blanc"), Fou("blanc"), Cavalier("blanc"), Tour("blanc")]
        self.board[1] = [Pion("blanc") for _ in range(8)]

        # Initialisation des pièces noires
        self.board[7] = [Tour("noir"), Cavalier("noir"), Fou("noir"), Dame("noir"), Roi("noir"), Fou("noir"), Cavalier("noir"), Tour("noir")]
        self.board[6] = [Pion("noir") for _ in range(8)]

    def afficher_plateau(self):
        for ligne in self.board:
            print(' '.join([type(piece).__name__[0].upper() if piece and piece.couleur == "blanc" else type(piece).__name__[0].lower() if piece else '.' for piece in ligne]))

    def deplacer_pion(self, depart, arrivee):
        # Vérifier si les coordonnées de départ et d'arrivée sont valides
        if not self.coord_valides(depart) or not self.coord_valides(arrivee):
            print("Coordonnées invalides.")
            return

        x_dep, y_dep = depart
        x_arr, y_arr = arrivee

        piece_dep = self.board[x_dep][y_dep]
        piece_arr = self.board[x_arr][y_arr]

        # Vérifier si la pièce dans la case de départ est un pion
        if not isinstance(piece_dep, Pion):
            print("La pièce dans la case de départ n'est pas un pion.")
            return

        # Vérifier si le déplacement est autorisé pour le pion
        if piece_dep.couleur == "blanc":
            # Déplacement normal d'une case en avant
            if x_arr == x_dep + 1 and y_arr == y_dep and piece_arr is None:
                self.deplacer_pion_effectif(depart, arrivee, piece_dep, piece_arr)
            # Premier déplacement de deux cases en avant
            elif x_dep == 1 and x_arr == x_dep + 2 and y_arr == y_dep and piece_arr is None and self.board[x_dep + 1][y_dep] is None:
                self.deplacer_pion_effectif(depart, arrivee, piece_dep, piece_arr)
            # Prise en diagonale
            elif abs(x_arr - x_dep) == 1 and abs(y_arr - y_dep) == 1 and piece_arr and piece_arr.couleur == "noir":
                self.deplacer_pion_effectif(depart, arrivee, piece_dep, piece_arr)
            else:
                print("Déplacement invalide pour un pion.")
        elif piece_dep.couleur == "noir":
            # Déplacement normal d'une case en avant
            if x_arr == x_dep - 1 and y_arr == y_dep and piece_arr is None:
                self.deplacer_pion_effectif(depart, arrivee, piece_dep, piece_arr)
            # Premier déplacement de deux cases en avant
            elif x_dep == 6 and x_arr == x_dep - 2 and y_arr == y_dep and piece_arr is None and self.board[x_dep - 1][y_dep] is None:
                self.deplacer_pion_effectif(depart, arrivee, piece_dep, piece_arr)
            # Prise en diagonale
            elif abs(x_arr - x_dep) == 1 and abs(y_arr - y_dep) == 1 and piece_arr and piece_arr.couleur == "blanc":
                self.deplacer_pion_effectif(depart, arrivee, piece_dep, piece_arr)
            else:
                print("Déplacement invalide pour un pion.")

    def deplacer_pion_effectif(self, depart, arrivee, piece_dep, piece_arr):
        # Effectuer le déplacement
        self.board[arrivee[0]][arrivee[1]] = piece_dep
        self.board[depart[0]][depart[1]] = None
        print(f"Pion {piece_dep.couleur} déplacé de {depart} à {arrivee}.")

        # Prise de pièce si possible
        if piece_arr:
            print(f"Prise de pièce {piece_arr.couleur} à {arrivee}.")

    def coord_valides(self, coord):
        x, y = coord
        return 0 <= x < 8 and 0 <= y < 8
    
    def deplacer_tour(self, depart, arrivee):
        # Vérifier si les coordonnées de départ et d'arrivée sont valides
        if not self.coord_valides(depart) or not self.coord_valides(arrivee):
            print("Coordonnées invalides.")
            return

        x_dep, y_dep = depart
        x_arr, y_arr = arrivee

        piece_dep = self.board[x_dep][y_dep]
        piece_arr = self.board[x_arr][y_arr]

        # Vérifier si la pièce dans la case de départ est une tour
        if not isinstance(piece_dep, Tour):
            print("La pièce dans la case de départ n'est pas une tour.")
            return

        # Vérifier si le déplacement est vertical ou horizontal
        if x_dep == x_arr or y_dep == y_arr:
            # Vérifier si le chemin est libre entre la tour et la case d'arrivée
            if self.chemin_libre(depart, arrivee):
                # Effectuer le déplacement et la prise de pièce si possible
                self.board[x_arr][y_arr] = piece_dep
                self.board[x_dep][y_dep] = None
                print(f"Tour {piece_dep.couleur} déplacée de {depart} à {arrivee}.")

                if piece_arr:
                    print(f"Prise de pièce {piece_arr.couleur} à {arrivee}.")
            else:
                print("Le chemin n'est pas libre pour la tour.")
        else:
            print("Déplacement invalide pour une tour.")

    def chemin_libre(self, depart, arrivee):
        # Vérifier si le chemin entre les coordonnées de départ et d'arrivée est libre
        x_dep, y_dep = depart
        x_arr, y_arr = arrivee

        if x_dep == x_arr:
            # Déplacement horizontal
            step = 1 if y_dep < y_arr else -1
            for y in range(y_dep + step, y_arr, step):
                if self.board[x_dep][y]:
                    return False
        elif y_dep == y_arr:
            # Déplacement vertical
            step = 1 if x_dep < x_arr else -1
            for x in range(x_dep + step, x_arr, step):
                if self.board[x][y_dep]:
                    return False

        return True
    
    def deplacer_cavalier(self, depart, arrivee):
        # Vérifier si les coordonnées de départ et d'arrivée sont valides
        if not self.coord_valides(depart) or not self.coord_valides(arrivee):
            print("Coordonnées invalides.")
            return

        x_dep, y_dep = depart
        x_arr, y_arr = arrivee

        piece_dep = self.board[x_dep][y_dep]
        piece_arr = self.board[x_arr][y_arr]

        # Vérifier si la pièce dans la case de départ est un cavalier
        if not isinstance(piece_dep, Cavalier):
            print("La pièce dans la case de départ n'est pas un cavalier.")
            return

        # Vérifier le motif de déplacement en L du cavalier
        if (abs(x_arr - x_dep) == 2 and abs(y_arr - y_dep) == 1) or (abs(x_arr - x_dep) == 1 and abs(y_arr - y_dep) == 2):
            # Effectuer le déplacement et la prise de pièce si possible
            self.board[x_arr][y_arr] = piece_dep
            self.board[x_dep][y_dep] = None
            print(f"Cavalier {piece_dep.couleur} déplacé de {depart} à {arrivee}.")

            if piece_arr:
                print(f"Prise de pièce {piece_arr.couleur} à {arrivee}.")
        else:
            print("Déplacement invalide pour un cavalier.")

# Condition pour la saisie utilisateur
if __name__ == '__main__':
    # Exemple d'utilisation avec des saisies utilisateur
    plateau = Plateau()
    plateau.initialiser_plateau()
    plateau.afficher_plateau()

    while True:
        # Saisies utilisateur pour déplacer une pièce
        depart = tuple(map(int, input("Entrez les coordonnées de départ (ligne colonne) : ").split()))
        arrivee = tuple(map(int, input("Entrez les coordonnées d'arrivée (ligne colonne) : ").split()))

        piece_dep = plateau.board[depart[0]][depart[1]]

        if isinstance(piece_dep, Pion):
            plateau.deplacer_pion(depart, arrivee)
        elif isinstance(piece_dep, Tour):
            plateau.deplacer_tour(depart, arrivee)
        elif isinstance(piece_dep, Cavalier):
            plateau.deplacer_cavalier(depart, arrivee)
        else:
            print("Type de pièce non pris en charge.")

        plateau.afficher_plateau()