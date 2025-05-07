import sys
import sqlite3

from PyQt5.QtWidgets import(QApplication,QWidget,QLabel,
QPushButton,QListWidget,QVBoxLayout,QMessageBox)
from PyQt5.QtGui import QIcon

class Menu(QWidget):
    #Default Constructor
   def __init__(self):
       super().__init__()
       self.setWindowTitle("Hungry Food")
       self.setWindowIcon(QIcon("logo.png"))
       self.setGeometry(300,300,600,700)
       self.cart=[]
       self.total=0
       self.setUi()

   #Function to set design of UI for application
   def setUi(self):
       self.layout=QVBoxLayout()
       self.layout.setObjectName("mylayout")
       self.myList=QListWidget()
       self.myList.setObjectName("my_list")


       self.good_list=QListWidget()
       self.good_list.setObjectName("goodList")

       self.lbl=QLabel("Total: Rs.0")

      #Display all item that are stored in database
       self.load()
       self.layout.addWidget(QLabel("Menu"))
       self.layout.addWidget(self.myList)


       #Making 'Add to cart' button to add food in order list
       btn=QPushButton("Add to cart")
       btn.setObjectName("mybtn")
       btn.clicked.connect(self.addCart)
       self.layout.addWidget(btn)


       #Display added item in cart's list
       self.layout.addWidget(QLabel("Cart"))
       self.layout.addWidget(self.good_list)
       self.layout.addWidget(self.lbl)

       #Making 'Place Order' button to order food
       order=QPushButton("Order")
       order.setObjectName("myorder")
       order.clicked.connect(self.orderPlace)
       self.layout.addWidget(order)

       #Styling widget
       self.setStyleSheet("""
       QVBoxLayout#mylayout{
       background-color:#b829e3;
       }
              QListWidget#my_list{
              background-color:#f54955;
              color:#9ca19d;
              font-weight:bold;
              font-size:16px;
              }
              
              QListWidget#goodList{
       background-color:#5179f0;
       color:#d2d4c7;
       }
       
        QPushButton#mybtn{
                     background-color:#066626;
                     color:#0c0d0d;
                     }
                     
        QPushButton#mybtn:hover{
                     background-color:#22e369;
                      color:white;
                     }
                     
                     QPushButton#myorder{
                     background-color:#f26411;
                     color:#141414;
                     }
                     
        QPushButton#myorder:hover{
                     background-color:#f27949;
                      color:white;
                     }
              
              """)

       #Initializing layout
       self.setLayout(self.layout)

   def load(self):
       conn=sqlite3.connect("menu.db")
       cursor=conn.cursor()
       cursor.execute("SELECT id,name,price FROM menu")
       for data in cursor.fetchall():
           self.myList.addItem(f"{data[0]}. :  {data[1]}...............................Rs.{data[2]}")
           conn.close()

   def addCart(self):
       food=self.myList.currentItem()
       if food:
           self.cart.append(food.text())
           self.good_list.addItem(food.text())

           price=float(food.text().split("-Rs.")[1])
           self.total+=price
           self.lbl.setText("Total:Rs self.total")

   def orderPlace(self):
       if not self.cart:
           QMessageBox.warning(self,"Notification","Cart is empty.")
           return

       conn=sqlite3.connect("menu.db")
       cursor=conn.cursor()

       for i in self.cart:
           food=i.split("-Rs.")[0]
           p=float(i.split("-Rs.")[1])
           cursor.execute("INSERT INTO orders(Foodname,Quantity,TotalPrice)VALUES(?,?,?)",(food,1,p))


       conn.commit()
       conn.close()
       QMessageBox.information(self,"Notification","Order has been placed.Please wait for moment.")
       self.cart=[]
       self.total=0
       self.lbl.setText("Total: Rs.0")

if __name__=='__main__':
    a=QApplication(sys.argv)
    w=Menu()
    w.show()
    sys.exit(a.exec_())