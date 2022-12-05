class log_out:
    __log_list = ['日志系统启动成功']

    def pop(self):
        if len(self.__log_list) > 0:
            return self.__log_list.pop(0)
        return None
    def push(self,data):
        self.__log_list.append(data)
log = log_out()