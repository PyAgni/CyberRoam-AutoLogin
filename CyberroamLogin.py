#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import sys,time

#check if username and password are passed as arguments
if(len(sys.argv)>2):
    userName = sys.argv[1]
    password = sys.argv[2]

#If no arguments are passed then ask user to enter details
else:
    userName = input('Enter username : ')
    password = getpass('Enter password : ')     

#Launch the browser
browser = webdriver.Firefox()

#Open Cyberroam url
browser.get('https://172.16.1.1:8090/')

time.sleep(2)

#Find the input boxes using xpath of the elements
userNameBox = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/input')
passwordBox = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input')

userNameBox.clear()
passwordBox.clear()

#Enter the username and password
userNameBox.send_keys(userName)
passwordBox.send_keys(password)

#Locate the login button using id
loginBtn = browser.find_element_by_id('logincaption')

#Click the login button
loginBtn.click()

if "You have successfully logged in" in browser.page_source:
    print("done!")
else:
    print('Please Enter correct details and try again! ')               #This would be automated in future commits soon

time.sleep(3)

browser.quit()
