import hashlib
import json
import random
import sys
import urllib
from http.client import HTTPConnection

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDesktopWidget, QGridLayout, QTextEdit, QWidget, \
    QLabel


class TransThread(QThread):
    """
    开一个翻译线程
    """
    finished_signal = pyqtSignal(object)

    def __init__(self, q, parent=None):
        super().__init__(parent)
        self._q = q

    def change_q(self, q):
        self._q = q

    def run(self):
        result = self.translate(self._q)
        self.finished_signal.emit(result)

    @staticmethod
    def translate(q):
        if not q:
            return None
        appid = "20180530000169197"
        secret_key = "wbwZhZfzgFwlh1EqVNaN"
        http_client = None
        url = "/api/trans/vip/translate"
        from_lang = "auto"
        to_lang = "zh"
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secret_key
        m1 = hashlib.md5()
        m1.update(sign.encode())
        sign = m1.hexdigest()
        url = url + "?appid=" + appid + "&q=" + urllib.parse.quote(q) + "&from=" + from_lang + "&to=" + to_lang + "&salt=" + str(salt) + "&sign=" + sign
        try:
            http_client = HTTPConnection("api.fanyi.baidu.com")
            http_client.request("GET", url)
            response = json.loads(http_client.getresponse().read())
            if "error_code" in response:
                return None
            return response["trans_result"][0]["dst"]
        except Exception as e:
            print(e)
            return None
        finally:
            if http_client:
                http_client.close()


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("transform")

        # 设置窗口大小
        self.setFixedSize(800, 400)

        # 使窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 设置状态栏
        self.statusBar()

        # 在窗口中创建两个文本框，一个用于输入，一个用于输出
        self.txt_in = QTextEdit()
        self.txt_out = QTextEdit()

        # 在窗口中创建按钮
        bt_clear = QPushButton("clear", self)
        bt_paste = QPushButton("clear&&paste", self)

        lb_tip = QLabel("使用的是百度翻译", self)

        # 创建网格分布布局，并将文本框和按钮添加入其中
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(bt_clear, 0, 0)
        grid.addWidget(bt_paste, 0, 1)
        grid.addWidget(lb_tip, 0, 7)
        grid.addWidget(self.txt_in, 1, 0, 5, 3)
        grid.addWidget(self.txt_out, 1, 6, 5, 3)

        # 将布局添加到窗口
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        # 监听input文本输入框变化，与事件相关联
        self.txt_in.textChanged.connect(self.txt_transform_when_changed)

        # 按钮与事件相关联
        bt_clear.clicked.connect(self.bt_clear_on_clicked)
        bt_paste.clicked.connect(self.bt_paste_on_clicked)

        # 创建一个翻译线程
        self.trans_thread = TransThread(None)

    def update_out(self, message):
        """
        message可能是None或者是翻译后的字符串
        :param message:
        :return:
        """
        if message:
            self.txt_out.setText(message)
        else:
            self.txt_out.clear()

    def txt_transform_when_changed(self):
        """
        监听input变化，实时将input按照规则转换之后再调用翻译线程进行翻译填入output
        :return:
        """
        # 获取input输入
        context = self.txt_in.toPlainText()
        # 将input输入按照规则转换
        convert_result = context.strip().replace("\n", " ").replace(" (", "(")
        # 如果线程没有在运行（即已结束）那么进行下一个翻译线程，如果还在进行，那么不进行操作
        if not self.trans_thread.isRunning():
            self.trans_thread.change_q(convert_result)
            self.trans_thread.finished_signal.connect(self.update_out)
            self.trans_thread.start()

    def bt_clear_on_clicked(self):
        """
        按下clear按钮，将input输入框清空
        :return:
        """
        self.txt_in.clear()
        self.statusBar().showMessage("Cleared the input")

    def bt_paste_on_clicked(self):
        """
        按下paste按钮，将剪贴板中的文本粘贴到input框中
        :return:
        """
        clipboard = QApplication.clipboard()
        self.txt_in.setText(clipboard.text())
        self.statusBar().showMessage("Cleared and pasted the input")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
