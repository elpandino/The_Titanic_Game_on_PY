("")#the_titanic_game_by_mosspands_corporation
#we_hope_you_will_enjoy_this_game!
#licensed_by_mosspands_copyright_2022
import curses
import random
import time
import os
import pickle
import bisect
import sqlite3
import sys
from copy import deepcopy
from random import randint
import sys
print('\u001b[92m'"copyright 2022 to Andrea Pandolfini and Leonardo Muschietti")
print(" ")
print(" ")
print(" ")
print('\u001b[31m''\u001b[4m'"Ti informiamo che dal momento in cui questo codice è sotto la licensa copyright 2022-2023 e Gnu 10.0 non potrai né copiare questo gioco né spacciarlo come un codice tuo; acconsenti dunque alla policy sopra elencata? rispondi con *si* (se accetti) o con *no* (se rifiuti)")
print("\u001b[0m ")
print(" ")
print(" ")
license=input("  ")
if license=="si":
    print("\u001b[0m  ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("       Hai scelto la giusta via, diamo inizio alle danze.")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    primoinvio=input("Premi invio per iniziare...")
else:
    print("'\u001b[0m' ")
    print(" ")
    print("'\u001b[31m'Mi dispiace ma ti è stato proibito di utilizzare il codice e il gioco, (ricordiamo che OpenSource non è uguale a 'il codice è mio') grazie; PROCESSO AUTODISTRUZIONE DEL CODICE ATTIVATO                                                                                                                  BOOM                                    \u001b[93m   ERROR 104")
    exit() 
print("'\u001b[0m' ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("\u001b[1m             il TITANIC ")
print("\u001b[0m ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
secondoinvio=input("Premi invio per continuare... ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("               INIZIO DEL GIOCO")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("                    TRAMA")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("\u001b[107m \u001b[30m \u001b[1m ella primavera del 1912 il TITANIC parte verso terre lontane, ma il protagonista, che è un membro dell'equipaggio, non sa cosa dovrà passare per riuscire a sopravvivere. Per farlo dovrai passare da essere un ragazzo maleducato a un uomo. Riuscirai a scappare sano e salvo?")
print("\u001b[0m ")
print(" ")
print(" ")
tramainvio=input("Premi invio per continuare...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Per prima cosa scegli il nome del protagonista ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
terzoinvio=input(" Premi invio per iniziare la personalizzazione del personaggio...")
#INIZIO_CON_DOMANDE
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
nomeinminuscolo=input(" Dunque qui di fianco digita il nome ------->                ")
nome=nomeinminuscolo.title()
if nome=="Rose":
    print ("Scegli un nome più originale... Nome non consentito arresto del gioco.")
    exit()
if nome=="Jack":
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Sarebbe stato meglio se avessi scelto un nome più originale...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
quartoinvio=input("Premi invio per continuare... ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(nome, "Ci siamo, ti auguriamo buona fortuna...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("1912 ")
print(" ")
print("14 aprile")
print(" ")
print("8:00 a.m.")
print(" ")