import sys
import time

import psutil
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, \
    QDesktopWidget


# function of Get CPU State;
def get_cpu_state(interval=1):
    """
    获取cpu信息
    :param interval:阻塞时间，单位为秒
    :return: cpu使用率，已转换为str类型
    """
    return str(psutil.cpu_percent(interval))


# function of Get Memory
def get_memory_state():
    """
    获取内存信息
    :return: 返回内存使用率，已用内存，总共内存的元组
    """
    phymem = psutil.virtual_memory()
    return phymem.percent, int(phymem.used), int(phymem.total)


# function of get data to loop
def get_data_loop(interval=1):
    """
    获取cpu和网络信息，需要阻塞，所以设置一段时间间隔，再获取cpu，内存，网络信息
    :param interval: 阻塞时间，单位为秒
    :return:
    """
    before = psutil.net_io_counters()
    cpu_state = get_cpu_state(interval)
    memory_state = get_memory_state()
    after = psutil.net_io_counters()

    return cpu_state, memory_state, after.bytes_sent, after.bytes_recv, after.bytes_sent - before.bytes_sent, after.bytes_recv - before.bytes_recv


def bytes2human(n):
    """
    将字节数进行单位转换，如
    bytes2human(10000)='9.8 K'
    bytes2human(100001221)='95.4 M'
    :param n:
    :return:
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return "{:.2f} {}".format(value, s)
    return "{:.2f} B".format(n)


def update_output(cpu_state, memory_state, now_sent, now_recv, sent_rate, recv_rate, init_sent, init_recv):
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")

    print("Time: " + time.asctime())
    print("CPU 使用率: " + cpu_state + "%")
    print("内存使用率: " + str(memory_state[0]) + ", " + bytes2human(memory_state[1]) + "/" + bytes2human(memory_state[2]))
    print("网络状况: " + "已发送数据" + bytes2human(now_sent - init_sent)
          + ", 已接收数据" + bytes2human(now_recv - init_recv)
          + ", 发送速率" + bytes2human(sent_rate) + "/s, 接收速率"
          + bytes2human(recv_rate) + "/s")
    print()


class MainWindow(QWidget):

    loop = False

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        start_button = QPushButton("start")
        start_button.setToolTip("Start to get system info.")
        start_button.clicked.connect(self.start)
        stop_button = QPushButton("stop")
        stop_button.setToolTip("Stop to get system info.")
        stop_button.clicked.connect(self.stop)
        self.text = QLabel()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(start_button, 0, 0)
        grid.addWidget(stop_button, 0, 1)
        grid.addWidget(self.text, 1, 0, 3, 3)

        # 设置窗口大小
        self.setFixedSize(300, 400)

        # 将窗口置于屏幕正中间
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setLayout(grid)
        self.setWindowTitle("xixi")
        self.show()

    def start(self):
        interval = 0
        init_network_state = psutil.net_io_counters()
        init_sent = init_network_state.bytes_sent
        init_recv = init_network_state.bytes_recv
        while True:
            args = get_data_loop(interval)
            self.update_text(*args, init_sent, init_recv)
            interval = 1

    def stop(self):
        self.loop = False

    def update_text(self, cpu_state, memory_state, now_sent, now_recv, sent_rate, recv_rate, init_sent, init_recv):
        self.text.clear()
        txt = "Time: " + time.asctime() + "\n" + \
              "CPU 使用率: " + cpu_state + "%" + "\n" + \
              "内存使用率: " + str(memory_state[0]) + ", " + bytes2human(memory_state[1]) + "/" + bytes2human(memory_state[2]) + "\n" + \
              "网络状况: " + "已发送数据" + bytes2human(now_sent - init_sent) + ", 已接收数据" + bytes2human(now_recv - init_recv) + ", 发送速率" + bytes2human(sent_rate) + "/s, 接收速率" + bytes2human(recv_rate) + "/s"
        self.text.setText(txt)


if __name__ == "__main__":
    # interval = 0
    # init_network_state = psutil.net_io_counters()
    # init_sent = init_network_state.bytes_sent
    # init_recv = init_network_state.bytes_recv
    # while True:
    #     args = get_data_loop(interval)
    #     update_output(*args, init_sent, init_recv)
    #     interval = 1
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
