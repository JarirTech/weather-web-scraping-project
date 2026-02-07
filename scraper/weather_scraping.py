

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import sleep


options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # headless mode
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
options.add_argument('--disable-gpu') 
options.add_argument('--window-size=1920x1080') 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)



#Part1:  Web Scraping
# Uses Selenium to retrieve data from the web.
# Handles common scraping challenges like missing tags, pagination, and user-agent headers.
# Saves raw data as a CSV.
# Avoids scraping duplication or redundant requests.
# Data Cleaning & Transformation
# Loads raw data into a Pandas DataFrame.
# Cleans missing, duplicate, or malformed entries effectively.
# Applies appropriate transformations, groupings, or filters.
# Shows before/after stages of cleaning or reshaping.

#city     country     Time    weather_condition   temperature

url = "https://www.timeanddate.com/weather/"
driver.get(url)
sleep(10)

scraped_data = []

# tabble CSS_SELECTOR'table tbody tr'
#tag_name'td'
# 1st => city  2d=>date   3d => condition  4th => temperature 
cities = []
countries = []
date_data =[]
weather_condition = []
temperature =[]
#rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
td_data = driver.find_elements(By.TAG_NAME, 'td')
sleep(5)


td_data = driver.find_elements(By.TAG_NAME, 'td')

for item in range(0, len(td_data), 4):

    # CITY + COUNTRY
    city_link = td_data[item].find_element(By.TAG_NAME, "a")
    city_name = city_link.text
    href = city_link.get_attribute("href")

    country = href.split("/")[4]   # https://www.timeanddate.com/weather/ghana/accra
                                   # index 4 =>ghana

    cities.append(city_name)
    countries.append(country)

    # DATE / TIME
    date_data.append(td_data[item + 1].text)

    # WEATHER CONDITION (from img alt)
    img = td_data[item + 2].find_element(By.TAG_NAME, "img")
    weather_condition.append(img.get_attribute("alt"))

    # TEMPERATURE
    temperature.append(td_data[item + 3].text)



# sleep(3)  

# print(cities)
# print('length of cities:\n')
# print(len(cities))



# print(countries)
# print('length of countries:\n')
# print(len(countries))



# print(date_data)
# print('length of date:\n')
# print(len(date_data))


# print(weather_condition)
# print('length of weather_condition:\n')
# print(len(weather_condition))

# print(temperature)
# print('length of temperature:\n')
# print(len(temperature))
#------------------------------------------------------------------------------
# save data as csv

scraped_data = pd.DataFrame({
    "City": cities,
    "Country": countries,
    "Date": date_data,
    "Weather Condition": weather_condition,
    "Temperature": temperature
})


scraped_data.to_csv("weather_data.csv", index=False)
#print("data saved to weather_data.csv")




driver.quit()