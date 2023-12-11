Feature: greenKart select product

  Scenario: select product from greenKart
    Given launch chrome browser
    When open greenKart Home page
    And search product "ber"
    And select all the searched products
    Then  User must see the products in the kart
    And Close Browser

  Scenario Outline: select product from greenKart
    Given launch chrome browser
    When open greenKart Home page
    And search product "<name>"
    And select all the searched products
    Then  User must see the products in the kart
    And Close Browser

    Examples:
      | name |
      | cau  |
      | ca   |
      | to   |