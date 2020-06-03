(Extension of) Official Nutritionix Python Client
==================================

This is python 3 compatible and will support the exercise APIs

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

####  Standard Search
```py
"""
This will perform a search. The object passed into this function
can contain all the perameters the API accepts in the `POST /v2/search` endpoint
"""
nutritionix.search(q='salad', limit=10, offset=0, search_nutrient='calories')
```

#### Brand Search - Yet to be implemented
```py
"""
This will perform a search. The object passed into this function
can contain all the perameters the API accepts in the `GET /v2/search/brands` endpoint

type: (1:restaurant, 2:cpg, 3:usda/nutritionix) defaults to undefined
"""
nutritionix.brand_search(q='just salad', limit=10, offset=0, type=1)
```

#### Natural
```py
"""
The natural endpoint allows you to translate plane text into a full spectrum analysis.
gram_weight: An {Integer} that will be used as a multiplier when calculating `total.nutrients`
"""

ingredients = """
1 tbsp sugar
16 fl oz water
1/2 lemon
"""
nutritionix.natural(q=ingredients, gram_weight=20)
```

#### Autocomplete
```py
#allow users the convenience of "as you type" suggestions.
nutritionix.autocomplete(q='greek y')
```

### Links
For more information about the API and extra arguments for calls:

https://trackapi.nutritionix.com/docs/

https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/
