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
for curso in param["cursos"]:
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(f"https://cursos.canvas.uc.cl/courses/{curso}/announcements")
    #Clase no leido: fOyUs_bGBk fOyUs_cuDs cnWSA_bcSS cnWSA_KksD cnWSA_bXiG cnWSA_dDWY cnWSA_bXgF cnWSA_bBTa
    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))
        username.send_keys(credential["username"] + Keys.RETURN)
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password")))
        password.send_keys(credential["password"] + Keys.RETURN)
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
        driver.quit()



