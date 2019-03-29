import requests
from ask_sdk_model import IntentRequest
from typing import Union, Dict, List
import urllib.request


def get_transit_57():
    """Return schedule for 57"""
    # type: () -> List

    in_timings = []
    out_timings = []


    with urllib.request.urlopen(
            'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&stopId=14704') as response:
        html = response.read()
        # to convert the byte object returned by the previous line into a string object
        decod = html.decode('cp855')


        for word in decod.split(" " or "=" or '\n'):
            if (word.startswith("minutes")):
                splitword = word.split('=')
                in_timings.append((splitword[1].replace('"', "")))

    with urllib.request.urlopen(
            'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&stopId=13981') as response:
        html = response.read()
        # to convert the byte object returned by the previous line into a string object
        decod = html.decode('cp855')


        for word in decod.split(" " or "=" or '\n'):
            if (word.startswith("minutes")):
                splitword = word.split('=')
                out_timings.append((splitword[1].replace('"', "")))

    timings = [in_timings[0], in_timings[1], out_timings[0], out_timings[1]]
    print(timings)
    return timings
