class Pion:
    def __init__(self, id, coordonnes, equipe, rules):
        self.id = id
        self.coordonnes = coordonnes
        self.rules = rules
        self.equipe = equipe
        self.skin = "  ♙  "
        self.elements = []

    def ajouter_element(self, element):
        self.elements.append(element)

    def obtenir_coordonnees(self):
        return (self.coordonnes)
    
    def obtenir_skin(self):
        if self.equipe == 1:
            return (self.skin)
        else:
            return (print_color(self.skin, RED))  
    
class Tour:
    def __init__(self, id, coordonnes, equipe, rules):
        self.id = id
        self.coordonnes = coordonnes
        self.rules = rules
        self.equipe = equipe
        self.skin = "  ♖  "
        self.elements = []

    def ajouter_element(self, element):
        self.elements.append(element)

    def obtenir_coordonnees(self):
        return (self.coordonnes)
    
    def obtenir_skin(self):
        if self.equipe == 1:
            return (self.skin)
        else:
            return (print_color(self.skin, RED))

class Cavaliers:
    def __init__(self, id, coordonnes, equipe, rules):
        self.id = id
        self.coordonnes = coordonnes
        self.rules = rules
        self.equipe = equipe
        self.skin = "  ♞  "
        self.elements = []

    def ajouter_element(self, element):
        self.elements.append(element)

    def obtenir_coordonnees(self):
        return (self.coordonnes)
    
    def obtenir_skin(self):
        if self.equipe == 1:
            return (self.skin)
        else:
            return (print_color(self.skin, RED))

class Fou:
    def __init__(self, id, coordonnes, equipe, rules):
        self.id = id
        self.coordonnes = coordonnes
        self.rules = rules
        self.equipe = equipe
        self.skin = "  ♗  "
        self.elements = []

    def ajouter_element(self, element):
        self.elements.append(element)

    def obtenir_coordonnees(self):
        return (self.coordonnes)
    
    def obtenir_skin(self):
        if self.equipe == 1:
            return (self.skin)
        else:
            return (print_color(self.skin, RED))

class Roi:
    def __init__(self, id, coordonnes, equipe, rules):
        self.id = id
        self.coordonnes = coordonnes
        self.rules = rules
        self.equipe = equipe
        self.skin = "  ♚  "
        self.elements = []

    def ajouter_element(self, element):
        self.elements.append(element)

    def obtenir_coordonnees(self):
        return (self.coordonnes)
    
    def obtenir_skin(self):
        if self.equipe == 1:
            return (self.skin)
        else:
            return (print_color(self.skin, RED))

class Reine:
    def __init__(self, id, coordonnes, equipe, rules):
        self.id = id
        self.coordonnes = coordonnes
        self.rules = rules
        self.equipe = equipe
        self.skin = "  ♛  "
        self.elements = []

    def ajouter_element(self, element):
        self.elements.append(element)

    def obtenir_coordonnees(self):
        return (self.coordonnes)
    
    def obtenir_skin(self):
        if self.equipe == 1:
            return (self.skin)
        else:
            return (print_color(self.skin, RED))



RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Fonction pour imprimer du texte coloré
def print_color(text, color):
    return(color + text + RESET)

# Exemples d'utilisation
print_color("Texte en rouge", RED)
print_color("Texte en vert", GREEN)
print_color("Texte en jaune", YELLOW)
print_color("Texte en bleu", BLUE)






joueurs = []

joueurs.append(Tour(1200, [0, 0], 1, "Some rules"))
joueurs.append(Tour(1200, [0, 7], 1, "Some rules"))

joueurs.append(Tour(1200, [7, 0], 0, "Some rules"))
joueurs.append(Tour(1200, [7, 7], 0, "Some rules"))

joueurs.append(Cavaliers(1200, [0, 1], 1, "Some rules"))
joueurs.append(Cavaliers(1200, [0, 6], 1, "Some rules"))

joueurs.append(Cavaliers(1200, [7, 1], 0, "Some rules"))
joueurs.append(Cavaliers(1200, [7, 6], 0, "Some rules"))

joueurs.append(Fou(1200, [0, 2], 1, "Some rules"))
joueurs.append(Fou(1200, [0, 5], 1, "Some rules"))

joueurs.append(Fou(1200, [7, 2], 0, "Some rules"))
joueurs.append(Fou(1200, [7, 5], 0, "Some rules"))

joueurs.append(Reine(1200, [0, 3], 1, "Some rules"))
joueurs.append(Reine(1200, [7, 3], 0, "Some rules"))

joueurs.append(Roi(1200, [0, 4], 1, "Some rules"))
joueurs.append(Roi(1200, [7, 4], 0, "Some rules"))


for i in range(8):
    joueurs.append(Pion(i, [1, i], 1, "Some rules"))
    joueurs.append(Pion(i, [6, i], 0, "Some rules"))

#print(joueurs[0].obtenir_coordonnees())

render = ""

# Exemples d'utilisation
print_color("Texte en rouge", RED)
print_color("Texte en vert", GREEN)
print_color("Texte en jaune", YELLOW)
print_color("Texte en bleu", BLUE)


for i in range(8):
    for i2 in range(8):
        pion_present = False
        for joueur in joueurs:
            if joueur.obtenir_coordonnees() == [i, i2]:
                render = render +  joueur.obtenir_skin()
                pion_present = True
                break
        if not pion_present:
            render += "  .  "
                
    render = render +  "\n\n"

print(render)


