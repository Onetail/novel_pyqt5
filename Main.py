from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QTextEdit
import sys

class Application(QWidget):
	# global var
	global button_id_list
	button_id_list = ["add","look","delete","list"]

	# __init__
	def __init__(self):
		super().__init__()
		self.appui()
	# init ui designer
	def appui(self):
		self.resize(800,600)

		#layout
		uplayout = QHBoxLayout()		# |||
		rightlayout = QHBoxLayout()
		toplayout = QHBoxLayout()		# |||
		centerlayout = QVBoxLayout()	# ---
		bottomlayout = QHBoxLayout()	# |||
		leftlayout = QVBoxLayout()		# ---
		mainlayout = QHBoxLayout()		# sum af layout

		#button
		for i in range(0,4):
			button_id_list[i] = QPushButton(button_id_list[i],self)
			leftlayout.addWidget(button_id_list[i])
		
		#text
		label = QLabel("",self)
		self.text = QTextEdit("",self)
		self.text.setReadOnly(True)

		#layout add

		toplayout.addWidget(label)
		rightlayout.addWidget(self.text)
		centerlayout.addLayout(toplayout)
		centerlayout.addLayout(rightlayout)
		uplayout.addLayout(leftlayout)
		uplayout.addLayout(centerlayout)
		mainlayout.addLayout(uplayout)
		mainlayout.addLayout(bottomlayout)
		
		self.setLayout(mainlayout)
		#show
		self.show()

# call ui frame
app = QApplication(sys.argv)
ui_run = Application()
sys.exit(app.exec_())