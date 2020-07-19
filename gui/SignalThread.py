from PyQt5.QtCore import QThread, pyqtSignal


class SignalThread(QThread):  # 线程类
    my_signal = pyqtSignal(dict)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self, func):
        super(SignalThread, self).__init__()
        self.count = 0
        self.func = func
        self.work = True
        self.result = {"result": "", "status": "start"}

    # 析构函数
    def __del__(self):
        self.work = False
        self.wait()

    def run(self):  # 线程执行函数
        try:
            self.result['status'] = "running"
            data = self.func()
            self.result['status'] = "end"
            self.result['result'] = "succ"
            self.result['data'] = data
            self.my_signal.emit(self.result)
        except:
            self.result['status'] = "end"
            self.result['result'] = "error"
            self.my_signal.emit(self.result)
        print("SignalThread Finish")
