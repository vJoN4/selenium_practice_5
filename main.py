from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import random
import string
import HtmlTestRunner
import unittest
import time

USER_NAME = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
PASSWORD = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

# ? ---------------------------------------------------------------------------------------------------------------------------------------------------------
def handleActions(self):
  for action in self.actions:
    for key in action:

      if key in ['username', 'password']:
        input = self._Driver.find_element(By.XPATH, action[key])
        input.send_keys(self.username if key == 'username' else self.password)
        time.sleep(2)

      if key in ['button', 'submit']:
        button = self._Driver.find_element(By.XPATH, action[key])
        button.click()
        time.sleep(2)

        try:
          alert = Alert(self._Driver)
          alert.accept()
        except:
          pass

    time.sleep(3)

# ? ---------------------------------------------------------------------------------------------------------------------------------------------------------
def handleLogin(self):
  self.actions = [
    self.actions[1],
  ]
  handleActions(self)

# ? ---------------------------------------------------------------------------------------------------------------------------------------------------------

def handleProducts(self):
  for product in self.products:

    cardProduct = self._Driver.find_element(By.XPATH, product)
    cardProduct.click()
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

# ? ---------------------------------------------------------------------------------------------------------------------------------------------------------

def handleShoppingCart(self):
  shoppingCart = self._Driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[4]/a')
  shoppingCart.click()
  time.sleep(2)

  shopping = self._Driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
  shopping.click()
  time.sleep(2)

  for input in self.shoppingActions:
    input = self._Driver.find_element(By.XPATH, self.shoppingActions[input])
    content = ''.join(random.choice(string.ascii_lowercase) for i in range(12))
    input.send_keys(content)
    time.sleep(2)

  buy = self._Driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
  buy.click()

  time.sleep(2)

  ok = self._Driver.find_element(By.XPATH, '/html/body/div[10]/div[7]/div/button')
  ok.click()

  time.sleep(2)

# ? ---------------------------------------------------------------------------------------------------------------------------------------------------------

class DemoPage(unittest.TestCase):

  def setUp(self):
    self._Driver = webdriver.Edge("./msedgedriver.exe")
    self._Driver.maximize_window()
    self.username = USER_NAME
    self.password = PASSWORD
    self.actions = [
      {
        'button': '//*[@id="signin2"]',
        'username': '//*[@id="sign-username"]',
        'password': '//*[@id="sign-password"]',
        'submit': '//*[@id="signInModal"]/div/div/div[3]/button[2]'
      },
      {
        'button': '//*[@id="login2"]',
        'username': '//*[@id="loginusername"]',
        'password': '//*[@id="loginpassword"]',
        'submit': '//*[@id="logInModal"]/div/div/div[3]/button[2]'
      }
    ]
    self.products = [
      '//*[@id="tbodyid"]/div[1]/div/a',
      '//*[@id="tbodyid"]/div[2]/div/a'
    ]
    self.shoppingActions = {
      'name': '//*[@id="name"]',
      'country': '//*[@id="country"]',
      'city': '//*[@id="city"]',
      'card': '//*[@id="card"]',
      'month': '//*[@id="month"]',
      'year': '//*[@id="year"]',
    }
    self._Driver.get('https://www.demoblaze.com/index.html')


  def test_a_signUn_signIn(self):
    time.sleep(3)
    handleActions(self)

  def test_b_add_buy_products(self):
    time.sleep(3)
    handleLogin(self)
    handleProducts(self)
    handleShoppingCart(self)

  def tearDown(self):
      self._Driver.quit()


if __name__ == '__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))