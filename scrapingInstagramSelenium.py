from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from dotenv import load_dotenv
from pathlib import Path
import os
import time

dotenv_path = Path("./config.env")

load_dotenv(dotenv_path=dotenv_path)
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

driver = webdriver.Firefox()
driver.get("https://instagram.com")
doubleClickAction = ActionChains(driver)

usernameElement = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username")))
usernameElement.send_keys(INSTAGRAM_USERNAME)

passwordElement = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))
passwordElement.send_keys(INSTAGRAM_PASSWORD)
passwordElement.send_keys(Keys.RETURN)

notNowElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, "//button[contains(text(),'Not Now')]")))
notNowElement.click()

notNowNotificationsButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Not Now')]")))
notNowNotificationsButton.click()

profileButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, "//a[contains(text(),'scrappybot2')]")))
profileButton.click()

followingButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'following')]")))
followingButton.click()

followingProfiles = []
followingProfiles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")))

# This can be change to  the amount of followers you would  like to iterate through
followingNumber = 7
iteratorFollowing = 0

focusWindow = driver.current_window_handle
parentWindow = driver.window_handles[0]


for followee in followingProfiles:
    if iteratorFollowing < followingNumber:

        ActionChains(driver).key_down(Keys.CONTROL).click(
            followee).key_up(Keys.CONTROL).perform()

        iteratorFollowing += 1
    # doubleClickAction.keyDown(Keys.LEFT_CONTROL).click(followee) #doubleClickAction.double_click(followee).perform() to perform double clicks
postVideos = []
videoLinks = []
for iterateTabs in range(1, followingNumber):

    childWindow = driver.window_handles[iterateTabs]
    driver.switch_to.window(childWindow)
    driver.execute_script("window.scrollTo(0,4000);")

    postVideos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']")))
    for post in postVideos:
        if post.find_element(By.XPATH, ".//svg[@aria-label='Clip']") is True:
            videoLinks.append(post.get_attribute('href'))
            print(videoLinks)
        else:
            continue
    print(videoLinks)
    # print(vid
    # if videos is None:
    #    continue

    time.sleep(5)
