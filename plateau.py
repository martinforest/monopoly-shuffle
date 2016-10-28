import joueurs

class caseGo(object):
    def __init__(self, nom):
        self.nom = nom

class caseSpeciale(object):
    def __init__(self, nom, loyer):
        self.nom = nom
        self.loyer = loyer
        
class caseStationnement(caseSpeciale):
    pass

class caseChance(caseSpeciale):
    pass

class caseCaisseCommune(caseSpeciale):
    pass

class caseAllezEnPrison(caseSpeciale):
    pass

class casePrison(caseSpeciale):
    pass

class caseImpot(caseSpeciale):
    def calcImpot(self, i, solde, proprietesJoueur):
        ##boucle calculant et affichant la valeur des proprietes du joueur
        sommeValeurProprietes = 0
        for p in proprietesJoueur:
            sommeValeurProprietes = sommeValeurProprietes + p.prixAchat
            print "Il possede", p.nom, "valant", p.prixAchat, "$."
        print "La valeur totale de ses proprietes est de", sommeValeurProprietes, "$."
        ##rien a payer si balance negative
        if (solde + sommeValeurProprietes) <0:
            impot = 0
        ##calcul selon solde + valeur propr (max 200)
        if 0.10 * (solde + sommeValeurProprietes) < 200:
            impot = int(round(0.10 * (solde + sommeValeurProprietes), 0))
        else:
            impot = 200
        return impot

class caseTaxe(caseSpeciale):
    pass

class casePropriete(object):
    def __init__(self, nom, proprietaire, prixAchat, loyer, serie, nomSerie):
        self.nom = nom
        self.proprietaire = proprietaire
        self.prixAchat = prixAchat
        self.loyer = loyer
        self.serie = serie
        self.nomSerie = nomSerie

class caseTerrain(casePropriete):
    ##calcul du loyer (garder lancerSomme comme arg meme si pas utilise)
    def calcLoyer(self, n, lancerSomme):
        if n == len(self.serie):
            loyer = 2 * self.loyer
        else:
            loyer = self.loyer

        return loyer

class caseChFer(casePropriete):
    ##calcul du loyer (garder lancerSomme comme arg meme si pas utilise)
    def calcLoyer(self, n, lancerSomme):
        loyer = 2**(n-1) * 25
        return loyer

class caseServPublic(casePropriete):
    ##calcul du loyer
    def calcLoyer(self, n, lancerSomme):
        loyer = (6 * n - 2) * lancerSomme
        return loyer

##le plateau sera un tuple rempli apres la definition des cases
plateau = ()
##les series seront des listes de cases remplies apres la definition des case
violet = []
bleuPale = []
rose = []
orange = []
rouge = []
jaune = []
vert = []
bleuFonce = []
servicePublic = []
train = []

case00 = caseGo("Case Go")
case01 = caseTerrain("Avenue de la Mediterrannee", "vacant", 60, 2, violet, "violet")
case02 = caseCaisseCommune("Caisse Commune", 0)
case03 = caseTerrain("Avenue de la Baltique", "vacant", 60, 4, violet, "violet")
case04 = caseImpot("Impot sur le revenu", 200)
case05 = caseChFer("Chemin de Fer Reading", "vacant", 200, 25, train, "train")
case06 = caseTerrain("Avenue de l'Orient", "vacant", 100, 6, bleuPale, "bleuPale")
case07 = caseChance("Chance", 0)
case08 = caseTerrain("Avenue Vermont", "vacant", 100, 6, bleuPale, "bleuPale")
case09 = caseTerrain("Avenue Connecticut", "vacant", 120, 8, bleuPale, "bleuPale")
case10 = casePrison("Prison", 50)
case11 = caseTerrain("Place St-Charles", "vacant", 140, 10, rose, "rose")
case12 = caseServPublic("Compagnie d'electricite", "vacant", 150, 0, servicePublic, "servicePublic")
case13 = caseTerrain("Avenue des Etats-Unis", "vacant", 140, 10, rose, "rose")
case14 = caseTerrain("Avenue Virginie", "vacant", 160, 12, rose, "rose")
case15 = caseChFer("Chemin de Fer Pennsylvanie", "vacant", 200, 25, train, "train")
case16 = caseTerrain("Place St-Jacques", "vacant", 180, 14, orange, "orange")
case17 = caseCaisseCommune("Caisse Commune", 0)
case18 = caseTerrain("Avenue Tennesse", "vacant", 180, 14, orange, "orange")
case19 = caseTerrain("Avenue New-York", "vacant", 200, 16, orange, "orange")
case20 = caseStationnement("Stationnement Gratuit", 0)
case21 = caseTerrain("Avenue Kentucky", "vacant", 220, 18, rouge, "rouge")
case22 = caseChance("Chance", 0)
case23 = caseTerrain("Avenue Indiana", "vacant", 220, 18, rouge, "rouge")
case24 = caseTerrain("Avenue Illinois", "vacant", 240, 20, rouge, "rouge")
case25 = caseChFer("Chemin de Fer B. & O.", "vacant", 200, 25, train, "train")
case26 = caseTerrain("Avenue Atlantique", "vacant", 260, 22, jaune, "jaune")
case27 = caseTerrain("Avenue Ventnor", "vacant", 260, 22, jaune, "jaune")
case28 = caseServPublic("Aqueduc", "vacant", 150, 0, servicePublic, "servicePublic")
case29 = caseTerrain("Jardins Marvin", "vacant", 280, 24, jaune, "jaune")
case30 = caseAllezEnPrison("Allez en prison!", 0)
case31 = caseTerrain("Avenue Pacifique", "vacant", 300, 26, vert, "vert")
case32 = caseTerrain("Avenue Caroline du Nord", "vacant", 300, 26, vert, "vert")
case33 = caseCaisseCommune("Caisse Commune", 0)
case34 = caseTerrain("Avenue Pennsylvanie", "vacant", 320, 28, vert, "vert")
case35 = caseChFer("Chemin de Fer Petit Reseau", "vacant", 200, 25, train, "train")
case36 = caseChance("Chance", 0)
case37 = caseTerrain("Place du Parc", "vacant", 350, 35, bleuFonce, "bleuFonce")
case38 = caseTaxe("Taxe de luxe", 75)
case39 = caseTerrain("Promenade", "vacant", 400, 50, bleuFonce, "bleuFonce")

plateau = (case00, case01, case02, case03, case04, case05, case06, case07, case08, case09, case10, case11, case12, case13, case14, case15, case16, case17, case18, case19, case20, case21, case22, case23, case24, case25, case26, case27, case28, case29, case30, case31, case32, case33, case34, case35, case36, case37, case38, case39)

##chaque case doit peupler sa propre serie
for case in plateau:
    ##exception: cases n'ayant pas de serie
    try:
        case.serie.extend([case])
    except:
        pass

def modeConditionFin():
    while True:
        mode = str(raw_input('Limite de lancers (l) ou de proprietes (p)?'))
        if mode not in ('p', 'P', 'l', 'L'):
            print('choix invalide')
            continue
        else:
            break
    return mode
                                 
def entrerConditionFinProprietes():
    while True:
        conditionFin = int(raw_input('Arreter le programme apres combien de proprietes vendues (maximum 28?)'))
        if conditionFin not in range(1,29):
            print('nombre invalide') 
            continue
        else:
            break
    return conditionFin

def entrerConditionFinLancers():
    while True:
        conditionFin = int(raw_input('Arreter le programme apres combien de lancers (environ 150 pour tout acheter)?'))
        if conditionFin <1:
            print('1 lancer minimum!') 
            continue
        else:
            break
    return conditionFin

def nbrJoueurSerie(p, case):
    ##exception si serie est N/A
    try:
        possede = sum(1 for c in case.serie if c.proprietaire == p)
        return possede
    except:
        pass
            
##compte le nombre vendus dans la serie
def nbrVendusSerie(case):
    vendus = sum(1 for c in case.serie if c.proprietaire <> "vacant")
    return vendus

##compte le nombre vendus sur le plateau
def nbrVendusPlateau():
    vendus = 0
    ##pas pu faire un sum() puisqu'il faut un continue pour la boucle quand proprietaire ne s'applique pas
    for c in plateau:
        try:
            if c.proprietaire <> "vacant":
                vendus = vendus +1
        except:
            pass
        continue
    return vendus

def nbrTotalPlateau():
    total = 0
    ##pas pu faire un sum() puisqu'il faut un continue pour la boucle quand proprietaire ne s'applique pas
    for c in plateau:
        try:
            if c.proprietaire <> "bogus string":
                total = total +1
        except:
            pass
        continue
    return total


#comment compter objet dans liste avec condition
#sera utile dans liste de proprietes de chaque joueur
#print sum(1 for c in plateau if c.loyer == 5)

#comment extraire la classe d'un objet
#print case38.__class__.__name__
