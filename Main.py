import Login_frame
import sys
import frame

# call ui frame
app = Login_frame.QApplication(sys.argv)
ui_run = Login_frame.Login()
# app = frame.QApplication(sys.argv)
# ui_run = frame.Application()
app.exec_()

