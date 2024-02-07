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
            print([type(piece).__name__[0] if piece else '.' for piece in ligne])

    def deplacer_pion(self, depart, arrivee):
        # Vérifier si les coordonnées de départ et d'arrivée sont valides
        if not self.coord_valides(depart) or not self.coord_valides(arrivee):
            print("Coordonnées invalides.")
            return

        x_dep, y_dep = depart
        x_arr, y_arr = arrivee

        piece = self.board[x_dep][y_dep]

        # Vérifier si la pièce dans la case de départ est un pion
        if not isinstance(piece, Pion):
            print("La pièce dans la case de départ n'est pas un pion.")
            return

        # Vérifier si le déplacement est valide pour un pion
        if (piece.couleur == "blanc" and x_arr == x_dep - 1 and y_arr == y_dep) or \
           (piece.couleur == "noir" and x_arr == x_dep + 1 and y_arr == y_dep):
            # Effectuer le déplacement
            self.board[x_arr][y_arr] = piece
            self.board[x_dep][y_dep] = None
            print(f"Pion déplacé de {depart} à {arrivee}.")
        else:
            print("Déplacement invalide pour un pion.")

    def coord_valides(self, coord):
        x, y = coord
        return 0 <= x < 8 and 0 <= y < 8

# Exemple d'utilisation
plateau = Plateau()
plateau.initialiser_plateau()
plateau.afficher_plateau()

# Déplacer un pion blanc
plateau.deplacer_pion((1, 0), (2, 0))
plateau.afficher_plateau()

# Déplacer un pion noir (mouvement invalide)
plateau.deplacer_pion((6, 0), (4, 0))