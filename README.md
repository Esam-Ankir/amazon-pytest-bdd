# amazon-pytest-bdd
testing some features in Amazon website 


## activating virtual environment
source amazon-pytest-bdd/bin/activate


## run all tests
python -m pytest

## run specific test(add to cart for example)
python -m pytest -s -v tests/step_defs/test_add_to_cart.py

## Testing Add To Cart
Create a test to check the following user journey:
- Visit amazon.com

- Type in a search term and click the search button

- Click any of the results to open the product page

- Click on add to cart button on the side
- Click on the cart button
- Check that the product added to the cart is the same product selected initially"		

