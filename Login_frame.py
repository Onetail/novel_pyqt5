from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QTextEdit,QVBoxLayout,QHBoxLayout
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

		log.setFont(FontColor_array.Font_list[2])

		# label
		title = QLabel("--登入畫面--",self)
		ac_text = QLabel("帳號: ",self)
		pw_text = QLabel("密碼: ",self)

		title.setFont(FontColor_array.Font_list[2])
		ac_text.setFont(FontColor_array.Font_list[2])
		pw_text.setFont(FontColor_array.Font_list[2])

		title.setStyleSheet(FontColor_array.Color_list[1])

		# textEdit
		self.account = QTextEdit("",self)
		self.passwd = QTextEdit("",self)

		self.account.setFont(FontColor_array.Font_list[2])
		self.passwd.setFont(FontColor_array.Font_list[2])
		
		# layout
		toplayout = QVBoxLayout()
		aclayout = QHBoxLayout()
		pwlayout = QHBoxLayout()
		mainlayout = QVBoxLayout()

		toplayout.addWidget(title)
		aclayout.addWidget(ac_text,2)
		aclayout.addWidget(self.account)
		pwlayout.addWidget(pw_text,2)
		pwlayout.addWidget(self.passwd)

		mainlayout.addLayout(toplayout,4)
		mainlayout.addLayout(aclayout,1)
		mainlayout.addLayout(pwlayout,1)
		mainlayout.addWidget(log,2)
		self.setLayout(mainlayout)

		# show
		self.show()

	# quit the Application
	def closeEvent(self,event):
		self.close_signal.emit()
		self.close()

	# button Actionlistener
	def determine(self):
		if re.search(self.account.toPlainText(),"[0-9a-zA-Z]{6,7}") != None and re.search(self.passwd.toPlainText,"^[\x30-\x39]$"):
			self.ui = frame.Application()
			self.hide()
			self.close_signal.connect(self.close)
			self.ui.show()
		else:
			return