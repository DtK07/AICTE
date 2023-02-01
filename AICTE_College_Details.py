from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

url = "https://facilities.aicte-india.org/dashboard/pages/angulardashboard.php#!/approved"

#Initiationg the webdriver
driver = webdriver.Chrome()
driver.get(url)
#driver.maximize_window()
driver.implicitly_wait(10)

#dropdown which contains states
states = driver.find_element(By.ID,"state")
state_dropdown = Select(states)
state_all_options = state_dropdown.options
#store the elements in the dropdown in a list so that we can iterate through all the states and collect the data
states_list =[]
for option in state_all_options:
    states_list.append(option.text)

#dropdown which contains programme
program = driver.find_element(By.ID,"program")
program_dropdown = Select(program)
program_dropdown.select_by_visible_text("Management")
program_all_options = program_dropdown.options

'''#dropdown which contains level
level = driver.find_element(By.ID, "level")
level_dropdown = Select(level)
level_dropdown.select_by_visible_text("DIPLOMA")'''

for state in states_list:
    print(state)
    state_dropdown.select_by_visible_text(state)
    time.sleep(3)
    button = driver.find_element(By.XPATH, '//*[@id="load"]')
    driver.execute_script("arguments[0].click();", button)
    entries = driver.find_element(By.NAME, "jsontable_length")
    entries_dropdown = Select(entries)
    entries_dropdown.select_by_visible_text("50")
    time.sleep(3)
    total_entries = []
    page_span = driver.find_elements(By.XPATH, '//*[@id="jsontable_paginate"]/span/a')
    try:
        total_pages = int(page_span[-1].text)
        print("Total Pages:", total_pages)
    except:
        pass
    if total_pages == 1:
        current_page = driver.find_element(By.CSS_SELECTOR, '#jsontable_paginate > span > a.paginate_button.current').text
        print("Current Page:", current_page)
        # next_page = int(driver.find_element(By.CSS_SELECTOR, '#jsontable_paginate > span > a.paginate_button.current').text) + 1
        # print(driver.find_element(By.CSS_SELECTOR, '#jsontable_paginate > span > a.paginate_button.current').text)
        # print(page.text)
        time.sleep(3)
        # clickhere elements to get course details
        click_here_elements = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[8]/button')
        # close button for clickhere menu
        close_button = driver.find_element(By.XPATH, '//button[@class="w3-button w3-large w3-red w3-right"]')
        time.sleep(3)
        for element in click_here_elements:
            # time.sleep(3)
            driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
            course_entries = driver.find_element(By.NAME, "coursetable_length")
            course_entries_dropdown = Select(course_entries)
            course_entries_dropdown.select_by_visible_text("50")
            time.sleep(3)
            aicte_id = driver.find_element(By.XPATH, '//div[@id="coursetitles"]').text
            programme = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[1]')
            university = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[2]')
            course_level = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[3]')
            course = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[4]')
            intake = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[5]')
            enrollment = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[6]')
            placement = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[7]')
            for entry in range(len(programme)):
                total_entries_dict = {"Aicte_id": aicte_id,
                                      "Programme": programme[entry].text,
                                      "university": university[entry].text,
                                      "course_level": course_level[entry].text,
                                      "course": course[entry].text,
                                      "intake": intake[entry].text,
                                      "enrollment": enrollment[entry].text,
                                      "placement": placement[entry].text,
                                      "state": state}
                # print(total_entries_dict)
                total_entries.append(total_entries_dict)
                # print(total_entries)
        driver.execute_script("arguments[0].click();", close_button)
        # print(total_entries)
        time.sleep(3)
    else:
        for page in range(total_pages):
        #while not IsNextdisabled:
            current_page = driver.find_element(By.CSS_SELECTOR, '#jsontable_paginate > span > a.paginate_button.current').text
            print("Current Page:",current_page)
            next_page = int(driver.find_element(By.CSS_SELECTOR, '#jsontable_paginate > span > a.paginate_button.current').text)+1
            #print(driver.find_element(By.CSS_SELECTOR, '#jsontable_paginate > span > a.paginate_button.current').text)
            #print(page.text)
            time.sleep(3)
            # clickhere elements to get course details
            click_here_elements = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[8]/button')
            # close button for clickhere menu
            close_button = driver.find_element(By.XPATH, '//button[@class="w3-button w3-large w3-red w3-right"]')
            time.sleep(3)
            for element in click_here_elements:
                #time.sleep(3)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
                course_entries = driver.find_element(By.NAME, "coursetable_length")
                course_entries_dropdown = Select(course_entries)
                course_entries_dropdown.select_by_visible_text("50")
                time.sleep(5)
                aicte_id = driver.find_element(By.XPATH, '//div[@id="coursetitles"]').text
                programme = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[1]')
                university = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[2]')
                course_level = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[3]')
                course = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[4]')
                intake = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[5]')
                enrollment = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[6]')
                placement = driver.find_elements(By.XPATH, '//table[@id="coursetable"]/tbody/tr/td[7]')
                for entry in range(len(programme)):
                    total_entries_dict = {"Aicte_id": aicte_id,
                                          "Programme": programme[entry].text,
                                          "university": university[entry].text,
                                          "course_level": course_level[entry].text,
                                          "course": course[entry].text,
                                          "intake": intake[entry].text,
                                          "enrollment": enrollment[entry].text,
                                          "placement": placement[entry].text,
                                          "state": state}
                    #print(total_entries_dict)
                    total_entries.append(total_entries_dict)
                    #print(total_entries)
            driver.execute_script("arguments[0].click();", close_button)
            #print(total_entries)
            try:
                next_page_click = driver.find_element(By.XPATH, f'//a[text()="{next_page}"]')
                driver.execute_script("arguments[0].click();", next_page_click)
            except:
                pass
            time.sleep(3)
df = pd.DataFrame(total_entries)
df.to_excel("Aicte_Mgmt.xlsx", sheet_name="Engineering And Technology", index=False)
print(df)
