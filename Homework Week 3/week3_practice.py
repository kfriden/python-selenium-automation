from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


# CSS Selectors, ID
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR,"select#searchDropdownBox")

# CSS Selectors, Class
driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR,".nav-input.nav-progressive-attribute")

# CSS Selector, Attribute
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR,"[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR,"select[aria-describedby='searchDropdownDescription']")

# CSS Selector, multiple attributes
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Amazon'][type='text']")

# CSS Selector, contains *=
driver.find_element(By.CSS_SELECTOR,"a[href*='topnav_lang']")
driver.find_element(By.CSS_SELECTOR,"h1[class*='StyledHeading']")




