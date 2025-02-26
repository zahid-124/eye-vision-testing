#!/usr/bin python3

#       Key Assign     #
########################
#Power - p
#Next -n
#Previous -u
#Snellen-s
#E Chart-e
#C Chart-c
#Number -m
#Bangla -b
#Arabic -a
#LogMAR-l
#ETDRS-t
#Pediatric-i
#Red-Green -r
#Ishihara-h
#Dot-o
#Contrast -c
########################
import subprocess
import cv2
import keyboard
import time
import os
import shlex
prev_key=['s']
#next_key=[]
global keypress
global i
i=0
##cv2.destroyAllWindows()
	

class cycle:
	def __init__(self,c):
		self._c=c
		self._index=-1
	
	def __next__(self):
		self._index+=1
		if self._index>=len(self._c):
			self._index=0
			
		return self._c[self._index]
	def previous(self):
		self._index-=1
		if self._index<0:
			self._index=len(self._c)-1
		return self._c[self._index]	



	
def chart(d_path,list_name,key):
	global prev_key
	global key_press
	x=cycle(list_name)
	#print(key_press)
	key_press=prev_key[0]
	while True:
		
		if ((key_press=="n") or (key_press==key)):
			time.sleep(0.2)
			y=next(x)
			image=d_path.rstrip()+"/"+y
			img=cv2.imread(image,1)
			cv2.namedWindow("frame2",cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty("frame2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("frame2",img)
			cv2.waitKey(0)
			#key_press=keyboard.read_key()
		elif key_press=="u":
			time.sleep(0.2)
			z=x.previous()	
			image=d_path.rstrip()+"/"+z
			img=cv2.imread(image,1)
			cv2.namedWindow("frame2",cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty("frame2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("frame2",img)
			cv2.waitKey(0)
			#key_press=keyboard.read_key()
			
		else:
			prev_key.pop(0)
			prev_key.append(key_press)
			#cv2.destroyAllWindows()
			break
		key_press=keyboard.read_key()
		#time.sleep(0.2)
	
	
with open("conf.txt")as f:
	path=f.read()


contrast_path= path.rstrip()+"contrast"
dot_path= path.rstrip()+"dot"
ishihara_path= path.rstrip()+"ishihara"
red_path= path.rstrip()+"red-green"
pediatric_path= path.rstrip()+"pediatric"
etdrs_path= path.rstrip()+"etdrs"
logmar_path= path.rstrip()+"logmar"
arabic_path= path.rstrip()+"arabic"
bangla_path= path.rstrip()+"bangla"
number_path= path.rstrip()+"number"	
cchart_path= path.rstrip()+"cchart"
snellen_path= path.rstrip()+"snellen"      
echart_path= path.rstrip()+"echart"


list_contrast=os.listdir(contrast_path)
list_dot=os.listdir(dot_path)
list_ishihara=os.listdir(ishihara_path)
list_red=os.listdir(red_path)
list_pediatic=os.listdir(pediatric_path)
list_etdrs=os.listdir(etdrs_path)
list_logmar=os.listdir(logmar_path)
list_arabic=os.listdir(arabic_path)
list_bangla=os.listdir(bangla_path)
list_number=os.listdir(number_path)
list_cchart=os.listdir(cchart_path)
list_snellen=os.listdir(snellen_path)
list_echart=os.listdir(echart_path)





def main():
	
	while True:
			
		key_press=prev_key[0]
		print(key_press)
			
		if key_press=='s':#Snellen Chart
			chart(snellen_path,list_snellen,'s')
					
		elif key_press=='e':#E Chart
			chart(echart_path,list_echart,'e')
				
				
		elif key_press=="c":#C Chart
			chart(cchart_path,list_cchart,"c")
				
				
		elif key_press=="b":#Bangla Chart
			chart(bangla_path,list_bangla,"b")
				
				
		elif key_press=="m":#Number Chart
			chart(number_path,list_number,"m")
				
				
		elif key_press=="a":#Arabic Chart
			chart(arabic_path,list_arabic,"a")
				
				
		elif key_press=="l":#LogMAR Chart
			chart(logmar_path,list_logmar,"l")
				
				
		elif key_press=="t":#ETDRS Chart
			chart(etdrs_path,list_etdrs,"t")
				
				
		elif key_press=="i":#Pediatric Chart
			chart(pediatric_path,list_pediatic,"i")
				
				
		elif key_press=="r":#Red_Green Chart
			chart(red_path,list_red,"r")
				
				
		elif key_press=="h":#Ishihara Chart
			chart(ishihara_path,list_ishihara,"h")
				
				
		elif key_press=="o":#Dot Chart
			chart(dot_path,list_dot,"o")
				
				
		elif key_press=="x":#Contrast Chart
			chart(contrast_path,list_contrast,"x")
						
			
		elif key_press=="8":#8 feet
			cv2.destroyAllWindows()
			with open("conf.txt","w") as f:
				f.write("/home/raspberrypi/Images/8ft/")	
			break		
		elif key_press=="9":#9 feet
			cv2.destroyAllWindows()
			with open("conf.txt","w") as f:
				f.write("/home/raspberrypi/Images/9ft/")	
			break		
		elif key_press=="p":#Power Off
				#cmd=shlex.split("sudo shutdown -h now")  #This is for shutdown
				#cmd=shlex.split("sudo reboot")			  #Thisis for reboot
				#subprocess.call(cmd)	
			break
	
				


if __name__ == "__main__":
    main()


























	
