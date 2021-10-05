# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:48:03 2021
@author: johnn
"""

# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import requests
from datetime import datetime
import time
#import sys
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.remote.webelement import WebElement

scheduler = BlockingScheduler()
def hello():
	#啟動時間設定年、月、日、時、分、秒
	# startTime = datetime(2021, 4, 16, 11, 59, 59)
	# print('Program not starting yet...')
	# while datetime.now() < startTime:
	# 	time.sleep(1)
	# print('Program now starts on %s' % startTime)
	print('Executing...')
	
	#如果使用headless會幫助跑的速度，因為不用顯示出來
	option = webdriver.ChromeOptions()
	# prefs = {"profile.managed_default_content_settings.images": 2}
	# option.add_experimental_option("prefs", prefs)
	#option.add_argument('headless')
	option.add_argument("--lang=en")
	driver = webdriver.Chrome(chrome_options=option,executable_path='./chromedriver.exe')
	# 
	#這邊放商品網址
	url = 'http://tplinkwifi.net/'

	driver.get(url)

	time.sleep(1)
	account = driver.find_element_by_id('userName')
	account.clear()
	account.send_keys('zack1007x2')

	password = driver.find_element_by_id('pcPassword')
	password.clear()
	password.send_keys('22642218') 
	driver.find_element_by_id('loginBtn').click()
	
	# time.sleep(5)
	driver.implicitly_wait(5)
	driver.switch_to.frame("mainFrame")
	driver.find_element_by_id('Disconnect').click()
	driver.implicitly_wait(5)
	driver.find_element_by_id('Connect').click()
	time.sleep(5)
	# try:
	# 	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='button'][id='Disconnect']"))).click()
	# except TimeoutException:
	#     print("err1")
	# try:
	# 	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='button'][id='Connect']"))).click()
	# except TimeoutException:
	#     print("err2")

	driver.quit()

    
hello()
scheduler.add_job(hello, 'interval', hours=1)
scheduler.start()
