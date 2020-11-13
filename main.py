import pyautogui, time
import schedule
from selenium import webdriver


def automation():
    # for drivers
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://lbschools.instructure.com/")
    time.sleep(1)
    # user
    elem_get = driver.find_element_by_xpath('//*[@id="identification"]')  # do not change this xpath
    elem_get.send_keys('#########')  # Add your student id here
    time.sleep(1)
    # pass
    elem_get = driver.find_element_by_xpath('//*[@id="ember486"]')  # do not change this xpath
    elem_get.send_keys('######')    # Add your student password here
    # btn
    elem_get = driver.find_element_by_xpath('//*[@id="authn-go-button"]')  # do not change this xpath
    elem_get.click()
    time.sleep(1)
    # inside canvas
    # go to period one
    canvas_find = driver.find_element_by_xpath('')  # change the xpath to the one that is in your browser
    canvas_find.click()
    time.sleep(1)
    # finds zoom
    canvas_find = driver.find_element_by_xpath('')  # change the xpath to the one that is in your browser
    canvas_find.click()
    # goes to zoom
    time.sleep(4)
    pyautogui.press('left')
    time.sleep(.2)
    pyautogui.press('enter')
    time.sleep(2)
    driver.quit()
    # this will automatically press yes for webcam, i do not have a webcam so zoom skips that
    # and go straight to the audio
    # if your zoom ask you to join with webcam and audio, this won't work for you, a new version will come soon
    #time.sleep(8)
    #pyautogui.press('enter')
    # this will automatically leave at the end of class
    # change the secs inside the parentheses to the time of your class
    # to find the secs multiply the minutes * 60 = the amount of secs
# time automations
# change the time to when your class starts for ex : 07:50

schedule.every().monday.at("08:00").do(automation)
schedule.every().tuesday.at("08:00").do(automation)
schedule.every().wednesday.at("08:00").do(automation)
schedule.every().thursday.at("08:00").do(automation)
schedule.every().friday.at("08:00").do(automation)
# for time
while True:
    schedule.run_pending()
    time.sleep(1)



