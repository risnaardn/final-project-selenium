import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestEmployeList(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_employe_list(self): 
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
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() # klik tombol sign in
        time.sleep(2)
        browser.maximize_window()
        browser.execute_script("window.scrollBy(0,450)","")
        time.sleep(2)
        browser.find_element(By.XPATH,"xpath=//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div/div/div/label/span/i").click() # klik tombol sign in
        time.sleep(2)

      


       
        


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()