import random as rd
import csv, os, pandas as pd

def weapon():
    weapns = ['Guitar', 'Big sword', 'chainsword', 'katana', 'spear', 'playful cloud', 'knife', 'sword', 'kunai', 'boomerang', 'shuriken', 'twinswords', 'whip', 'shield', 'gloves', 'skimitar', 'stick', 'fighting boots', 'shortsword', 'slingshot', 'axe', 'revolver', 'none']
    rollWeapon = rd.choice(weapns)
    return rollWeapon
    

def cursetech(): #cursed technique of each person
    regulartechs= ["Tool manipulation", "Boogie woogie", "7:3", "Sound Amplification", "Puppet manipulation", "Inverse", "Black Bird Manipulation", "Wound stopping", "Contractual Recreation", "Body Detonation", "Left hand claws", "Scorpion hair", "Discharge", "Idle Death Gamble", "Solo Forbidden Area", "Heart Catch", "Prayer Song", ]
    strongtechs=["Curse manipulation", "Limitless", "Ten shadows", "Projection sorcery", "Shrine", "Blood Manipulation", "Copy", "Cursed speech", "Construction", "Idle Transfiguration", "Fire Manipulation", "Immortality", "Cloning", "Beast Summon", "Water Manipulation", "Doll Manipulation", "Ice Formation", "Blazing Courage", "Glaze Pressure", "Love Rendezvous", "Death Court", "Comedian", "Sky Manipulation", "Star rage", "Antigravity System", "Technique Estinguishment", "Mythical Beast Amber", ]
    rollTech = rd.randint(1, 100)
    regchoiceTech=rd.choice(regulartechs)
    strongchoiceTech=rd.choice(strongtechs)
    if rollTech >= 30:
        return strongchoiceTech
    else: return regchoiceTech
