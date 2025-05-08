import sys
import traceback
import sqlite3
from PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,QHBoxLayout,
QLineEdit,QPushButton,QListWidget,QMessageBox,QLabel)
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
from PyQt5.sip import delete

sys.excepthook = lambda exctype, value, tb: print("".join(traceback.format_exception(exctype, value, tb)))

class AdminPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        self.setWindowTitle("Admin")
        self.setWindowIcon(QIcon("admin.png"))
        self.setGeometry(300,300,600,700)

        #To show menu item
        self.l=QVBoxLayout()
        self.mList=QListWidget()
        self.mList.setObjectName("menuList")
        self.l.addWidget(QLabel("Menu Item"))
        self.l.addWidget(self.mList)

        #Input Item name and price
        self.name=QLineEdit()
        self.name.setPlaceholderText("Item name")
        self.price=QLineEdit()
        self.price.setPlaceholderText("Price")


        self.input=QHBoxLayout()
        self.input.addWidget(self.name)
        self.input.addWidget(self.price)
        self.l.addLayout(self.input)

        #For button layout
        self.btnLayout=QHBoxLayout()
        self.add_btn=QPushButton("Add") #Add button
        self.add_btn.setObjectName("btn1")
        self.add_btn.clicked.connect(self.add)
        self.edit_btn=QPushButton("Edit") #Edit button
        self.edit_btn.setObjectName("btn2")
        self.edit_btn.clicked.connect(self.edit)
        self.delete_btn=QPushButton("Delete") #Delete button
        self.delete_btn.setObjectName("btn3")
        self.delete_btn.clicked.connect(self.delete)
        self.btnLayout.addWidget(self.add_btn)
        self.btnLayout.addWidget(self.edit_btn)
        self.btnLayout.addWidget(self.delete_btn)
        self.l.addLayout(self.btnLayout)

        self.setStyleSheet('''
        QPushButton#btn1{
        background-color:green;
        font-weight:bold;
        }
        QPushButton#btn1:hover{
        background-color:#52fa7c;
        color:white;
        }
        
        QPushButton#btn2{
        background-color:blue;
        font-weight:bold;
        }
        QPushButton#btn2:hover{
        background-color:#536bf5;
        color:white;
        }
        
        QPushButton#btn3{
        background-color:red;
        font-weight:bold;
        }
        QPushButton#btn3:hover{
        background-color:#f74a5c;
        color:white;
        }
        
        QListWidget#menuList{
        background-color:#72e9ed;
        color:black;
        font-weight:bold;
        font-size:18px;
        }
        ''')

        self.setLayout(self.l)
        self.load()


    def load(self):
        try:
         self.mList.clear()
         con=sqlite3.connect('menu.db')
         cursor=con.cursor()
         cursor.execute("SELECT * FROM menu")
         for r in cursor.fetchall():
            self.mList.addItem(f"{r[0]}. : {r[1]}..............................Rs.{r[2]:.2f}")
         con.close()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Failed to load menu:{e}")

    def add(self):
        n=self.name.text().strip()
        p=self.price.text().strip()

        if not n or not p:
            QMessageBox.warning(self,"Notification","Data should not be empty.")
            return

        try:
            p=int(p)
        except ValueError:
            QMessageBox.warning(self,"Notice","price should be number not in word")
            return

        try:
         con=sqlite3.connect('menu.db')
         cursor=con.cursor()
         cursor.execute("INSERT INTO menu (Name,Price) VALUES (?,?)",(n,p))
         con.commit()
         con.close()
         self.name.clear()
         self.price.clear()
         self.load()
        except Exception as e:
            QMessageBox.critical(self,"Error",f"Failed to load menu:{e}")

    def edit(self):
        i=self.mList.currentItem()
        if not i:
            QMessageBox.warning(self,"Notice","Select an item for edit.")
            return
        try:
         i_id=int(i.text().split("-")[0])
         n = self.name.text().strip()
         p = self.price.text().strip()

         if not n or not p:
             QMessageBox.warning(self,"Notification","Data should not be empty.")
             return

         p=float(p)
         con=sqlite3.connect('menu.db')
         cursor=con.cursor()
         cursor.execute("UPDATE menu SET Name=? ,Price=? WHERE Id=?",(n,p,i_id))
         con.commit()
         con.close()
         self.load()
        except ValueError:
            QMessageBox.warning(self,"Notice","price should be number not in word")
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to edit item: {e}")

    def delete(self):
        i = self.mList.currentItem()
        if not i:
            QMessageBox.warning(self, "Notice", "Select an item for delete.")
            return
        try:
         i_id=float(i.text().split("-")[0])

         con=sqlite3.connect('menu.db')
         cursor=con.cursor()
         cursor.execute("DELETE FROM menu WHERE Id=?",(i_id,))
         con.commit()
         con.close()
         self.load()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to delete item: {e}")


if __name__=="__main__":
    a=QApplication(sys.argv)
    w=AdminPanel()
    w.show()
    sys.exit(a.exec_())