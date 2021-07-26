# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json


def obtenerapi(pais):
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name": pais}

    headers = {
        'x-rapidapi-key': "0bb6204312mshdcc0190bbf7b974p13bc50jsnf9114da6ba1e",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonDataString = response.text
    jsonDictionary = json.loads(jsonDataString)
    ##print(json.dumps(jsonDictionary, indent=4, sort_keys=True))
    return jsonDictionary[0]




