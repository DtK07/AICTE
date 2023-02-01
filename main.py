from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re

url = "https://facilities.aicte-india.org/dashboard/pages/dashboardaicte.php"
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options = chrome_options)
driver.get(url)
time.sleep(4)

year_btn = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[1]/div[1]/div/button' )
year_btn.click()
year = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[1]/div[1]/div/div/ul/li/label/input[@value = "10"]' )
print(year.text)
year.click()
program_btn = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[1]/div[2]/div/button' )
program_btn.click()
all_btn_program = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[1]/div[2]/div/div/ul/li[1]')
all_btn_program.click()
engineering = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[1]/div[2]/div/div/ul/li[9]')
engineering.click()
program_btn.click()
level = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[2]/div[1]/div/button')
level.click()
all_btn_level = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[2]/div[1]/div/div/ul/li[1]')
all_btn_level.click()
driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[2]/div[1]/div/div/ul/li[2]').click()
driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[2]/div[1]/div/div/ul/li[3]').click()
level.click()
state = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[3]/div[1]/div/button')
state.click()
all_btn_state = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/form/div[3]/div[1]/div/div/ul/li[1]')
all_btn_state.click()
state.click()
lst = []
i = 2
while i < len(driver.find_elements(By.XPATH, '//input[@data-name = "selectItemstate"]'))+2:
    state.click()
    if i != 2:
        try:
            driver.find_element(By.XPATH, f'//*[@id="dashboard"]/div[2]/form/div[3]/div[1]/div/div/ul/li[{i-1}]').click()
        except:
            pass
    curr_state = driver.find_element(By.XPATH, f'//*[@id="dashboard"]/div[2]/form/div[3]/div[1]/div/div/ul/li[{i}]')
    states = curr_state.text
    print(states)
    curr_state.click()
    state.click()
    submit_btn = driver.find_element(By.XPATH, '//*[@id="loaded"]')
    submit_btn.click()
    time.sleep(8)
    dict = {"State": states,
            "total_inst" : driver.find_element(By.XPATH, '//*[@id="instcount"]').text,
            "new_inst":  driver.find_element(By.XPATH, '//*[@id="newinstitute"]').text,
            "closed_inst": driver.find_element(By.XPATH, '//*[@id="closedinstitute"]').text,
            "total_intake" : driver.find_element(By.XPATH, '//*[@id="intake"]').text,
            "girls_enrol": driver.find_element(By.XPATH, '//*[@id="girls"][2]').text,
            "boys_enrol": driver.find_element(By.XPATH, '//*[@id="boys"][2]').text,
            "faculties": driver.find_element(By.XPATH, '//*[@id="faculty"]').text,
            "pass_out" : driver.find_element(By.XPATH, '//*[@id="studentpassed"][2]').text,
            "placed ": driver.find_element(By.XPATH, '//*[@id="placement"]').text
            }
    lst.append(dict)
    i += 1
print(lst)
df = pd.DataFrame(lst)
with pd.ExcelWriter('Aicte_Dash.xlsx', engine='openpyxl', mode='a') as writer:
    df.to_excel(writer, sheet_name='2023', index= False)
driver.close()






