from tkinter import *

# Window positioning variables
w = 320
h = 170
x = 350
y = 10

def display():

	# Main window
	root = Tk()

	root.title("Compare With Friends!")

	textWidget = Text(root)

	readFile = open('out.txt', 'r')
	fileLog = readFile.read()
	readFile.close()

	textWidget.insert(0.0,fileLog) 

	textWidget.pack(expand=1, fill=BOTH)


	root.geometry('%dx%d+%d+%d' % (w, h, x, y))

	root.mainloop()

if __name__ == "__main__":
	display()
