"""

    Python 3 wrapper for the v2 nutritionix API (June 2020)
    Consult https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/
    for information on parameters for each endpoint

    Built out from official python2 client:
    https://github.com/nutritionix/library-python

"""

import logging
import json
import requests
import urllib.parse as urlparse

API_VERSION = "v2"
BASE_URL = "https://trackapi.nutritionix.com/%s/" % (API_VERSION)


class NutritionixClient:

    def __init__(self, application_id=None, api_key=None, debug=False, *arg, **kwarg):
        self.APPLICATION_ID = application_id
        self.API_KEY = api_key
        self.DEBUG = False

        if debug == True:
            self.DEBUG = debug
            logging.basicConfig(level=logging.DEBUG)

    def get_api_version(self, *arg):
        return API_VERSION

    def get_application_id(self, *arg):
        return self.APPLICATION_ID

    def get_api_key(self, *arg):
        return self.API_KEY

    def execute(self, url=None, method='GET', params={}, data={}, headers={}):
        """
            Bootstrap, execute and return request object, default method: GET
        """

        # Bootstraps the request
        method = method.lower()

        headers['X-APP-ID'] = self.APPLICATION_ID
        headers['X-APP-KEY'] = self.API_KEY

        # Executes the request
        if method == "get" or not 'method' in locals():
            r = requests.get(url, params=params, headers=headers)

        elif method == "post":
            r = requests.post(url, params=params, data=data, headers=headers)

        else:
            return None

        # Log response content
        logging.debug("Response Content: %s" % (r.text))

        return r


    #--------------
    # API (Food) Methods #
    #--------------

    def search(self, q, **kwargs):  # TODO: Support for the nutrient filters
        """
        Use this method to access the search/instant endpoint

        Extra parameters can be added in the following way:
        nutrtitionix.search(query, limit=6, ...)

        Search for an entire food term like "mcdonalds big mac" or "celery."
        """
        params = {}
        params['query'] = q
        # Adding any extra parameters (using a dictionary merge trick)
        if kwargs:
            params = {**params, **kwargs}
        endpoint = urlparse.urljoin(BASE_URL, 'search/instant')
        return self.execute(endpoint, params=params)

    def autocomplete_food(self, q, **kwargs):
        """
        Specifically designed to provide autocomplete functionality for search
        boxes. The term selected by the user in autocomplete will pass to
        the /search endpoint.

        NB: From what I've seen this uses the same endpoint (/search/instant)
            but if this isn't the case, raise an issue on the repo
        """
        return self.search(q)


    def natural_nutrients(self, q, **kwargs):
        """
        Natural language queries about quantities of ingredients e.g:
        "1 tbsp butter"
        """
        data = {'query': q}
        endpoint = urlparse.urljoin(BASE_URL, 'natural/nutrients')
        return self.execute(endpoint, method="POST", params=kwargs, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    def item(self, id, **kwargs):
        """
        Look up a specific item by ID or UPC
        """
        # Adds keyword args to the params dictionary
        params = {}
        if kwargs:
            params = kwargs
        params['nix_item_id'] = id
        endpoint = urlparse.urljoin(BASE_URL, 'search/item')
        return self.execute(endpoint, params=params)

        """

            Brand searches appear to be legacy functionality at this point
            However they are part of the v1_1 API so I can add that in the
            future.

            (TODO: add brand functionality)

        """

    #--------------
    # API (Exercise) Methods #
    #--------------

    def natural_exercise(self, q, **kwargs):
        """
        Natural language queries for exercise e.g:
        "i went on a 3km run" / "3 min row"
        """
        data = {'query': q}
        endpoint = urlparse.urljoin(BASE_URL, 'natural/exercise')
        return self.execute(endpoint, method="POST", params=kwargs, data=json.dumps(data), headers={'Content-Type': 'application/json'})


    #--------------
    # API (Location) Methods #
    #--------------

    def locations_distance(self, coordinate, distance, **kwargs):
        """
        Finds locations within "distance" of your location
        Expects lat/long coordinate as a tuple.
        """

        if len(coordinate) != 2 :
            print("Incorrect tuple length: expected lat/long tuples for coordinate arg")

        params = kwargs
        params['ll'] = "" + str(coordinate[0]) + "," + str(coordinate[1])
        params['distance'] = distance

        endpoint = urlparse.urljoin(BASE_URL, 'locations')
        return self.execute(endpoint, params=params)

    def locations_bounding_box(self, north_east, south_west, **kwargs):
        """
        Finds locations within a bounding box defined by two coordinates
        This expects two tuples representing the lat/long coordinates.
        """

        if len(north_east) != 2 or len(south_west) != 2 :
            print("Incorrect tuple length: expected lat/long tuples for north east and south west coordinates")

        params = kwargs
        params['north_east'] = "" + str(north_east[0]) + "," + str(north_east[1])
        params['south_west'] = "" + str(south_west[0]) + "," + str(south_west[1])

        endpoint = urlparse.urljoin(BASE_URL, 'locations')
        return self.execute(endpoint, params=params)
