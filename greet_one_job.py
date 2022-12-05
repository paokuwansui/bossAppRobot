# -*- coding: utf-8 -*-
""" 
Created on Sun Nov 27 23:49:23 2022

@author: 10597
"""
#%%

from selenium.webdriver.common.by import By
from json import load
from time import sleep
from log_code import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class greet_one_job:
    推荐牛人 = "/html/body/div[2]/div[1]/div[1]/dl[2]/dt/a"
    帖子选择下拉框 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]"
    具体职位选项 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/ul/li[{}]"
    子页面 = '//*[@id="recommendContent"]/div[2]/iframe'
    下一份简历 = "/html/body/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div"
    退出简历 = "/html/body/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div[1]/h3/div/span"
    筛选 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div"
    不限性别 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[2]/dd/a[1]/span"
    男 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[2]/dd/a[2]/span"
    女 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[2]/dd/a[3]/span"
    近一个月没有和同事交换简历 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[3]/dd/a[2]/div/span"
    今日活跃 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[5]/dd/a[3]/div/span"
    三日内活跃 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[5]/dd/a[4]/div/span"
    刚刚活跃 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[5]/dd/a[2]/div/span"
    近14天没有看过 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[3]/dl[6]/dd/a[2]/div/span"
    离职随时到岗 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[2]/dl[4]/dd/a[2]/span"
    在职月内到岗 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[2]/dl[4]/dd/a[5]/span"
    在职考虑机会 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[1]/div[2]/dl[4]/dd/a[4]/span"
    确认 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div[2]/div/span[2]"
    牛人期望职位 = "/html/body/div/div/div/div/div[2]/div/div/div[2]/div/ul/li[{}]/div/div[1]/div[2]/div[3]"
    牛人打招呼 = "/html/body/div/div/div/div/div[2]/div/div/div[2]/div/ul/li[{}]/div/div[3]"
    牛人打招呼按钮3 = '//*[@id="recommend-list"]/div/ul/li[{}]/div/div[3]/div/span/div/button'
    牛人打招呼按钮2 = '//*[@id="recommend-list"]/div/ul/li[{}]/div/div[3]/div[2]/span/div/button'
    牛人打招呼按钮1 = '//*[@id="recommend-list"]/div/ul/li[{}]/div/div[3]/div/span/div/button'
    在线 = "/html/body/div/div/div/div/div[2]/div/div/div[2]/div/ul/li[{}]/div/div[1]/div[2]/div[1]/img"
    牛人过往经历 = "/html/body/div/div/div/div/div[2]/div/div/div[2]/div/ul/li[{}]/div/div[1]/div[4]"
    筛选下拉 = "/html/body/div/div/div/div/div[1]/div/div/div/div/div[4]/div/div/div[1]/span[2]"
    到达上限的退出按钮 = '/html/body/div[9]/div[1]/div[2]'
    达到上限界面 = '/html/body/div[9]/div[1]'
    
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
        
    def try_close_page(self):
        try:
            close = self.driver.find_element(By.XPATH,self.退出简历)
            self.driver.execute_script("arguments[0].click()",close)
        except Exception:
            pass
        sleep(0.5)
    
    def decline(self):
        self.driver.execute_script("window.scrollBy(0, 5000);")
        sleep(2)
    
    def select_job(self, index):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.具体职位选项.replace("{}",str(index)))))
            self.driver.find_element(By.XPATH,self.具体职位选项.replace("{}",str(index))).click()
        except Exception:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.帖子选择下拉框)))
            self.driver.find_element(By.XPATH,self.帖子选择下拉框).click()
            sleep(0.5)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.具体职位选项.replace("{}",str(index)))))
            self.driver.find_element(By.XPATH,self.具体职位选项.replace("{}",str(index))).click()
        sleep(2.5)
        
    def select_job_flow(self, job_name):
        self.try_close_page()
        self.try_go_root()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.推荐牛人)))
        self.driver.find_element(By.XPATH,self.推荐牛人).click()
        self.try_go_son_page()
        self.try_close_page()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.帖子选择下拉框)))
        self.driver.find_element(By.XPATH,self.帖子选择下拉框).click()
        with open('./config.json','r',encoding='utf8')as fp:
            config = load(fp)
        index = config[job_name]["排序"]
        self.select_job(index)

    def selet_filter_criteria(self, config):
        if "男" in config["性别"] and "女" in config["性别"]:
            self.driver.find_element(By.XPATH,self.不限性别).click()
        elif "男" in config["性别"]:
            self.driver.find_element(By.XPATH,self.男).click()
        elif "女" in config["性别"]:
            self.driver.find_element(By.XPATH,self.女).click()
            
        if "刚刚活跃" in config["活跃度"]:
            self.driver.find_element(By.XPATH,self.刚刚活跃).click()
        elif "今日活跃" in config["活跃度"]:
            self.driver.find_element(By.XPATH,self.今日活跃).click()
        elif "近三日活跃" in config["活跃度"]:
            self.driver.find_element(By.XPATH,self.三日内活跃).click()
        else:
            self.driver.find_element(By.XPATH,self.刚刚活跃).click()
            
        if "离职随时到岗" in config["求职意向"]:
            self.driver.find_element(By.XPATH,self.离职随时到岗).click()
        if "在职月内到岗" in config["求职意向"]:
            self.driver.find_element(By.XPATH,self.在职月内到岗).click()
        if "在职考虑机会" in config["求职意向"]:
            self.driver.find_element(By.XPATH,self.在职考虑机会).click()
        
        self.driver.find_element(By.XPATH,self.近一个月没有和同事交换简历).click()
        #self.driver.find_element(By.XPATH,self.近14天没有看过).click()
        self.driver.find_element(By.XPATH,self.确认).click()
        sleep(3)
        
    def selet_filter_criteria_flow(self, job_name):
        self.try_go_son_page()
        self.try_close_page()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,self.筛选)))
        if '取消' in self.driver.find_element(By.XPATH,self.筛选).text:
            return
        self.driver.find_element(By.XPATH,self.筛选).click()
        sleep(0.5)
        with open('./config.json','r',encoding='utf8')as fp:
            config = load(fp)
        config = config[job_name]
        self.selet_filter_criteria(config)
        
    def update(self, delay):
        try:
            self.driver.find_element(By.XPATH,self.筛选下拉).click()
            sleep(0.5+delay)
            self.driver.find_element(By.XPATH,self.确认).click()
            sleep(3+delay)
        except Exception:
            self.update(delay+0.5)
        self.try_go_son_page()
    
    def start_sift(self, job_name):
        while self.job_index > 0:
            with open('./config.json','r',encoding='utf8')as fp:
                config_data = load(fp)
            config = config_data[job_name]
            err = 0
            for index in range(49):
                if index == 0:
                    self.decline()
                if (index + 1) % 10 == 0:
                    self.decline()
                if self.job_index <= 0:
                    break
                try:
                    desired_position = self.driver.find_element(By.XPATH,self.牛人期望职位.replace("{}",str(index + 1))).text
                    state = self.driver.find_element(By.XPATH,self.牛人打招呼.replace("{}",str(index + 1))).text
                    before_job = self.driver.find_element(By.XPATH,self.牛人过往经历.replace("{}",str(index + 1))).text
                    try:
                        self.driver.find_element(By.XPATH,self.在线.replace("{}",str(index + 1)))
                        online = True
                    except Exception:
                        online = False
                    err = 0
                except Exception:
                    print("err,",err)
                    err += 1
                    if err >= 10:
                        break
                    continue
                if "打招呼" not in state:
                    continue
                if config["是否只看在线"] == "是" and online == False:
                    print("当前人选不符合只看在线")
                    continue
                if config["期望职位关键字"] != []:
                    desired_position_falg = False
                    for i in config["期望职位关键字"]:
                        if i in desired_position:
                            desired_position_falg = True
                    
                    if desired_position_falg == False:
                        print("当前人选不符合期望职位关键字")
                        continue
                
                if config["期望职位排除关键字"] != []:
                    desired_position_falg_not = False
                    for i in config["期望职位排除关键字"]:
                        if i in desired_position:
                            desired_position_falg_not = True
                    if desired_position_falg_not == True:
                        print("当前人选不符合期望职位排除关键字")
                        continue
                
                if config["过往经历关键字"] != []:
                    before_job_falg = False
                    for i in config["过往经历关键字"]:
                        if i in before_job:
                            before_job_falg = True
                    
                    if before_job_falg == False:
                        print("当前人选不符合过往经历关键字")
                        continue
                
                if config["过往经历排除关键字"] != []:
                    before_job_falg_not = False
                    for i in config["过往经历排除关键字"]:
                        if i in before_job:
                            before_job_falg_not = True
                    if before_job_falg_not == True:
                        print("当前人选不符合过往经历排除关键字")
                        continue
                try:
                    hello = self.driver.find_element(By.XPATH,self.牛人打招呼按钮3.replace("{}",str(index + 1)))
                    self.driver.execute_script("arguments[0].click()",hello)
                    log.push(f'该职位还需要打{self.job_index}个招呼')
                except Exception:
                    try:
                        hello = self.driver.find_element(By.XPATH,self.牛人打招呼按钮2.replace("{}",str(index + 1)))
                        self.driver.execute_script("arguments[0].click()",hello)
                        log.push(f'该职位还需要打{self.job_index}个招呼')
                    except Exception:
                        try:
                            hello = self.driver.find_element(By.XPATH,self.牛人打招呼按钮1.replace("{}",str(index + 1)))
                            self.driver.execute_script("arguments[0].click()",hello)
                            log.push(f'该职位还需要打{self.job_index}个招呼')
                        except Exception:
                            log.push(f'本次点击失效，请查看页面是否正常')
                            continue
                self.job_index -= 1
                

                sleep(0.5)
                try:
                    self.try_go_root()
                    self.driver.find_element(By.XPATH, self.到达上限的退出按钮).click()
                    self.job_index = -50
                except Exception as e:
                    pass
                if self.job_index <= 0:
                    log.push('该职位已经完成任务')
                self.try_go_son_page()
            self.update(0)
        


        
        
    def start(self, job_name, job_index):
        log.push(f"正在为{job_name}打招呼，本次运行将打{job_index}个招呼")
        self.job_index = job_index
        try:
            self.select_job_flow(job_name)
            self.selet_filter_criteria_flow(job_name)
            self.start_sift(job_name)
            if self.job_index < 0:
                return -50 
            return 0
        except Exception:
            log.push('打招呼线程报错，等待10秒后继续当前任务')
            sleep(10)
            return self.job_index


