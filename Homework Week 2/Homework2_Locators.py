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

# Creating Locators - Amazon Sign In Page

# Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email Field
driver.find_element(By.XPATH, "//input[@id='ap_email']")

# Continue Button
driver.find_element(By.XPATH, "//input[@id='continue']")

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice Link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Need Help Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password Link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-in Link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")