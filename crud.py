"""CRUD operations."""

from model import db, User, DrinkNames, connect_to_db

# def create_user(user_name):
#     """Create and return a new user."""

#     user = User(user_name=user_name)

#     return user

def create_drink(name, description):
    """Create and return a new drink."""

    drink = DrinkName(name=name, description=description,)

    return drink


if __name__ == "__main__":
    from server import app

    connect_to_db(app)