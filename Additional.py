
import time
import FontColor_array
import requests
from bs4 import BeautifulSoup

# save all list name & get search url 

def addbtn():
	print("1")
def lookbtn():
	print("2")
def deletebtn():
	print("3")
def listbtn():
	print("4")

button_id_list = ["add","look","delete","list"]
button_def_list = [addbtn,lookbtn,deletebtn,listbtn]

# get now time
def Timeget():
	global stime
	stime = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
	return stime

# get url 
def url_Search():
	
    res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/')
	res.encoding = 'utf=8'
	soup = BeautifulSoup(res.text,"html.parser")
    


