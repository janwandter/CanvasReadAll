import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logs(course, title, detail):
    template = '{:^12} | {:^30} | {:^40} |'
    table = [course, title, detail]
    print(template.format(*table))

with open("parametros.json") as file:
    param = json.load(file)
with open("credentials.json") as file:
    credential = json.load(file)
PATH = "C:\Program Files (x86)\chromedriver.exe"
op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument('--disable-gpu')
op.add_argument("--log-level=3")
driver = webdriver.Chrome(PATH, options=op)
driver.get(f"https://cursos.canvas.uc.cl")
try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    username.send_keys(credential["username"] + Keys.RETURN)
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password.send_keys(credential["password"] + Keys.RETURN)
finally:
    pass
for curso in param["cursos"]:
    try:
        driver.get(f"https://cursos.canvas.uc.cl/courses/{curso}/announcements")
        content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content")))
        time.sleep(2)
        wrapper = content.find_elements_by_class_name("ic-item-row__content-col")
        for j in wrapper:
            if "no leídos" in j.text:
                pos = wrapper.index(j)
                txt = j.text
                txt = txt.split("\n")
                print(f"{param['cursos'][curso]} | {txt[1]}")
                print(txt[3])
                print("")
    finally:
        pass
       # driver.quit()



