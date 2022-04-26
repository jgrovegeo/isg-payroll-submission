from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = '/usr/bin/chromedriver'
brave_path = '/snap/bin/brave'

options = Options()

options.binary_location = brave_path
options.add_argument('--remote-debugging-port=9224') #NOT 9222

driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get('https://portal.insightglobal.com/Candidate/#!/timesheet/manage/4559609')
driver.quit