Nutritionix Python Client - Unofficial Update (2020)
==================================

![alt text](attributions/NutritionixAPI_hires_flat.png)

This fork is python 3 compatible and supports a lot more endpoints:
- Food
- Exercise
- Location

### Installation:

```
pip install nutritionix-unofficial
```

### Usage

#### import inside your project

```py
from nutritionix.nutritionix import NutritionixClient

nutritionix = NutritionixClient(
    application_id='YOUR_APP_ID',
    api_key='YOUR_API_KEY',
    # debug=True, # defaults to False
)

```

#### Quick note on parameters

Each function accepts all the parameters accepted by their respective endpoints (detailed in the nutritionix docs at https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/).

The parameters can be given like so:
```py
nutritionix.search(q='QUERY', parameter1='...', parameter2='...', ...)
```
#### All of these methods return a dictionary object

#### nutritionix.search(q, ...)
```py
"""
This will perform a search of the nutritionix database.
(v2/search/instant endpoint)
e.g:
"""

nutritionix.search(q='salad')
# or in the case of extra parameters:
nutritionix.search(q='salad', common=False)
```

Endpoint docs:

https://trackapi.nutritionix.com/docs/#/default/get_v2_search_instant

#### nutritionix.autocomplete(q, ...)
```py
# Autocomplete facility for search interfaces - the same as search.
# (v2/search/instant endpoint) e.g:

nutritionix.autocomplete(q='greek y')
```

(Same endpoint as above)

#### nutritionix.natural_nutrients(q, ...)

```py
"""
Performs analysis on plain text list of ingredients
(v2/natural/nutrients endpoint)
e.g:
"""

ingredients = """
1 tbsp sugar
16 fl oz water
1/2 lemon
"""
nutritionix.natural_nutrients(q=ingredients)
# or in the case of extra parameters:
nutritionix.natural_nutrients(q=ingredients, gram_weight=20)
```

Endpoint docs:

https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_nutrients

#### nutritionix.item(id, ...)

```py
"""
Looks up a specific item by ID or UPC
e.g:
"""
nutritionix.item(id="513fc9e73fe3ffd40300109f")

```

Endpoint docs:

https://trackapi.nutritionix.com/docs/#/default/get_v2_search_item

#### nutritionix.natural_exercise(q, ...)

```py
"""
Performs analysis on plain text description of exercise
"""
nutnutritionix.natural_exercise(q='five mile run')
# or in the case of extra arguments:
nutritionix.natural_exercise(q='five mile run', gender='female')
```

Endpoint docs:

https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

#### nutritionix.locations_distance(coordinate, distance, ...)

```py
"""
Finds locations within the distance specified of the longitude and latitude coordinate
"""

location = (38.89814, -77.029446)

nutritionix.locations_distance(location, "10m")
# or in the case of extra parameters:
nutritionix.locations_distance(location, "10m", limit=1)
```

Endpoint docs:

https://trackapi.nutritionix.com/docs/#/Locations/get_v2_locations

#### nutritionix.locations_bounding_box(north_east, south_west)

```py
"""
Finds locations in a box bounded by north_east and south_west coords
"""

a = (38.89814, -77.029446)
b = (40.91000, -77.331800)

nutritionix.locations_bounding_box(a, b)
# or in the case of extra parameters:
nutritionix.locations_bounding_box(a, b, limit=1)
```

(Same endpoint as above)

### Links
For more information about the API and extra arguments for calls:

https://trackapi.nutritionix.com/docs/

https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/
