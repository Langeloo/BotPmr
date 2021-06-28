# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import system
import time
import pandas as pd

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'


info = {"NOMBRE": "Miguel Anguel", "APELLIDO":"Ramirez Bonilla",
        "CEDULA": "1003751809", "EMAIL":"miguelitoramirez02.2@gmail.com",
        "TEL":"3212854076"}


driver = webdriver.Chrome(driver_path, chrome_options=options)
'''
# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)
'''
# Inicializamos el navegador
driver.get('https://conectateconpomy.com/')
'''
system("cls")
driver.quit()
'''
#time.sleep(3)
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(1.5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#codigo1'.replace(' ', '.'))))\
    .send_keys('Rx4-19850')


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.boton-fondo btn-lg d-flex align-items-center justify-content-center'.replace(' ', '.'))))\
    .click()
time.sleep(1)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[8]/div/div[1]/h2')))
respuesta = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/h2')
respuesta = respuesta.text
print(respuesta)\

if "Error" in respuesta:
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[8]/div/div[3]/button[1]')))\
        .click()
    #time.sleep(2)
    #driver.refresh()
elif 'Puedes' in respuesta:
    print('Aqui es cuando si encuentra un codigo')
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

    print('ESCRITO CON EXITO')
else:
    print("No Found")

'''
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.icon_weather_s.icon.icon-local')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div/article/section/ul/li[2]/a')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')))

texto_columnas = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')
texto_columnas = texto_columnas.text

tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

horas = list()
temp = list()
v_viento = list()

for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    v_viento.append(tiempo_hoy[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'V_viento(km_h)':v_viento})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()
'''
'''



for i in range(1,100000):
    print("Rx8-"+str(i).zfill(5))
'''
