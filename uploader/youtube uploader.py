from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--no-sandbox')
driver = webdriver.Firefox()
driver.implicitly_wait(5) # Wait up 5 sec before throwing an error if selenium cannot find the element (!important)
driver.get("https://www.youtube.com/upload")
elem = driver.find_element_by_xpath("//input[@type='file']")
elem.send_keys("0.mp4"); # Window$