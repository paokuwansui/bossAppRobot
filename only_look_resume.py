# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from json import load
from time import sleep
from log_code import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class only_look_resume:
    推荐牛人 = "/html/body/div[2]/div[1]/div[1]/dl[2]/dt/a"
    帖子选择下拉框 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]"
    具体职位选项 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/ul/li[{}]"
    子页面 = '//*[@id="recommendContent"]/div[2]/iframe'
    第一个牛人简历 = "/html/body/div/div/div/div/div[2]/div/div/div[2]/div/ul/li[1]/div"
    下一份简历 = "/html/body/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div"
    退出简历 = "/html/body/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div[1]/h3/div/span"
    def __init__(self, driver):
        self.driver = driver
        
    def try_go_root(self):
        try:
            self.driver.switch_to.default_content()
            sleep(0.5)
        except Exception:
            pass
        
    def try_go_son_page(self):
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,self.子页面))
        except Exception:
            pass
        
    def select_job(self, index):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.具体职位选项.replace("{}",str(index)))))
            self.driver.find_element(By.XPATH,self.具体职位选项.replace("{}",str(index))).click()
        except Exception:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.帖子选择下拉框)))
            self.driver.find_element(By.XPATH,self.帖子选择下拉框).click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.具体职位选项.replace("{}",str(index)))))
            self.driver.find_element(By.XPATH,self.具体职位选项.replace("{}",str(index))).click()
        sleep(2.5)
        
    def try_close_page(self):
        try:
            close = self.driver.find_element(By.XPATH,self.退出简历)
            self.driver.execute_script("arguments[0].click()",close)
        except Exception:
            pass
        sleep(0.5)
        
    def start_thumb(self, frequency, index):
        if frequency > 450:
            frequency = 450
        if frequency <= 1:
            return
        sleep(3)
        for i in range(frequency - 1):
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.下一份简历)))
                next = self.driver.find_element(By.XPATH,self.下一份简历)
                self.driver.execute_script("arguments[0].click()",next)
                sleep(3)
            except Exception:
                self.one_job(index, frequency - i - 1)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.退出简历)))
        close = self.driver.find_element(By.XPATH,self.退出简历)
        self.driver.execute_script("arguments[0].click()",close)
        sleep(0.5)
        
    def one_job(self, index, frequency):
        
        for i in range(5):
            try:
                self.try_go_root()
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.推荐牛人)))
                self.driver.find_element(By.XPATH,self.推荐牛人).click()
                self.try_go_son_page()
                self.try_close_page()
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.帖子选择下拉框)))
                self.driver.find_element(By.XPATH,self.帖子选择下拉框).click()
                self.select_job(index)
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.第一个牛人简历)))
                self.driver.find_element(By.XPATH,self.第一个牛人简历).click()
                self.start_thumb(frequency, index)
                break
            except Exception:
                pass
        
    def one_cycle(self, job_list, frequency):
        with open('./config.json','r',encoding='utf8')as fp:
            config = load(fp)
        for job_name in job_list:
            log.push(f'开始翻阅{job_name}的简历')
            index = config[job_name]["排序"]
            self.one_job(index, frequency)
        
    def start(self, job_list, frequency):
        try:
            while True:
                for i in range(3):
                    self.one_cycle(job_list, frequency)
                    log.push('已经翻看完一轮了，本程序将歇息10分钟')
                    sleep(600)
                log.push('已经翻看完3轮了，本程序将歇息30分钟')
                sleep(1800)
        except Exception:
            log.push('查看简历线程报错，等待10秒后再次运行')
            sleep(10)
            self.start()

            
