"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb drinknames")
os.system('createdb drinknames')

model.connect_to_db(server.app)
model.db.create_all()

with open('drink_data/drink_names.json') as f:
    drink_names = json.loads(f.read())

drinks_in_db = []

for drink in drink_names:
    drink_name = drink['drinkname']
    drink_description = drink['description']
   
    drink = crud.create_drink(
        drink_name=drink_name,
        drink_description=drink_description 
    )
    
    drinks_in_db.append(drink)


model.db.session.add_all(drinks_in_db)
model.db.session.commit()



