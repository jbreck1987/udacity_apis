from geocode import get_coordinates

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = ''
foursquare_client_secret = ''
g_client_id = ''


def find_restaurant(meal_type, location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and meal_type strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url
if __name__ == '__main__':
	find_restaurant('Pizza', 'Tokyo, Japan')
	find_restaurant('Tacos', 'Jakarta, Indonesia')
	find_restaurant('Tapas', 'Maputo, Mozambique')
	find_restaurant('Falafel', 'Cairo, Egypt')
	find_restaurant('Spaghetti', 'New Delhi, India')
	find_restaurant('Cappuccino', 'Geneva, Switzerland')
	find_restaurant('Sushi', 'Los Angeles, California')
	find_restaurant('Steak', 'La Paz, Bolivia')
	find_restaurant('Gyros', 'Sydney Australia')
