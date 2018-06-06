import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDesktopWidget, QGridLayout, QTextEdit, QWidget


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
        bt_clear_paste = QPushButton("clear&&paste", self)
        bt_paste = QPushButton("paste", self)
        bt_copy = QPushButton("copy", self)

        # 创建网格分布布局，并将文本框和按钮添加入其中
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(bt_clear, 0, 0)
        grid.addWidget(bt_clear_paste, 0, 1)
        grid.addWidget(bt_paste, 0, 2)
        grid.addWidget(bt_copy, 0, 7)
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
        bt_clear_paste.clicked.connect(self.bt_clear_paste_on_clicked)
        bt_paste.clicked.connect(self.bt_paste_on_clicked)
        bt_copy.clicked.connect(self.bt_copy_on_clicked)

    def txt_transform_when_changed(self):
        """
        监听input变化，实时将input按照规则转换之后填入output
        :return:
        """
        context = self.txt_in.toPlainText()
        self.txt_out.setText(context.strip().replace("\n", " ").replace(" (", "("))
        self.statusBar().showMessage("Transformed from input to output")

    def bt_clear_on_clicked(self):
        """
        按下clear按钮，将input输入框清空
        :return:
        """
        self.txt_in.clear()
        self.statusBar().showMessage("Cleared the input")

    def bt_clear_paste_on_clicked(self):
        """
        按下clear&paste按钮，将清空input框并将剪贴板中的文本粘贴到input框中
        :return:
        """
        clipboard = QApplication.clipboard()
        self.txt_in.setText(clipboard.text())
        self.statusBar().showMessage("Cleared and pasted the input")

    def bt_paste_on_clicked(self):
        """
        按下paste按钮，将剪贴板中的文本粘贴到input框文本后边
        :return:
        """
        clipboard = QApplication.clipboard()
        original = self.txt_in.toPlainText()
        if original:
            later = original + "\n" + clipboard.text()
        else:
            later = clipboard.text()
        self.txt_in.setText(later)

    def bt_copy_on_clicked(self):
        """
        按下copy按钮，将output框中文本复制如剪贴板中
        :return:
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.txt_out.toPlainText())
        self.statusBar().showMessage("Copied the output to the clipboard")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
