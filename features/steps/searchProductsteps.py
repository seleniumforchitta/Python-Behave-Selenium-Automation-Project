import time

from behave import *
from selenium.webdriver.common.by import By


@when('search product "{productName}"')  # We need to put curley braces to treat it as arguments
def searchProduct(context, productName):  # We need to pass the same positional arguments here
    context.driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys(productName)
    time.sleep(4)


@when('select all the searched products')
def selectProducts(context):
    products = context.driver.find_elements(By.XPATH, "//div[@class='products']/div")
    product_count = len(products)
    try:
        assert product_count > 0
    except:
        context.driver.close()
        assert False, "Test Failed"
    for product in products:
        product.find_element(By.XPATH, "div/button").click()


@then('User must see the products in the kart')
def productsInKart(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
        status = context.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"

    assert status is True
