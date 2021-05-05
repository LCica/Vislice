STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'

ZACETEK = "S"

ZMAGA, PORAZ = 'W', 'X'


class Vislice:
    def __init__(self):
        self.igre = {}
        self.max_id = 0

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

    """ Druga možnost
        def prost_id_igre_drugace(self):
            if not self.igre: return 0
            m = max(self.igre.keys())
            return m + 1
    """
    def nova_igra(self):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra(bazen_besed)

        self.igre[nov_id] = (sveza_igra, ZACETEK)
        
        return nov_id
    
    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)


    
    



class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo
        self.crke = crke
    def napacne_crke(self):
        return [c for c in self.crke if c.upper() not in self.geslo.upper()]

    def pravilne_crke(self):  
        return [c for c in self.crke if c.upper() in self.geslo.upper()]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK 

    def zmaga(self):
        return not self.poraz() and len(set(self.pravilne_crke())) == len(set(self.geslo))
    
    def pravilni_del_gesla(self):
        novo = ''
        for x in self.geslo:
            if x.upper() in self.crke:
                novo += x
            else:
                novo += '_'
        return novo
        #return ''.join([c if c in self.crke else '_' for c in self.geslo.upper()])#
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
        
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

with open('besede.txt', encoding="utf-8") as f:
    bazen_besed = f.read().split()

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)