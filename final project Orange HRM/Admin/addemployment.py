import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class TestAdmin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_admin(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("admin") # isi email
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(2)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList") # masuk ke halaman 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() # klik tombol sign in
        time.sleep(2)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers") # masuk ke halaman 
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() # klik tombol sign in
        time.sleep(2)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser") # masuk ke halaman 
        time.sleep(3)
        browser.find_element(By.XPATH,"xpath=(//button[@type='button'])[4]").click() # klik tombol sign in
        time.sleep(2)
        browser.find_element(By.XPATH,"xpath=//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div/div[2]/div/div/div[2]/i").click() # klik tombol sign in
        time.sleep(2)
        


       
        


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()