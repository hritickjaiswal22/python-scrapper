import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

path = "...your path..."
web = "https://www.realestate.com.au/buy/in-epping,+vic+3076/list-1"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)

# xpath for property listing : //ul[contains(@class, 'tiered-results tiered-results--exact')]//li[div[@role="presentation"]//article]//article

properties = driver.find_elements(
    by="xpath",
    value=
    "//ul[contains(@class, 'tiered-results tiered-results--exact')]//li[div[@role='presentation']//article]//article"
)

# xpath for price : //span[contains(@class,"property-price ")]
# xpath for address : //a[contains(@class,"details-link residential-card__details-link")]//span
# xpath for bedrooms : //div[contains(@class, 'View__PropertyDetail-sc-11ysrk6-0 haFtfe')][contains(@aria-label, 'bedroom') or contains(@aria-label, 'bedrooms')]
# xpath for bathroom : //div[contains(@class, 'View__PropertyDetail-sc-11ysrk6-0 haFtfe')][contains(@aria-label, 'bathroom') or contains(@aria-label, 'bathrooms')]

priceList = []
addressList = []
bedroomList = []
bathroomList = []

for property in properties:
  priceList.append(
      property.find_element(
          by="xpath",
          value=".//span[contains(@class, 'property-price')]").text)

  addressList.append(
      property.find_element(
          by="xpath",
          value=
          ".//a[contains(@class, 'details-link residential-card__details-link')]//span"
      ).text)

  bedroomList.append(
      property.find_element(
          by="xpath",
          value=
          ".//div[contains(@class, 'View__PropertyDetail-sc-11ysrk6-0 haFtfe')][contains(@aria-label, 'bedroom') or contains(@aria-label, 'bedrooms')]"
      ).text)

  bathroomList.append(
      property.find_element(
          by="xpath",
          value=
          ".//div[contains(@class, 'View__PropertyDetail-sc-11ysrk6-0 haFtfe')][contains(@aria-label, 'bathroom') or contains(@aria-label, 'bathrooms')]"
      ).text)

driver.quit()

data = pd.DataFrame({
    "priceRange": priceList,
    "address": addressList,
    "bedroom": bedroomList,
    "bathroom": bathroomList
})

data.to_csv("properties_info", index=False)
