from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import *
import re
import sys
import FontColor_array
import frame

# login frame
class Login(QWidget):
	close_signal = pyqtSignal()
	def __init__(self):
		super(Login,self).__init__()
		self.loginui()

	def loginui(self):
		self.resize(600,300)
		self.setWindowTitle("Login")
		
		# button
		log = QPushButton("登入",self)
		log.clicked.connect(self.determine)

		log.setFont(FontColor_array.Font_list[3])

		# label
		title = QLabel("--登入畫面--",self)
		self.error_login = QLabel("",self)
		# self.error_login.setStyleSheet(FontColor_array.Color_list[1])
		ac_text = QLabel("帳號: ",self)
		pw_text = QLabel("密碼: ",self)

		title.setFont(FontColor_array.Font_list[2])
		ac_text.setFont(FontColor_array.Font_list[2])
		pw_text.setFont(FontColor_array.Font_list[2])
		self.error_login.setFont(FontColor_array.Font_list[4])

		# LineEdit
		self.account = QLineEdit("",self)
		self.passwd = QLineEdit("",self)

		self.account.setFont(FontColor_array.Font_list[2])
		self.passwd.setFont(FontColor_array.Font_list[2])
		

		# layout
		toplayout = QHBoxLayout()
		aclayout = QHBoxLayout()
		pwlayout = QHBoxLayout()
		mainlayout = QVBoxLayout()
		toplayout.addWidget(title)
		toplayout.addStretch(1)
		toplayout.addWidget(self.error_login)
		aclayout.addStretch(1)
		aclayout.addWidget(ac_text)
		aclayout.addWidget(self.account)
		aclayout.addStretch(1)
		pwlayout.addStretch(1)
		pwlayout.addWidget(pw_text)
		pwlayout.addWidget(self.passwd)
		pwlayout.addStretch(1)
		mainlayout.addLayout(toplayout)
		mainlayout.addLayout(aclayout)
		mainlayout.addLayout(pwlayout)
		mainlayout.addWidget(log)
		self.setLayout(mainlayout)
		self.setStyleSheet(FontColor_array.Color_list[2])

		# show
		self.show()

	# quit the Application
	def closeEvent(self,event):
		self.close_signal.emit()
		self.close()

	# button Actionlistener
	def determine(self):
		try:
			if re.search(r"^[0-9a-zA-Z]{6,}$",self.account.text()) != None and re.search("^[\x30-\x39]$",self.passwd.text()) != None:
				self.ui = frame.Application()
				self.hide()
				self.close_signal.connect(self.close)
				self.ui.show()
			else:

				self.account.setText("")
				self.passwd.setText("")
				self.error_login.setText("帳號或密碼錯誤...")

		except:
			return