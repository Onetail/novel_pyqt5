import frame
import sys

# call ui frame
app = frame.QApplication(sys.argv)
ui_run = frame.Application()
sys.exit(app.exec_())