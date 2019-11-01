from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
#from pywinauto.application import Application
import time
import random
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import urllib.request
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import numpy as np
import datetime



##################
year = '2012'

Output_Format = "miniSEED"
wave_type = "S arrival"
start_number = 0
EQ_time = '5'
Your_Name =  year + '_miniseed'
index_number = year + "M4.0+.xlsx"
print(index_number)
df2 = pd.read_excel(index_number, sheet_name= 'earthquake')

#excel 파일 만들기df = pd.DataFrame(columns=['Event Number','Magnitude','Name','url','Station'])



tor_open = r'C:\Users\CONYSD_ANALYSIS\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe'
profile_default_open = r'C:\Users\CONYSD_ANALYSIS\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default'





for i in range(start_number,  df2.shape[0]):

    if (float(df2.iloc[i, 10]) >= 5):
        try:
            print("-------------" , i , "----------------")
            print("number :" , str(df2.iloc[i, 0]))
            #driver = webdriver.Chrome('chromedriver')

            ##Firefox_tor IP 우회 --------------------------------------------------------------------
            torexe = os.popen()
            time.sleep(random.random(tor_open))
            profile = FirefoxProfile(profile_default_open
                )
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
            driver = webdriver.Firefox(firefox_profile=profile)
            ##------------------------------------------------------------------------------------------

            search_world = str(df2.iloc[i, 0])
            url = 'http://ds.iris.edu/wilber3/find_stations/{}'.format(search_world)
            time.sleep(random.random()*10)
            driver.implicitly_wait(0.5)
            driver.get(url)

            time.sleep(random.randint(60,70))
            #title = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID, "dataGrid")))
            table = driver.find_element_by_xpath('//*[@id="dataGrid"]/div[5]/div/div[1]/div[2]/a')

            time.sleep(random.randint(1,5))

            table_data = table.text
            print("Station : ", table_data)
            element = driver.find_element_by_xpath('//*[@id="selectRows"]/button[2]')
            driver.implicitly_wait(100000000)
            element.send_keys(u'\ue007')
            element.send_keys(Keys.RETURN);
            time.sleep(random.random()  + 2)
            checkbox = driver.find_element_by_xpath('//*[@id="dataGrid"]/div[5]/div/div[1]/div[1]/input')
            checkbox.click()

            driver.find_element_by_xpath('//*[@id="startRequest"]').send_keys(Keys.ENTER)
            time.sleep(random.random()  + 2)
            driver.find_element_by_id("dataRequestDialog_windowEndAfter").send_keys(EQ_time)
            time.sleep(random.random()  + 2)
            driver.find_element_by_id("dataRequestDialog_windowEndPhase").send_keys(wave_type)
            time.sleep(random.random() + 2)
            driver.find_element_by_id("dataRequestDialog_output").send_keys(Output_Format)
            time.sleep(random.random()  + 2)
            driver.find_element_by_xpath('//*[@id="dataRequestDialog_user"]').send_keys(Your_Name)
            time.sleep(random.random()  + 2)
            # driver.find_element_by_xpath('//*[@id="dataRequestDialog_email"]').send_keys(Email)
            time.sleep(random.random()*10)
            driver.find_element_by_xpath('//*[@id="dataRequestDialog_submit"]').click()
            time.sleep(random.random() * 10)

            try:
                driver.find_element_by_xpath('//*[@id="dataRequestDialog_submit"]').click()
                time.sleep(random.random() * 10)
                print("click")
            except:
                time.sleep(random.random() * 10)
                pass

            try:
                raise Exception
            except:
                try:
                    print("----------dataRequestResult_message check ----------------------")
                    dataRequestResult_message = driver.find_element_by_xpath('//*[@id="dataRequestResult_message"]')
                    time.sleep(random.random())
                    dataRequestResult_message_data = dataRequestResult_message.text
                    print("dataRequestResult_message", dataRequestResult_message_data)
                    if dataRequestResult_message_data == '' or dataRequestResult_message_data == ' ':
                        driver.close()
                        print("Your data request has been submitted to the BREQ_FAST system. You should receive notification by email when your data is ready. ")
                        df.loc[i] = [str(df2.iloc[i, 0]), df2.iloc[i, 10], 0,0,0]
                        df.to_csv(year + "_Miniseed_data_csv_" + str(start_number) + ".csv", mode='w')

                    else :
                        print(exception)
                        raise Exception
                except :
                    try:
                        dispatch_button = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[1]/div[2]/div/div[5]/div[2]/div/div[2]/div/a")
                        time.sleep(random.random()*10)
                        href = dispatch_button.get_attribute('href')
                        print("href", href)
                        driver.close()

                        print("driver.current_url", href)
                        earthquake_name = href.replace("http://ds.iris.edu/wilber3/data_request/"+Your_Name + "/", "")
                        print("earthquake_name", earthquake_name)  #print earthquake_name
                        url2 = "http://ds.iris.edu/pub/userdata/wilber/"+Your_Name+"/{}".format(earthquake_name)
                        print("url2", url2)
                        #driver.get(url2)
                        url3 = url2 + '/' + earthquake_name + ".miniseed"
                        time.sleep(random.random())
                        print("url3" , url3)
                        #url3 = "http://ds.iris.edu/pub/userdata/wilber/park/2018-01-01-mb42-mariana-islands-6/2018-01-01-mb42-mariana-islands-6.miniseed"
                        print("Magnitude : ", df2.iloc[i, 10]) #print magnitude
                        #driver.get(url3)


                        time.sleep(random.random())

                        df.loc[i] = [str(df2.iloc[i, 0]), df2.iloc[i, 10], earthquake_name, url3, table_data]
                        df.to_csv(year + "_Miniseed_data_csv_"+str(start_number)+".csv", mode='w')
                        print("---finish_data----")

                        time.sleep(1)

                        try:
                            driver.close()
                        except:
                            pass

                    except:
                        pass

        except:
            print("FAIL")
            df.loc[i] = [str(df2.iloc[i, 0]),0,0,0,0]
            df.to_csv(year + "_Miniseed_data_csv_"+str(start_number)+".csv", mode='w')
            time.sleep(random.random()*10)
            try :
                driver.close()
            except:
                print("FAIL - error")
    else:
        print("------",float(df2.iloc[i, 10]))