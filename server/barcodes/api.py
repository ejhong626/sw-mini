from rest_framework import serializers

from barcodes.models import Recipe

import requests
import config

API_KEY = config.fdc

# Implement get for urls
def getJSON(query, serving, barcode = None):
    search_str = query.replace(" ", "%20") if (barcode == None) else barcode
    url = ['https://api.nal.usda.gov/fdc/v1/foods/search?api_key=', API_KEY, '&query=', search_str]
    get_req = requests.get(''.join(url)).json()['foods'][0]

    data = {
    'name': get_req['lowercaseDescription'],
    'protein': round(int(get_req['foodNutrients'][0]['value'])/100*serving),
    'fats': round(int(get_req['foodNutrients'][1]['value'])/100*serving),
    'carbohydrate': round(int(get_req['foodNutrients'][2]['value'])/100*serving),
    'calorie': round(int(get_req['foodNutrients'][3]['value'])/100*serving),
    'quantity': serving
    }

    return data


# save by Item(**data)
