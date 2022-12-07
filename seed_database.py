"""Script to seed database."""

import os
import json

import crud
import model
import server

os.system("dropdb drinkorders")
os.system("createdb drinkorders")

model.connect_to_db(server.app)
model.db.create_all()

with open('/Users/laurenglynn/src/final_project/drink_data/drink_names.json') as f:
    drink_data = json.loads(f.read())

drinks_in_db = []

for drink in drink_data:
    name = drink["name"],
    description = drink["description"]
    
    drink = crud.create_drink(
        name=name, 
        description=description
    )
    
    drinks_in_db.append(drink)

model.db.session.add_all(drinks_in_db)
model.db.session.commit()
