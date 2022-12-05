#%%
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from json import load
from time import sleep
from log_code import log
#%%
class call_old:
    沟通 = '/html/body/div[2]/div[1]/div[1]/dl[4]/dt/a'
    职位 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div/ul/li[{}]'
    第一个已沟通的牛人 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[{}]/div/div/div[1]/img'
    第一个已沟通的牛人div = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[{}]'
    常用语 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[2]'
    第一句常用语 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div/ul/li[1]'
    发送按钮 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div'
    选择职位 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]'
    当前页面牛人名字 = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]'
    def __init__(self, driver):
            self.driver = driver
            self.scroll_flag = 10
            self.xpath_index = 0
            self.remainder = 13
            self.label_list = []
            self.up_name = None
            self.up_style = '0'
    def try_go_root(self):
        try:
            self.driver.switch_to.default_content()
            sleep(0.5)
        except Exception:
            pass
    def decline(self):
        xpath_urls = '/html/body/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]'
        urls_pre = self.driver.find_elements(By.XPATH, xpath_urls)
        style = urls_pre[0].get_attribute("style")
        if style != self.up_style:
            self.xpath_index = 1
        self.up_style = style
        self.scroll_flag = self.scroll_flag + 78
        self.driver.execute_script(f'document.getElementsByClassName("user-list")[0].scrollTop={self.scroll_flag}')
        self.xpath_index += 1
    def send_say(self):
        sleep(1)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.当前页面牛人名字)))
        str_name = self.driver.find_element(By.XPATH,self.当前页面牛人名字).text
        if str_name != self.up_name:
            self.up_name = str_name
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.常用语)))
            self.driver.find_element(By.XPATH,self.常用语).click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.第一句常用语)))
            self.driver.find_element(By.XPATH,self.第一句常用语).click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.发送按钮)))
            self.driver.find_element(By.XPATH,self.发送按钮).click()
        
            
    def select_job(self):
        self.try_go_root()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.沟通)))
        self.driver.find_element(By.XPATH,self.沟通).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.选择职位)))
        self.driver.find_element(By.XPATH,self.选择职位).click()
        sleep(3)
        with open('./config.json','r',encoding='utf8')as fp:
            config = load(fp)
        index = config[self.job_name]["排序"]
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.职位.replace('{}',str(index + 1)))))
        select = self.driver.find_element(By.XPATH,self.职位.replace('{}',str(index + 1)))
        self.driver.execute_script("arguments[0].click()",select)
    def goto_start_flag(self, start_flag):
        sleep(2)
        for i in range(start_flag):
            self.decline()
            sleep(0.05)
    def while_send(self):
        while self.flag > 0:
            while True:
                sleep(0.25)
                urls_pre = self.driver.find_elements(By.XPATH, self.第一个已沟通的牛人div.replace('{}',str(self.xpath_index)))
                data_id = urls_pre[0].get_attribute("key")
                if data_id in self.label_list:
                    self.xpath_index += 1
                else:
                    break
            job = self.driver.find_element(By.XPATH,self.第一个已沟通的牛人.replace('{}',str(self.xpath_index)))
            self.driver.execute_script("arguments[0].click()",job)
            sleep(0.25)
            self.send_say()
            
            self.label_list.append(data_id)
            if len(self.label_list) > 40:
                self.label_list.pop(0)
            self.decline()
            self.flag -= 1
    def start(self, job_name, start_flag, flag):
        self.job_name = job_name
        self.start_flag = start_flag
        self.flag = flag
        log.push(f"正在给{job_name}职位沟通过的“老人”送去温暖")
        try:
            while self.flag > 0:
                self.select_job()
                self.goto_start_flag(self.start_flag)
                self.while_send()
            return self.flag, self.start_flag + flag - self.flag
        except Exception:
            log.push(f"给{job_name}职位沟通过的“老人”送温暖时发生错误,等待10秒后将继续")
            sleep(10)
            self.start(job_name, self.start_flag + flag - self.flag, self.flag)
    def test_start(self, job_name, start_flag, flag):
        self.job_name = job_name
        self.start_flag = start_flag
        self.flag = flag
        while self.flag > 0:
            self.select_job()
            self.goto_start_flag(self.start_flag)
            self.while_send()
            print(self.start_flag + flag - self.flag)
        return self.flag, self.start_flag + flag - self.flag
#%%
# call = call_old(driver)
# num = 450
# start_num = 150
# while num > 0:
#     num, start_num = call.test_start("宜企出行招聘网约车司机_北京_9-13K(4)", start_num ,num)
#     print(start_num)
