Feature: greenKart select product using background

  Background:
    Given launch chrome browser

  Scenario: select ber from greenKart
    When open greenKart Home page
    And search product "ber"
    And select all the searched products
    Then  User must see the products in the kart
    And Close Browser

  Scenario: select ca from greenKart
    When open greenKart Home page
    And search product "ca"
    And select all the searched products
    Then  User must see the products in the kart
    And Close Browser

  Scenario: select to from greenKart
    When open greenKart Home page
    And search product "to"
    And select all the searched products
    Then  User must see the products in the kart
    And Close Browser