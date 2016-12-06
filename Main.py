import Login_frame
import sys

# call ui frame
app = Login_frame.QApplication(sys.argv)
ui_run = Login_frame.Login()
sys.exit(app.exec_())

# button
Login_frame.log = QPushButton("登入",self)
Login_frame.log.clicked.connect(self.determine)
def determine(self):
	app.quit()
	app2 = frame.QApplication(sys.argv)
	ui_run = frame.Application()
	sys.exit(app2.exec_())