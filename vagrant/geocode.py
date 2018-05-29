import json
import requests


def get_coordinates(input_string):
    """Takes an input string of a location
    and returns the long/lat coordinates of the 
    location"""

    # Try and retrieve client_id from file
    # Used to keep the client_id from making it
    # into version control
    try:
        with open('g_client_id') as client_id:
            g_id = client_id.read()
    except IOError as e:
        print('Could not open g_client_id.txt: {}'.format(e))
    else:
        print(g_id)

