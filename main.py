
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
class Internet_speed_monitoring:
    def __init__(self , min_download_speed , min_upload_speed):
        self.min_downolad_speed = min_download_speed
        self.min_upload_speed = min_upload_speed


    def obtain_current_speed(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.google.com/')

        search_bar = driver.find_element(By.CSS_SELECTOR , '.a4bIc textarea')
        search_bar.send_keys('internet speed test')
        search_bar.send_keys(Keys.ENTER)

        time.sleep(2)
        speed_test_btn = driver.find_element(By.CLASS_NAME , 'fSXkBc')
        speed_test_btn.click()

        time.sleep(30)
        internet_speed_details = [float(item.text) for item in driver.find_elements(By.CLASS_NAME , 'spiqle')]

        driver.quit()
        return internet_speed_details
    
    def add_complaint_tweet(self ,md, mu , cd , cu):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://twitter.com/home')
        time.sleep(3)

        username_area = driver.find_element(By.TAG_NAME , 'input')
        username_area = username_area.send_keys(os.environ['MY_EMAIL'])

        next_btn = driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_btn.click()

        time.sleep(2)
        authenticate = driver.find_element(By.TAG_NAME , 'input')
        authenticate.send_keys(os.environ['MY_USERNAME'])
        authenticate.send_keys(Keys.ENTER)

        time.sleep(2)
        passwaord_box = driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwaord_box.send_keys(os.environ['MY_PASS'])
        passwaord_box.send_keys(Keys.ENTER)


        time.sleep(4)
        tweet_area = driver.find_element(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_area.send_keys(f'My internet speed is {cd}/down and {cu}/up , when it should be {md}/down and {mu}/up')

        post_btn = driver.find_element(By.CSS_SELECTOR , '#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19u6a5r.r-2yi16.r-1qi8awa.r-ymttw5.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l > div > span > span')
        post_btn.click()
        time.sleep(4)

        driver.quit()



user1 = Internet_speed_monitoring(100,80)
speed_details = user1.obtain_current_speed()
print(speed_details)
time.sleep(2)
if speed_details[0] < user1.min_downolad_speed and speed_details[1] <user1.min_upload_speed:
    user1.add_complaint_tweet(user1.min_downolad_speed, user1.min_upload_speed, speed_details[0] , speed_details[1])









