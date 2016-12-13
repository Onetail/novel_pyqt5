from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QTextEdit,QScrollBar
from bs4 import BeautifulSoup
import FontColor_array
import time
import requests

# Main sccreen

class Application(QWidget):

	global button_id_list,search_url
	button_id_list = ["add","look","delete","list"] # button id
	search_url = ["http://ck101.com/forum-237-1.html","http://ck101.com/forum-3419-1.html"] # 爬蟲的url
	
	# __init__
	def __init__(self):
		super(Application,self).__init__()
		for i in range(3,10):
			search_url.append("http://ck101.com/forum.php?mod=forumdisplay&fid=237&filter=typeid&typeid=13"+str(i))
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
			button_id_list[i] = QPushButton(button_id_list[i],self)
			leftlayout.addWidget(button_id_list[i])
			button_id_list[i].setFont(FontColor_array.Font_list[0])
			button_id_list[i].setStyleSheet(FontColor_array.Color_list[0])

		button_id_list[0].clicked.connect(self.addbtn)
		button_id_list[1].clicked.connect(self.lookbtn)
		button_id_list[2].clicked.connect(self.deletebtn)
		button_id_list[3].clicked.connect(self.listbtn)
		
		#text
		nowtime = QLabel(self.Timeget(),self)

		self.text = QTextEdit("",self)
		self.text.setReadOnly(True)
		self.text.setText("測試版")
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
	# save all list name & get search url 
	def addbtn(self):
		self.url_Search()
	def lookbtn(self):
		self.text.setText("sda")
	def deletebtn(self):
		print("3")
	def listbtn(self):
		print("4")

	#search url to get detail
	def url_Search(self):
		# 存爬蟲資料
		global requests_txt
		requests_txt = ""
		try:
			for j in range(0,len(search_url)):
				res = requests.get(search_url[j])
				res.encoding = 'utf=8'
				soup = BeautifulSoup(res.text,"html.parser")
				try:
					for i in range(0,35):
						requests_txt += soup.select('.titleBox')[i].setText
				except:
					requests_txt += "\n1"
		except:
			requests_txt+="無法連網，或URL錯誤"
		finally:
			self.text.setText(requests_txt)

	# get now time
	def Timeget(self):
		stime = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
		return stime 