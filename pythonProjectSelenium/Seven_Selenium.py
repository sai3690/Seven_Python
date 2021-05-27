''' Author: Sai Samarpan Sahu'''

import time
from selenium import webdriver
import requests as requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome(executable_path="C:\Python36\chromedriver.exe")


class Test(unittest.TestCase):

    def test_1Brokrn_Img(self):

        driver.get("http://the-internet.herokuapp.com//broken_images")
        driver.maximize_window()
        img_list = driver.find_elements(By.TAG_NAME, "img")
        print('Total number of images on '  + str(len(img_list)))

        Broken_images = 0
        for img in img_list:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    Broken_images=(Broken_images + 1)

                print('Broken image count' + str(Broken_images) )
        driver.close()


    def test_2forgot_password(self):

       
        driver.get("http://the-internet.herokuapp.com/forgot_password")
        driver.maximize_window()
        driver.find_element(By.ID,"email").send_keys("saisamarpan2012@gmail.com")
        driver.find_element(By.XPATH,"//i[contains(text(),'Retrieve password')]").click()
        '''After this stepwe are getting inter server error'''
        driver.close()






    def test_3Login(self):
        driver=webdriver.Chrome(executable_path="C:\Python36\chromedriver.exe")
        driver.get("http://the-internet.herokuapp.com/login")
        driver.maximize_window()
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/form[1]/button[1]").click()

        message = driver.find_element(By.XPATH,"//h4[contains(text(),'Welcome to the Secure Area. When you are done clic')]")
        message_7 = message.text
        self.assertEqual("Welcome to the Secure Area. When you are done click logout below.",message_7,"Login unsucessfull")
        driver.close()

    def test_4alpha(self):
        driver.get("http://the-internet.herokuapp.com/inputs")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//body/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("ABC")

        inp_txt = driver.find_element(By.XPATH,"//body/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
        inp_txt_7 = inp_txt.text
        self.assertEqual("ABC", inp_txt_7, "Input unsucessful")
        driver.close()

    def test_5Table(self):

        '''We are not able to perform any action in the webpage, Hence extracting the Due amount
    and sorting the same'''
        C=1
        DueT = []
        driver.get("http://the-internet.herokuapp.com/tables")
        driver.maximize_window()
        for i in range(0,4,1):
            Due = driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[1]/table[2]/tbody[1]/tr["+str(C)+"]/td[4]")
            DueT.append(Due.text)
            C=C+1


        print(sorted(DueT))

        driver.close()

    def test_6Loop(self):

        driver.get("http://the-internet.herokuapp.com/notification_message_rendered")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[contains(text(),'Click here')]").click()
        Loop_msg = driver.find_element(By.XPATH, "//div[@id='flash']")

        while Loop_msg !="Action successful":
            driver.find_element(By.XPATH, "//a[contains(text(),'Click here')]").click()
            time.sleep(2)
            Loop_msg1 = driver.find_element(By.XPATH, "//div[@id='flash']")
            print(Loop_msg1.text)
            if Loop_msg1.text == "Action successful":
                break
                print("Script Completed")
        driver.close()









if __name__ == "__main__":
    unittest.main()
