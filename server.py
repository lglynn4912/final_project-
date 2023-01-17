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
app.secret_key = "supersecret"


@app.route("/")
def show_homepage():
    """Show the application's homepage."""

    return render_template("homepage.html")


@app.route("/accounts")
def show_account_page():
    "Show create account page"

    return render_template("accounts.html")


@app.route("/login")
def show_login_page():
    """Show the login page"""

    return render_template("login.html")


@app.route("/myprofile")
def show_myprofile():
    """Show the user's profile page"""

    return render_template("myprofile.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user_name."""

    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.create_user(user_name, email, password)

    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        new_user = crud.create_user(user_name, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/login")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user_name login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user_name = crud.get_user_by_email(email)
    if not user_name.email or user_name.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user_name by storing the user_name's email in session
        session["email"] = user_name.email
        flash(f"Welcome back, {user_name.user_name}!")

    return redirect("/myprofile")



@app.route("/inputorder", methods=["GET"])
def show_coffee_search_page():
    "Show coffee order search page"
 
    return render_template("inputorder.html") 



@app.route("/coffeesearchresults", methods=["POST"])
def show_coffee_search_results():
    "Show coffee order search results"
    
    term = request.form.get("drinkname")
    location = request.form.get("zipcode")
    radius = request.form.get("radius")
    open_now = request.form.get("open-now")

  
    if len(location) < 5:

        flash(f"Zipcode required. Please input a valid zipcode")
        return redirect("/inputorder")


    elif open_now == "false" and len(radius) == 0:
        print("term:", term)
        print("zipcode:", location)


        url = "%s?term=%s&location=%s" % (SEARCH_URL, term, location)
        print("search url", url)

        response = requests.get(url, headers=HEADERS )
        print("response", response)
        print("response", response.json())

        search_results = response.json()
        total_results = search_results['total'] 
        coffee_order_results_sorted =  sorted(search_results['businesses'], key=lambda x: x['distance'])


    elif open_now == "false":
        miles_to_meters_conversion = float(radius) * 1609
        radius_value_as_integer= int(miles_to_meters_conversion)
        print("term:", term)
        print("zipcode:", location)
        print("within radius:", radius_value_as_integer)


        url = "%s?term=%s&location=%s&radius=%s" % (SEARCH_URL, term, location, radius_value_as_integer)
        print("search url", url)

        response = requests.get(url, headers=HEADERS )
        print("response", response)
        print("response", response.json())
        
        search_results = response.json()
        total_results = search_results['total'] 
        coffee_order_results_sorted =  sorted(search_results['businesses'], key=lambda x: x['distance'])

    
    elif len(radius) == 0:
        yes_open_now = bool(open_now)
        print("term:", term)
        print("zipcode:", location)
        print("open_now:", yes_open_now)

        url = "%s?term=%s&location=%s&open_now=%s" % (SEARCH_URL, term, location, yes_open_now)
        print("search url", url)

        response = requests.get(url, headers=HEADERS )
        print("response", response)
        print("response", response.json())
        
        search_results = response.json()
        total_results = search_results['total'] 
        coffee_order_results_sorted =  sorted(search_results['businesses'], key=lambda x: x['distance'])


    else:
        miles_to_meters_conversion = float(radius) * 1609
        radius_value_as_integer= int(miles_to_meters_conversion)
        yes_open_now = bool(open_now)
        print("term:", term)
        print("zipcode:", location)
        print("within radius:", radius_value_as_integer)
        print("open_now:", yes_open_now)


        url = "%s?term=%s&location=%s&radius=%s&open_now=%s" % (SEARCH_URL, term, location, radius_value_as_integer,yes_open_now)
        print("search url", url)

        response = requests.get(url, headers=HEADERS )
        print("response", response)
        print("response", response.json())

        search_results = response.json()
        total_results = search_results['total'] 
        coffee_order_results_sorted =  sorted(search_results['businesses'], key=lambda x: x['distance'])

  
    return render_template("results.html",
        search_results=coffee_order_results_sorted, 
        total_results=total_results
     )



# @app.route("/coffeesearchresults", methods=["POST"])
# def show_coffee_search_results():
#     "Show coffee order search results"
    

#     term = request.form.get("drinkname", "milk")
#     location = request.form.get("zipcode")

#     print("Search terms:")
#     print("term:", term)
#     print("zipcode:", location)

#     url = "%s?term=%s&location=%s" % (SEARCH_URL, term, location)
#     print("search url", url)

#     response = requests.get(url, headers=HEADERS )
#     print("response", response)
#     print("response", response.json())

#     coffee_order_results = response.json()

#     return render_template("results.html", search_results=coffee_order_results)


# @app.route("/preferredorder", methods=["POST"])
# def preferred_order(preferred_order):
#     """Create a preferred order"""

#     logged_in_email = session.get("email")
#     preferred_order = request.form.get("drinkname")

#     if logged_in_email is None:
#         flash("You must log in to create a preferred order")
#     elif not preferred_order:
#         flash("Error: you didn't select that you wanted a preferred order.")
#     else:
#         user = crud.get_user_by_email(logged_in_email)
#         preferred_order = crud.create_preferred_order(preferred_order)

#         user_preferred_order = crud.create_preferred_order(preferred_order)
#         db.session.add(user_preferred_order)
#         db.session.commit()

#         flash(f"You updated your order to {preferred_order}")


 
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")