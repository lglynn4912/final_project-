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

    # preferred_orders = db.relationship("Preferred Orders", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


# class PreferredOrder(db.Model):
#     """An order made by a user"""

#     __tablename__ = 'preferred-orders'

#     preferred_order_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     preferred_order_name = db.Column(db.String, unique=False, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


#     # user = db.relationship("User", back_populates="preferred-orders")

#     def __repr__(self):
#         return f"<>"


class MilkTypes(db.Model):
    """Milk types"""

    __tablename__ = 'milktypes'

    milk_id = db.Column(db.Integer,
                        autoincrement=False,
                        primary_key=True)
    milk_name = db.Column(db.String, unique=True, nullable=False)


class DrinkOptions(db.Model):
    """Standard drink names"""

    __tablename__ = 'drinknames'

    drink_options_id = db.Column(db.Integer,
                        autoincrement=False,
                        primary_key=True)
    drink_opions_name = db.Column(db.String, unique=True, nullable=False)


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