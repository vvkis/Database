from PyQt5 import QtCore, QtGui, QtWidgets
from login_ui import Ui_Form as Login
from main_ui import Ui_Form as Admin
from add_ui import Ui_Form as Add
from delete_ui import Ui_Form as Delete
from change_class_ui import Ui_Form as ChangeClass
from attend_ui import Ui_Form as Attend
import pymssql
import sys


class Widget_main(QtWidgets.QWidget, Admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('管理员主界面')
        self.pushButton_5.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.change_class)
        self.pushButton_4.clicked.connect(self.add_student)
        self.pushButton.clicked.connect(self.search_student)
        self.pushButton_6.clicked.connect(self.delete_student)
        self.pushButton_2.clicked.connect(self.attend)
        self.tableWidget.cellChanged.connect(self.cell_changed)
        self.init_table()

    def set_changed(self):
        for row in range(self.tableWidget.rowCount()):
            item1 = self.tableWidget.item(row, 0)
            item1.setFlags(QtCore.Qt.ItemIsEnabled)
            item2 = self.tableWidget.item(row, 3)
            item2.setFlags(QtCore.Qt.ItemIsEnabled)
            item3 = self.tableWidget.item(row, 4)
            item3.setFlags(QtCore.Qt.ItemIsEnabled)
            item4 = self.tableWidget.item(row, 5)
            item4.setFlags(QtCore.Qt.ItemIsEnabled)

    def cell_changed(self, row, col):
        # 在这里实现您的代码，知道发生更改的行和列
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        print("Cell changed at row %d, column %d" % (row, col))
        item = self.tableWidget.item(row, col)
        item_name = ['Sno', 'Sname', 'Sage', 'Sdeptno', 'Sclassno', 'Sdormarea']
        index = self.tableWidget.item(row, 0)
        new_content = item.text()
        new_content = new_content.encode('cp936')
        print(new_content)
        sno = index.text()
        sql = "update student set " + item_name[col] + " = %s where Sno = %s"
        # print(sql)
        cursor.execute(sql, (new_content, sno))
        conn.commit()
        conn.close()
        self.init_table()

    def init_table(self):
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        self.tableWidget.cellChanged.disconnect(self.cell_changed)
        self.tableWidget.setRowCount(0)
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        current_row_count = 0
        # self.tableWidget.setRowCount(len(rows))
        for data_list in rows:
            self.tableWidget.insertRow(current_row_count)
            for index, ele in enumerate(data_list):
                cell = QtWidgets.QTableWidgetItem(str(ele))
                self.tableWidget.setItem(current_row_count, index, cell)
            current_row_count += 1
        self.set_changed()
        conn.close()
        self.tableWidget.cellChanged.connect(self.cell_changed)

    def add_student(self):
        global add_window
        add_window.show()
        # self.close()

    def search_student(self):
        self.tableWidget.cellChanged.disconnect(self.cell_changed)
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        sno = self.lineEdit.text()
        if sno:
            sql = "select * from student where sno = %s"
            self.tableWidget.setRowCount(0)
            cursor.execute(sql, sno)
            rows = cursor.fetchall()
            current_row_count = 0
            # self.tableWidget.setRowCount(len(rows))
            for data_list in rows:
                self.tableWidget.insertRow(current_row_count)
                for index, ele in enumerate(data_list):
                    cell = QtWidgets.QTableWidgetItem(str(ele))
                    self.tableWidget.setItem(current_row_count, index, cell)
                current_row_count += 1
            self.set_changed()
            self.tableWidget.cellChanged.connect(self.cell_changed)
        else:
            self.tableWidget.cellChanged.connect(self.cell_changed)
            self.init_table()
        conn.close()

    def delete_student(self):
        global delete_window
        delete_window.show()

    def change_class(self):
        global change_class_window
        change_class_window.show()

    def check(self):
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        sql = 'select dno, dname, dcount from dept'
        cursor.execute(sql)
        rows = cursor.fetchall()
        sql1 = 'select * from student where sdeptno = %s'
        diff = 0
        for ele in rows:
            dno = ele[0]
            cursor.execute(sql1, dno)
            dnumber = ele[2]
            stu_number = len(cursor.fetchall())
            if dnumber != stu_number:
                sql2 = 'update dept set dcount = %s where dno = %s'
                cursor.execute(sql2, (stu_number, dno))
                conn.commit()
                info = '系号：' + str(dno) + '   系名：' + str(ele[1]) + '   原人数：' + str(dnumber) + '   实际人数：' + str(
                    stu_number)
                print(info)
                diff += 1
        message = '共有' + str(diff) + '个系人数存在问题，已经修改'
        if diff != 0:
            QtWidgets.QMessageBox.warning(self, "修改", message)
        else:
            QtWidgets.QMessageBox.warning(self, "修改", '系全部正确')
        conn.close()

    def attend(self):
        global attend_window
        attend_window.show()


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
            main_window.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "错误", "账号或密码错误")


class Widget_Add(QtWidgets.QWidget, Add):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('添加界面')
        self.pushButton.clicked.connect(self.add_student)
        self.pushButton_2.clicked.connect(self.return_main)

    def add_student(self):
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        sno = self.lineEdit.text()
        sname = self.lineEdit_2.text()
        sname = sname.encode('cp936')
        sdept = self.lineEdit_3.text()
        sclass = self.lineEdit_4.text()
        sdormarea = self.lineEdit_5.text()
        sdormarea = sdormarea.encode('cp936')
        sage = self.lineEdit_6.text()
        sql = 'insert into student values(%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (sno, sname, sage, sdept, sclass, sdormarea))
        conn.commit()
        conn.close()
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()

    def return_main(self):
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()


class Widget_Delete(QtWidgets.QWidget, Delete):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('删除界面')
        self.pushButton.clicked.connect(self.delete_student)
        self.pushButton_2.clicked.connect(self.return_main)

    def delete_student(self):
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        sno = self.lineEdit.text()
        sql = 'delete from student where sno=%s'
        cursor.execute(sql, sno)
        conn.commit()
        conn.close()
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()

    def return_main(self):
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()


class Widget_ChangeClass(QtWidgets.QWidget, ChangeClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('更改班号')
        self.pushButton.clicked.connect(self.change_class)
        self.pushButton_2.clicked.connect(self.return_main)

    def change_class(self):
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        old = self.lineEdit.text()
        new = self.lineEdit_2.text()
        sql0 = 'select * from student where sclassno = %s'
        cursor.execute(sql0, old)
        number = len(cursor.fetchall())
        message = '该班共有' + str(number) + '人'

        print(message)
        sql = 'update student set sclassno = NULL where sclassno=%s'
        cursor.execute(sql, old)
        conn.commit()

        sql1 = 'update class set cno = %s where cno=%s'
        cursor.execute(sql1, (new, old))
        conn.commit()

        sql2 = 'update student set sclassno = %s where sclassno is NULL'
        cursor.execute(sql2, new)
        conn.commit()

        conn.close()
        QtWidgets.QMessageBox.warning(self, "人数统计", message)
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()

    def return_main(self):
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()


class Widget_Attend(QtWidgets.QWidget, Attend):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('学会界面')
        self.pushButton.clicked.connect(self.add_attend)
        self.pushButton_2.clicked.connect(self.return_main)

    def add_attend(self):
        conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='StudentManage',
                               charset='cp936')
        cursor = conn.cursor()
        sno = self.lineEdit.text()
        uno = self.lineEdit_2.text()
        sql = 'insert into attend values(%s,%s)'
        cursor.execute(sql, (sno, uno))
        conn.commit()
        conn.close()
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()

    def return_main(self):
        self.close()
        global main_window
        main_window.init_table()
        # main_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Widget_main()
    add_window = Widget_Add()
    delete_window = Widget_Delete()
    change_class_window = Widget_ChangeClass()
    attend_window = Widget_Attend()
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
