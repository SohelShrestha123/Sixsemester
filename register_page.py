import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle("Register Account")
        self.setGeometry(200, 200, 500, 550)
        self.setWindowIcon(QIcon("r.jpg"))

        f = QFormLayout()
        self.lbl = QLabel("Register Account")
        self.lbl.setObjectName("lbl")
        self.lbl1 = QLabel("First Name")
        self.txt1 = QLineEdit(self)
        self.lbl2 = QLabel("Last Name")
        self.txt2 = QLineEdit(self)
        self.lbl3 = QLabel("Address")
        self.txt3 = QLineEdit(self)
        self.lbl4 = QLabel("Phone Number")
        self.txt4 = QLineEdit(self)
        self.lbl5 = QLabel("Email")
        self.txt5 = QLineEdit(self)
        self.lbl6 = QLabel("New Password")
        self.txt6 = QLineEdit(self)
        self.lbl7 = QLabel("Confirm Password")
        self.txt7 = QLineEdit(self)
        self.lbl8 = QLabel("Gender")
        self.radiobutton1 = QRadioButton("Male")
        self.radiobutton1.setChecked(True)
        self.radiobutton1.gender = "Male"
        self.radiobutton2 = QRadioButton("Female")
        self.radiobutton2.setChecked(True)
        self.radiobutton2.gender = "Female"
        self.btn = QPushButton("Submit")
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.radiobutton1)
        self.btn_group.addButton(self.radiobutton2)
        self.loglbl = QLabel("<a href='login.py'>Login</a>")
        self.loglbl.setOpenExternalLinks(False)
        self.loglbl.linkActivated.connect(self.open_log)
        self.loglbl.setObjectName("loglbl")

        self.lbl.setAlignment(Qt.AlignHCenter)
        self.loglbl.setAlignment(Qt.AlignHCenter)

        f.addRow(self.lbl)
        f.addRow(self.lbl1, self.txt1)
        f.addRow(self.lbl2, self.txt2)
        f.addRow(self.lbl3, self.txt3)
        f.addRow(self.lbl4, self.txt4)
        f.addRow(self.lbl5, self.txt5)
        f.addRow(self.lbl6, self.txt6)
        f.addRow(self.lbl7, self.txt7)
        f.addRow(self.lbl8)
        f.addRow(self.radiobutton1, self.radiobutton2)
        f.addRow(self.btn)
        f.addRow(self.loglbl)

        self.setStyleSheet('''
        QLabel#lbl{
        font-size:30px;
        font-weight:bold;
        font-family:Times New Roman;
        margin:5px;
        }

        QLabel{
        font-size:18px;
        font-weight:bold;
        font-family:Times New Roman;
        margin:5px;
        }

        QRadioButton{
        font-size:16px;
        font-family:Times New Roman;
        }

        QLineEdit{
        font-size:16px;
        font-family:Times New Roman;
        }

        QLabel#loglbl{
        font-size:16px;
        font-family:Times New Roman;
        color:green;
        margin:5px;
        }

        QPushButton{
        font-size:20px;
        font-family:Times New Roman;
        background-color:#025222;
        color:white;
        border-radius:6px;
        padding:5px;
        margin:5px;
        }

        QPushButton::hover{
        color:#c784db;
        background-color:#2ff538;
        }
        ''')

        self.setLayout(f)

    def open_log(self):
        from login_page import LoginPage
        self.login=LoginPage()
        self.login.show()
        self.close()


if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = RegisterPage()
    w.show()
    sys.exit(a.exec_())

