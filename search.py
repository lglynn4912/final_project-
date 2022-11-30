import requests
from appdetails import *
from urllib.parse import quote_plus

HEADERS = {'Authorization': 'bearer %s' % api_key}

def search_Yelp_api(term, location):
     """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
results = []

#https://api.yelp.com/v3/businesses/search?term=goat+milk+latte+iced&location=94116#
url = SEARCH_URL.format(term=quote_plus(term),location=quote_plus(location))

response = requests.get(url, HEADERS)

coffee_order_results = response.json

results += coffee_order_results['businesses']
   
# res = requests.get(SEARCH_URL, api_key, url_params=url_params)

# response = requests.get(url=SEARCH_URL, params=search_parameters, headers=HEADERS)
    
# for i in range(results):
#     BusinessName = results['businesses'][i].get("name")
#     BusinessWebsite = results['businesses'][i].get("url")
#     IsClosed = results['businesses'][i].get("is_closed")
#     Location = results['businesses'][i].get("display_address")
#     print(f'{BusinessName}, Is Currently Closed:{IsClosed}. {Location} {BusinessWebsite}')