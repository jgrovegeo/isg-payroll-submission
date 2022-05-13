from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import username, password
import time

PATH = '/usr/bin/chromedriver'
url = 'https://portal.insightglobal.com/Candidate/#!/timesheet/manage/4559609'
username = username
password = password
job_title = 'HP Inc. - Data Analyst'
clock_in = '7:30 AM'
clock_out = '4:00 PM'

driver = webdriver.Chrome(PATH)
driver.get(url)
driver.maximize_window()

usr_name = driver.find_element_by_id('ctl00_cphMain_logIn_UserName')
usr_name.send_keys(username)

usr_pass = driver.find_element_by_id('ctl00_cphMain_logIn_Password')
usr_pass.send_keys(password)

log_in_btn = driver.find_element_by_id('ctl00_cphMain_logIn_Login')
log_in_btn.send_keys(Keys.RETURN)

iframe_dashboard = driver.find_element_by_xpath("//*[@id='dashboard']")
driver.switch_to.frame(iframe_dashboard)

wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, f"//tr[@class='rgRow']//td[2]/a[@title='{job_title}' and text()='{job_title}']"))).click()
driver.switch_to.default_content()

iframe_timesheet = driver.find_element_by_xpath("/html/body/form/div[4]/div[2]/iframe[2]")
driver.switch_to.frame(iframe_timesheet)

def button_12():
    """Clicks button 12"""
    twelve_pm = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table/tbody/tr/td[1]/table/tbody/tr[3]/td[1]/a')))
    return ActionChains(driver).move_to_element(twelve_pm).click().perform()

def button_30():
    """Clicks button 30"""
    thirty = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/a")))
    return ActionChains(driver).move_to_element(thirty).click().perform()

def monday():
    class_elements = driver.find_elements_by_xpath("//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']")[1]
    class_elements.click()

    # fill out time sheet
    start_time = wait.until(EC.element_to_be_clickable((By.XPATH, "//html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[2]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[1]/div/input")))
    start_time.click()
    start_time.send_keys(clock_in)

    end_time = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[2]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[2]/div/input")))
    end_time.click()
    end_time.send_keys(clock_out)

    break_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[2]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[4]/td/div/div/div[1]/button')
    break_btn.send_keys(Keys.RETURN)
    
    start_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/span/input")))
    start_break_time.click()

    button_12()

    end_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/span/input")))
    end_break_time.click()

    button_12()

    button_30()

    break_save_btn = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/footer/div/button[2]')
    break_save_btn.send_keys(Keys.RETURN)

    add_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[2]/div/div/div[2]/div[4]/div[2]/span/button[2]')
    add_btn.send_keys(Keys.RETURN)

    time.sleep(1)
    
def tuesday():
    class_elements = driver.find_elements_by_xpath("//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']")[2]
    class_elements.click()

    # fill out time sheet
    start_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[3]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[1]/div/input')))
    start_time.click()
    start_time.send_keys(clock_in)
    
    end_time = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[3]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[2]/div/input')))
    end_time.click()
    end_time.send_keys(clock_out)

    break_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[3]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[4]/td/div/div/div[1]/button')
    break_btn.send_keys(Keys.RETURN)
   
    start_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/span/input')))
    start_break_time.click()

    button_12()

    end_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/span/input')))
    end_break_time.click()

    button_12()
    
    button_30()

    break_save_btn = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/footer/div/button[2]')
    break_save_btn.send_keys(Keys.RETURN)

    add_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[3]/div/div/div[2]/div[4]/div[2]/span/button[2]')
    add_btn.send_keys(Keys.RETURN)

    time.sleep(1)

def wednesday():
    class_elements = driver.find_elements_by_xpath("//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']")[3]
    class_elements.click()

    # fill out time sheet
    start_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[4]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[1]/div/input')))
    start_time.click()
    start_time.send_keys(clock_in)
    
    end_time = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[4]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[2]/div/input')))
    end_time.click()
    end_time.send_keys(clock_out)

    break_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[4]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[4]/td/div/div/div[1]/button')
    break_btn.send_keys(Keys.RETURN)
    
    start_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/span/input')))
    start_break_time.click()
    
    button_12()

    end_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/span/input')))
    end_break_time.click()

    button_12()
    
    button_30()

    break_save_btn = driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/div[2]/div/footer/div/button[2]')
    break_save_btn.send_keys(Keys.RETURN)

    add_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[4]/div/div/div[2]/div[4]/div[2]/span/button[2]')
    add_btn.send_keys(Keys.RETURN)

    time.sleep(1)
 
def thursday():
    class_elements = driver.find_elements_by_xpath("//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']")[4]
    class_elements.click()

    # fill out time sheet
    start_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[5]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[1]/div/input')))
    start_time.click()
    start_time.send_keys(clock_in)
    
    end_time = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[5]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[2]/div/input')))
    end_time.click()
    end_time.send_keys(clock_out)

    break_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[5]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[4]/td/div/div/div[1]/button')
    break_btn.send_keys(Keys.RETURN)
 
    start_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/span/input')))
    start_break_time.click()

    button_12()

    end_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/span/input')))
    end_break_time.click()

    button_12()
    
    button_30()

    break_save_btn = driver.find_element_by_xpath('/html/body/div[10]/div[3]/div/div[2]/div/footer/div/button[2]')
    break_save_btn.send_keys(Keys.RETURN)
    
    add_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[5]/div/div/div[2]/div[4]/div[2]/span/button[2]')
    add_btn.send_keys(Keys.RETURN)

    time.sleep(1)
    
def friday():
    class_elements = driver.find_elements_by_xpath("//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']")[5]
    class_elements.click()

    # fill out time sheet
    start_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[6]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[1]/div/input')))
    start_time.click()
    start_time.send_keys(clock_in)
    
    end_time = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[6]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[3]/td[2]/div/input')))
    end_time.click()
    end_time.send_keys(clock_out)

    break_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[6]/div/div/div[2]/div[4]/div[1]/table/tbody/tr[4]/td/div/div/div[1]/button')
    break_btn.send_keys(Keys.RETURN)
    
    start_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[11]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[2]/span/input')))
    start_break_time.click()

    button_12()

    end_break_time = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[11]/div[3]/div/div[2]/div/div/table/tbody/tr[1]/td[3]/span/input')))
    end_break_time.click()

    button_12()
    
    button_30()

    break_save_btn = driver.find_element_by_xpath('/html/body/div[11]/div[3]/div/div[2]/div/footer/div/button[2]')
    break_save_btn.send_keys(Keys.RETURN)
    
    add_btn = driver.find_element_by_xpath('/html/body/form/div[7]/div[1]/div[2]/div[1]/table[2]/tbody/tr/td[6]/div/div/div[2]/div[4]/div[2]/span/button[2]')
    add_btn.send_keys(Keys.RETURN)

    time.sleep(1)

monday()
tuesday()
wednesday()
thursday()
friday()

print("Don't forget to hit the $ubmit button.")