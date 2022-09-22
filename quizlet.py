#!/usr/bin/env python

import os
import random


def zalozeni():
    if os.path.exists("soubory/"):
        return False
    else:
        os.makedirs("soubory/profile1")
        print("Welcome in Quizlet\n")
        username = input("How is your name: ")
        with open("soubory/profile1/userdata", "w") as soubor:
            soubor.write(username)
        return True
        
        
def vytvoreni_lekce():
    with open("soubory/profile1/seznam_lekci", "a") as soubor:
        nazev = input("\nNew lesson name: ")
        soubor.write(nazev)
    term = []
    definice = []
    while True:
        term1 = input("\nEnter term: ")
        if term1 == "end":
            break
        else:
            definice1 = input("Enter definition: ")
        term.append(term1)
        definice.append(definice1)
    
    with open("soubory/profile1/" + nazev, "a") as soubor:
        for i in range(len(term)):
            soubor.write(term[i]+"\n")
            soubor.write(definice[i]+"\n")        

def lekce_nabidka(lekce_seznam):
    pass
            
 
def main():
    novy = zalozeni()
    if novy == True:
        print("\nStart a new lesson")
        vytvoreni_lekce()   
    while True:
        pass


















main()
