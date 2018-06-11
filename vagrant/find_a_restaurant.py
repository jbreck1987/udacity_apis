from geocode import get_coordinates, open_id_file

import sys
import codecs
import requests
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = open_id_file('fsq_client_id')
foursquare_client_secret = open_id_file('fsq_client_secret')
foursquare_version = '20180505'
foursquare_photo_uri = 'https://api.foursquare.com/v2/venues/{}/photos'


def find_restaurant(meal_type, location):
    # Get latitutde, longitude dict for location passed to function
    # using Google Geocode
    coords = get_coordinates(location)

    # Define request to search for restaurant near given location
    if coords is not None:
        search_uri = 'https://api.foursquare.com/v2/venues/search'
        search_params = {
            'll': '{},{}'.format(coords['lat'], coords['lng']),
            'radius': '6000',
            'query': str(meal_type),
            'client_id': foursquare_client_id,
            'client_secret': foursquare_client_secret,
            'limit': '5',
            'v': foursquare_version
        }
        response = requests.get(url=search_uri, params=search_params).json()
    else:
        print("Oops, didnt have any coordinates!")
        return None

    # Grab the first restaurant from response
    if response['response']['venues']:
        restaurant = {
            'name': response['response']['venues'][0]['name'],
            'id': response['response']['venues'][0]['id']
        }
    else:
        print("Oops, didnt find anything!")
        return None

    # Create URL to get image information for the restaurant
    search_uri = foursquare_photo_uri.format(restaurant['id'])
    search_params = {
        'client_id': foursquare_client_id,
        'client_secret': foursquare_client_secret,
        'v': foursquare_version
    }
    response = requests.get(url=search_uri, params=search_params).json()
    return response
    # 5. Grab the first image
    # 6. If no image is available, insert default a image url
    # 7. Return a dictionary containing the restaurant name, address, and image url
# if __name__ == '__main__':
#   find_restaurant('Pizza', 'Tokyo, Japan')
#   find_restaurant('Tacos', 'Jakarta, Indonesia')
#   find_restaurant('Tapas', 'Maputo, Mozambique')
#   find_restaurant('Falafel', 'Cairo, Egypt')
#   find_restaurant('Spaghetti', 'New Delhi, India')
#   find_restaurant('Cappuccino', 'Geneva, Switzerland')
#   find_restaurant('Sushi', 'Los Angeles, California')
#   find_restaurant('Steak', 'La Paz, Bolivia')
#   find_restaurant('Gyros', 'Sydney Australia')
