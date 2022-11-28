from appdetails import *
import requests



def search(api_key, term, location):
     """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """


url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
res = request.get(API_HOST, SEARCH_PATH, api_key, url_params=url_params)
    
coffee_order_possibilities = res.json()

coffee_order_results = coffee_order_possibilities['businesses']

for i in range(coffee_order_results):
    BusinessName = coffee_order_results['businesses'][i].get("name")
    BusinessWebsite = coffee_order_results['businesses'][i].get('url')
    IsClosed = coffee_order_results['businesses'][i].get("is_closed")
    Location = coffee_order_results['businesses'][i].get("display_address"
    print(f'{BusinessName}, Is Currently Closed:{IsClosed}. {Location} {BusinessWebsite}')

