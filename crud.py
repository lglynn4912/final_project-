"""CRUD operations."""

from model import db, User, DrinkName, MilkName, connect_to_db


def create_drink(name, description):
    """Create and return a new drink."""

    return DrinkName(name=name, description=description)


def get_drinks(): 
    "returns all drinknames"

    return DrinkName.query.all()

def create_milk(name):
    """Create and return a new drink."""

    return MilkName(name=name)


def create_user(user_name, email, password):
    """Create and return a new user."""

    user = User(user_name=user_name, email=email, password=password)

    return user 

if __name__ == "__main__":
    from server import app
    connect_to_db(app)