from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Initiating options for a webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument('--headless')
url = "https://facilities.aicte-india.org/dashboard/pages/angulardashboard.php#!/approved"
#Initiationg the webdriver
driver = webdriver.Chrome(options= options)
driver.get(url)
time.sleep(10)
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
program_all_options = program_dropdown.options
for elem1 in program_all_options:
    if elem1.text == "MCA":
        elem1.click()
        break
#dropdown which contains gender
'''gender = driver.find_element(By.ID,"Women")
gender_dropdown = Select(gender)
gender_all_options = gender_dropdown.options
for elem2 in gender_all_options:
    if elem2.text == "Y":
        elem2.click()
        break
time.sleep(5)'''
#dropdown which contains program level
'''level = driver.find_element(By.ID, "level")
level_dropdown = Select(level)
level_dropdown.select_by_visible_text("PG")'''
total_entries_list = []
for state in states_list:
    state_dropdown.select_by_visible_text(state)
    time.sleep(5)
    button = driver.find_element(By.XPATH ,'//*[@id="load"]')
    driver.execute_script("arguments[0].click();", button)
    entries = driver.find_element(By.NAME, "jsontable_length")
    entries_dropdown = Select(entries)
    entries_dropdown.select_by_visible_text("50")
    time.sleep(5)
    IsNextdisabled = False
    page_no = 1
    while not IsNextdisabled:
        #while not IsNextdisabled:
        time.sleep(5)
        aicte_id = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[1]')
        college_name = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[2]')
        address = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[3]')
        district = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[4]')
        college_type = driver.find_elements(By.XPATH, '//table[@id="jsontable"]/tbody/tr/td[5]')
        for entry in range(len(college_name)):
            total_entries_dict = {"Aicte_Id" : aicte_id[entry].text,
                                  "College_Name": college_name[entry].text,
                                  "Address" : address[entry].text,
                                  "District": district[entry].text,
                                  "College_Type": college_type[entry].text,
                                  "State": state }
            total_entries_list.append(total_entries_dict)
        time.sleep(5)
        try:
            driver.find_element(By.XPATH, '//a[@class = "paginate_button next"]').click()
            print("Next Button found")
            print("page_no:", page_no)
            page_no = page_no + 1
        except:
            IsNextdisabled = True
            print("Next Button Not Found")
    df = pd.DataFrame(total_entries_list)
    df.to_excel("Aicte.xlsx", sheet_name ="Management", index=False)
    print(df)






