import json
import requests


def open_id_file(filename):
    try:
        with open(filename) as id_file:
            id = id_file.read().rstrip('\n')
    except IOError as e:
        print('Could not open {}: {}'.format(filename, e))
    else:
        return id
    return None


def get_coordinates(input_string):
    """Takes an input string of a location
    and returns the long/lat coordinates of the
    location."""

    # Try and retrieve client_id from file.
    # Used to keep the client_id from making it
    # into version control.
    g_id = open_id_file('g_client_id')

    # Create the URL for API request
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': input_string,
        'key': g_id
    }

    # Use requests library to send request to Google API
    response = requests.get(url=base_url, params=params).json()

    # Extract longitude, latitude, and location name response
    try:
        latitude = response['results'][0]['geometry']['location']['lat']
        longitude = response['results'][0]['geometry']['location']['lng']
        # location_string = response['results'][0]['formatted_address']
    except Exception as e:
        print('Error in extracting information from response: {}'.format(e))
    else:
        return {'lng': longitude, 'lat': latitude}
        # print(location_string)
        # print('longitude = {}'.format(longitude))
        # print('latitude = {}'.format(latitude))
