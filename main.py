from cgi import test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import random
import string
# import HtmlTestRunner
import unittest
import time

def test_Sign_Login(self, isSignUp):
  modalButton = self._Driver.find_element(By.XPATH, '//*[@id="signin2"]' if isSignUp else '//*[@id="login2"]')
  modalButton.click()

  time.sleep(2)

  userInput = self._Driver.find_element(By.XPATH, '//*[@id="sign-username"]' if isSignUp else '//*[@id="loginusername"]')
  userInput.send_keys(self.username)

  time.sleep(2)

  passwordInput = self._Driver.find_element(By.XPATH, '//*[@id="sign-password"]' if isSignUp else '//*[@id="loginpassword"]')
  passwordInput.send_keys(self.password)

  time.sleep(2)

  submitButton = self._Driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]' if isSignUp else '//*[@id="logInModal"]/div/div/div[3]/button[2]')
  submitButton.click()

  time.sleep(1)

  if isSignUp:
    alert = Alert(self._Driver)
    alert.accept()

  time.sleep(3)

def test_add_products(self, product):
  product = self._Driver.find_element(By.XPATH, product)

  product.click()

  time.sleep(2)

  addToCart = self._Driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')

  addToCart.click()

  time.sleep(1)

  alert = Alert(self._Driver)
  alert.accept()

  time.sleep(2)

  home = self._Driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')

  home.click()

  time.sleep(3)

class DemoPage(unittest.TestCase):

  def setUp(self):
    self._Driver = webdriver.Edge("./msedgedriver.exe")
    self._Driver.maximize_window()
    self._Driver.get('https://www.demoblaze.com/index.html')
    self.username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    self.password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

  def test_actions(self):
    test_Sign_Login(self, True)
    test_Sign_Login(self, False)
    test_add_products(self, '//*[@id="tbodyid"]/div[1]/div/a')
    test_add_products(self, '//*[@id="tbodyid"]/div[2]/div/a')

if __name__ == '__main__':
  # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
  unittest.main()