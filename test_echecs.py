import unittest
from io import StringIO
import sys
from unittest.mock import patch
from echecs import Plateau  # Importez les classes de votre code principal

class TestPlateau(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau()
        self.capture_output = StringIO()
        sys.stdout = self.capture_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_afficher_plateau(self):
        expected_output = "T C F D R F C T\n" \
                          "P P P P P P P P\n" \
                          ". . . . . . . .\n" \
                          ". . . . . . . .\n" \
                          ". . . . . . . .\n" \
                          ". . . . . . . .\n" \
                          "P P P P P P P P\n" \
                          "T C F D R F C T\n"

        # Initialiser le plateau avant d'afficher
        self.plateau.initialiser_plateau()

        # Capturer la sortie standard
        with self.subTest():
            self.plateau.afficher_plateau()
            self.assertEqual(self.capture_output.getvalue(), expected_output)

    def test_prise_piece(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.plateau = Plateau()
            self.plateau.initialiser_plateau()
            # Déplacer un pion blanc vers le bas jusqu'à manger un autre pion
            self.plateau.deplacer_pion((1, 0), (2, 0))
            self.plateau.deplacer_pion((2, 0), (3, 0))
            self.plateau.deplacer_pion((3, 0), (4, 0))
            self.plateau.deplacer_pion((4, 0), (5, 0))
            self.plateau.deplacer_pion((5, 0), (6, 1))
            expected_output = "Prise de pièce noir à (6, 1).\n"            
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_deplacement_pion_valide(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.plateau = Plateau()
            self.plateau.initialiser_plateau()
            # Déplacer un pion blanc vers le bas
            depart = (1, 0)
            arrivee = (2, 0)
            self.plateau.deplacer_pion(depart, arrivee)
            expected_output = "Pion blanc déplacé de (1, 0) à (2, 0).\n"            
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_deplacement_pion_invalide(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Tentative de déplacement de pièce autre qu'un pion
            self.plateau = Plateau()
            self.plateau.initialiser_plateau()
            self.plateau.deplacer_pion((0, 0), (3, 0))
            expected_output = "La pièce dans la case de départ n'est pas un pion.\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_deplacement_pion_invalide_droite(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Tentative de déplacement d'un pion vers la droite (ce qui est invalide)
            self.plateau = Plateau()
            self.plateau.initialiser_plateau()
            self.plateau.deplacer_pion((1, 0), (3, 0))
            expected_output = "Déplacement invalide pour un pion.\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()