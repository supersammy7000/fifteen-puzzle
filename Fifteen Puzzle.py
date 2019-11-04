import tkinter as tk
import random as rand

class Main:
	def __init__(self):
		self.master = tk.Tk()
		self.frame = tk.Frame()

		self.title = tk.Label(self.frame,text="Welcome to the Fifteen Puzzle!")
		self.title.pack()

		self.frame.pack()

	def getMaster(self):
		return self.master

	def mainloop(self):
		self.master.mainloop()

class button:
	def __init__(self,frame,number,column,row):
		self.number = tk.StringVar()
		self.label = tk.StringVar()
		self.number.set(number)
		self.label.set(number+1)
		self.index = number
		self.Button = tk.Button(frame, textvariable=self.label, command=self.action)
		self.Button.grid(column=column, row=row)
	def setNumber(self,number):
		self.number.set(number)
	def getLabel(self):
		return self.label.get()
	def setLabel(self,label):
		self.label.set(label)
	def getIndex(self):
		return self.index
	def getNumber(self):
		return int(self.number.get())
	def action(self):
		print(self.getIndex())
		action(self.getIndex())

class movement:
	def __init__(self, buttons):
		self.buttons = buttons

	def checkVerticle(self):
		beginning = self.position % 4
		for i in range(beginning,beginning+15,4):
			if self.buttons[i].getNumber() == 15:
				return (i - self.position)/4
		return None

	def checkHorizontal(self):
		beginning = (self.position // 4)*4
		for i in range(beginning,beginning+4):
			if self.buttons[i].getNumber() == 15:
				return i - self.position
		return None

	def check(self,position):
		self.position = position
		#print('wack',self.checkHorizontal())
		#print('dis shit',self.checkVerticle())
		return self.checkHorizontal(),self.checkVerticle()


def action(number):
	hori,vert = move.check(number)
	print(hori,vert)
	if hori == 1:

		##Number
		old = Buttons[number].getNumber()
		new = Buttons[number+1].getNumber()

		Buttons[number].setNumber(new)
		Buttons[number+1].setNumber(old)
		
		##Label
		old = Buttons[number].getLabel()
		new = Buttons[number+1].getLabel()

		Buttons[number].setLabel(new)
		Buttons[number+1].setLabel(old)
	elif hori == -1:
		old = Buttons[number].getNumber()
		new = Buttons[number-1].getNumber()
		
		Buttons[number].setNumber(new)
		Buttons[number-1].setNumber(old)

		##Label
		old = Buttons[number].getLabel()
		new = Buttons[number-1].getLabel()
		
		Buttons[number].setLabel(new)
		Buttons[number-1].setLabel(old)
	elif vert == 1:
		old = Buttons[number].getNumber()
		new = Buttons[number+4].getNumber()

		Buttons[number].setNumber(new)
		Buttons[number+4].setNumber(old)

		##Label
		old = Buttons[number].getLabel()
		new = Buttons[number+4].getLabel()

		Buttons[number].setLabel(new)
		Buttons[number+4].setLabel(old)
	elif vert == -1:
		old = Buttons[number].getNumber()
		new = Buttons[number-4].getNumber()
		
		Buttons[number].setNumber(new)
		Buttons[number-4].setNumber(old)

		##Label
		old = Buttons[number].getLabel()
		new = Buttons[number-4].getLabel()
		
		Buttons[number].setLabel(new)
		Buttons[number-4].setLabel(old)

main = Main()

frame = tk.Frame(main.getMaster())
frame.pack()
Buttons = list()
for i in range(16):
	test = button(frame,i,i%4,i//4)
	Buttons.append(test)
Buttons[-1].setLabel("")
move = movement(Buttons)


main.mainloop()