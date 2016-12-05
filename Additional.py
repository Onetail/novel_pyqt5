
import time
import FontColor_array
import requests
from bs4 import BeautifulSoup

# save all list name & get search url 

def addbtn():
	url_Search()
def lookbtn():
	import frame
	frame.Application().self.text.setText("sda")
def deletebtn():
	print("3")
def listbtn():
	print("4")

button_id_list = ["add","look","delete","list"]
button_def_list = [addbtn,lookbtn,deletebtn,listbtn]
search_url = ["http://ck101.com/forum-237-1.html","http://ck101.com/forum-3419-1.html"]


# get now time
def Timeget():
	global stime
	stime = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
	return stime

# init 初始化
def __init__():
	for i in range(3,10):
		search_url.append("http://ck101.com/forum.php?mod=forumdisplay&fid=237&filter=typeid&typeid=13"+str(i))

# get url 
def url_Search():
	
	#search url to get detail
	for j in range(0,len(search_url)):
		res = requests.get(search_url[j])
		res.encoding = 'utf=8'
		soup = BeautifulSoup(res.text,"html.parser")
    	# for i in soup.select('.common.subject')[i]:
