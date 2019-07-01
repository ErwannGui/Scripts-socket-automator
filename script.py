from datetime import datetime
import random
import json

# on ecrase la totalité du contenu du fichier
myFile = open('data.json', 'w').close()


def getRandomNumber(start, stop):
    return random.uniform(start, stop)


# on génère 5 mesures random
temp_int = [getRandomNumber(2.5, 4), getRandomNumber(2.5, 4), getRandomNumber(2.5, 4), getRandomNumber(2.5, 4), getRandomNumber(2.5, 4)]
temp_ext = [getRandomNumber(8, 14), getRandomNumber(8, 14), getRandomNumber(8, 14), getRandomNumber(8, 14), getRandomNumber(8, 14)]
weight_milk = [getRandomNumber(3512, 4607), getRandomNumber(3512, 4607), getRandomNumber(3512, 4607), getRandomNumber(3512, 4607), getRandomNumber(3512, 4607)]
weight_product = [getRandomNumber(0, 1095), getRandomNumber(0, 1095), getRandomNumber(0, 1095), getRandomNumber(0, 1095), getRandomNumber(0, 1095)]
ph = [getRandomNumber(6.8, 7.2), getRandomNumber(6.8, 7.2), getRandomNumber(6.8, 7.2), getRandomNumber(6.8, 7.2), getRandomNumber(6.8, 7.2)]
potassium = [getRandomNumber(35, 47), getRandomNumber(35, 47), getRandomNumber(35, 47), getRandomNumber(35, 47), getRandomNumber(35, 47)]
nacl = [getRandomNumber(1, 1.7), getRandomNumber(1, 1.7), getRandomNumber(1, 1.7), getRandomNumber(1, 1.7), getRandomNumber(1, 1.7)]
salmonelle = [getRandomNumber(17, 37), getRandomNumber(17, 37), getRandomNumber(17, 37), getRandomNumber(17, 37), getRandomNumber(17, 37)]
ecoli = [getRandomNumber(35, 49), getRandomNumber(35, 49), getRandomNumber(35, 49), getRandomNumber(35, 49), getRandomNumber(35, 49)]
listeria = [getRandomNumber(28, 54), getRandomNumber(28, 54), getRandomNumber(28, 54), getRandomNumber(28, 54), getRandomNumber(28, 54)]
time = datetime.now()
# unit = 1
unit = round(getRandomNumber(1, 3))

# et on créé notre dictionaire avec ces données précédement génerées
mesures = {
    "data": {
        "unit": unit,
        "mesures": [{
            "num_automate": 1,
            "type_automate": 0X0000BA20,
            "temp_int": round(temp_int[0], 1),
            "temp_ext": round(temp_ext[0], 1),
            "weight_milk": round(weight_milk[0], 0),
            "weight_product": round(weight_product[0], 0),
            "ph": round(ph[0], 1),
            "potassium": round(potassium[0], 0),
            "nacl": round(nacl[0], 1),
            "salmonelle": round(salmonelle[0], 0),
            "ecoli": round(ecoli[0], 0),
            "listeria": round(listeria[0], 0),
            "time": str(time)
        },{
            "num_automate": 2,
            "type_automate": 0X0000BA21,
            "temp_int": round(temp_int[1], 1),
            "temp_ext": round(temp_ext[1], 1),
            "weight_milk": round(weight_milk[1], 0),
            "weight_product": round(weight_product[1], 0),
            "ph": round(ph[1], 1),
            "potassium": round(potassium[1], 0),
            "nacl": round(nacl[1], 1),
            "salmonelle": round(salmonelle[1], 0),
            "ecoli": round(ecoli[1], 0),
            "listeria": round(listeria[1], 0),
            "time": str(time)
        },{
            "num_automate": 3,
            "type_automate": 0X0000BA22,
            "temp_int": round(temp_int[2], 1),
            "temp_ext": round(temp_ext[2], 1),
            "weight_milk": round(weight_milk[2], 0),
            "weight_product": round(weight_product[2], 0),
            "ph": round(ph[2], 1),
            "potassium": round(potassium[2], 0),
            "nacl": round(nacl[2], 1),
            "salmonelle": round(salmonelle[2], 0),
            "ecoli": round(ecoli[2], 0),
            "listeria": round(listeria[2], 0),
            "time": str(time)
        },{
            "num_automate": 4,
            "type_automate": 0X0000BA23,
            "temp_int": round(temp_int[3], 1),
            "temp_ext": round(temp_ext[3], 1),
            "weight_milk": round(weight_milk[3], 0),
            "weight_product": round(weight_product[3], 0),
            "ph": round(ph[3], 1),
            "potassium": round(potassium[3], 0),
            "nacl": round(nacl[3], 1),
            "salmonelle": round(salmonelle[3], 0),
            "ecoli": round(ecoli[3], 0),
            "listeria": round(listeria[3], 0),
            "time": str(time)
        },{
            "num_automate": 5,
            "type_automate": 0X0000BA24,
            "temp_int": round(temp_int[4], 1),
            "temp_ext": round(temp_ext[4], 1),
            "weight_milk": round(weight_milk[4], 0),
            "weight_product": round(weight_product[4], 0),
            "ph": round(ph[4], 1),
            "potassium": round(potassium[4], 0),
            "nacl": round(nacl[4], 1),
            "salmonelle": round(salmonelle[4], 0),
            "ecoli": round(ecoli[4], 0),
            "listeria": round(listeria[4], 0),
            "time": str(time)
        }
        ]

    }
}
# que l'on transforme en onjet json
data = json.dumps(mesures)

file_name = str(unit)+'_'+str(time.timestamp())+'.json'
print(file_name)

# et qu'on écris dans le fichier prévu à cet effet
myFile = open('history/'+file_name, 'a')
# myFile = open('data.json', 'a')
myFile.write(data)

