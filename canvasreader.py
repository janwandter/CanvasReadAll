import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        not_read = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "no leídos")))
        #print(content.text)
        print(not_read.text)
    finally:
        driver.quit()
    time.sleep(5)

