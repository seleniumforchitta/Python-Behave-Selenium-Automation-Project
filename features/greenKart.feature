Feature: greenKart Logo
  Scenario: Logo presence on greenKart Home page
    Given launch chrome browser
    When open greenKart Home page
    Then verify that the searchbar present on the page
    And close browser