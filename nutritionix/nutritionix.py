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
        """ Bootstrap, execute and return request object,
                default method: GET
        """

        # Verifies params
        if params.get('limit') != None and params.get('offset') == None:
            raise Exception('Missing offset',
                            'limit and offset are required for paginiation.')

        elif params.get('offset') != None and params.get('limit') == None:
            raise Exception('Missing limit',
                            'limit and offset are required for paginiation.')

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
    # API Methods #
    #--------------

    def search(self, q, **kwargs):  # TODO: Add advance search filters
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
        Supports natural language queries like "1 cup butter" or "100cal yogurt"
        """

        data = {'query': q}

        endpoint = urlparse.urljoin(BASE_URL, 'natural/nutrients')

        return self.execute(endpoint, method="POST", params=kwargs, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    def item(self, **kwargs):
        """Look up a specific item by ID or UPC"""

        # Adds keyword args to the params dictionary
        params = {}
        if kwargs:
            params = kwargs

        endpoint = urlparse.urljoin(BASE_URL, 'item/%s' % (params.get('id')))

        return self.execute(endpoint)

    def brand(self, **kwargs):
        """Look up a specific brand by ID. """

        # Adds keyword args to the params dictionary
        params = {}
        if kwargs:
            params = kwargs

        endpoint = urlparse.urljoin(BASE_URL, 'brand/%s' % (params.get('id')))

        return self.execute(endpoint)

    def brand_search(self, **kwargs):
        """Look up a specific brand by ID. """

        # Adds keyword args to the params dictionary
        params = {}
        if kwargs:
            params = kwargs

        endpoint = urlparse.urljoin(BASE_URL, 'search/brands/')

        return self.execute(endpoint, params=params)
