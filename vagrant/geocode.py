import json
import requests


def get_coordinates(input_string):
    """Takes an input string of a location
    and returns the long/lat coordinates of the
    location."""

    # Try and retrieve client_id from file.
    # Used to keep the client_id from making it
    # into version control.
    try:
        with open('g_client_id') as client_id:
            g_id = client_id.read()
    except IOError as e:
        print('Could not open g_client_id.txt: {}'.format(e))
    else:
        print(g_id)

    # Create the URL for API request
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': input_string,
        'key': g_id
    }

    # Use requests library to send request to Google API
    response = requests.get(url=base_url, params=params).json()
    print(response)
