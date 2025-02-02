 #-*-coding:utf-8-*-

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import datetime
import time


import importlib,sys
importlib.reload(sys)

class textfree:  

  def __init__(self, TN_USER, TN_PASS, PHONE_NUMBER, MESSAGE):
    self.TN_USER = TN_USER
    self.TN_PASS = TN_PASS
    self.PHONE_NUMBER = PHONE_NUMBER
    self.MESSAGE = MESSAGE
    self.url = "https://messages.textfree.us/login"

  def send_text(self):
    for phone in self.PHONE_NUMBER.split(','):  #可直接一次发送多个号码
      #profile = webdriver.FirefoxProfile()
      #proxy = '127.0.0.1:10808'
      #ip, port = proxy.split(":")
      #port = int(port)
      ## 不使用代理的协议，注释掉对应的选项即可
      #settings = {
      #  'network.proxy.type': 1,
      #  'network.proxy.http': ip,
      #  'network.proxy.http_port': port,
      #  'network.proxy.ssl': ip,  # https的网站,
      #  'network.proxy.ssl_port': port,
      #}
      #
      ## 更新配置文件
      #for key, value in settings.items():
      #    profile.set_preference(key, value)
      #profile.update_preferences()
      #
      options = webdriver.FirefoxOptions()
      options.add_argument('-headless')  # 无头参数

      #https://sites.google.com/a/chromium.org/chromedriver/home
      #driver = webdriver.Chrome(r'C:/Python27/Scripts/chromedriver')

      #https://github.com/mozilla/geckodriver/releases
      driver = webdriver.Firefox(executable_path='geckodriver', options=options)
      #driver = webdriver.Firefox(firefox_profile=profile, options=options)
      #driver = webdriver.Firefox(proxy = proxy)

      #这两种设置都进行才有效
      #driver.set_page_load_timeout(5)
      #driver.set_script_timeout(5)
      try:
          driver.get(self.url)
      except:
          pass
      #强制等待8s,主要是等待reCaptcha加载
      time.sleep(8)

      # 分辨率 1920*1080
      driver.set_window_size(1920,1080)
      time.sleep(3)

      WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
      uname_box = driver.find_element_by_xpath("//input[@name='username']")
      pass_box = driver.find_element_by_xpath("//input[@name='password']")
      uname_box.send_keys(self.TN_USER)
      pass_box.send_keys(self.TN_PASS)

      login_btn = driver.find_element_by_xpath("//button[@type='submit']")
      login_btn.click()

      #显性等待，每隔3s检查一下条件是否成立
      try:
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form_button']")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='contactInput']")))
      except:
        pass

      if driver.current_url != self.url :
         print(u'登录成功'+driver.current_url)
      else:
         print(u'登录失败')
         sys.exit()
      # 隐性等待,最长等待30秒
      driver.implicitly_wait(30)


      #toast = driver.find_element_by_css_selector("#recent-header .toast-container")
      #if toast:
      #  driver.execute_script("arguments[0].remove();", toast)
      #  time.sleep(1)
      #notification = driver.find_element_by_css_selector(".notification-priming-modal")
      #if notification:
      #  driver.execute_script("arguments[0].remove();", notification)
      #  time.sleep(1)
      #driver.execute_script("$('#recent-header .toast-container').remove();")
      #driver.execute_script("$('.notification-priming-modal').remove();")
      #driver.execute_script("$('.modal').remove();")
      time.sleep(2)

      try:
          
        print (u'开始给%s发短信' % phone)

        #点击 新建短信按钮
        new_text_btn = driver.find_element_by_id("SyncContactsXDismissPopup")
        if new_text_btn.is_displayed():
          new_text_btn.click()
        else:
          driver.execute_script("arguments[0].scrollIntoView();", new_text_btn)
          if new_text_btn.is_displayed():
            new_text_btn.click()
          else:
            driver.execute_script("$(arguments[0]).click()", "#SyncContactsXDismissPopup")
        time.sleep(10)
        
   
        
        #点击 新建短信按钮
        new_text_btn = driver.find_element_by_id("startNewConversationButton")
        if new_text_btn.is_displayed():
          new_text_btn.click()
        else:
          driver.execute_script("arguments[0].scrollIntoView();", new_text_btn)
          if new_text_btn.is_displayed():
            new_text_btn.click()
          else:
            driver.execute_script("$(arguments[0]).click()", "#startNewConversationButton")
        time.sleep(10)

        
        #输入：短信内容
        text_field = driver.find_element_by_css_selector(".emojionearea-editor")
        if text_field.is_displayed():
          text_field.click()
          text_field.send_keys(self.MESSAGE)
        else:
          driver.execute_script("arguments[0].scrollIntoView();", text_field)
          if text_field.is_displayed():
            text_field.click()
            text_field.send_keys(self.MESSAGE)
          else:
            driver.execute_script("$(arguments[0]).val('arguments[1]')", "#messageForm", self.MESSAGE)
        time.sleep(10)
        
        #输入号码
        number_field = driver.find_element_by_id("contactInput")
        if number_field.is_displayed():
          number_field.send_keys(phone)
        else:
          driver.execute_script("arguments[0].scrollIntoView();", number_field)
          if number_field.is_displayed():
            number_field.send_keys(phone)
          else:
            driver.execute_script("$(arguments[0]).val('arguments[1]')", "#contactInput", phone)
        time.sleep(10)

        #点击短信内容
        text_field = driver.find_element_by_css_selector(".emojionearea-editor")
        if text_field.is_displayed():
          text_field.click()
        else:
          driver.execute_script("arguments[0].scrollIntoView();", text_field)
          if text_field.is_displayed():
            text_field.click()
          else:
            driver.execute_script("$(arguments[0]).focus()", "#messageForm")
        time.sleep(10)
        
        #点击发送按钮
        send_btn = driver.find_element_by_id("sendButton")
        if send_btn.is_displayed():
          send_btn.click()
        else:
          driver.execute_script("arguments[0].scrollIntoView();", send_btn)
          if send_btn.is_displayed():
            send_btn.click()
          else:
            driver.execute_script("$(arguments[0]).click()", "#sendButton")
            driver.execute_script("setTimeout($(arguments[0]).click,2000)", "#sendButton")
        time.sleep(10)
        
        #执行页面刷新
        #try:
        #  driver.get(self.url.replace('/login','/messaging'))
        #  
        #  time.sleep(10)
        #  # 隐性等待,最长等待30秒
        #  driver.implicitly_wait(30)
        #  WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='newText']")))
        #  print (u'刷新页面完成')
        #except:
        #    pass
        

      except:
        print (u'给%s发短信时发生异常：' % phone)
        info = sys.exc_info()
        #print(info)
        #print(info[0])
        print(info[1])
        time.sleep(2)
        pass
      continue
  
      driver.close()
    print (u'处理完毕---end')
    
