import requests
import os
from main import API_URL
from main import AUTH_TOKEN_DEFINITION


def checkToken():
    """Checks if an authentication token exists and puts it in file"""

    # Check if the file exists and if the auth token is correct
    if os.path.exists('auth.txt'):
        existing_file = open('auth.txt', 'r')
        token = existing_file.read()
        if checkTokenValidity(token):
            return True

    # If the above-mentioned doesn't recognize authentication token
    # the user is asked to provide a token
    with open('auth.txt', 'w') as auth_file:
        while True:
            print('Insert your authentication token >')
            alleged_token = input()
            if checkTokenValidity(alleged_token):
                auth_file.write(alleged_token)
                auth_file.close()
                return True


def checkTokenValidity(token):
    """Returns true if the token is valid"""
    try:
        request = f'{API_URL}userinfo{AUTH_TOKEN_DEFINITION}{token}'
        response = requests.get(request)
        if response.status_code != 200:
            print(f'{response.status_code}: Token is not valid.')
            return False
        else:
            print('The token is valid.')
            return True
    except:
        print('Token is not valid.')
        return False