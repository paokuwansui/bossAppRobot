# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from log_code import log
class login_boss:
    登录按钮 = '/html/body/div[1]/div[1]/div[1]/div[4]/div/a[5]'
    切换扫码登录 = '//*[@id="wrap"]/div/div[2]/div[2]/div[1]'
    def login(self):
        try:
            driver = webdriver.Edge()    # 打开 Edge 浏览器
            driver.get("https://www.zhipin.com/beijing/")
            sleep(0.2)
            driver.find_element(By.XPATH,self.登录按钮).click()
            try:
                driver.find_element(By.XPATH,self.切换扫码登录).click()
            except Exception:
                sleep(0.3)
                try:
                    driver.find_element(By.XPATH,self.切换扫码登录).click()
                except Exception:
                    sleep(0.5)
                    driver.find_element(By.XPATH,self.切换扫码登录).click()
            return driver
        except Exception:
            log.push('登录线程出错，等待10秒后重新运行')
            sleep(10)
            self.login()
