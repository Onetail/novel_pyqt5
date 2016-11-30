from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

class QApplication(QWidget):
	def __init__(self):
		super().__init__()
		self.appui()
	def appui(self):
		self.resize(800,600)
		self.show()

app = QApplication(sys.argv)
ui_run = init_ui()
sys.exit(app.exec_())