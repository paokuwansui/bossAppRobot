from tkinter import *
from tkinter.ttk import *
from json import load, dump
# from thread import ctrl_class
from time import sleep
from log_code import log
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_tabs_config_and_log = Frame_config_and_log(self)
        self.ctrl_windows = ctrl_windows(self)
        self.tk_button_lay4zau3 = self.__tk_button_lay4zau3()

    def __win(self):
        self.title("刘暄的工作小工具")
        # 设置窗口大小、居中
        width = 600
        height = 520
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_button_lay4zau3(self):
        btn = Button(self, text="保存修改后的配置")
        btn.place(x=220, y=486, width=155, height=31)
        return btn
        
class Frame_config_and_log(Notebook):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):
        with open('./config.json','r',encoding='utf8')as fp:
            config_json_data = load(fp)
        self.area_list = []
        for i, item in enumerate(config_json_data):
            tk_tabs_config = Frame_config(self, item, config_json_data[item])
            self.add(tk_tabs_config, text='帖子 ' + str(i+1))
            self.area_list.append(tk_tabs_config)
        self.tk_tabs_log = Frame_log(self)
        self.add(self.tk_tabs_log, text="工具运行日志")
        self.place(x=5, y=160, width=595, height=400)

class Frame_config(Frame):
    def __init__(self,parent, name, config):
        super().__init__(parent)
        self.__frame()
        self.name = name
        self.config = config
        # self.tk_label_lay0xugu = self.__tk_label_lay0xugu()
        # self.tk_input_stant_age = self.__tk_input_stant_age()
        # self.tk_input_end_gae = self.__tk_input_end_gae()
        # self.tk_label_lay10gxf = self.__tk_label_lay10gxf()
        self.tk_label_lay11xnf = self.__tk_label_lay11xnf()
        self.tk_label_lay19pd0 = self.__tk_label_lay19pd0()
        self.tk_label_lay1ftex = self.__tk_label_lay1ftex()
        self.tk_check_button_intention_1 = self.__tk_check_button_intention_1()
        self.tk_check_button_intention_2 = self.__tk_check_button_intention_2()
        self.tk_check_button_intention_3 = self.__tk_check_button_intention_3()
        self.tk_label_lay1x4sl = self.__tk_label_lay1x4sl()
        self.tk_label_lay1z1pb = self.__tk_label_lay1z1pb()
        self.tk_label_lay1zz8r = self.__tk_label_lay1zz8r()
        self.tk_label_lay20ov5 = self.__tk_label_lay20ov5()
        self.tk_input_greet_input_time = self.__tk_input_greet_input_time()
        self.tk_input_expectation_input = self.__tk_input_expectation_input()
        self.tk_input_expectation_not_input = self.__tk_input_expectation_not_input()
        self.tk_input_experienced_input = self.__tk_input_experienced_input()
        self.tk_input_experienced_not_input = self.__tk_input_experienced_not_input()
        self.tk_label_lay40p5c = self.__tk_label_lay40p5c()
        self.tk_check_button_man = self.__tk_check_button_man()
        self.tk_check_button_woman = self.__tk_check_button_woman()
        self.tk_check_button_active_1 = self.__tk_check_button_active_1()
        self.tk_check_button_active_2 = self.__tk_check_button_active_2()
        self.tk_check_button_active_3 = self.__tk_check_button_active_3()
        self.tk_label_name = self.__tk_label_name(name)
        self.tk_check_button_only_look_online = self.__tk_check_button_only_look_online()
        self.tk_check_button_greet_of_time = self.__tk_check_button_greet_of_time()
        self.tk_label_greet_flag = self.__tk_label_greet_flag()
        
    def __frame(self):
        self.place(x=5, y=150, width=590, height=325)

    # def __tk_label_lay0xugu(self):
    #     label = Label(self,text="年龄：")
    #     label.place(x=0, y=60, width=38, height=18)
    #     return label

    # def __tk_input_stant_age(self):
    #     ipt = Entry(self)
    #     ipt.insert(0, self.config["年龄"][0])
    #     ipt.place(x=58, y=60, width=28, height=19)
    #     return ipt

    # def __tk_input_end_gae(self):
    #     ipt = Entry(self)
    #     ipt.insert(0, self.config["年龄"][1])
    #     ipt.place(x=108, y=60, width=28, height=19)
    #     return ipt

    # def __tk_label_lay10gxf(self):
    #     label = Label(self,text="-")
    #     label.place(x=90, y=60, width=15, height=19)
    #     return label

    def __tk_label_lay11xnf(self):
        label = Label(self,text="性别：")
        label.place(x=0, y=60, width=58, height=18)
        return label

    def __tk_label_lay19pd0(self):
        label = Label(self,text="活跃度：")
        label.place(x=0, y=100, width=50, height=18)
        return label

    def __tk_label_lay1ftex(self):
        label = Label(self,text="求职意向：")
        label.place(x=0, y=140, width=58, height=18)
        return label

    def __tk_check_button_intention_1(self):
        self.check_button_intention_1 = BooleanVar()
        if "离职随时到岗" in self.config["求职意向"]:
            self.check_button_intention_1.set(True)
        else:
            self.check_button_intention_1.set(False)
        cb = Checkbutton(self,text="离职随时到岗",var = self.check_button_intention_1)
        cb.place(x=70, y=140, width=125, height=24)
        return cb

    def __tk_check_button_intention_2(self):
        self.check_button_intention_2 = BooleanVar()
        if "在职月内到岗" in self.config["求职意向"]:
            self.check_button_intention_2.set(True)
        else:
            self.check_button_intention_2.set(False)
        cb = Checkbutton(self,text="在职月内到岗",var = self.check_button_intention_2)
        cb.place(x=210, y=140, width=125, height=24)
        return cb

    def __tk_check_button_intention_3(self):
        self.check_button_intention_3 = BooleanVar()
        if "在职考虑机会" in self.config["求职意向"]:
            self.check_button_intention_3.set(True)
        else:
            self.check_button_intention_3.set(False)
        cb = Checkbutton(self,text="在职考虑机会",var = self.check_button_intention_3)
        cb.place(x=350, y=140, width=125, height=24)
        return cb

    def __tk_label_lay1x4sl(self):
        label = Label(self,text="期望职位关键字：")
        label.place(x=0, y=180, width=97, height=18)
        return label

    def __tk_label_lay1z1pb(self):
        label = Label(self,text="过往经历关键字：")
        label.place(x=0, y=220, width=97, height=18)
        return label

    def __tk_label_lay1zz8r(self):
        label = Label(self,text="期望职位排除关键字：")
        label.place(x=280, y=180, width=122, height=18)
        return label

    def __tk_label_lay20ov5(self):
        label = Label(self,text="过往经历排除关键字：")
        label.place(x=280, y=220, width=121, height=18)
        return label

    def __tk_input_greet_input_time(self):
        self.greet_input_time = StringVar()
        ipt = Entry(self, textvar=self.greet_input_time)
        self.greet_input_time.set(','.join(self.config["打招呼时间段"]))
        ipt.place(x=100, y=260, width=477, height=24)
        return ipt

    def __tk_input_expectation_input(self):
        self.expectation_input = StringVar()
        ipt = Entry(self, textvar=self.expectation_input)
        self.expectation_input.set(','.join(self.config["期望职位关键字"]))
        ipt.place(x=100, y=180, width=171, height=24)
        return ipt

    def __tk_input_expectation_not_input(self):
        self.expectation_not_input = StringVar()
        ipt = Entry(self, textvar=self.expectation_not_input)
        self.expectation_not_input.set(','.join(self.config["期望职位排除关键字"]))
        ipt.place(x=410, y=180, width=171, height=24)
        return ipt

    def __tk_input_experienced_input(self):
        self.experienced_input = StringVar()
        ipt = Entry(self, textvar=self.experienced_input)
        self.experienced_input.set(','.join(self.config["过往经历关键字"]))
        ipt.place(x=100, y=220, width=171, height=24)
        return ipt

    def __tk_input_experienced_not_input(self):
        self.experienced_not_input = StringVar()
        ipt = Entry(self, textvar=self.experienced_not_input)
        self.experienced_not_input.set(','.join(self.config["过往经历排除关键字"]))
        ipt.place(x=410, y=220, width=171, height=24)
        return ipt

    def __tk_label_lay40p5c(self):
        label = Label(self,text="打招呼时间段：")
        label.place(x=0, y=260, width=85, height=18)
        return label

    def __tk_check_button_man(self):
        self.check_button_man = BooleanVar()
        if "男" in self.config["性别"]:
            self.check_button_man.set(True)
        else:
            self.check_button_man.set(False)
        cb = Checkbutton(self,text="男",var = self.check_button_man)
        cb.place(x=40, y=60, width=42, height=24)
        return cb

    def __tk_check_button_woman(self):
        self.check_button_woman = BooleanVar()
        if "女" in self.config["性别"]:
            self.check_button_woman.set(True)
        else:
            self.check_button_woman.set(False)
        cb = Checkbutton(self,text="女",var = self.check_button_woman)
        cb.place(x=80, y=60, width=42, height=24)
        return cb

    def __tk_check_button_active_1(self):
        self.check_button_active_1 = BooleanVar()
        if "刚刚活跃" in self.config["活跃度"]:
            self.check_button_active_1.set(True)
        else:
            self.check_button_active_1.set(False)
        cb = Checkbutton(self,text="刚刚活跃",var = self.check_button_active_1)
        cb.place(x=60, y=100, width=98, height=24)
        return cb

    def __tk_check_button_active_2(self):
        self.check_button_active_2 = BooleanVar()
        if "今日活跃" in self.config["活跃度"]:
            self.check_button_active_2.set(True)
        else:
            self.check_button_active_2.set(False)
        cb = Checkbutton(self,text="今日活跃",var = self.check_button_active_2)
        cb.place(x=170, y=100, width=98, height=24)
        return cb

    def __tk_check_button_active_3(self):
        self.check_button_active_3 = BooleanVar()
        if "近三日活跃" in self.config["活跃度"]:
            self.check_button_active_3.set(True)
        else:
            self.check_button_active_3.set(False)
        cb = Checkbutton(self,text="近三日活跃",var = self.check_button_active_3)
        cb.place(x=280, y=100, width=114, height=24)
        return cb

    def __tk_label_name(self, name):
        label = Label(self,text="帖子名称：" + name)
        label.place(x=0, y=0, width=300, height=18)
        return label

    def __tk_check_button_only_look_online(self):
        self.check_button_only_look_online = BooleanVar()
        if "是" in self.config["是否只看在线"]:
            self.check_button_only_look_online.set(True)
        else:
            self.check_button_only_look_online.set(False)
        cb = Checkbutton(self,text="是否只看在线",var = self.check_button_only_look_online)
        cb.place(x=0, y=22, width=128, height=24)
        return cb

    def __tk_check_button_greet_of_time(self):
        self.check_button_greet_of_time = BooleanVar()
        if "是" in self.config["是否按时间段打招呼"]:
            self.check_button_greet_of_time.set(True)
        else:
            self.check_button_greet_of_time.set(False)
        cb = Checkbutton(self,text="是否按时间段打招呼",var = self.check_button_greet_of_time)
        cb.place(x=144, y=22, width=181, height=24)
        return cb

    def __tk_label_greet_flag(self):
        label = Label(self,text="该帖子已打招呼：")
        label = Label(self)
        label.place(x=300, y=0, width=103, height=18)
        return label
        
class Frame_log(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.log_area = self.__tk_text_lay422hf()
        self.bind()
    def __frame(self):
        self.place(x=10, y=150, width=583, height=325)

    def __tk_text_lay422hf(self):
        sb = Scrollbar(self)  
        text = Text(self, yscrollcommand = sb.set)
        text.place(x=10, y=10, width=549, height=265)
        sb.pack(side=RIGHT,fill=Y) 
        sb.config(command=text.yview)
        text.config(yscrollcommand=sb.set)
        log.push('日志系统输出正常')
        return text
    def bind(self):
        log_data = log.pop()
        if log_data != None:
            self.log_area.insert(END, log_data + '\n')
        self.after(750, self.bind)

class ctrl_windows(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_button_only_look_resume = self.__tk_button_only_look_resume()
        self.tk_button_start_greet_all = self.__tk_button_start_greet_all()
        self.tk_button_start_greet_five = self.__tk_button_start_greet_five()
        self.tk_button_start_call_old = self.__tk_button_start_call_old()
        self.tk_button_stop_all = self.__tk_button_stop_all()
        self.check_list = []
        with open('./config.json','r',encoding='utf8')as fp:
            config_json_data = load(fp)
        self.config = config_json_data
        for i in config_json_data:
            self.check_list.append([self.__tk_check_button(i), i])
        self.bind_env()
            
    def __frame(self):
        self.place(x=10, y=10, width=585, height=130)

    def __tk_button_only_look_resume(self):
        btn = Button(self, text="开始翻简历")
        btn.place(x=0, y=0, width=100, height=30)
        return btn

    def __tk_button_start_greet_all(self):
        btn = Button(self, text="开始打全部招呼")
        btn.place(x=120, y=0, width=100, height=30)
        return btn
        
    def __tk_button_start_greet_five(self):
        btn = Button(self, text="再打5个招呼")
        btn.place(x=240, y=0, width=100, height=30)
        return btn
    
    def __tk_button_start_call_old(self):
        btn = Button(self, text="沟通已打招呼的")
        btn.place(x=360, y=0, width=100, height=30)
        return btn
    
    def __tk_button_stop_all(self):
        btn = Button(self, text="停止沟通和翻阅")
        btn.place(x=480, y=0, width=100, height=30)
        return btn
    
    def bind_env(self):
        self.tk_button_only_look_resume.bind('<Button>',self.start_look_resume)
        self.tk_button_start_greet_all.bind('<Button>',self.start_greet_all)
        self.tk_button_start_greet_five.bind('<Button>',self.start_greet_five)
        self.tk_button_start_call_old.bind('<Button>',self.start_call_old)
        self.tk_button_stop_all.bind('<Button>',self.stop_all)
    def __tk_check_button(self, name):
        cb_value = BooleanVar()
        cb_value.set(True)
        cb = Checkbutton(self,text = name,var = cb_value)
        index = self.config[name]["排序"]
        if index <= 5:
            x = 0 + 120 * (index - 1)
            y = 60
        else:
            x = 0 + 120 * (index - 6)
            y = 100
        cb.place(x=x, y=y, width=105, height=24)
        return cb_value
        
    def start_look_resume(self,evt):
        job_list = []
        for i in self.check_list:
            if i[0].get() == True:
                job_list.append(i[1])
        ctrl.look_resume(job_list, 25)

    def start_greet_all(self,env):
        job_list = []
        for i in self.check_list:
            if i[0].get() == True:
                job_list.append(i[1])
        for i in job_list:
            ctrl.add_greet_max_num(i, 100)

    def start_greet_five(self,env):
        job_list = []
        for i in self.check_list:
            if i[0].get() == True:
                job_list.append(i[1])
        for i in job_list:
            ctrl.add_greet_max_num(i, 5)

    def start_call_old(self,env):
        job_list = []
        for i in self.check_list:
            if i[0].get() == True:
                job_list.append(i[1])
        ctrl.call_old(job_list, 250)

    def stop_all(self,env):
        ctrl.stop_all()

        

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        # global ctrl 
        # ctrl = ctrl_class()
        # ctrl.login()
        # sleep(2.5)
        # ctrl.start_greet()
        # ctrl.open_time_greet()
        
    def save_config(self,evt):
        log.push("系统配置文件正在保存")
        save_dict = {}
        area_list = self.tk_tabs_config_and_log.area_list
        for ob in area_list:
            save_dict[ob.name] = ob.config
            # save_dict[ob.name]["年龄"][0] = eval(ob.tk_input_stant_age.get())
            # save_dict[ob.name]["年龄"][1] = eval(ob.tk_input_end_gae.get())

            if ob.check_button_man.get() == True:
                save_dict[ob.name]["性别"].append("男")
            else:
                if "男" in save_dict[ob.name]["性别"]:
                    save_dict[ob.name]["性别"].remove("男")
            if ob.check_button_woman.get() == True:
                save_dict[ob.name]["性别"].append("女")
            else:
                if "女" in save_dict[ob.name]["性别"]:
                    save_dict[ob.name]["性别"].remove("女")
            save_dict[ob.name]["性别"] = list(set(save_dict[ob.name]["性别"]))

            if ob.check_button_only_look_online.get() == True:
                save_dict[ob.name]["是否只看在线"] = "是"
            else:
                save_dict[ob.name]["是否只看在线"] = "否"

            if ob.check_button_greet_of_time.get() == True:
                save_dict[ob.name]["是否按时间段打招呼"] = "是"
            else:
                save_dict[ob.name]["是否按时间段打招呼"] = "否"

            if ob.check_button_active_1.get() == True:
                save_dict[ob.name]["活跃度"].append("刚刚活跃")
            else:
                if "刚刚活跃" in save_dict[ob.name]["活跃度"]:
                    save_dict[ob.name]["活跃度"].remove("刚刚活跃")
            if ob.check_button_active_2.get() == True:
                save_dict[ob.name]["活跃度"].append("今日活跃")
            else:
                if "今日活跃" in save_dict[ob.name]["活跃度"]:
                    save_dict[ob.name]["活跃度"].remove("今日活跃")
            if ob.check_button_active_3.get() == True:
                save_dict[ob.name]["活跃度"].append("近三日活跃")
            else:
                if "近三日活跃" in save_dict[ob.name]["活跃度"]:
                    save_dict[ob.name]["活跃度"].remove("近三日活跃")
            save_dict[ob.name]["活跃度"] = list(set(save_dict[ob.name]["活跃度"]))

            if ob.check_button_intention_1.get() == True:
                save_dict[ob.name]["求职意向"].append("离职随时到岗")
            else:
                if "离职随时到岗" in save_dict[ob.name]["求职意向"]:
                    save_dict[ob.name]["求职意向"].remove("离职随时到岗")
            if ob.check_button_intention_2.get() == True:
                save_dict[ob.name]["求职意向"].append("在职月内到岗")
            else:
                if "在职月内到岗" in save_dict[ob.name]["求职意向"]:
                    save_dict[ob.name]["求职意向"].remove("在职月内到岗")
            if ob.check_button_intention_3.get() == True:
                save_dict[ob.name]["求职意向"].append("在职考虑机会")
            else:
                if "在职考虑机会" in save_dict[ob.name]["求职意向"]:
                    save_dict[ob.name]["求职意向"].remove("在职考虑机会")
            save_dict[ob.name]["求职意向"] = list(set(save_dict[ob.name]["求职意向"]))

            save_dict[ob.name]["期望职位关键字"] = ob.expectation_input.get().replace("，",",").split(',')
            if save_dict[ob.name]["期望职位关键字"] == [""]:
                save_dict[ob.name]["期望职位关键字"] = []

            save_dict[ob.name]["期望职位排除关键字"] = ob.expectation_not_input.get().replace("，",",").split(',')
            if save_dict[ob.name]["期望职位排除关键字"] == [""]:
                save_dict[ob.name]["期望职位排除关键字"] = []

            save_dict[ob.name]["过往经历关键字"] = ob.experienced_input.get().replace("，",",").split(',')
            if save_dict[ob.name]["过往经历关键字"] == [""]:
                save_dict[ob.name]["过往经历关键字"] = []

            save_dict[ob.name]["过往经历排除关键字"] = ob.experienced_not_input.get().replace("，",",").split(',')
            if save_dict[ob.name]["过往经历排除关键字"] == [""]:
                save_dict[ob.name]["过往经历排除关键字"] = []

            save_dict[ob.name]["打招呼时间段"] = ob.greet_input_time.get().replace("，",",").split(',')
            if save_dict[ob.name]["打招呼时间段"] == [""]:
                save_dict[ob.name]["打招呼时间段"] = []
            
        with open('./config.json','w',encoding='utf8')as fp:
            dump(save_dict,fp,ensure_ascii=False)
        log.push("系统配置文件保存完成")
    def __event_bind(self):
        self.tk_button_lay4zau3.bind('<Button>',self.save_config)
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
