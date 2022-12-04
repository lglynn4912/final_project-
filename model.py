"""Models for preferred coffee orders app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User user_name={self.user_name} email={self.email}>"

 # preferred_orders = db.relationship("Preferred Orders", back_populates="user")

# class PreferredOrder(db.Model):
#     """An order made by a user"""

#     __tablename__ = 'preferred-orders'

#     preferred_order_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     preferred_order_name = db.Column(db.String, unique=False, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


#     def __repr__(self):
#         return f"<>"


#     # user = db.relationship("User", back_populates="preferred-orders")



class MilkType(db.Model):
    """Milk types"""

    __tablename__ = 'milktypes'

    milk_id = db.Column(db.Integer,
                        autoincrement=False,
                        primary_key=True)
    milk_name = db.Column(db.String, unique=True, nullable=False)

   def __repr__(self):
        return f"<MilkTypes milk_name={self.milk_name}>"

class DrinkName(db.Model):
    """Standard drink names"""

    __tablename__ = 'drinknames'

    drink_name_id = db.Column(db.Integer,
                        autoincrement=False,
                        primary_key=True)
    drink_name = db.Column(db.String, unique=True, nullable=False)
    drink_description = db.Column(db.String, unique=True, nullable=False)


def connect_to_db(flask_app, db_uri="postgresql:///preferredorders", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("You've connected to the database!")
    

if __name__ == "__main__":
    from server import app

    connect_to_db(app)