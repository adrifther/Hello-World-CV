from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
import time
import io

# Initialize the Firefox webdriver
driver = webdriver.Firefox()

# Navigate to Kaggle website
driver.get("https://clinicaltrials.gov/")

# Clicar search
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/main/ctg-home/div/div[2]/ctg-home-search-panel/div/div[3]/div/div/button"))).click()

#numero elements per pàgina en aquest cas 100
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pageSizeOption"]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/main/ctg-search-results-page/div[2]/section/div[2]/div/div/ctg-search-results-list/div[2]/div/div/select/option[4]"))).click()


comptador = 0

while comptador < 50:
    comptador += 1
    
    # Cridar a next
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/main/ctg-search-results-page/div[2]/section/div[2]/div/div/ctg-search-results-list/div[2]/div/pagination-template/ctg-pagination-uswds/div/nav/ul/li[10]/button"))).click()
    
    element = driver.find_element(By.XPATH, "/html/body/app-root/main/ctg-search-results-page/div[2]/section/div[2]")

    element_text = element.text

    with io.open("clinicaltrials.txt", 'a', encoding="utf-8") as fitxer:
         fitxer.write( element_text+"\n")
    
        
driver.quit()
