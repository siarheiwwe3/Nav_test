from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep 
BASE_URL = "http://www.wwe.com"


class SignInTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url=BASE_URL
        self.verificationErrors = []
        self.driver.get(self.base_url)
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors, "Test passed")    
        sleep(2)
        
    def signOut(self):
        driver = self.driver
        driver.find_element_by_class_name("logout").click()
        
        
        
    """def test_sign_in_wwe(self):
        print "Start execusion", SignInTest.test_sign_in_wwe.__name__
        driver = self.driver
        driver.find_element_by_css_selector(".sign-in").click()
        driver.maximize_window()
        d = driver
        d.find_element_by_id('emailAddress').send_keys('siarhei.wwe3@gmail.com')
        d.find_element_by_id('password-login').send_keys('mytest1241')
        WebDriverWait(d, 10)
        d.find_element_by_name("submitButton").submit()
        user_name =  d.find_element_by_class_name("display-name-new").text
        self.assertEqual("THOMAS T.", user_name, "Can't sign in like Thomas T") 
        print "User name successfully confirmed"
        
         
    def test_sign_in_facebook(self):
        print "Start execusion", SignInTest.test_sign_in_facebook.__name__    
        driver = self.driver
        driver.find_element_by_css_selector(".sign-in").click()
        driver.maximize_window()
        d = driver 
        d.find_element_by_class_name("fb-login").click() 
        #dr handle in d.window_handles:
        driver.switch_to_window(d.window_handles[1])
        d.find_element_by_id("email").send_keys("siarhei.wwe3@gmail.com")
        d.find_element_by_id("pass").send_keys("mytest1241")
        d.find_element_by_id("u_0_1").click() 
        driver.switch_to_window(d.window_handles[1])
        #driver.switch_to_default_content()
        driver.switch_to_window(d.window_handles[0])
        user_name =  d.find_element_by_class_name("display-name-new").text
        self.assertEqual("THOMAS T.", user_name, "Can't sign in like Thomas T")
        print "User name successfully confirmed"
    
    def test_sign_in_twitter(self):
        print "Start execusion", SignInTest.test_sign_in_twitter.__name__    
        driver = self.driver
        driver.find_element_by_css_selector(".sign-in").click()
        driver.maximize_window()
        d = driver 
        d.find_element_by_class_name("twitter-login").click() 
        driver.switch_to_window(d.window_handles[1])
        d.find_element_by_id("username_or_email").send_keys("siarheiwwe3")
        d.find_element_by_id("password").send_keys("mytest1241")
        d.find_element_by_id("allow").click()     
        d.find_element_by_id("allow").click() 
        #driver.maximize_window()
        sleep(3)
        driver.switch_to_window(d.window_handles[0])
        sleep(3)
        #driver.back()
        #driver.get("http://www.wwe.com")
        user_name =  d.find_element_by_class_name("display-name-new").text
        self.assertEqual("THOMAS T.", user_name, "Can't sign in like Thomas T")
        print "User name successfully confirmed"
        

    
    def test_sign_in_google(self):
        print "Start execusion", SignInTest.test_sign_in_google.__name__    
        driver = self.driver
        driver.find_element_by_css_selector(".sign-in").click()
        driver.maximize_window()
        d = driver 
        d.find_element_by_class_name("google-login").click() 
        driver.switch_to_window(d.window_handles[1])
        d.find_element_by_id("Email").send_keys("siarhei.wwe2")
        d.find_element_by_id("Passwd").send_keys("mytest1241")
        d.find_element_by_id("signIn").click()     
        sleep(3)
        driver.switch_to_window(d.window_handles[0])
        sleep(3)
        user_name =  d.find_element_by_class_name("display-name-new").text
        self.assertEqual("SERGE W.", user_name, "Can't sign in like Thomas T")
        print "User name successfully confirmed"
    """    



class WwePollTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url=BASE_URL
        self.verificationErrors = []
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors, "Test passed")    
        sleep(2)

    def test_fortest(self):
        print "Hello world"
        driver = self.driver
        #driver.find_element_by_css_selector(".sign-in").click()
        try:
            driver.find_element_by_css_selector(r'.content > a[href^="/inside/polls"]:first-child').click()
            driver.find_element_by_css_selector(".choices div:first-child a:first-child").click()
            driver.find_element_by_class_name("submit").click()
            count_value = driver.find_element_by_class_name("total").text
            value = count_value[13:]
            
            print value
        except:
            print "Can't locate poll"
        






if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase( \
    SignInTest)
    suite.addTest(WwePollTest("test_fortest"))
    unittest.TextTestRunner(verbosity=2).run(suite)
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        