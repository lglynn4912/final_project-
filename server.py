"""Coffe Order Flask app."""

from flask import Flask, request, session, flash, render_template,redirect

from model import connect_to_db, db
from appdetails import SEARCH_URL, api_key 
import crud
import requests
from urllib.parse import quote_plus


#Yelp API formatting
HEADERS = {'Authorization': 'Bearer %s' % api_key}


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

    user = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(user, email, password)
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
        session["email"] = user.email
        flash(f"Welcome back, {user.user_name}!")

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

    print("Search terms:")
    print("term:", term)
    print("zipcode:", location)

    url = "%s?term=%s&location=%s" % (SEARCH_URL, term, location)
    print("search url", url)

    response = requests.get(url, headers=HEADERS )
    print("response", response)
    print("response", response.json())

    coffee_order_results = response.json()

    return render_template("results.html", search_results=coffee_order_results)

 
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")