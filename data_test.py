import pymssql

conn = pymssql.connect(server='(local)', user='sa', password='Mrma0807.', database='test')
cursor = conn.cursor()
# cursor.execute("SELECT * FROM student")
# rows = cursor.fetchall()
# print(len(rows))
# for row in rows:
#     # print(type(row))
#     # for elem in row:
#     #     print(elem)
#     print(row)
sno = '1'
sname = 'E'
sdept = '2'
sclass = '2'
sdormarea = '2'
sage = '24'
# sql = 'insert into student values(%s,%s,%s,%s,%s,%s)'
# sql1 = 'select * from student where sno = %s'
# # cursor.execute(sql, (sno, sname, sdept, sclass, sdormarea, sage))
# # cursor.execute(sql1, sno)
# cursor.execute(sql1, sno)
# rows = cursor.fetchall()
old = '44'
sql = 'select cno, cnumber from class'
cursor.execute(sql)
rows = cursor.rowcount
# number = len(rows)
# message = '该班共有' + str(number) + '人'
# QtWidgets.QMessageBox.warning(self, "人数统计", message)
# print(message)
# for data in rows:
#     print(data)
# if rows:
#     print('yes')
# else:
#     print('no')
# conn.commit()
print(rows)
conn.close()
