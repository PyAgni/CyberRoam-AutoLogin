#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import sys,time


if(len(sys.argv)>1):
    userName = sys.argv[1]
    password = sys.argv[2]

else:
    userName = input('Enter username : ')
    password = getpass('Enter password : ')     

browser = webdriver.Firefox()
browser.get('https://172.16.1.1:8090/')
time.sleep(2)
userNameBox = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/input')
passwordBox = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input')

userNameBox.clear()
passwordBox.clear()

userNameBox.send_keys(userName)
passwordBox.send_keys(password)

loginBtn = browser.find_element_by_id('logincaption')

loginBtn.click()

if "You have successfully logged in" in browser.page_source:
    print("done!")
else:
    print('Please Enter correct details and try again! ')

time.sleep(3)

browser.quit()
