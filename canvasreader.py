import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
with open("parametros.json") as file:
    param = json.load(file)
with open("credentials.json") as file:
    credential = json.load(file)
for curso in param["cursos"]:
    driver.get(f"https://cursos.canvas.uc.cl/courses/{curso}")
    #Clase no leido: fOyUs_bGBk fOyUs_cuDs cnWSA_bcSS cnWSA_KksD cnWSA_bXiG cnWSA_dDWY cnWSA_bXgF cnWSA_bBTa
    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))
        username.send_keys(credential["username"] + Keys.RETURN)
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password")))
        password.send_keys(credential["password"] + Keys.RETURN)

        #content = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.ID, "content")))
    #print(driver.find_elements_by_tag_name(f"no leído"))
    finally:
        driver.close()
    time.sleep(5)

