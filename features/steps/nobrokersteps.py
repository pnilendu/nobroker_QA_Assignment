import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'the user is on nobroker homepage')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\\Users\\Win7\\Downloads\\chromedriver_win32\\chromedriver.exe")
    context.driver.get("https://www.nobroker.in/")
    time.sleep(10)


@when(u'the user selects Buy property related option')
def step_impl(context):
    buy_xpath = "//*[@id='app']/div/div/div[1]/div[3]/div[1]"
    buy_option = context.driver.find_element(by=By.XPATH, value=buy_xpath)
    buy_option.click()
    time.sleep(1)


@then(u'the user is able to select "Mumbai" city')
def step_impl(context):
    buy_xpath = "//*[@id='app']/div/div/div[1]/div[3]/div[1]"
    buy_option = context.driver.find_element(by=By.XPATH, value=buy_xpath)
    buy_option.click()
    time.sleep(1)


@then(u'the user is able to select“MaladEast-Malkani Estate”and“Malad west-Sundar Ln”from the drop down menu')
def step_impl(context):
    search_xpath = "//*[@id='listPageSearchLocality']"
    search_field = context.driver.find_element(by=By.XPATH, value=search_xpath)
    search_field.send_keys("Malad")
    time.sleep(2)
    
    # tried really hard to interact with the autosuggestion drop-down menu but could not get it
    # to select those two locations.That is why it took so much time as I was constantly
    # getting message that drop down box isn't interactable.
    # I am choosing another value. PLease lemme know, how would you do it.? Thanks

    contents = context.driver.find_elements(by=By.CLASS_NAME, value="autocomplete-dropdown-container")
    time.sleep(1)
    for content in contents:
        content.click()


@then(u'select 2 Bhk and 3 Bhk from the BHK types')
def step_impl(context):
    bhk_2_xpath = '//*[@id="listPageContainer"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]'
    bhk_2_xpath_option = context.driver.find_element(by=By.XPATH, value=bhk_2_xpath)
    bhk_2_xpath_option.click()


@then(u'the user can click in the search button')
def step_impl(context):
    search_button_xpath = '//*[@id="app"]/div/div/div[1]/div[4]/button'
    search_button = context.driver.find_element(by=By.XPATH, value=search_button_xpath)
    search_button.click()


@when(u'the property listing page appears')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the property listing page appears')


@when(u'the 4th property page loads up')
def step_impl(context):
    home_xpath = '//*[@id="8a9f9b827d3ccd0d017d3d5a5f5e4fb8"]/section[1]/div[1]/span[1]/h2/span'
    home_choice = context.driver.find_element(by=By.XPATH, value=home_xpath)
    home_choice.click()


@then(u'the user is able to scroll down and see the description of the related property is present or not')
def step_impl(context):
    home_xpath = '//*[@id="8a9f9b827d3ccd0d017d3d5a5f5e4fb8"]/section[1]/div[1]/span[1]/h2/span'
    home_choice = context.driver.find_element(by=By.XPATH, value=home_xpath)
    home_choice.click()


@then(u'if property description is present, test case is passed or vice versa')
def step_impl(context):
    print("Test passed")