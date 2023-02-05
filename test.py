from PyQt5 import QtCore, QtGui, QtWidgets
from login_ui import Ui_Form as Login
from main_ui import Ui_Form as Admin


class Widget_main(QtWidgets.QWidget, Admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('管理员主界面')


# main_window = Widget_main()


class Widget_login(QtWidgets.QWidget, Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('登陆界面')
        self.pushButton.clicked.connect(self.check_password)

    def check_password(self):
        # 获取密码并进行校验
        account = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if account == '123' and pwd == '456':
            print("登录成功")
            global main_window
            main_window = Widget_main()
            main_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "错误", "账号或密码错误")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = Widget_main()
    ui_login = Widget_login()
    ui_login.show()
    # main_window = Widget_main()
    # main_window.show()
    # widget_admin = QtWidgets.QWidget()
    # ui_admin = Admin()
    # ui_admin.setupUi(widget_admin)
    # if ui_login.is_clicked:
    #     # print(ui_login.is_clicked)
    #     account = ui_login.lineEdit.text()
    #     pwd = ui_login.lineEdit_2.text()
    #     if account == '123' and pwd == '456':
    #         print("登录成功")
    #         ui_login.is_clicked = 0
    #         widget_login.close()
    #         widget_admin.show()
    #         break
    #     else:
    #         print("登录失败")
    #         QtWidgets.QMessageBox.warning(widget_login, '错误', '账号密码错误')
    #         ui_login.is_clicked = 0
    #         widget_admin.show()
    #         break

    sys.exit(app.exec_())
