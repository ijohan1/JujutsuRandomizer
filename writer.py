import random as rd
import csv, os 
import naming, other, weaponry, writer
import json

def student():#генерує список студентів, для кожного з яких задаються стати
    sex = naming.statb()
    studnt = {
    "sex": sex, 
    "name": naming.name(sex),
    "year of school": other.year(),
    "cursed energy amount": other.cursenergy(),
    "weapon": weaponry.weapon(),
    "cursed technique": weaponry.cursetech()  }
    
    return studnt

def generator():
    global studentlist
    studentlist = []
    amount = rd.randint(5, 30)
    for _ in range(amount): studentlist.append(student())
    return studentlist

def writing(): #write in .json file
    global studentlist

    base = os.path.dirname(os.path.abspath(__file__))
    datdir = os.path.join(base, "data")
    os.makedirs(datdir, exist_ok = True)

    file = os.path.join(datdir, "students.json")

    with open(file, "w", encoding="utf-8") as f:
        json.dump(studentlist, f, indent=4, ensure_ascii=False)
    
