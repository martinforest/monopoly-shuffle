################################  Ver3  ########################
import random

class deuxDes(object):

    def __init__(self):
        '''
        Roulement des deux des
        double == 1 si un double est obtenu, sinon double == 0
        '''
        self.de1 = random.randint(1,6)
        self.de2 = random.randint(1,6)
        self.somme = self.de1 + self.de2
        self.double = int(not(self.de1-self.de2)) # ==1 si double

    def affiche(self):
        '''
        affichage du resultat
        '''
        print "a lance un",
        if self.double == 1:
            print "double! Un",
        print self.de1,
        print "et un",
        print self.de2,
        print ". Total:",
        print self.somme

#pour tester
##lancer1 = deuxDes()
##lancer1.affiche()
