from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBroswer(context):
    service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
    context.driver = webdriver.Chrome(service=service_obj)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@when('open greenKart Home page')
def openHomePage(context):
    #context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


@then('verify that the searchbar present on the page')
def verifyLogo(context):
    #status = context.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-branding']/img").is_displayed()
    status = context.driver.find_element(By.CSS_SELECTOR, "input.search-keyword").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
    #test
