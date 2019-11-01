from selenium.webdriver.firefox.options import Options
from selenium import webdriver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time
import os
import urllib.request
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import threading
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from urllib.request import FancyURLopener
import numpy as np


tor_open = r'C:\Users\CONYSD_ANALYSIS\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe'
profile_default_open = r'C:\Users\CONYSD_ANALYSIS\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default'
save_place_folder = "D:\\"



year = "2012"
start_number = 14
file_type = "Miniseed"
index_number = year + "_Miniseed_data_csv_0.csv"
df2 = pd.read_csv(index_number)




##진도별 폴더 생성
mylist = np.arange(4,10,0.1)



if not os.path.exists(year+"_miniseed"):
    os.mkdir(year + "_miniseed")



#지진 데이터 다운로드
for i in range(start_number , df2.shape[0]):
    print("\n\n-------------", i ,"-------------" )
    print("Earthquake number", df2.iloc[i, 1])

    try:
        ##Firefox_tor IP 우회 --------------------------------------------------------------------
        torexe = os.popen(tor_open)
        time.sleep(random.random())
        profile = FirefoxProfile(
            profile_default_open)
        time.sleep(random.random())
        profile.set_preference('network.proxy.type', 1)
        time.sleep(random.random())
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        time.sleep(random.random())
        profile.set_preference('network.proxy.socks_port', 9050)
        time.sleep(random.random())
        profile.set_preference("network.proxy.socks_remote_dns", False)
        time.sleep(random.random())
        profile.update_preferences()
        time.sleep(random.random())
        #driver =webdriver.Firefox(firefox_profile=profile)

        try:

            url = df2.iloc[i, 4]
            #url = 'http://ds.iris.edu/pub/userdata/wilber/2018_sac/2018-01-01-mb42-mariana-islands-5/sac_data/IRISDMC/SACPZ.IU.GUMO.00.BH2'
            print("url", url)


            options = Options()
            options.set_preference("browser.download.folderList",2)
            options.set_preference("browser.download.manager.showWhenStarting", False)

            place = save_place_folder

            save_place = place + year + "_miniseed\\"
            print("save_place : ", save_place)
            options.set_preference("browser.download.dir", save_place)

            print("save_place", save_place)

            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")


            driver = webdriver.Firefox(firefox_options= options,firefox_profile=profile)
            time.sleep(random.random()*10)

            driver.set_page_load_timeout(15)
            try:
                driver.get(url)
            except TimeoutException as e:
                print(e)
            finally:
                driver.close()

            time.sleep(random.random() * 10)
            print("first place " , save_place + "\\" +  str(df2.iloc[i, 3]) + '.miniseed')
            print("second place ", save_place + "\\" +  str(df2.iloc[i, 1]) + '.miniseed')

            try:
                os.rename (save_place + '/' +  str(df2.iloc[i, 3]) + '.miniseed', save_place + '/' + str(df2.iloc[i, 1]) + '.miniseed')
            except:
                print("Fail ")

            time.sleep(random.random() * 10)

        except:
            print("not found on this server.")
    except:
        print("Error")
