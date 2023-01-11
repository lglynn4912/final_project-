"""CRUD operations."""

from model import db, User, DrinkName, PreferredOrder, connect_to_db


def create_drink(name, description):
    """Create and return a new drink."""

    drinkname = DrinkName(name=name, description=description)

    return drinkname


def get_drinks(): 
    "returns all drinknames"

    return DrinkName.query.all()


def create_user(user_name, email, password):
    """Create and return a new user."""

    user = User(user_name=user_name, email=email, password=password)

    return user 


def get_user_by_email(email):
    """Create and return a new user."""

    user_email = User(email=email)

    return user_email

def create_preferred_order(preferred_order_name):
    """Create and return a user's new preferred order"""

    preferredorder = PreferredOrder(preferred_order_name=preferred_order_name)
    
    return preferredorder

def get_preferred_order_by_id(preferred_order_id):
    """Return a preferred order by primary key."""

    return PreferredOrder.query.get(preferred_order_id)



if __name__ == "__main__":
    from server import app
    connect_to_db(app)