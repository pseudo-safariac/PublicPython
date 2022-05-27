import tkinter as tk
import tkinter.ttk as ttk


class Widgets(ttk.Frame):
	def __init__(self, container):
		super(Widgets, self).__init__(container)



class App(tk.Tk):
	def __init__(self):
		super(App, self).__init__()
		self.title('Tkinter Widgets and Styling')
		self.geometry()