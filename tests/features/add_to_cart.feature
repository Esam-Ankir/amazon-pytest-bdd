Feature: Amazon Web Browsing
    As a web surfer,
    I want to find information online,
    So I can learn new things and get tasks done.

    Background:  Amazon Cart
        Given the Amazon home page is displayed
        When Type in a search term "phone" in the search box and search

    Scenario: Add To Cart
        When Click any of the results to open the product page
        And Click on add to cart button on the side
        And Click on the cart button
        Then Check that the product added to the cart is the same product selected initially

    Scenario: Remove from Cart
        When Click any of the results to open the product page
        And Click on add to cart button on the side
        And Click on the cart button
        And Click on Qty list and choose 0
        Then Check that the header contains "Your Amazon Cart is empty."
