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
        soubor.write(nazev + "\n")
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
    os.system("clear")       


def lekce_nabidka():
    with open("soubory/profile1/seznam_lekci", "r") as soubor:
        os.system("clear")  
        print("Lesson:\n")
        text = soubor.read()
        text = text.split("\n")[:-1]
        for i in range(len(text)):
            print(i + 1, "-", text[i])
        print(i + 2, "-", "Create new lesson")
        
        
def provedeni_prikazu(vyber_prikazu, vyber_lekce, text):
    if vyber_prikazu == 1:
        cviceni(vyber_lekce, text)
    elif vyber_prikazu == 2:
        edit(vyber_lekce, text)
    elif vyber_prikazu == 3:
        delete(vyber_lekce, text)
    else:
        pass
        

def edit(vyber_lekce, lekce):
    with open("soubory/profile1/" + lekce[vyber_lekce - 1], "r") as soubor:
        text = soubor.read()
        text = text.split("\n")[:-1]
    opakovani = 0
    karty = []
    karta = []
    for i in text:
        karta.append(i)
        opakovani += 1
        if opakovani == 2:
            karty.append(karta)
            karta = []
            opakovani = 0
    os.system("clear")
    for i in range(len(karty)):
        print(i + 1, "- Term: " + karty[i][0])
        print("    Definition: " + karty[i][-1])
    while True:    
        vyber_karty = input("\nNumber of card: ")
        if vyber_karty == "end":
            break 
        else:
            term1 = input("\nEnter term: ")
            if term1 == "":
                del karty[int(vyber_karty)-1]
            else:
                definice1 = input("Enter definition: ")
                karty[int(vyber_karty)-1][0] = term1
                karty[int(vyber_karty)-1][-1] = definice1
        with open("soubory/profile1/" + lekce[vyber_lekce - 1], "w") as soubor:
            for i in range(len(karty)):
                soubor.write(karty[i][0]+"\n")
                soubor.write(karty[i][-1]+"\n")   
    
    
def delete(vyber_lekce, text):
    pass 


def cviceni(vyber_lekce, text):
    with open("soubory/profile1/" + text[vyber_lekce - 1], "r") as soubor:
        text = soubor.read()
        text = text.split("\n")[:-1] 
    opakovani = 0
    karty = []
    karta = []
    for i in text:
        karta.append(i)
        opakovani += 1
        if opakovani == 2:
            karty.append(karta)
            karta = []
            opakovani = 0
    random.shuffle(karty)
    os.system("clear")
    
    opakovani = 0
    while len(karty) != 0:
        print("Term:", karty[0][-1])
        definice = input("Definice: ")
        if definice == karty[0][0]:
            print("Correct")
            karty.remove(karty[0])
            os.system("clear")  
        else:
            print("Wrong --", karty[0][0])
            karty.append(karty[0])
            karty.remove(karty[0])
            input()
            os.system("clear")
      
    
def main():
    novy = zalozeni()
    if novy == True:
        print("\nStart a new lesson")
        vytvoreni_lekce()   
    while True:
        lekce_nabidka()
        vyber_lekce = int(input("Number of lesson: "))
        with open("soubory/profile1/seznam_lekci", "r") as soubor:
            text = soubor.read()
            text = text.split("\n")[:-1]
        if vyber_lekce == len(text) + 1:
            vytvoreni_lekce()
        else:
            os.system("clear")    
            print("Lesson", text[vyber_lekce-1] + ":\n")
            print("1 - Exercise lesson")
            print("2 - Edit lesson")
            print("3 - Delete lesson")
            vyber_prikazu = int(input("Number of operation: "))
            provedeni_prikazu(vyber_prikazu, vyber_lekce, text)

main()
