# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import system
import time
import pandas as pd

b = False
inputTag = [0]

def inner_info(info):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[8]/div/div[3]/button[1]')))\
        .click()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[2]/input')))\
        .send_keys(info['NOMBRE'])
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[3]/input')))\
        .send_keys(info['APELLIDO'])
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[4]/input')))\
        .send_keys(info['CEDULA'])
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[5]/input')))\
        .send_keys(info['EMAIL'])
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[6]/div[1]/input')))\
        .send_keys(info['TEL'])
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[6]/div[2]/select')))\
        .click()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[6]/div[2]/select/option[2]')))\
        .click()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[8]/input')))\
        .click()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[3]/div/div[4]/form/div[9]/button')))\
        .click()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[8]/div/div[3]/button[1]')))\
        .click()
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[8]/div/div[3]/button[1]')))\
        .click()

    print('ESCRITO CON EXITO')

    
            #driver.refresh()
            #time.sleep(2)


# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'


info = {"NOMBRE": "Name", "APELLIDO":"Last_Name",
        "CEDULA": "000000", "EMAIL":"pruebaproject@gmail.com",
        "TEL":"3000000000"}



driver = webdriver.Chrome(driver_path, chrome_options=options)



# Inicializamos el navegador
driver.get('https://conectateconpomy.com/')
'''
system("cls")
driver.quit()
'''
#time.sleep(3)
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(1.5)

for i in range(31267,100000):
    
    p = str("Rx8-" + str(i).zfill(5))

    inputTag[0] = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/form/div[1]/input')

    if b:
        #inputTag[0].send_keys(Keys.CONTROL + "a")
        #inputTag[0].send_keys(Keys.DELETE)
        inputTag[0].clear()
    

    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[3]/div/div[3]/div/div/form/div[1]/input')))\
        .send_keys(p)

    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[3]/div/div[3]/div/div/form/div[2]/div/button')))\
        .click()

    #time.sleep(1)


    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[8]/div/div[1]/h2')))\

    respuesta = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/h2')
    respuesta = respuesta.text
    print(respuesta)

    if "Error" in respuesta:
        WebDriverWait(driver, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                                   '/html/body/div[8]/div/div[3]/button[1]')))\
            .click()
        
    elif 'Puedes' in respuesta:
            #inner_info(info)
        with open("positives.txt", "a") as g:
            d = p + "\n"
            g.write(d)
        b = False
        driver.refresh()
        time.sleep(2)
    else:
        print("No Found")
        system("pause")
    b = True     
    with open("flag.txt","w") as f:
        f.write(p)

driver.quit()