"""Coffe Order Flask app."""

from flask import Flask, request, session, flash, render_template,redirect
import crud
from appdetails import SEARCH_URL, api_key 
import requests
from urllib.parse import quote_plus
import json

#Yelp API formatting
HEADERS = {'Authorization': 'bearer %s' % api_key}


app = Flask(__name__)


@app.route("/")
def show_homepage():
    """Show the application's homepage."""

    return render_template("homepage.html")


@app.route("/accounts")
def show_account_page():
    "Show login and create account page"

    return render_template("accounts.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    user = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/inputorder")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user.email or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.username}!")

    return redirect("/inputorder")



@app.route("/inputorder", methods=["GET"])
def show_coffee_search_page():
    "Show coffee order search page"
 
    return render_template("inputorder.html") 


@app.route("/coffeesearchresults", methods=["POST"])
def show_coffee_search_results():
    "Show coffee order search results"

    term = request.form.get("drinkname", "milk")
    location = request.form.get("zipcode")

    url = SEARCH_URL.format(term=quote_plus(term),location=quote_plus(location))

    payload = {'term' : term.replace(' ', '+'),
        'zipcode': location.replace(' ', '+')}

    response = requests.get(url, headers=HEADERS, params=payload)

    coffee_order_results = response.json

    return render_template("results.html", search_results=coffee_order_results )

 
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")