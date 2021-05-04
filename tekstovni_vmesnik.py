import model

PONOVNI_ZAGON = 'p'
IZHOD = 'i'

def stopnja_obesenosti(igra):
    stopnje_obesenosti = [
"""
""",
"""
       
       
       
       
       
      _______ 
""", 
"""
       
       |   
       |   
       | 
       |  
      _|______ 
""", 
"""
       _____
       |   
       |   
       |  
       |  
      _|______ 
""", 
"""
       _____
       |   |
       |   
       |  
       |  
      _|______ 
""", 
"""
       _____
       |   |
       |   o
       |  
       |  
      _|______ 
""", 
"""
       _____
       |   |
       |   o
       |   |
       |  
      _|______ 
""", 
"""
       _____
       |   |
       |   o
       |  /|
       |  
      _|______ 
""", 
"""
       _____
       |   |
       |   o
       |  /|\\
       |  
      _|______ 
""", 
"""
       _____
       |   |
       |   o
       |  /|\\
       |  / 
      _|______ 
""", 
"""
       _____
       |   |
       |   o
       |  /|\\
       |  / \\
      _|______ 
"""
]
    stopnja = igra.stevilo_napak()
    return stopnje_obesenosti[stopnja]

def izpis_igre(igra):
    tekst = f"""###################################\n
    IGRAJMO! {igra.pravilni_del_gesla()}\n
    {stopnja_obesenosti(igra)}\n
    Nepravilne crke: {igra.nepravilni_ugibi()}\n
###################################
    """ 
    return tekst

testna_igra = model.nova_igra()
print(izpis_igre(testna_igra))

def izpis_zmage(igra):
    tekst = f"""###################################\n
    ČESTITKE!!!\n
    PRAVILNO STE UGANILI GESLO *** {igra.pravilni_del_gesla()} ***\n
###################################
    """ 
    return tekst

def izpis_poraza(igra):
    tekst = f"""###################################\n
    ŽAL STE PORABILI VSE POSKUSE.\n
    ODGOVOR JE BIL *** {igra.geslo} ***\n
###################################
    """ 
    return tekst



def zahtevaj_vnos():
    return input('Vnesite črko:')

def zahtevaj_moznost():
    return input('Vnesite možnost')

def ponudi_moznosti():
    tekst = f"""Vpišite črko za izbor naslednjih možnosti:\n
    {PONOVNI_ZAGON}: ponovni zagon igre\n
    {IZHOD}: izhod\n
    """
    return tekst

def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = model.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD
    

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.ZMAGA:
            print(izpis_zmage(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        else:
            print(izpis_igre(igra))

pozeni_vmesnik()


