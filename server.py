"""Coffe Order Flask app."""

from flask import Flask, request, session, flash, render_template,redirect
import crud
from appdetails import SEARCH_URL, api_key
import requests
from search import search_Yelp_api

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
def show_coffee_page():
    "Show coffee order search page"

    return render_template("inputorder.html")

@app.route("/coffeesearch", methods=["POST"])
def show_coffee_search_terms():
    "Show coffee order search page"
 
    if request.method == "POST":
        term = request.form.get("drinkname")
        location = request.form.get("zipcode")
        limit = 10
        return run_search(term,location,limit)
    else:
        return render_template("inputorder.html") 

def_run_search(term,location,limit):
    results = search 

    response = requests.get(url=SEARCH_URL, params= headers=HEADERS)

    coffee_order_results = response.json()

    requested_coffee_order = coffee_order_results['businesses']

    for i in range(requested_coffee_order):
        BusinessName = coffee_order_results['businesses'][i].get("name")
        BusinessWebsite = coffee_order_results['businesses'][i].get("url")
        IsClosed = coffee_order_results['businesses'][i].get("is_closed")
        Location = coffee_order_results['businesses'][i].get("display_address")
        
    return render_template("results.html", business_name=BusinessName, is_closed=IsClosed, location=Location, business_website=BusinessWebsite)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
