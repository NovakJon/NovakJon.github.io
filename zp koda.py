import random
import turtle
import time

t = turtle.Turtle()
Mpalice = 0
Ppalice = 0
a = 0
a_pomoc = 0
stopnje = []
vrednosti_stopenj = []
aREV = (len(stopnje)) + 1
b = 0
c = 0
ciklicni_x = 0
ciklicni_x_2 = 0
ciklicni_x_3 = 0
ciklicni_x_4 = 0
ciklicni_x_5 = 0
ciklicni_x_6 = 0
ciklicni_x_7 = 0
ciklicni_x_8 = 0
ciklicni_x_9 = 0
ciklicni_x_10 = 0
konec = 0
h = 0
n = 0
najvecja_liha_stopnja = 0
nakljucno_stevilo_palic = 0
nenicelna_dolzina_stopenj = 0
pomoc_2 = 0
pomoc_3 = 0
random_poteza_palce = 0
random_poteza_skatle = 0
signal = 0
signal_2 = 0
signal_3 = 0
signal_4 = 0
signal_5 = 0
signal_6 = 0
skatla_za_zmanjsevanje = 0
stevilo_palic_za_brisanje = 0
stpalic = 0
stskatel = 0
tezavnost = 0
x = 0
xREV = (len(vrednosti_stopenj)) + 1
y = 0
zmagovalec = 0
prazne_skatle = []
skatle = []
skatle_z_liho_stopnjo = []
skatle_za_racunanje = []
stopnje_skatle_za_zmanjsevanje = []
screen = turtle.Screen()
# this assures that the size of the screen will always be 400x400 ...
screen.setup(900, 525)


def check_input(r):
        if r.isdigit() != True:
            while r.isdigit() != True:
                r=(input("Mislim, da si se zatipkal, poizkusi ponovno."))
        return(int(r))


def nastavitve_igre_in_start_2():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    stskatel = input("S koliko skatlami zelis igrati?")
    stskatel = check_input(stskatel)
    while not (3 <= stskatel <= 9):
        print("Izberes lahko od 3 do 9 skatel.")
        stskatel = input("S koliko skatlami zelis igrati?")
        stskatel = check_input(stskatel)
    stpalic = input("Do koliko palic zelis na skatlo?")
    stpalic = check_input(stpalic)
    while not (6 <= stpalic <= 31):
        print("Izberes lahko od 6 do 31 palic na skatlo.")
        stpalic = input("Do koliko palic zelis na skatlo?")
        stpalic = check_input(stpalic)
    Ppalice = stpalic
    Mpalice = 1
    t.goto(400, -400)  # OOOOOOOOOOOOO
    #globals().update(locals())


def risanje_palic():
    objavi_risanje_palic()
    #globals().update(locals())


def generacija_stopenjskih_spremenljivk():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    x = 0
    skatle_z_liho_stopnjo=[]#dodano 24.2. - bugfix
#     print("PODATKI skatle_za_racunanje",skatle_za_racunanje)#koment
#     print("PODATKI stopnje",stopnje)#koment
#     print("PODATKI najvecja_liha_stopnja",najvecja_liha_stopnja)#koment
#     print("PODATKI signal=",signal)#koment
    for i in range(len(skatle)):
        x += 1
        xREV = (len(vrednosti_stopenj)) + 1
        while not skatle_za_racunanje[(x) - 1] == 0:
#             print(skatle_za_racunanje)#koment
#             print(x,xREV,vrednosti_stopenj)#koment
            xREV -= 1
            if skatle_za_racunanje[(x) - 1] - vrednosti_stopenj[(xREV) - 1] >= 0:
                stopnje[(xREV) - 1] += 1
                skatle_za_racunanje[(x) - 1] = (skatle_za_racunanje[(x) - 1] - vrednosti_stopenj[(xREV) - 1])
                if signal == 1:
                    if xREV == najvecja_liha_stopnja:
                        skatle_z_liho_stopnjo.append(skatle[(x) - 1])
#                         print("VMESNI PODATKI skatle_z_liho_stopnjo",skatle_z_liho_stopnjo)#koment
#                         print("VMESNI PODATKI skatle_za_racunanje",skatle_za_racunanje)#koment
#                         print("VMESNI PODATKI x,xREV,vrednosti_stopenj",x,xREV,vrednosti_stopenj)#koment
#     print("ZGENERIRANE skatle_z_liho_stopnjo",skatle_z_liho_stopnjo)#koment
    #globals().update(locals())
                        

def poteza_igralca():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    barva = 0
    #t.goto(-200,-80)# OOOOOOOOOOOOO
    skatla_za_zmanjsevanje = input("Iz katere skatle zelis vzeti palice? (napisi le stevilko od zgoraj navzdol)")
    skatla_za_zmanjsevanje = check_input(skatla_za_zmanjsevanje)
    if (len(skatle)) < skatla_za_zmanjsevanje:
        while not (len(skatle)) >= skatla_za_zmanjsevanje:
            skatla_za_zmanjsevanje = input("Mislim, da si se zatipkal, poizkusi ponovno.")
            skatla_za_zmanjsevanje = check_input(skatla_za_zmanjsevanje)
    if skatle[(skatla_za_zmanjsevanje) - 1] == 0:
        while not skatle[(skatla_za_zmanjsevanje) - 1] > 0:
            skatla_za_zmanjsevanje = input("Ta skatla je ze prazna izberi drugo.")
            skatla_za_zmanjsevanje = check_input(skatla_za_zmanjsevanje)
            if (len(skatle)) < skatla_za_zmanjsevanje:
                while not (len(skatle)) >= skatla_za_zmanjsevanje:
                    skatla_za_zmanjsevanje = input("Mislim, da si se zatipkal, poizkusi ponovno.")
                    skatla_za_zmanjsevanje = check_input(skatla_za_zmanjsevanje)

    stevilo_palic_za_brisanje = input("Koliko palic zelis vzeti?")
    #print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"a")#koment
    stevilo_palic_za_brisanje = check_input(stevilo_palic_za_brisanje)
    if stevilo_palic_za_brisanje > skatle[(skatla_za_zmanjsevanje) - 1]:
        while not stevilo_palic_za_brisanje <= skatle[(skatla_za_zmanjsevanje) - 1] and stevilo_palic_za_brisanje != 0:
            stevilo_palic_za_brisanje = input("V tej skatli ni toliko palic.")
            stevilo_palic_za_brisanje = check_input(stevilo_palic_za_brisanje)
    
    #t.goto(400,-400)# OOOOOOOOOOOOO
    objavi_brisanje()  # OOOOOOOOOOOOO
    zmagovalec = 1
    #globals().update(locals())
    #print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"b")#koment


def vse_skatle_prazne():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    signal_5 = 0
    ciklicni_x_9 = 0
    for i in range(len(skatle)):
        ciklicni_x_9 += 1
        if not skatle[(ciklicni_x_9) - 1] == 0:
            signal_5 = 1
    if signal_5 == 0:
        konec = 1
    #globals().update(locals())


def random_poteza():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    odstranitev_nic_skatel()
    barva = 1
    signal_2 = 0
    #print("tle")#koment
    random_poteza_skatle = random.randint(1, (len(skatle)))
    if (len(prazne_skatle)) > 0:
        while not signal_2 == 1:
            random_poteza_skatle = random.randint(1, (len(skatle)))
            signal_4 = 0
            ciklicni_x_7 = 0
            for i in range(len(prazne_skatle)):
                ciklicni_x_7 += 1
                if random_poteza_skatle == prazne_skatle[(ciklicni_x_7) - 1]:
                    signal_4 = 1
            if signal_4 == 0:
                signal_2 = 1
                #print(random_poteza_skatle)#koment
    #print("tle2")#koment
    #print(random_poteza_skatle, skatle[(random_poteza_skatle)-1], (len(skatle)))#koment
    if skatle[(random_poteza_skatle) - 1] == 1:
        random_poteza_palce = 1
    else:
        random_poteza_palce = random.randint(1, skatle[(random_poteza_skatle) - 1])
    pomoc_3 = 0
    signal_6 = 0
    ciklicni_x_10 = 0
    for i in range(len(skatle)):
        ciklicni_x_10 += 1
        if skatle[(ciklicni_x_10) - 1] == 0:
            signal_6 += 1
        else:
            pomoc_3 = skatle[(ciklicni_x_10) - 1]
    if (len(skatle)) - signal_6 == 1:
        random_poteza_palce = pomoc_3
    skatla_za_zmanjsevanje = random_poteza_skatle
    stevilo_palic_za_brisanje = random_poteza_palce
    #print(skatla_za_zmanjsevanje)#koment
    #print(stevilo_palic_za_brisanje)#koment
    objavi_brisanje()  # OOOOOOOOOOOOO
    zmagovalec = 0
    #globals().update(locals())


def odstranitev_nic_skatel():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    ciklicni_x_6 = 0
    for i in range(len(skatle)):
        ciklicni_x_6 += 1
        if skatle[(ciklicni_x_6) - 1] == 0:
            ciklicni_x_8 = 0
            signal_3 = 0
            for i in range(len(prazne_skatle)):
                ciklicni_x_8 += 1
                if ciklicni_x_6 == prazne_skatle[(ciklicni_x_8) - 1]:
                    signal_3 = 1
            if signal_3 == 0:
                prazne_skatle.append(ciklicni_x_6)
            if (len(prazne_skatle)) == 0:
                prazne_skatle.append(ciklicni_x_6)
    #print(skatle,prazne_skatle)#koment
    #globals().update(locals())


def racunalniska_poteza():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    barva = 1
    signal = 0
    refresh_stopnje_stopnje_za_zmanjsevanje()
    polnjenje_skatel_za_racunanje()
#     print("PRVI PODATEK signal=",signal)#koment
    generacija_stopenjskih_spremenljivk()
    h = 0
    najvecja_liha_stopnja = 0
    ciklicni_x = (len(stopnje))
    aREV = (len(stopnje)) + 1
    while not ciklicni_x == 0:
        ciklicni_x -= 1
        aREV -= 1
        if stopnje[(aREV) - 1] % 2 > 0:
            najvecja_liha_stopnja = aREV
            ciklicni_x = 0
            h = 1
    if h == 0:
        random_poteza()
    else:
        signal = 1
        refresh_stopnje_stopnje_za_zmanjsevanje()
        polnjenje_skatel_za_racunanje()
        generacija_stopenjskih_spremenljivk()
        dolocanje_najvecjega_stevila_z_liho_stopnjo()
        dolocanje_skatle_za_zmanjsevanje()
        izracun_skatel_z_liho_stopnjo()
        izracunanje_stevila_ki_ga_zmanjsa_racunalnik()
        #print(skatla_za_zmanjsevanje)#koment
        objavi_brisanje()
    zmagovalec = 0
#     print(skatle)#koment
#     print("brise skatle =",skatla_za_zmanjsevanje,"  brise palce =",stevilo_palic_za_brisanje)#koment
#     if stevilo_palic_za_brisanje <= 0:#koment
#         print("negativno")#koment
    #globals().update(locals())


def refresh_stopnje_stopnje_za_zmanjsevanje():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    ciklicni_x_4 = (len(stopnje))
    for i in range(len(stopnje)):
        ciklicni_x_4 -= 1
        if not stopnje[(ciklicni_x_4) - 1] == 0:
            stopnje_skatle_za_zmanjsevanje[(ciklicni_x_4) - 1] = 0
            stopnje[(ciklicni_x_4) - 1] = 0
    #globals().update(locals())


def polnjenje_skatel_za_racunanje():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    y = 0
    for i in range(len(skatle)):
        y += 1
        skatle_za_racunanje[(y) - 1] = skatle[(y) - 1]
    #globals().update(locals())


def dolocanje_najvecjega_stevila_z_liho_stopnjo():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
#     print("skatle_z_liho_stopnjo",skatle_z_liho_stopnjo)#koment
    while not (len(skatle_z_liho_stopnjo)) == 1:
        if skatle_z_liho_stopnjo[0] > skatle_z_liho_stopnjo[1]:
            del skatle_z_liho_stopnjo[1]
        else:
            del skatle_z_liho_stopnjo[0]
#     print("skatle_z_liho_stopnjo",skatle_z_liho_stopnjo)#koment
    #globals().update(locals())


def dolocanje_skatle_za_zmanjsevanje():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    ciklicni_x_5 = 0
    if (len(skatle)) == 1:# se nikoli ne izvede ker se praznih skatelj ne brise
        skatla_za_zmanjsevanje = 1
#         print("preverjam # se nikoli ne izvede ker se praznih skatelj ne brise####")#koment
    else:
        for i in range(len(skatle)):
            ciklicni_x_5 += 1
            if skatle[(ciklicni_x_5) - 1] == skatle_z_liho_stopnjo[0]:
                skatla_za_zmanjsevanje = ciklicni_x_5
#         print("skatle_z_liho_stopnjo",skatle_z_liho_stopnjo)#koment
#         print("skatle",skatle)#koment
    #globals().update(locals())
    #print(skatla_za_zmanjsevanje)#koment


def izracun_skatel_z_liho_stopnjo():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    pomoc_2 = skatle_z_liho_stopnjo[0]
    xREV = (len(vrednosti_stopenj)) + 1
#     print("PREJ stopnje_skatle_za_zmanjsevanje=",stopnje_skatle_za_zmanjsevanje)#koment
#     print("PREJ skatle_z_liho_stopnjo=",skatle_z_liho_stopnjo)#koment
    while not xREV == 0:
        xREV -= 1
        if (skatle_z_liho_stopnjo[0] - vrednosti_stopenj[(xREV) - 1]) >= 0:
            stopnje_skatle_za_zmanjsevanje[(xREV) - 1] += 1
            skatle_z_liho_stopnjo[0] = skatle_z_liho_stopnjo[0] - vrednosti_stopenj[(xREV) - 1]
#     print("stopnje_skatle_za_zmanjsevanje=",stopnje_skatle_za_zmanjsevanje)#koment
#     print("skatle_z_liho_stopnjo=",skatle_z_liho_stopnjo)#koment
    #globals().update(locals())


def izracunanje_stevila_ki_ga_zmanjsa_racunalnik():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    b = 0
    if (len(skatle)) == 1:
        stevilo_palic_za_brisanje = skatle[0]
        skatla_za_zmanjsevanje = 1
    else:
        while not b == (len(stopnje_skatle_za_zmanjsevanje)):
#             print("skatle=",skatle)#koment
#             print("stopnje=",stopnje)#koment
#             print("stopnje_skatle_za_zmanjsevanje=",stopnje_skatle_za_zmanjsevanje)#koment
#             print("skatle_z_liho_stopnjo=",skatle_z_liho_stopnjo)#koment
            b += 1
            if stopnje[(b) - 1] > 0:
                if stopnje[(b) - 1] % 2 == 0:
                    if stopnje_skatle_za_zmanjsevanje[(b) - 1] == 1:
                        skatle_z_liho_stopnjo[0] = skatle_z_liho_stopnjo[0] + vrednosti_stopenj[(b) - 1]
                else:
                    if stopnje_skatle_za_zmanjsevanje[(b) - 1] == 0:
                        skatle_z_liho_stopnjo[0] = skatle_z_liho_stopnjo[0] + vrednosti_stopenj[(b) - 1]
            stevilo_palic_za_brisanje = pomoc_2 - skatle_z_liho_stopnjo[0]
#     print("skatle=",skatle)#koment
#     print("stopnje=",stopnje)#koment
#     print("stopnje_skatle_za_zmanjsevanje=",stopnje_skatle_za_zmanjsevanje)#koment
#     print("skatle_z_liho_stopnjo=",skatle_z_liho_stopnjo)#koment
    #print("vrednosti_stopenj=",vrednosti_stopenj)#koment
#     print("pomoc_2=",pomoc_2)#koment
#     print("stevilo_palic_za_brisanje=",stevilo_palic_za_brisanje)#koment
    #globals().update(locals())


def tezavnost_igre():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    screen.bgpic('backdrop5.1.png')
    screen.update()
    #print("Klikni v to polje.")#koment
    tezavnost = input("Klikni v to polje in izberi tezavnost igre.")
    tezavnost = check_input(tezavnost)
    while not 0 < tezavnost < 4:
        tezavnost = input("Ta tezavnost ni mogoca.")
        tezavnost = check_input(tezavnost)
    #globals().update(locals())


def generiranje_vrednosti_stopenj():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    a_sen_pac = 0
    #vrednosti_stopenj=[]#koment
    #stopnje=[]#koment
    #stopnje_skatle_za_zmanjsevanje=[]#koment
    for i in range(9):
        vrednosti_stopenj.append(2**a_sen_pac)
        a_sen_pac += 1
        stopnje.append(0)
        stopnje_skatle_za_zmanjsevanje.append(0)
        #print(vrednosti_stopenj)#koment
    #globals().update(locals())


#OPOMNIK: zacasno izklojucen blok
def length_stopenj_brez_nic():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    nenicelna_dolzina_stopenj = 0
    ciklicni_x_2 = (len(stopnje))
    while not ciklicni_x_2 == 0:
        ciklicni_x_2 -= 1
        if stopnje[(ciklicni_x_2) - 1] > 0:
            nenicelna_dolzina_stopenj = ciklicni_x_2
            ciklicni_x_2 = 0
    #globals().update(locals())


def objavi_start():
    t.hideturtle()
    t.penup()
    #t.goto(-300,300) #koment
    #globals().update(locals())


def objavi_izbrisi_svincnik():
    t.clear()
    #globals().update(locals())


def zp():
    t.pendown()
    t.pensize(6)
    t.color("gold")
    t.hideturtle()
    t.setheading(90)
    t.speed(2)
    t.forward(20)
    t.speed(0)
    t.penup()
    #globals().update(locals())


def objavi_risanje_palic():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    n = 0
    for i in range(stskatel):
        t.goto(-350, (165 - (37 * n)))
        n += 1
        nakljucno_stevilo_palic = 0
        #print(Mpalice)#koment
        #Mpalice=1#koment
        nakljucno_stevilo_palic = random.randint(Mpalice, Ppalice)
        for i in range(nakljucno_stevilo_palic):
            t.speed(0)
            t.penup()
            t.setheading(0)
            t.forward(20)
            t.setheading(270)
            t.forward(20)
            #             print("n je ",n)
            #             print(t.xcor())#koment
            #             print(t.ycor())#koment
            zp()
#         print("samo risem")#koment
        skatle.append(nakljucno_stevilo_palic)
        skatle_za_racunanje.append(nakljucno_stevilo_palic)
    #globals().update(locals())


def objavi_brisanje():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    if barva == 1:
        #print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"c",barva)#koment
        t.goto((-330 + (20 * (skatle[(skatla_za_zmanjsevanje) - 1]))),
               (156 - (37 * (skatla_za_zmanjsevanje - 1))))
        #         print(t.xcor())#koment
        #         print(t.ycor())#koment
        for i in range(stevilo_palic_za_brisanje):
            t.speed(0)
            t.setheading(180)
            t.forward(20)
            sprite1()
            #t.goto(-300,300)
        #print("preden zbrise rac =",stevilo_palic_za_brisanje,skatle)
        skatle[(skatla_za_zmanjsevanje) - 1] = (skatle[(skatla_za_zmanjsevanje) - 1] - stevilo_palic_za_brisanje)
    else:
        druga_figura()
    #globals().update(locals())


def druga_figura():
    global stopnje_skatle_z_liho_stopnjo, barva, Mpalice, Ppalice, a, a_pomoc, stopnje, vrednosti_stopenj, aREV, b, c, ciklicni_x, ciklicni_x_2, ciklicni_x_3, ciklicni_x_4, ciklicni_x_5, ciklicni_x_6, ciklicni_x_7ciklicni_x_9, ciklicni_x_10, konec, n, najvecja_liha_stopnja, nakljucno_stevilo_palic, nenicelna_dolzina_stopenj, pomoc_2, pomoc_3, random_poteza_palce, random_poteza_skatle, signal, signal_2, signal_3, signal_4, signal_5, signal_6, skatla_za_zmanjsevanje, stevilo_palic_za_brisanje, stpalic, stskatel, tezavnost, x, xREV, y, zmagovalec, prazne_skatle, skatle, skatle_z_liho_stopnjo, skatle_za_racunanje, stopnje_skatle_za_zmanjsevanje, ciklicni_x_11, posebnost_1, posebnost_2, signal_7, lovro_1
    t.goto((-330 + (20 * (skatle[(skatla_za_zmanjsevanje) - 1]))),
           (156 - (37 * (skatla_za_zmanjsevanje - 1))))
    #     print(skatle[(skatla_za_zmanjsevanje)-1],skatla_za_zmanjsevanje)#koment
    for i in range(stevilo_palic_za_brisanje):
        #         print(t.xcor())#koment
        #         print(t.ycor())#koment
        #         print(stevilo_palic_za_brisanje,skatla_za_zmanjsevanje,skatle,"d")#koment
        t.speed(0)
        t.setheading(180)
        t.forward(20)
        sprite2()
    #print("preden zbrise igralec =",stevilo_palic_za_brisanje,skatle)
    skatle[(skatla_za_zmanjsevanje) - 1] = (skatle[(skatla_za_zmanjsevanje) - 1] - stevilo_palic_za_brisanje)
    #globals().update(locals())


def sprite1():
    t.pendown()
    t.pensize(5)
    t.hideturtle()
    t.color("blue")
    t.penup()
    t.setheading(135)
    t.forward(4)
    t.pendown()
    t.setheading(315)
    t.speed(1)
    t.forward(8)
    t.speed(0)
    t.setheading(135)
    t.forward(4)
    t.setheading(180)
    t.penup()
    #globals().update(locals())


def sprite2():
    t.pendown()
    t.pensize(5)
    t.hideturtle()
    t.color("green")
    t.penup()
    t.setheading(45)
    t.forward(4)
    t.pendown()
    t.setheading(225)
    t.speed(1)
    t.forward(8)
    t.speed(0)
    t.setheading(45)
    t.forward(4)
    t.setheading(180)
    t.penup()
    #globals().update(locals())


objavi_izbrisi_svincnik()  # OOOOOOOOOOOOO
generiranje_vrednosti_stopenj()
ciklicni_x_11 = 0
posebnost_1 = 0
posebnost_2 = 0
signal_7 = 0
lovro_1 = 0
#globals().update(locals())


objavi_start()  # OOOOOOOOOOOOO
# start()
t.hideturtle()
screen = turtle.Screen()
t.speed(0)
t.penup()
#t.goto(400,-400)# OOOOOOOOOOOOO #koment
screen.bgpic('backdrop1.1.png')
screen.update()
time.sleep(2)
screen.bgpic('backdrop8.1.png')
screen.update()
#t.goto(-200,-80)# OOOOOOOOOOOOO #koment
tezavnost_igre()
#t.goto(400,-400)# OOOOOOOOOOOOO #koment
screen.bgpic('backdrop4.1.png')
screen.update()
lovro_1 = str(input("Napisi navodila ali pa pritisni le enter."))
if lovro_1.lower() == "navodila":
    t.goto(-327, -80)  # OOOOOOOOOOOOO
    screen.bgpic('backdrop9.1.png')
    screen.update()
    print("Dobro preberi navodila.")
    time.sleep(15)
screen.bgpic('backdrop10.1.png')
screen.update()
#t.goto(400,-400)# OOOOOOOOOOOOO #koment
nastavitve_igre_in_start_2()
screen.bgpic('backdrop8.1.png')
risanje_palic()
#print(vrednosti_stopenj)#koment
generacija_stopenjskih_spremenljivk()
if tezavnost == 1:
    while not konec == 1:
        if konec == 0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        if konec == 0:
            random_poteza()
            time.sleep(1)
            vse_skatle_prazne()
if tezavnost == 2:
    while not konec == 1:
        if konec == 0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        if konec == 0:
            racunalniska_poteza()
            time.sleep(1)
            vse_skatle_prazne()
        if konec == 0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        time.sleep(2)
        if konec == 0:
            random_poteza()
            time.sleep(1)
            vse_skatle_prazne()
if tezavnost == 3:
    while not konec == 1:
        if konec == 0:
            poteza_igralca()
            time.sleep(1)
            vse_skatle_prazne()
        if konec == 0:
            racunalniska_poteza()
            time.sleep(1)
            vse_skatle_prazne()
objavi_izbrisi_svincnik()  # OOOOOOOOOOOOO
objavi_start()
t.goto(400, -400)  # OOOOOOOOOOOOO
t.clear()
if zmagovalec == 1:
    if tezavnost == 1:
        screen.bgpic('backdrop2.1.png')
        screen.update()
    if tezavnost == 2:
        screen.bgpic('backdrop7.1.png')
        screen.update()
    if tezavnost == 3:
        screen.bgpic('backdrop6.1.png')
        screen.update()
else:
    screen.bgpic('backdrop3.1.png')
    screen.update()
