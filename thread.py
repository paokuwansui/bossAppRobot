# -*- coding: utf-8 -*-
#%%
from login_boss import login_boss
from only_look_resume import only_look_resume
import threading as td
from json import load
from  greet_one_job import greet_one_job
import datetime
from time import sleep
from log_code import log
import inspect
import ctypes   
from call_old import call_old
#%%
class ctrl_class:
    def __init__(self):
        self._driver = None
        self._login = login_boss()
        self._look_resume = None
        self._greet_one_job = None
        self._call_old = None
        self.look_resume_threading = None
        self.greet_threading = None
        self.call_old_threading = None
        self.job_greet_flag_dict = {}
        self.job_greet_max_dict = {}
        self.job_name = []
        with open('./config.json','r',encoding='utf8')as fp:
            config = load(fp)
        for i in config:
            self.job_greet_flag_dict[i] = 0
        for i in config:
            self.job_greet_max_dict[i] = 0
        for i in config:
            self.job_name.append(i)

    def _login_threading_fun(self):
        self._driver = self._login.login()
    
    def _look_resume_threading_fun(self, job_list, flag_num):
        if self._driver == None:
            # self.login()
            return {"err":"还未进行登录"}
        if self._look_resume == None:
            self._look_resume = only_look_resume(self._driver)
        self._look_resume.start(job_list, flag_num)
        


    def add_greet_max_num(self, job_name, add_num):
        if self.job_greet_max_dict[job_name] + add_num> 50:
            self.job_greet_max_dict[job_name] = 50
            log.push(f"现在{job_name}任务队列新增至50个")
            return 
        self.job_greet_max_dict[job_name] += add_num
        log.push(f"现在{job_name}任务队列新增{add_num}个")
    
    def _greet_threading_fun(self):
        try:
            while self._driver == None:
                sleep(1)
            if self._greet_one_job == None:
                self._greet_one_job = greet_one_job(self._driver)
            
            while True:
                for i in self.job_name:
                    if self.job_greet_max_dict[i] > self.job_greet_flag_dict[i]:
                        log.push("打招呼功能启动中....")
                        num = self.job_greet_max_dict[i]-self.job_greet_flag_dict[i]
                        while num > 0:
                            num = self._greet_one_job.start(i, num)
                        self.job_greet_flag_dict[i] = self.job_greet_max_dict[i]
                        if num < 0:
                            self.job_greet_flag_dict[i] = 50
                            self.job_greet_max_dict[i] = 50
        except Exception:
            log.push('按时间段打招呼功能线程出错，正在重新启动')
            try:
                self.greet_threading._is_stopped = True  # 修改线程状态
                self._async_raise(self.greet_threading.ident, SystemExit)
            except Exception:
                pass
            self.start_greet()
    
    def _time_greet_threading_fun(self):
        log.push("按时间段打招呼功能线程正常启动")
        while True:
            flag = False
            with open('./config.json','r',encoding='utf8')as fp:
                config = load(fp)
            now_time = datetime.datetime.now().strftime("%H:%M")
            for job_name in config:
                config_data = config[job_name]
                if config_data["是否按时间段打招呼"] == "是":
                    time_list = config_data["打招呼时间段"]
                    for i in time_list:
                        if i[:i.find("-")] == now_time:
                            add = eval(i[i.find("-")+1:])
                            self.add_greet_max_num(job_name, add)
                            flag = True
                            log.push(f"{job_name}进入{add}个任务队列")
            if flag == True:
                sleep(65)
            sleep(5)
        
            
    def _async_raise(self, tid, exctype):
        if not inspect.isclass(exctype):
            raise TypeError("Only types can be raised (not instances)")
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    def set_driver(self, driver):
        self._driver = driver
    def login(self):
        if self._driver == None:
            self.login_threading = td.Thread(target=self._login_threading_fun)
            self.login_threading.start()
    def look_resume(self,job_list, flag_num):
        self.stop_all()
        self.job_list_flag = job_list
        self.job_flag_num = flag_num
        self.look_resume_threading = td.Thread(target=self._look_resume_threading_fun, args=(job_list,flag_num))
        self.look_resume_threading.start()
        log.push('刷简历线程正在启动')
    def start_greet(self):
        self.stop_all()
        self.greet_threading = td.Thread(target=self._greet_threading_fun)
        self.greet_threading.start()
        log.push('自动打招呼正在启动')
    def open_time_greet(self):
        self.time_greet_threading = td.Thread(target=self._time_greet_threading_fun)
        self.time_greet_threading.start()
    def stop_look_resume(self):
        try:
            self.look_resume_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.look_resume_threading.ident, SystemExit)
        except Exception:
            pass
        log.push('刷简历线程已经停止')
    
    def _call_old_threading_fun(self, job_list, flag_num):
        if self._call_old == None:
            self._call_old = call_old(self._driver)
        log.push("成功启动给“老人”送问候功能")
        for job_name in job_list:
            self._call_old.start(job_name, 50 ,flag_num)
        
    def call_old(self, job_list, flag_num):
        self.stop_all()
        self.call_old_threading = td.Thread(target=self._call_old_threading_fun, args=(job_list,flag_num))
        self.call_old_threading.start()
    def stop_all(self):
        log.push("正在停止翻阅简历和沟通老人")

        try:
            self.look_resume_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.look_resume_threading.ident, SystemExit)
        except Exception:
            pass

        try:
            self.call_old_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.call_old_threading.ident, SystemExit)
        except Exception:
            pass

    def __del__(self):
        try:
            self.greet_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.greet_threading.ident, SystemExit)
        except Exception:
            pass
        try:
            self.look_resume_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.look_resume_threading.ident, SystemExit)
        except Exception:
            pass
        try:
            self.login_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.login_threading.ident, SystemExit)
        except Exception:
            pass
        try:
            self.time_greet_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.time_greet_threading.ident, SystemExit)
        except Exception:
            pass
        try:
            self.call_old_threading._is_stopped = True  # 修改线程状态
            self._async_raise(self.call_old_threading.ident, SystemExit)
        except Exception:
            pass

