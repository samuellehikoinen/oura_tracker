#!/usr/bin/env python3
import requests
from printData import *
from tokenCheck import *

# Declaring global variables
API_URL = 'https://api.ouraring.com/v1/'
AUTH_TOKEN_DEFINITION = '?access_token='
AUTH_TOKEN = ''
DATA = {}


def getApiResponse(page):
    """Return Oura API request"""
    return_data = ''
    try:
        request = f'{API_URL}{page}{AUTH_TOKEN_DEFINITION}{AUTH_TOKEN}'
        return_data = requests.get(request).json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    return return_data


def printDayReport():
    """Prints a report of the most recent Oura status"""
    print('=== YOUR CURRENT OURA STATUS ===')
    print()
    last_sleep_data = DATA['sleep']['sleep'][-1]
    last_activity_data = DATA['activity']['activity'][-1]
    last_readiness_data = DATA['readiness']['readiness'][-1]

    printSleepData(last_sleep_data)
    printActivityData(last_activity_data)
    printReadinessData(last_readiness_data)


def getData():
    """Adds all data to json from users userinfo, sleep, activity and readiness."""
    userinfo_json = getApiResponse('userinfo')
    sleep_json = getApiResponse('sleep')
    activity_json = getApiResponse('activity')
    readiness_json = getApiResponse('readiness')
    DATA['userinfo'] = userinfo_json
    DATA['sleep'] = sleep_json
    DATA['activity'] = activity_json
    DATA['readiness'] = readiness_json


def setAuthToken():
    """Gets authentication token from auth.txt and sets it as global variable"""
    auth_file = open('auth.txt', 'r')
    token = auth_file.read()
    global AUTH_TOKEN
    AUTH_TOKEN = token


def main():
    """Main function for the program."""
    if checkToken():
        setAuthToken()
        getData()
        printDayReport()


if __name__ == '__main__':
    main()