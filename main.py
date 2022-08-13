import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:\Development/chromedriver.exe"
SIMILAR_ACCOUNT = "python.learning"
USERNAME = "*****************"
PASSWORD = "************"
INSTAGRAM_LOGIN = " https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self, login_url):
        self.driver.get(login_url)
        accept_cookies = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]')
        accept_cookies.click()
        time.sleep(2)
        enter_email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        enter_email.send_keys(USERNAME)
        enter_password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        enter_password.send_keys(PASSWORD)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        log_in.click()

    def find_followers(self):
        time.sleep(6)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="mount_0_0_o5"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        time.sleep(2)
        fl = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fl)
            time.sleep(3)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for follow_button in follow_buttons:
            try:
                follow_button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(INSTAGRAM_LOGIN)
bot.find_followers()
bot.follow()
