from selenium import webdriver

class Com():

    def __init__(self, driver):
        self.driver = driver
        self.addBtn = "add" #id
        self.comname = "name" #id
        self.introduceddate = "introduced" #id
        self.discontinueddate = "discontinued" #id
        self.company = "//select[@id='company']//option[contains(text(), 'RCA')]" #xpath
        self.savecom = "//input[@class='btn primary']" #xpath
        self.search = "searchbox" #id
        self.searchsub = "searchsubmit" #id
        self.selelem = "//tr[1]//td[1]//a[1]" #xpath
        self.editcompany = "//select[@id='company']//option[contains(text(), 'MOS Technology')]" #xpath
        self.deletecompany = "//input[@class='btn danger']" #xpath

    def addComputerBtn(self):
        self.driver.find_element_by_id(self.addBtn).click()

    def Comname(self):
        self.driver.find_element_by_id(self.comname).clear()
        self.driver.find_element_by_id(self.comname).send_keys("aaa")

    def IntroducedDate(self):
        self.driver.find_element_by_id(self.introduceddate).clear()
        self.driver.find_element_by_id(self.introduceddate).send_keys("2010-10-10")

    def DiscontinuedDate(self):
        self.driver.find_element_by_id(self.discontinueddate).clear()
        self.driver.find_element_by_id(self.discontinueddate).send_keys("2030-10-10")

    def Company(self):
        self.driver.find_element_by_xpath(self.company).click()

    def SaveCom(self):
        self.driver.find_element_by_xpath(self.savecom).click()

    def Search(self):
        self.driver.find_element_by_id(self.search).send_keys("aaa")

    def SearchSub(self):
        self.driver.find_element_by_id(self.searchsub).click()

    def SelElement(self):
        self.driver.find_element_by_xpath(self.selelem).click()

    def EditCompany(self):
        self.driver.find_element_by_xpath(self.editcompany).click()

    def DelCompany(self):
        self.driver.find_element_by_xpath(self.deletecompany).click()