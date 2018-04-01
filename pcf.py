import numpy as np
import matplotlib
from matplotlib import pyplot as plt 
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

matplotlib.use("TkAgg")

class poly:

	def load(self):
		self.a.clear()
		abc=filedialog.askopenfilename(initialdir=".",title ="Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
		if abc!=() and abc!="":
			self.Data=np.genfromtxt( abc,dtype='float')
			self.n=len(self.Data)
			self.a.clear()
			self.a.set_ylim(min([i[1] for i in self.Data]),max([i[1] for i in self.Data]))
			self.a.set_xlim(min([i[0] for i in self.Data]),max([i[0] for i in self.Data]))
			dot=self.a.scatter([i[0] for i in self.Data],[i[1] for i in self.Data],c='green',label="Data Points")
			self.a.legend()
			self.canvas.show()
			
		

	
	def generatecurve(self):
		self.k=int(self.entry.get())
		xc=np.array([i[0] for i in self.Data])
		yc=np.array([i[1] for i in self.Data])		
		z=np.polyfit(xc,yc,self.k)
		xn = np.linspace(np.min(xc), np.max(xc))
		yn = np.polyval(z, xn)
		self.a.plot(xn,yn,label="Curve(deg= {})".format(self.k))
		self.a.legend()
		self.canvas.show()
		self.canvas.get_tk_widget().place(x=10,y=10)
		
		


	def __init__(self,tk):
		
		Button(tk,text="Load Data",command=lambda:self.load()).place(x=550,y=60)
		Label(tk,text="Enter Degree of curve:",bg="light blue").place(x=550,y=150)
		self.entry=Entry(tk,width=5)
		self.entry.place(x=700,y=150)
		Button(tk,text="Generate",command=lambda:self.generatecurve()).place(x=550,y=250)

		self.f=plt.Figure(figsize=(5,5))
		self.a=self.f.add_subplot(111) 
		self.a.set_title("Polynomial Curve Fitting")
		self.a.set_xlabel("X-axis")
		self.a.set_ylabel("Y-axis")
		self.canvas=FigureCanvasTkAgg(self.f,master=tk)
		toolbar = NavigationToolbar2TkAgg(self.canvas,tk)
		toolbar.update()
		self.canvas._tkcanvas.place(x=10,y=10)
		



tk=Tk()
tk.title("Polynomial Curve Fitting")
tk.geometry('800x600+80+60')
tk.configure(background='light blue')
obj=poly(tk)


tk.mainloop()











