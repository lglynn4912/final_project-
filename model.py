"""Models for Find my Coffee flask app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user with a coffee profile"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


    user_preferred_order = db.relationship("PreferredOrder", back_populates="user")

    def __repr__(self):
        return f'<User user_name={self.user_name} email={self.email}>'


class PreferredOrder(db.Model):
    """An order made by a user"""

    __tablename__ = 'user-preferred-orders'

    preferred_order_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    preferred_order_name = db.Column(db.String, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="user_preferred_order")

    def __repr__(self):
        return f'<PreferredOrder preferred_order_name={self.preferred_order_name} preferred_order_id={self.preferred_order_id} >'


class DrinkName(db.Model):
    """Standard list of coffee drink names"""

    __tablename__ = 'drinknames'

    drink_name_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)

def __repr__(self):
        return f'<DrinkName name={self.name}>'


def connect_to_db(flask_app, db_uri="postgresql:///drinkorders", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("You've connected to the database!")
    

if __name__ == "__main__":
    from server import app
    connect_to_db(app)