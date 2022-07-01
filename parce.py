import sqlite3

from selenium import webdriver
from selenium.webdriver.common.by import By

from consts import *


def parce():
    options = webdriver.ChromeOptions()
    options.add_argument(OPTION_1)
    options.add_argument(OPTION_2)
    options.add_argument(OPTION_3)
    options.add_argument(OPTION_4)

    driver = webdriver.Chrome(
        executable_path=NAME_DRIVER,
        options=options
    )

    driver.get(PATH_WEBSITE)
    driver.implicitly_wait(30)

    table_1 = driver.find_element(By.XPATH, TABLE_1)
    body_table = table_1.find_element(By.XPATH, TABLE_BODY_1)
    elements_table = body_table.find_elements(By.TAG_NAME, TABLE_TAG_TR)

    table_2 = driver.find_element(By.XPATH, TABLE_2)
    body_table = table_2.find_element(By.XPATH, TABLE_BODY_2)
    elements_table2 = body_table.find_elements(By.TAG_NAME, TABLE_TAG_TR)

    for element in elements_table:
        elements_td = element.find_elements(By.TAG_NAME, TABLE_TAG_TD)
        a_tag = elements_td[1].find_element(By.TAG_NAME, TABLE_TAG_A)

        city = elements_td[1].text
        city_href = a_tag.get_attribute(ATTRIBUTE_HREF)
        region = elements_td[2].text
        population = elements_td[4].text

        db = sqlite3.connect(DATA_BASE)

        cur = db.cursor()

        cur.execute(f"{COMMAND_SAVE} ('{city}','{city_href}','{region}','{population}')")

        db.commit()

        db.close()

    for element in elements_table2:
        elements_td = element.find_elements(By.TAG_NAME, TABLE_TAG_TD)
        a_tag = elements_td[1].find_element(By.TAG_NAME, TABLE_TAG_A)

        city = elements_td[1].text
        city_href = a_tag.get_attribute(ATTRIBUTE_HREF)
        region = elements_td[2].text
        population = elements_td[4].text

        db = sqlite3.connect(DATA_BASE)

        cur = db.cursor()

        cur.execute(f"{COMMAND_SAVE} ('{city}','{city_href}','{region}','{population}')")

        db.commit()

        db.close()

