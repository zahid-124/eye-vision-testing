#!/usr/bin python3

#      Key Assign     #
########################
#Power - p
#Next -u
#Previous -y
#Snellen-s
#E Chart-e
#C Chart-c
#Number -n
#Bangla -b
#LogMAR-l
#ETDRS-t
#Pediatric-p
#Red-Green -r
#Ishihara-i
#Dot-d
#Contrast -m
#amsler -a
#astig-q
#cross -x
#fourdot -f
#letter -k
#break -g
########################

import cv2
from subprocess import call
from keyboard import read_key
from shlex import split



with open("/home/pi/Vision/conf.txt")as f:  #conf.txt file holds the chart destination path
	chart_dest=f.read()



prev_key=['s']


##################################Image List##############################################
com1_img=["60.jpg","36.jpg","24.jpg","18.jpg","12.jpg","9.jpg","6.jpg"] #List for E,C,7,Bangla,Pediatric,Dot,Letter,Phoria
com2_img=["1.jpg","2.jpg","3.jpg"]#list for snellen,astig,cross
com3_img=["1.jpg"]#list for ETDRS,Contrast,Amsler
logmar_img=["1.jpg","2.jpg"] 
fourdot_img=["1.jpg","2.jpg","3.jpg","4.jpg"]
ishihara_img=["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg"]
	

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



	
def chart(folder_name,key,img_list):
    
	global prev_key
	x=cycle(img_list)
	key_press=prev_key[0]
        
	while 1:
        
		if ((key_press=="u") or (key_press==key)):
			y=next(x)
			image=chart_dest.rstrip()+"/"+folder_name+"/"+y
			img=cv2.imread(image,1)
			#cv2.namedWindow("frame2",cv2.WND_PROP_FULLSCREEN)
			#cv2.setWindowProperty("frame2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("frame2",img)
			cv2.waitKey(0)
            
		elif key_press=="y":
			z=x.previous()	
			image=chart_dest.rstrip()+"/"+folder_name+"/"+z
			img=cv2.imread(image,1)
			#cv2.namedWindow("frame2",cv2.WND_PROP_FULLSCREEN)
			#cv2.setWindowProperty("frame2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("frame2",img)
			cv2.waitKey(0)
			
		else:
			prev_key.pop(0)
			prev_key.append(key_press)
			break
		key_press=read_key()
		

def main():
	
	while 1:
			
		key_press=prev_key[0]
			
		if key_press=='s':#Snellen Chart
			chart("snellen",'s',com2_img)
					
		elif key_press=='e':#E Chart
			chart("echart",'e',com1_img)	
			
		elif key_press=='c':#C Chart    
			chart("cchart",'c',com1_img)    
            
		elif key_press=='n':#Number Chart
			chart("number",'n',com1_img)   
            
		elif key_press=='b':#Bangla Chart
			chart("bangla",'b',com1_img)
			
		elif key_press=='k':#letter Chart
			chart("letter",'k',com1_img)
		
		elif key_press=="a":#Amsler Chart
			chart("amsler","a",com3_img)
						
		elif key_press=="l":#LogMAR Chart
			chart("logmar","l",logmar_img)
						
		elif key_press=="t":#ETDRS Chart
			chart("etdrs","t",com3_img)
						
		elif key_press=="p":#Pediatric Chart
			chart("pediatric","p",com1_img)	
				
		elif key_press=="r":#Red_Green Chart
			chart("red-green","r")	
				
		elif key_press=="i":#Ishihara Chart
			chart("ishihara","i",ishihara_img)	
				
		elif key_press=="d":#Dot Chart
			chart("dotchart","d",com1_img)	
				
		elif key_press=="m":#contrast Chart
			chart("contrast","m",com3_img)
			
		elif key_press=="x":#Cross Chart
			chart("cross","x",com2_img)  	  
         
		elif key_press=="f":#fourdot Chart
			chart("fourdot","f",fourdot_img)  
		
		elif key_press=='q':#astig Chart
			chart("astig",'q',com2_img)	
        
		elif key_press=="8":#8 feet
			cv2.destroyAllWindows()
			with open("conf.txt","w") as f:
				f.write("/home/pi/Vision/Images/8feet/")	
			break		
                
		elif key_press=="10":#10 feet
			cv2.destroyAllWindows()
			with open("conf.txt","w") as f:
				f.write("/home/pi/Vision/Images/10feet/")	
			break	
            	
                
		elif key_press=="w":#Power Off
				#cmd=split("sudo shutdown -h now")  #This is for shutdown
				#cmd=split("sudo reboot")			  #Thisis for reboot
				#call(cmd)	
			break
	
		elif key_press=="g":
			break;		


if __name__ == "__main__":
    main()


























	
