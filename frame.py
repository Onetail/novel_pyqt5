from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QTextEdit,QScrollBar
import FontColor_array
import Additional
# Main sccreen

class Application(QWidget):
	# global var

	# __init__
	def __init__(self):
		super().__init__()
		self.appui()
	# init ui designer
	def appui(self):
		self.resize(1040,800)
		#layout
		uplayout = QHBoxLayout()		# |||
		rightlayout = QHBoxLayout()
		toplayout = QHBoxLayout()		# |||
		centerlayout = QVBoxLayout()	# ---
		bottomlayout = QHBoxLayout()	# |||
		leftlayout = QVBoxLayout()		# ---
		mainlayout = QVBoxLayout()		# sum af layout

		#button
		for i in range(0,4):
			Additional.button_id_list[i] = QPushButton(Additional.button_id_list[i],self)
			leftlayout.addWidget(Additional.button_id_list[i])
			Additional.button_id_list[i].setFont(FontColor_array.Font_list[0])
			Additional.button_id_list[i].setStyleSheet(FontColor_array.Color_list[0])
			Additional.button_id_list[i].clicked.connect(Additional.button_def_list[i])
		
		#text
		nowtime = QLabel(Additional.Timeget(),self)
		global text
		self.text = QTextEdit("",self)
		self.text.setReadOnly(True)

		nowtime.setFont(FontColor_array.Font_list[1])

		#scroll
		scroll = QScrollBar()
		
		#layout add
		bottomlayout.addWidget(scroll)
		toplayout.addWidget(nowtime)
		rightlayout.addWidget(self.text)
		centerlayout.addLayout(toplayout)
		centerlayout.addLayout(rightlayout)
		uplayout.addLayout(leftlayout)
		uplayout.addLayout(centerlayout)
		mainlayout.addLayout(uplayout,5)
		mainlayout.addLayout(bottomlayout)
		
		self.setLayout(mainlayout)
		
		#show
		self.show()
