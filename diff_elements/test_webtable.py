import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_table():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(30)
    driver.get("https://qavbox.github.io/demo/webtable/")
    driver.maximize_window()

    assert "webtable" in driver.title
    table = driver.find_element(By.ID,"table01" )
    table_rows = table.find_elements(By.TAG_NAME, "tr")
    print("rows - " + str(len(table_rows)))

    for i in range(len(table_rows)):
        table_columns = table_rows[i].find_elements(By.TAG_NAME, "td")

        for j in range(len(table_columns)):
            # print(table_columns[j].text)
            if table_columns[j].text == "TFS":
                table_columns[0].click()

    time.sleep(5)
    driver.quit()
