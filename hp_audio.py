import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class AlternateBar(ttk.Frame):
	def __init__(self, container):
		super(AlternateBar, self).__init__(container)
		self.config(width=950, height=30)


		close_label = ttk.Button(self, text='Close', )
		close_label.place(x=880, y=0)

		self.place(x=0, y= 0)


class MenuBar(ttk.Frame):
	def __init__(self, container):
		super(MenuBar, self).__init__(container)
		self.config(width=950, height=70)
		





		self.place(x=0, y=30)

class App(tk.Tk):
	def __init__(self):
		super(App, self).__init__()
		self.title('No deleting nothing.... Just write code, upload and let them hopefully want to have a piece of '
		           'the code but no new step-by-step method in writing')
		self.attributes('-topmost', 1)
		self.attributes('-alpha', 0.99)
		# self.overrideredirect(True)
		self.config(bg='#030303')

		width = 950
		height = 600
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		screen_center_x = int(screen_width/2 - width/2)
		screen_center_y = int(screen_height/2 - height/2)
		self.geometry(f'{width}x{height}+{screen_center_x}+{screen_center_y}')

		AlternateBar(self)
		MenuBar(self)


from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
app = App()
app.mainloop()