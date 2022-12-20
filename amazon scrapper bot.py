from selenium import webdriver
from selenium.webdriver.common.by import By

search_term = input("Enter Your Search Term:- ")

driver = webdriver.Edge()
driver.get('https://www.amazon.in')

driver.find_element(by=By.ID,value= 'twotabsearchtextbox').send_keys(search_term)
driver.find_element(by=By.ID,value='nav-search-submit-button').click()

products = driver.find_elements(by=By.XPATH,value='//div[@data-component-type="s-search-result"]')

for product in products:
    try:
        product.find_element(by=By.TAG_NAME,value='a').click()
        driver.switch_to.window(driver.window_handles[1])

        try:
            title = driver.find_element(by=By.ID,value='productTitle').text
        except:
            title = "Not Available"
        try:
            mrp = driver.find_element(by=By.XPATH,value='//span[@class="a-price a-text-price"]').text
        except:
            mrp = "Not Available"
        try:
            price = driver.find_element(by=By.XPATH,value='//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]').text
        except:
            price = "Not Available"
        try:
            discount = driver.find_element(by=By.XPATH,value='//span[@class="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"]').text
            discount = str((-1)*int(discount[:3]))+discount[3:]
        except:
            discount = "Not Available"
        try:
            availability = driver.find_element(by=By.ID,value='availability').text
        except:
            availability = "Not Present"

        print(f"Title:- {title}")
        print(f"MRP:- {mrp}")
        print(f"Price:- {price}")
        print(f"Discount:- {discount}")
        print(f"Availability:- {availability}")
        print(f"Url:- {driver.current_url}")

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        print('\n')
