from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as webdriver
import json
import time
import os

if str(os.name) == "posix":
    ordi="MAC"
else:
    ordi="WINDOWS"


title = "Urbex"
description = "Video d'urbex"
tags="urbex, URBEX,"
day="11"
month="04"
year="2023"
hour="13"
minute="05"
file_path="/Volumes/Untitled/Ecole/Programation/Html_Css/HaussMann/result/clip_39.mp4"

def start_youtube(file_path,title,description,tags,day,month,year,hour,minute):
    if ordi=="WINDOWS":
        driver = webdriver.Chrome(executable_path="chromedriver.exe",  user_data_dir = "C:\\Users\\Elève\\AppData\\Local\\Google\\Chrome\\User Data")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/Users/mathis_kremer/Library/Application Support/Google/Chrome/")
        driver = webdriver.Chrome(options=options, executable_path=r"chromedriver")
    # Old code to restore cookie
    """
    file = open("cookie.json","r")
    content = file.read()
    file.close()
    cookie = json.loads(content)


    driver.get("https://studio.youtube.com/channel/UCA_eV-kml7ehF3V2yyMo7SQ/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")
    for cook in cookie:
        dico = {"name":cook['name'],"value":cook['value'],'sameSite': 'None'}
        print(dico) 
        driver.add_cookie(dico)
    """

    try:
        driver.get("https://youtube.com")

        def loading(driver, xpath):
            find=False
            tour=0
            while not find:
                try:
                    upload = driver.find_element(By.XPATH, f'{xpath}')
                    find=True
                except:
                    time.sleep(1)
                if tour>20:
                    print("Err #001")
                    find=True
                tour += 1

        def loading_ByID(driver, id):
            find=False
            tour=0
            while not find:
                try:
                    upload = driver.find_element(By.ID, f'{id}')
                    find=True
                except:
                    time.sleep(1)
                if tour>20:
                    print("Err #002")
                    find=True
                tour += 1

        def click_xpath(driver, xpath):
            try:
                driver.find_element(By.XPATH, f'{xpath}').click()
                return True
            except:
                return False

        time.sleep(1)
        loading(driver,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button")
        click_xpath(driver,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button")

        time.sleep(1)
        loading(driver,"/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item")
        click_xpath(driver,"/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item")

        time.sleep(1)
        #UPLOAD VIDEO
        loading(driver,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div")
        time.sleep(3)
        upload_bt = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_bt.send_keys(f"{file_path}")

        #TITRE DESCRIPTION
        time.sleep(1)
        loading(driver, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
        time.sleep(1)
        textbox = driver.find_elements(By.ID, "textbox")
        if ordi=="WINDOWS":textbox[0].send_keys(Keys.CONTROL + 'a')
        else:textbox[0].send_keys(Keys.COMMAND + 'a')
        time.sleep(0.5)
        textbox[0].send_keys(Keys.BACK_SPACE)
        textbox[0].send_keys(f"{title}")
        textbox[1].send_keys(f"{description}")

        time.sleep(3)
        #No Kids
        loading_ByID(driver, "radioLabel")
        driver.find_elements(By.ID, "radioLabel")[1].click()

        time.sleep(3)
        #Show More
        loading(driver, "//*[@id=\"toggle-button\"]")
        driver.find_element(By.XPATH, "//*[@id=\"toggle-button\"]").click()

        time.sleep(3)
        #TAG
        loading(driver, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input")
        tag = driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input")
        tag.send_keys(f"{tags}")

        time.sleep(20)
        #Visibility
        loading(driver,'//*[@id="step-badge-3"]')
        click_xpath(driver,'//*[@id="step-badge-3"]')

        time.sleep(1)
        #Schedule
        loading_ByID(driver, "schedule-radio-button")
        driver.find_element(By.ID, "schedule-radio-button").click()

        time.sleep(2)
        loading(driver,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[1]/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon")
        click_xpath(driver,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[1]/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon")

        time.sleep(2)
        #DATE
        loading(driver,'/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input') 
        date = driver.find_element(By.XPATH, '/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input')

        for i in range(20):
            date.send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        date.send_keys(f"{day}/{month}/{year}")
        date.send_keys(Keys.RETURN)


        #HEURE
        time.sleep(4)
        loading(driver,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[2]/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input')
        heure = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[2]/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input')
        for i in range(20):
            heure.send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        heure.send_keys(f"{hour}:{minute}")


        time.sleep(30)
        loading_ByID(driver, "done-button")
        driver.find_element(By.ID, "done-button").click()

        time.sleep(10)
        driver.close()
    except:
        driver.close()


def start_tiktok(file_path,title,tags):
    if ordi=="WINDOWS":
        driver = webdriver.Chrome(executable_path="chromedriver.exe",  user_data_dir = "C:\\Users\\Elève\\AppData\\Local\\Google\\Chrome\\User Data")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/Users/mathis_kremer/Library/Application Support/Google/Chrome/")
        driver = webdriver.Chrome(options=options, executable_path=r"chromedriver")
    try:
        time.sleep(10)
        driver.get("https://www.tiktok.com/upload?lang=fr")

        def loading(driver, xpath):
            find=False
            tour=0
            while not find:
                try:
                    upload = driver.find_element(By.XPATH, f'{xpath}')
                    find=True
                except:
                    time.sleep(1)
                if tour>20:
                    print("Err #001")
                    find=True
                tour += 1

        def click_xpath(driver, xpath):
            try:
                driver.find_element(By.XPATH, f'{xpath}').click()
                return True
            except:
                return False

        time.sleep(10)
        iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
        driver.switch_to.frame(iframe)

        #VIDEO
        loading(driver,"/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input")
        upload_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input")
        upload_input.send_keys(f"{file_path}")

        #TITLE
        time.sleep(1)
        loading(driver, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span")
        title_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span")
        title_input.send_keys(f"{title} {tags}")

        #ALLOW DESCRIPTION
        time.sleep(1)
        loading(driver, "/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[6]/div[2]")
        click_xpath(driver,"/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[6]/div[2]")

        #PUBLISH
        time.sleep(60)
        bt=driver.find_elements(By.CLASS_NAME,"css-y1m958")[-1]
        bt.click()

        time.sleep(60)
        driver.close()
    except:
        driver.close()

#start_tiktok(file_path,"Urbex Exploration","#Urbex")