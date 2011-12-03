#!/usr/bin/env python2.7

import json
import urllib2

# Your URL from https://www.google.com/latitude/b/0/apps (click 'Developer Information')
LATITUDE_URL = ""

# Your Singly API key from https://singly.com/users/me/settings
SINGLY_API_KEY = ""

# The name of the dataset within Singly
SINGLY_DATASET_NAME = "latitude"

SINGLY_URL = "https://api.singly.com/%s/push/%s" % (SINGLY_API_KEY, SINGLY_DATASET_NAME)

def post_singly(data):
    """Post the data to Singly"""

    data_json = json.dumps(data)

    request = urllib2.Request(SINGLY_URL, data_json, {'content-type': 'application/json'})
    stream = urllib2.urlopen(request)

    print stream.read()

def get_latitude():
    """Get the current location from Latitude"""

    request = urllib2.Request(LATITUDE_URL, None)
    stream = urllib2.urlopen(request)

    data = json.load(stream)

    timestamp = data['features'][0]['properties']['timeStamp']

    longitude = data['features'][0]['geometry']['coordinates'][0]
    latitude = data['features'][0]['geometry']['coordinates'][1]

    return { "data": [{
        "obj": {
            "id": timestamp,
            "timestamp": timestamp,
            "lat": latitude,
            "lng": longitude
        }
    }]}

def main():
    post_singly(get_latitude())

if __name__ == "__main__":
    main()
