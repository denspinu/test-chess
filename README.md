# test-chess
Projet test driven development

Initialisation du jeu :
Au démarrage du jeu, le plateau est affiché dans le terminal avec les pièces positionnées.
Les pièces blanches sont représentées par des lettres majuscules, et les pièces noires par des lettres minuscules.

Tour par tour :
Le jeu se déroule tour par tour, les blancs commençant en premier (l'ordre n'est pas géré dans notre jeu car nous n'avons pas eu le temps de nous en charger).
Vous êtes invité à saisir les coordonnées de la pièce que vous souhaitez déplacer et les coordonnées de la case vers laquelle vous souhaitez la déplacer.

Saisie des coordonnées :
Les coordonnées sont saisies sous forme de paires (ligne, colonne). Par exemple, (2, 3) représente la case située à la deuxième ligne et à la troisième colonne.
Les saisies sont demandées de manière interactive dans le terminal.

Types de pièces :
Vous pouvez déplacer des pions, des tours, et des cavaliers.
Pour déplacer une pièce, vous devez entrer les coordonnées de départ et d'arrivée.

Déplacement des pions :
Les pions peuvent avancer d'une case en avant, mais lors de leur premier déplacement, ils peuvent avancer de deux cases.
Les pions peuvent capturer une pièce ennemie en diagonale.

Déplacement des tours :
Les tours peuvent se déplacer horizontalement ou verticalement, mais seulement si le chemin est libre.

Déplacement des cavaliers :
Les cavaliers ont un motif de déplacement en L : deux cases dans une direction et une case perpendiculaire.
Les cavaliers peuvent "sauter" par-dessus d'autres pièces.

Affichage du plateau :
Après chaque déplacement, le plateau est réaffiché avec les nouvelles positions des pièces.

Fin du jeu :
Pour l'instant, le jeu ne détecte pas la fin de la partie (échec, échec et mat). 

Boucle continue :
Le jeu continue à demander des mouvements jusqu'à ce que vous décidiez de le quitter en utilisant une commande spécifique (par exemple, CTRL+C).