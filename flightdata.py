import requests
import json
import urllib
import sys
import Image 

# Get all the datas

def get_flight_data():
    r = requests.get("http://services.inflightpanasonic.aero/inflight/services/flightdata/v1/flightdata")
    return r.json()

def get_conn_data():
    r = requests.get("http://services.inflightpanasonic.aero/inflight/services/exconnect/v1/status")
    return r.json()

def get_session_data():
    r = requests.get("http://www.unitedwifi.com/portal/r/getAllSessionData");
    return r.json();

def get_flight_map():
    url = get_session_data['flifo']['flightMapPath']
    image = requests.get(url)
    output.show()


# Cool thngs with the datas

