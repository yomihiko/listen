import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as Keys
from selenium import webdriver

driver = webdriver.Chrome('C:\\webDriver\\bin\\chromedriver.exe')  # Optional argument, if not specified will search path.
# Navigate to url
driver.get("https://www.google.com")

# Returns and base64 encoded string into image
driver.save_screenshot('C:\\webDriver\\bin\\image.png')
time.sleep(3)
driver.quit()
