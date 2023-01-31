Feature: Amazon Web Browsing
    As a web surfer,
    I want to find information online,
    So I can learn new things and get tasks done.

    Background: Basic Amazon Search
        Given the Amazon home page is displayed
        When Type in a search term "phone" in the search box and search
        And Click on the sort dropdown

    Scenario: sort dropdown
        Then check that it has "5" list items

    Scenario: Newest Arrivals
        When Select “Newest Arrivals” in the list
        Then check if there are search results appearing

    Scenario: Featured
        When Select “Featured” in the list
        Then check if there are search results appearing


