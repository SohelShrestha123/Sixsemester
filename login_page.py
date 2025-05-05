import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle(" Customer Login")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(200, 200, 350, 450)

        l = QFormLayout()
        self.lbl = QLabel("User Login")

        self.i = QLabel(self)
        self.i.setGeometry(10, 10, 1, 1)
        self.pixel_map = QPixmap("p.png")
        self.i.setPixmap(self.pixel_map)
        self.i.setScaledContents(True)

        self.lbl1 = QLabel("Username:")
        self.user_input = QLineEdit(self)
        self.lbl2 = QLabel("Password:")
        self.pass_input = QLineEdit(self)
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton("Login")
        self.lbl3 = QLabel("Create an account?")
        self.lbl4 = QLabel("<a href='register_page.py'>Register</a>")
        self.lbl4.setOpenExternalLinks(False)
        self.lbl4.linkActivated.connect(self.open_reg)
        self.lbl3.setObjectName("lbl3")
        self.lbl4.setObjectName("lbl4")
        self.lbl.setObjectName("lbl")

        # Add widget in form format layout
        l.addRow(self.lbl)
        l.addRow(self.i)
        l.addRow(self.lbl1)
        l.addRow(self.user_input)
        l.addRow(self.lbl2)
        l.addRow(self.pass_input)
        l.addRow(self.login_btn)
        l.addRow(self.lbl3, self.lbl4)

        self.lbl.setAlignment(Qt.AlignHCenter)
        self.lbl1.setAlignment(Qt.AlignHCenter)
        self.user_input.setAlignment(Qt.AlignHCenter)
        self.lbl2.setAlignment(Qt.AlignHCenter)
        self.pass_input.setAlignment(Qt.AlignHCenter)

        self.setStyleSheet("""
        QPushButton{
        font-family:Times New Roman;
        font-size:20px;
        font-weight:bold;
        background-color:#79f7f7;
        border-radius:5px;
        color:#f67dfa;
        padding:10px;
        }

        QPushButton::hover{
         background-color:#5fd6fa;
         color: white;
        }

        QLabel{
         font-family:Times New Roman;
         font-size:20px;
         font-weight:bold;
        }

        QLabel#lbl3{
         font-family:Times New Roman;
         font-size:18px;
         font-weight:bold;
         padding:10px;
        }

        QLabel#lbl4{
         font-family:Times New Roman;
         font-size:16px;
         color:red;
        }

        QLabel#lbl{
        font-weight:bold;
        font-family:Times New Roman;
        font-size:30px;
        }

        QLineEdit{
        font-family:Times New Roman;
         font-size:20px;
         margin:4px;
         padding:4px;
        }

        QLabel#i{
        margin:1px;
        }
       
        """)

        self.setLayout(l)

    def open_reg(self):
        from register_page import  RegisterPage
        self.register=RegisterPage()
        self.register.show()
        self.close()


if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = LoginPage()
    w.show()
    sys.exit(a.exec_())