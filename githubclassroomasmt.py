# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time
import sys
import pyperclip as pc 
import os
import frontmatter

class GHClassroomAsmt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    # https://stackoverflow.com/questions/3663450/remove-substring-only-at-the-end-of-string
    def rchop(self, s, suffix):
        if suffix and s.endswith(suffix):
            return s[:-len(suffix)]
        return s
    
    def getasmts(self):
        result = []
        
        f = open(MDFILE, 'r')
        mdcontents = f.read()
        post = frontmatter.loads(mdcontents)
        postdict = post.to_dict()
        
        for item in postdict['schedule']:  
            if 'deliverables' in item:
                for deliverable in item['deliverables']:        
                    dtitle = deliverable['dtitle']        
                    
                    if not 'handed out' in dtitle.lower():
                        dtitle = self.rchop(dtitle, 'Handed Out')
                        dtitle = self.rchop(dtitle, "Due")
                        
                        result.append(dtitle)
                        
        return result
        
    def createasmt(self, title, driver):
        courseidx = 1
        coursesearchdone = False
        while not coursesearchdone:
            try:
                if driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Archive'])[" + str(courseidx) + "]/following::h1[1]").text == COURSE:
                    coursesearchdone = True
                else:
                    courseidx = courseidx + 1
            except Exception as e:
                print(e)
                break
        
        if not coursesearchdone:
            print("Course not found: might already be on the course page; otherwise, this will fail")
        else:
            print("Found course index " + str(courseidx))
            
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Archive'])[" + str(courseidx) + "]/following::h1[1]").click()           
        
        try:
            driver.find_element_by_link_text("New assignment").click() # if an assignment exists
        except:
            try:
                driver.find_element_by_link_text("Create an assignment").click() # if this is the first assignment
            except Exception as e:
                print(e)
                sys.exit(-1)

        driver.find_element_by_id("assignment_title").click()
        driver.find_element_by_id("assignment_title").clear()
        driver.find_element_by_id("assignment_title").send_keys(title)
        
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='/'])[2]/following::div[2]").click()
        driver.find_element_by_id("new-assignment-submit").click()
        driver.find_element_by_id("new-assignment-submit").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Run C++'])[1]/following::input[2]").click()
        driver.find_element_by_name("commit").click()

        # Copy the link address
        driver.find_element_by_css_selector("svg.octicon.octicon-clippy").click()
        print(title)
        print(pc.paste())
        
        driver.find_element_by_link_text("View my classroom").click()
        
    def test_createassignment(self):
        asmts = self.getasmts()
        
        driver = self.driver
        driver.get("https://classroom.github.com/")
        driver.find_element_by_link_text("Sign in").click()
        
        print("Log in now!")
        time.sleep(30)
        
        for asmt in asmts:
            title = ASMTTITLE + asmt
            title = title.strip()
            self.createasmt(title[0:59], driver)

        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    COURSE = os.getenv('COURSE') # billmongan-CS173-Fall2020
    ASMTTITLE = os.getenv('ASMTTITLE') # just the prefix CS173-Fall2020-
    MDFILE = os.getenv('MDFILE') # pages/_syllabus.md
    
    if COURSE is None:
        print("Usage Environment Variables: COURSE=<GitHub Classroom Class Name> ASMTTITLE=<Assignment title prefix> MDFILE=_pages/syllabus.md")
        sys.exit(-1)
    
    unittest.main()

