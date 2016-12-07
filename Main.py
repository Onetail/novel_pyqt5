import Login_frame
import sys

# call ui frame
app = Login_frame.QApplication(sys.argv)
ui_run = Login_frame.Login()
app.exec_()

