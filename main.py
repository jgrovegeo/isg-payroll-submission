from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import config
import time

PATH = '/usr/bin/chromedriver'
url = 'https://portal.insightglobal.com/Candidate/#!/timesheet/manage/4559609'
username = config.username
password = config.password

driver = webdriver.Chrome(PATH)
driver.get(url)

usr_name = driver.find_element_by_id('ctl00_cphMain_logIn_UserName')
usr_name.send_keys(username)

usr_pass = driver.find_element_by_id('ctl00_cphMain_logIn_Password')
usr_pass.send_keys(password)

log_in_btn = driver.find_element_by_id('ctl00_cphMain_logIn_Login')
log_in_btn.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()