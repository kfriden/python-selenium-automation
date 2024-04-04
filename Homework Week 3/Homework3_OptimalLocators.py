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


# Creating Optimal Locators

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

# Create Account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Name input field
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

# Mobile/email input field
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# Password input field
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

# Password must contain text
driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least 6 characters')]")

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

# Continue/create account button
driver.find_element(By.CSS_SELECTOR, "input#continue")

# Conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")