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
            print(' '.join([type(piece).__name__[0].upper() if piece else '.' for piece in ligne]))

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

        # Vérifier si la case d'arrivée est vide ou contient une pièce ennemie
        if piece_arr is None or (piece_arr.couleur != piece_dep.couleur and abs(x_arr - x_dep) == 1 and abs(y_arr - y_dep) == 1):
            # Effectuer le déplacement et la prise de pièce si possible
            self.board[x_arr][y_arr] = piece_dep
            self.board[x_dep][y_dep] = None
            print(f"Pion {piece_dep.couleur} déplacé de {depart} à {arrivee}.")

            if piece_arr:
                print(f"Prise de pièce {piece_arr.couleur} à {arrivee}.")
        else:
            print("Déplacement invalide pour un pion.")

    def coord_valides(self, coord):
        x, y = coord
        return 0 <= x < 8 and 0 <= y < 8

# Condition pour la saisie utilisateur
if __name__ == '__main__':
    # Exemple d'utilisation avec des saisies utilisateur
    plateau = Plateau()
    plateau.initialiser_plateau()
    plateau.afficher_plateau()

    while True:
        # Saisies utilisateur pour déplacer un pion
        depart = tuple(map(int, input("Entrez les coordonnées de départ (ligne colonne) : ").split()))
        arrivee = tuple(map(int, input("Entrez les coordonnées d'arrivée (ligne colonne) : ").split()))

        plateau.deplacer_pion(depart, arrivee)
        plateau.afficher_plateau()