import os
import keyboard
import threading

line=0
letter="H"
left=10
right=9
os.system("cls")

def animation():
	global line
	global left,right
	while line<20:
		os.system("timeout 01>>null")
		os.system("cls")
		print("-"*22)
		for i in range(20):
			print("|",end="")
			if(line==i):
				print(" "*left,end="")
				print(letter,end="")
				print(" "*right,end="")
			else:
				print(" "*20,end="")
			print("|",end="")
			print()
		line+=1
		if(line>19):
			line=0
		print("-"*22)

def key():
	global left,right
	while True:
		if keyboard.read_key() == "a":
			left-=1
			right+=1
		elif keyboard.read_key() == "d":
			left+=1
			right-=1


if __name__ =="__main__":
	animationTred = threading.Thread(target=animation)
	keyboardTred = threading.Thread(target=key)

	animationTred.start()
	keyboardTred.start()

	animationTred.join()
	keyboardTred.join()