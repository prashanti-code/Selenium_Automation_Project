from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# --------------------------
# Setup WebDriver (Chrome)
# --------------------------
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# --------------------------
# 1. Open Amazon Website
# --------------------------
driver.get("https://www.amazon.com")
# --------------------------
# 2. Locate Search Box
# --------------------------
search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
# --------------------------
# 3. Enter Search Term
# --------------------------
search_term = "laptop"
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)
# --------------------------
# 4. Wait for Results to Load
# --------------------------
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
# --------------------------
# 5. Extract Product Titles
# --------------------------
product_titles = driver.find_elements(By.CSS_SELECTOR, "h2 a span")
print("\nTop 5 Amazon Search Results:\n")
for i, title in enumerate(product_titles[:5], start=1):
    print(f"{i}. {title.text}")
# --------------------------
# Close Browser
# --------------------------
driver.quit()
