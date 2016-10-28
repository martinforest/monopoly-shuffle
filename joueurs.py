##entree du nombre de joueurs
import plateau

def entrerNbrJoueurs():
    while True:
        nbrJoueurs = int(raw_input('Combien de joueurs (2-6)?'))
        if nbrJoueurs not in range(2,7):
            print('nombre invalide') 
            continue
        else:
            break
    return nbrJoueurs

class joueur(object):
    def __init__(self):
        self.solde = 1500 ##doit etre 1500
        self.position = 0
        self.enPrison = False
        self.nbrDoubles = 0
        self.proprietesObjets = []
        self.proprietesAffichables = []

    def afficheSolde(self, i):
        print "Le joueur", i, "a", self.solde, "$"

    def affichePosition(self, i):
        case = plateau.plateau[self.position]
        print "Le joueur " + str(i) + " est sur " + case.nom,
        print "(",
        if hasattr(case, "nomSerie"): ##verifie si la case contient cet attribut
            print case.nomSerie + ",",
        print "case no " + str(self.position) + ")."

    def avance(self, i, lancerSomme):
        print "le joueur", i, "avance son pion: "
        ##ajoute 200 au solde si case go est atteinte ou passee
        if (self.position + lancerSomme) >= len(plateau.plateau):
            self.solde = self.solde + 200
            print "(il passe Go et reclame 200$)"
        ##position d'arrivee
        self.position = (self.position + lancerSomme) % len(plateau.plateau)

    def incrementeDoubles(self):
        self.nbrDoubles = self.nbrDoubles + 1

    def allezEnPrison(self, i):
            print "Le joueur", i, "va en prison"
            self.nbrDoubles = 0
            self.position = 10
            self.enPrison = True
            ##self.affichePosition(i)

    def afficheProprietaire(self):
        case = plateau.plateau[self.position]
        try:
            case.proprietaire
            if case.proprietaire == "vacant":
                print "Cette propriete est encore vacante."
            else:
                print "Le joueur", case.proprietaire,
                print "en est le proprietaire."
            return case.proprietaire
        except:
            pass

    def achat(self, i, d, seqAchats):
        case = plateau.plateau[self.position]
        print "\tLe joueur", i, "achete", case.nom,
        print "pour la somme de", case.prixAchat, "$."
        seqAchats.append("Au lancer # " + str(d) + ", le joueur " + str(i) + " a achete " + case.nom + " (" + case.nomSerie + ")")
        ##change le proprietaire du terrain pour le joueur actif (i)
        case.proprietaire = i
        self.proprietesObjets.append(case)
        self.proprietesAffichables.append(case.nom + " (" + case.nomSerie + ")")
        ##deduit du solde du joueur le prix d'achat
        self.solde = self.solde - case.prixAchat

    def afficheNbrJoueurSerie(self, i, n):
        case = plateau.plateau[self.position]
        ##donne le nombre que possede le joueur dans la serie
        print "Le joueur", i, "possede maintenant", n,
        print "propriete(s) dans cette serie (" + case.nomSerie + ")."

    def afficheNbrVendusSerie(self, x):
        case = plateau.plateau[self.position]
        ##donne le nombre vendus dans la serie
        ######x = plateau.nbrVendusSerie(case)
        print x,
        print "propriete(s) sont maintenant vendue(s) dans cette serie (" + case.nomSerie + ")."

    def afficheNbrVendusPlateau(self, y, z):
        ##donne le nombre vendus sur le plateau
        ######y = plateau.nbrVendusPlateau()
        print y,
        print "propriete(s) vendue(s) sur le plateau",
        print "sur un total de",
        print z, "."

