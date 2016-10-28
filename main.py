from sys import exit
import de6
import plateau
import joueurs

##entree du nombre de joueurs par l'usager
nbrJoueurs = joueurs.entrerNbrJoueurs()

##selection du mode d'entree de condition de fin
mode = plateau.modeConditionFin()

##question et validation si choisi mode maximum de proprietes
if mode in ['p', 'P']:
    conditionFin = plateau.entrerConditionFinProprietes()
##question et validation si choisi mode maximum de lancers
else:
    conditionFin = plateau.entrerConditionFinLancers()

##entree de la condition de fin de programme
##conditionFin = plateau.entrerConditionFin()

##cree la liste de joueurs
joueur = [joueurs.joueur() for i in range(nbrJoueurs)]

##compteur de lancers de des
d = 0

##cree une liste vide qui sera populee d'une entree pour chaque achat de propriete (pour rapport final)
seqAchats = []

while True:         #pour revenir au premier joueur apres le tour du dernier joueur

    for i in range(nbrJoueurs):     #prochain joueur

        ##ligne double pour indiquer changement de joueur
        print "======================================================"
        
        ##reinitialise le nombre de doubles du joueur avant le 1e lancer de son nouveau tour
        joueur[i].nbrDoubles = 0

        ## rejouer sera change a False si un double n'est pas roule ou si 3 doubles sont roules
        rejouer = True

        while rejouer:

            ##compteur de lancer de des
            d = d + 1
            print "-----lancer # " + str(d) + "----------"
            
            ##affichage du solde avant le lancer de des
            joueur[i].afficheSolde(i)

            ##Si le joueur est en prison, il paie 50$ et sort.
            if joueur[i].enPrison:
                joueur[i].solde = joueur[i].solde -50
                print "Le joueur", i, "paie 50$ pour sortir de prison"
                joueur[i].enPrison = False

            ##affichage de la position avant le lancer de des
            joueur[i].affichePosition(i)
            
            ##lancer de des et affichage du resultat
            lancer = de6.deuxDes()
            print "Le joueur", i,
            lancer.affiche()

            ##increment du nombre de doubles du joueur
            if lancer.double:
                joueur[i].incrementeDoubles()
            ##si pas un double, ne pas faire rejouer le meme joueur
            else:
                rejouer = False

            ##si 3 doubles, le joueur va en prison
            if joueur[i].nbrDoubles == 3:
                joueur[i].allezEnPrison(i)
                break ##pour que le joueur sorte de la boucle "while rejouer" sans avancer son pion

            ##deplacement du pion
            joueur[i].avance(i, lancer.somme)

            ##raccourci pour le nom de case d'arrivee du joueur
            case = plateau.plateau[joueur[i].position]

            ##case Allez En Prison envoie en prison
            if case == plateau.case30:
                joueur[i].affichePosition(i)
                joueur[i].allezEnPrison(i)


            ##affichage de la position apres le deplacement.
            joueur[i].affichePosition(i)

            ##case Impot
            if case == plateau.case04:
                impot = case.calcImpot(i, joueur[i].solde, joueur[i].proprietesObjets)
                joueur[i].solde = joueur[i].solde - impot
                print "Le joueur", i, "paie", impot, "$ en impot."

            ##case Impot
            if case == plateau.case38:
                joueur[i].solde = joueur[i].solde - 75
                print "Le joueur", i, "paie 75$ en taxe de luxe."

            ##affiche proprietaire de la case et retourne le no du proprietaire.
            try:
                ##prend p comme entier pour no du joueur pas "vacant"
                ##besoin d'un entier pour plus tard quand p sera utilise comme index
                if case.proprietaire <> "vacant":
                    p = int(joueur[i].afficheProprietaire())
                else:
                    p = joueur[i].afficheProprietaire()
            ##si proprietaire ne s'applique pas a la case
            except:
                ##doit attribuer une valeur a p puisque p est utilise plus tard comme argument
                p = None

            ##si case vacante, achat et affichage de donnees sur la distribution des proprietes
            if p == "vacant":
                joueur[i].achat(i, d, seqAchats)
                w = plateau.nbrJoueurSerie(i, case)
                x = plateau.nbrVendusSerie(case)
                y = plateau.nbrVendusPlateau()
                z = plateau.nbrTotalPlateau()
                
                ##met le loyer a jour pour les proprietes du joueur dans cette serie
                for c in case.serie:
                    if c in joueur[i].proprietesObjets:
                        c.loyer = c.calcLoyer(w, lancer.somme)

                joueur[i].afficheNbrJoueurSerie(i, w)
                joueur[i].afficheNbrVendusSerie(x)
                joueur[i].afficheNbrVendusPlateau(y, z)

            ##contrairement a w, n trouve les donnes du proprietaire, non du joueur actif
            n = plateau.nbrJoueurSerie(p, case)

            ##si case appartient a un autre joueur, paiement du loyer
            ##pas de loyer si solde du proprietaire est negatif
            ##autrement dit au lieu de gerer les hypotheques
            ##on desactive tous les terrains du joueur en deficit, sans interet
            try:
                ##si la case appartient deja a un autre joueur
                if p not in [i, "vacant"]:
                    if hasattr(case, "nomSerie"):
                        ##si la case est un service public, met a jour le loyer avec le lancer de des courant
                        if case.nomSerie == "servicePublic":
                            case.loyer = case.calcLoyer(n, lancer.somme)
                    ##paiement du loyer au proprietaire        
                    if joueur[p].solde >= 0:
                        print "\tLe joueur", i, "paye un loyer de", case.loyer,
                        print "$ au joueur", p
                        joueur[i].solde = joueur[i].solde - case.loyer
                        joueur[p].solde = joueur[p].solde + case.loyer
                        joueur[p].afficheSolde(p)
                    ##pas de paiement si proprietaire a un solde < 0
                    else:
                        print "Le proprietaire (joueur", p,
                        print ")est en deficit et ne collecte aucun loyer."
                        
                ##si case appartient au joueur actif (i), pas de loyer a payer
                elif p == i:
                    print "Pas de loyer a payer quand on est a la maison!"
            except:
                pass

                


            ##affichage du solde a la fin du tour
            joueur[i].afficheSolde(i)

            ##condition de terminaison
            if (mode in ['p', 'P'] and plateau.nbrVendusPlateau() == conditionFin) or (mode in ['L', 'l'] and d == conditionFin):
            ##if plateau.nbrVendusPlateau() == conditionFin:
            ##affichage du rapport de fin
                print "**********************************"
                print "condition de terminaison atteinte"
                print "***********************************"
                print "Voici la sequence des achats:"
                ##Affiche tous les achats dans l'ordre chronologique
                for s in seqAchats:
                    print s
                ##Affiche les achats par joueur dans l'ordre chronologique
                for i in range(nbrJoueurs):
                    print "====================================="
                    case = plateau.plateau[joueur[i].position]
                    print "Joueur", i, "a achete ces proprietes (dans l'ordre):"
                    for p in joueur[i].proprietesAffichables:
                        print p
                    print "Joueur", i, "a", joueur[i].solde, "$"
                    print "Joueur", i, "est sur la case", case.nom
                    print "====================================="
                exit()

