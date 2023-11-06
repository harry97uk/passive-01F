from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def youtube_search(username):
    # Set up the web driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no browser window)
    driver = webdriver.Chrome(options=options)
    driver.get("https://youtube.com/@{}".format(username))

    # Wait for the privacy consent pop-up to appear and click the "Accept all" button
    wait = WebDriverWait(driver, 5)
    try:
        reject_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Reject all"]')))
        reject_button.click()
    except Exception as e:
        print("Could not find the 'Reject all' button.")
        driver.quit()
        return

    # Wait for the content to load
    #wait.until(EC.presence_of_element_located((By.ID, "content")))

    # Get the page content
    page_content = driver.page_source

    # Close the web driver
    driver.quit()

    # Process the page content as needed (e.g., with BeautifulSoup)
    features = "html.parser"
    soup = BeautifulSoup(page_content, features)

    data = soup.find_all('title')

    found = not data.__contains__("<title>404 Not Found</title>")

    return found

