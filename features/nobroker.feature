Feature: NOBROKER Log
  Scenario: To verify search functionality for the multiple locality and description tag for the property.
    Given the user is on nobroker homepage
    When the user selects Buy property related option
    Then the user is able to select "Mumbai" city
    And  type "Malad" in the search box
    Then the user is able to select“MaladEast-Malkani Estate”and“Malad west-Sundar Ln”from the drop down menu
    Then select 2 Bhk and 3 Bhk from the BHK types
    And the user can click in the search button
    When the property listing page appears
    Then the user can scroll and click on the 4th property
    When the 4th property page loads up
    Then the user is able to scroll down and see the description of the related property is present or not
    And if property description is present, test case is passed or vice versa
