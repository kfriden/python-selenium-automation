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
driver.get('https://www.target.com/')


# click signin button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

# wait for 4 sec
sleep(4)

# click signin button
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

# wait for 3 sec
sleep(3)

# verification
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
print(actual_text)