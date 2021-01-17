from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from chaojiying_Python.chaojiying import Chaojiying_Client
import time
import

EMAIL = '1787618676@qq.com'
PASSWORD = ''
CHAOJIYING_USERNAME = 'shating'
CHAOJIYING_PASSWORD = 'a1111000a'
CHAOJIYING_SOFT_ID = '911793'
CHAOJIYING_KIND = '	911793'

class YYverification():
    def __init__(self):
        self.url = ''
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,20)
        self.chaojiying = Chaojiying_Client(CHAOJIYING_USERNAME,CHAOJIYING_PASSWORD,CHAOJIYING_SOFT_ID)

    def get_img_element(self):
        """获取验证码图片对象"""
        self.driver.get('https://aq.yy.com/p/reg/account.do?appid=&url=&fromadv=udbclsd_r')
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//iframe')))
        i = self.driver.find_element_by_xpath('//iframe')
        url_1 = i.get_attribute('src')
        self.driver.get(url_1)
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pw_main')))
        return element
    def get_screenshot(self):
        screen_shot = self.driver.get_screenshot_as_png()
        return screen_shot

    def get_position(self):
        """获取验证码位置"""
        element = self.get_img_element()
        time.sleep(1)
        location = element.location
        size = element.size
        top,bottom,left,right = location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_yy_image(self,name='captcha.png'):
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
       # captcha = screenshot.crop(left,top,right,bottom)
       # captcha.save(name)
       # return captcha
        print(screenshot,type(screenshot))

test = YYverification()
result = test.get_yy_image()
print(result)