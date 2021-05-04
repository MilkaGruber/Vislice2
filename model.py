import random


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke): #konstruktor nastavi vrednosti spremenljivk
        self.geslo = geslo
        self.crke = crke[:] #ne more biti preprosto crke, ker se bo to tekom izvajanja programa zadeva spreminjala, zato naredimo kopijo

    def napacne_crke(self):
        napacne_crke = []
        for x in self.crke:
            if x not in self.geslo:
                napacne_crke.append(x)
        return napacne_crke

    def pravilne_crke(self):
        pravilne_crke = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne_crke.append(crka)
        return pravilne_crke

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        if self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK:
            return False
        else:
            for crka in self.geslo:
                if crka in self.pravilne_crke():
                    pass
                else:
                    vse_crke = False
                    break
            return vse_crke

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()
        
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka + ' '
            else:
                niz += '_ '
        return niz[:-1]

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.crke:
            if crka in self.geslo:
                pass
            else:
                niz += crka + ' '
        return niz[:-1]

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo: #če je črka prava, je lahko že zmaga, lahko pa ne 
            self.crke += crka
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke += crka
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

#testno_geslo = 'DEŽUJE'
#testne_crke = ['A', 'I', 'O', 'U', 'D', 'J', 'K']
#igra = Igra(testno_geslo, testne_crke)

with open('besede.txt', 'r') as f: #to kar tu napišemo je odvisno od tega od kod poganjamo naš program
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]


def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, '')






