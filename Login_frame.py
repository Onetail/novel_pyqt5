from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QTextEdit,QVBoxLayout
import sys
import FontColor_array
import frame

# login frame
class Login(QWidget):
	def __init__(self):
		super().__init__()
		self.loginui()

	def loginui(self):
		self.resize(600,300)
		self.setWindowTitle("Login")
		# button
		log = QPushButton("登入",self)
		log.clicked.connect(self.determine)

		# label
		title = QLabel("--登入畫面--",self)
		ac_text = QLabel("帳號: ",self)
		pw_text = QLabel("密碼: ",self)

		title.setFont(FontColor_array.Font_list[0])

		# textEdit
		account = QTextEdit("",self)
		passwd = QTextEdit("",self)

		# layout
		layout = QVBoxLayout()
		layout.addWidget(title)
		layout.addWidget(ac_text)
		layout.addWidget(pw_text)
		layout.addWidget(account)
		layout.addWidget(passwd)
		layout.addWidget(log)
		self.setLayout(layout)
		# show
		self.show()

	def determine(self):
		self.quit()
		app = frame.QApplication(sys.argv)
		ui_run = frame.Application()
		sys.exit(app.exec_())