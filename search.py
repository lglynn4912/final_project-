import requests
from appdetails import *
from urllib.parse import quote_plus


def search_Yelp_api(term, location):
     """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

results = []

url = SEARCH_URL.format(
    term=quote_plus(drink)+quote_plus(milk),
    location=quote_plus(zipcode)
    )

response = requests.get(url,HEADERS)

coffee_order_results = response.json

results += coffee_order_results['businesses']
   
# res = requests.get(SEARCH_URL, api_key, url_params=url_params)

# response = requests.get(url=SEARCH_URL, params=search_parameters, headers=HEADERS)
    
for i in range(coffee_order_results):
    BusinessName = coffee_order_results['businesses'][i].get("name")
    BusinessWebsite = coffee_order_results['businesses'][i].get("url")
    IsClosed = coffee_order_results['businesses'][i].get("is_closed")
    Location = coffee_order_results['businesses'][i].get("display_address")
    print(f'{BusinessName}, Is Currently Closed:{IsClosed}. {Location} {BusinessWebsite}')

