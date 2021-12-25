from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5) # Wait up 5 sec before throwing an error if selenium cannot find the element (!important)
driver.get("https://www.youtube.com/upload")
elem = driver.find_element_by_xpath("//input[@id='identifierId']")
elem.send_keys("yauto619"); # Window$
elem.send_keys(Keys.ENTER)

elem = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
elem.send_keys("qwe123~!@"); # Window$
elem.send_keys(Keys.ENTER)

try:
    xpath_continue = '//*[@id="dismiss-button"]/div'
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_continue)))
    driver.find_element_by_xpath(xpath_continue).click()

except:
    print("Didn't find Welcome Screen")

elem = driver.find_element_by_xpath("//input[@type='file']")
elem.send_keys("d:/uploader/0.mp4"); # Window$
