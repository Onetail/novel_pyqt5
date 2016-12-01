import time
import FontColor_array
import requests
from bs4 import BeautifulSoup

button_id_list = ["add","look","delete","list"]

def Timeget():
	global stime
	stime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	return stime