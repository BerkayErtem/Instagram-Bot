from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import *
from info import username, password
from info import username, password
import time
import requests


class instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/?hl=tr")
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    @property
    def getFollowers(self):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)
        fb = self.browser.find_element_by_css_selector('ul li a')
        fb.click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerscount = len(dialog.find_elements_by_css_selector("li"))
        followers = dialog.find_elements_by_css_selector("li")
        print(followerscount)

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            count = len(dialog.find_elements_by_css_selector("li"))
            if followerscount != count:
                followerscount = count
                print(count)

                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()


            else:
                break

            followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            list = user.find_element_by_css_selector("a").get_attribute("href")
            print(list)




ig = instagram(username, password)
ig.signIn()
ig.getFollowers
