import time
import unittest
from selenium import webdriver
from ComputerDB.Pages.ComputerPage import Com

class DeleteComputer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Ritika Nath/Documents/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        # cls.driver.maximize_window()

    def test_add_computer(self):
        driver = self.driver
        driver.get("http://computer-database.herokuapp.com/computers")
        time.sleep(2)
        print(driver.title)
        assert "Computers database" in driver.title
        delete = Com(driver)
        delete.Search()
        time.sleep(1)
        delete.SearchSub()
        time.sleep(1)
        delete.SelElement()
        time.sleep(1)
        delete.DelCompany()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()