from ctypes import windll
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import threading
from time import sleep



class SplashScreen(tk.Tk):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 0.0)
        self.overrideredirect(True)
        self.after(10, self.set_appwindow)
        self.config(bg='#231651')

        # Screen geometry
        width = 630
        height = 330
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        center_x = int(s_width / 2 - width / 2)
        center_y = int(s_height / 2 - height / 2)
        self.geometry(f'{width}x{height}+{center_x}+{center_y}')

        visibility = threading.Thread(target=self.alpha_settings)
        letter_flashes = threading.Thread(target=self.random_flashes)
        visibility.start()
        letter_flashes.start()

        # Styling
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('red.Horizontal.TProgressbar', foreground='red',
                    background='#0000c6', troughcolor= '#2626ff',
                    darkcolor= '#aaaaff', lightcolor='#aaaaff',
                    bordercolor='#231651',
                    )
        s.map('TButton',
                  background=[('focus', '#231651')],
                  foreground=[('focus', '#231651')]
                  )

        #Adding Labels
        company_label = ttk.Label(self, text='WALTER\'S', background= '#231651',
                          foreground='#5b5bff', borderwidth=15,
                          font=('Helvetica', 49, 'bold'))
        company_label.place(x=50, y=80)

        lab_label = ttk.Label(self, text='Lab',
                                  foreground='#6666ff', background='#231651',
                                  font=('Proxima Nova', 27, 'bold', 'italic')
                                  )
        lab_label.place(x=420, y=180)

        loading_label = ttk.Label(self, text='Loading...',
                                  foreground='#476C9B', background='#231651',
                                  font=('Proxima Nova', 10, 'bold', 'italic'))

        progress = ttk.Progressbar(self, style='red.Horizontal.TProgressbar',
                                   orient= tk.HORIZONTAL,
                                   length= 630,
                                   mode='determinate')
        progress['value'] = 0

        def launch():
            loading_label.place(x=520, y=280)
            progress.place(x=0, y=310)
            while progress['value'] < 100:
                self.update_idletasks()
                # print(progress['value'])
                progress['value'] += 1
                sleep(0.03)
            else:
                # print('ERROR IN PROGRESSBAR!!!')
                launch_login()

        # Adding Buttons
        start_button = tk.Button(self, text='launch',
                                 background='#231651',
                                 foreground='#dcdcdc',
                                 font=('Helvetica', 9, 'bold'),
                                 command=launch, borderwidth=0)
        start_button.place(x=5, y=5)

        close_button = tk.Button(self, text='close',
                                 background='#231651',
                                 foreground='#dcdcdc',
                                 font=('Helvetica', 9, 'bold'),
                                 command=self.close, borderwidth=0)
        close_button.place(x=570, y=5)

        ######################################################
    def random_flashes(self):
        from random import randrange
        from winsound import PlaySound, SND_FILENAME  # Reduces loading time drastically!

        intro_sound_path = r'C:/Windows/Media/Alarm05.wav'
        PlaySound(intro_sound_path, SND_FILENAME)

        """x_value = 90
        y_value = 0
        count = 0
        label_number = 0
        while count != 8:
            sleep(0.1)
            label_number = tk.Label(self, text='lab',
                                    background= '#231651',
                                    foreground='#476C9B',
                                    borderwidth=15,
                          font=('Helvetica', 9, 'bold'))
            label_number.place(x=x_value, y=y_value)
            x_value = randrange(100, 500)
            y_value = randrange(0, 5)
            count += 1
            label_number = y_value
            # print(x_value)
            continue"""
        ######################################################

        self.update_idletasks()

    def alpha_settings(self):
        timer = 50
        contrast = 0.5
        while timer != 0:
            self.attributes('-alpha', contrast)
            contrast = contrast + 0.01
            timer-=1
            sleep(0.03)

    def close(self):
        self.destroy()

    def set_appwindow(self):
        """This is used for ensuring the window in Windows is not lost all the other
        features that are used in a window are set"""
        GWL_ESTYLE = -20
        WS_EX_APPWINDOW = 0X00040000
        WS_EX_TOOLWINDOW = 0X00000080

        hwnd = windll.user32.GetParent(self.winfo_id())
        style =windll.user32.GetWindowLongPtrW(hwnd, GWL_ESTYLE)
        style = style | WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongPtrW(hwnd, GWL_ESTYLE, style)
        # re-assert the new window style
        self.withdraw()
        self.after(10, self.deiconify)


class Login(tk.Tk):
    def __init__(self):
        super(Login, self).__init__()
        self.wm_title('Splash Screen')
        self.attributes('-topmost', 1)
        self.attributes('-alpha', 0.99)
        self.overrideredirect(True)
        self.after(10, SplashScreen.set_appwindow(self))
        self.config(bg='#231651')

        # Screen geometry
        width = 630
        height = 330
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        center_x = int(s_width / 2 - width / 2)
        center_y = int(s_height / 2 - height / 2)
        self.geometry(f'{width}x{height}+{center_x}+{center_y}')

        # Styling
        s = ttk.Style()
        s.theme_use('clam')

        # Entry Style
        """Has an internal error"""
        """s.element_create('just_plain.field', 'from', 'clam')
        s.layout("Entry.TEntry",
                 [('Entry.just_plain.field', {'children' : [(
                   'Entry.background', {'children' : [(
                       'Entry.padding', {'children' : [(
                           'Entry.textarea', {'sticky' : 'nsew'})],
                           'sticky' : 'nsew'})],'sticky' : 'nsew'})],
                     'border':'2', 'sticky' : 'nsew'})])"""
        s.configure('Entry.TEntry',
                    background= 'green',
                    foreground= 'black',
                    borderwidth= 0,
                    fieldbackground= '#b3b3ff')

        # Forgot Password Button Style
        forgot_pass_font = Font(family='Times', size=9,
                                underline= True, weight='bold')
        s.configure('forgot_pass.TButton', font= forgot_pass_font,
                    background= '#231651', foreground= '#778899', borderwidth=0)

        s.map('forgot_pass.TButton', background= [('active', '#231651')],
              foreground=[('active', '#dcdcdc')])

        # Close button Style
        s.configure('close.TButton', font=('Helvetica', 9, 'bold'),
                    background='#231651', foreground='#778899',
                    borderwidth=0,
                    )

        s.map('close.TButton', background=[('active', '#301a78')],
              foreground=[('active', '#dcdcdc')]
              )

        # Login button Style
        s.configure('login.TButton', font=('Helvetica', 12, 'bold'),
                    background='#231651', foreground='#778899',
                    borderwidth=0,
                    )

        s.map('login.TButton', background=[('active', '#301a78')],
              foreground=[('active', '#dcdcdc')]
              )
        self.widgets_create()

    def widgets_create(self):
        # Adding Title
        kibendera_label = ttk.Label(self, text='CLEAN WATER', background='#231651',
                                   foreground='#476C9B', borderwidth=15,
                                   font=('Helvetica', 29, 'bold')
                                   )
        kibendera_label.place(x=50, y=0)

        section_label = ttk.Label(self, text='Section',
                              foreground='#aba8d7', background='#231651',
                              font=('Proxima Nova', 14, 'bold', 'italic')
                              )
        section_label.place(x=380, y=70)

        # Adding Labels
        username_text = ttk.Label(self, text='Username :', background='#231651',
                               foreground='white', font=('Arial', 14, 'bold'))
        username_text.place(x=100, y=120)

        password_text = ttk.Label(self, text='Password :', background='#231651',
                               foreground='white', font=('Arial', 14, 'bold')
                               )
        password_text.place(x=100, y=190)

        notification_message = ttk.Label(self,
                                         background='#231651',
                                         font=('Helvetica', 14)
                                         )
        notification_message.place(x=200, y=85)

        # Adding Entries
        username_entry_var = tk.StringVar()
        password_entry_var = tk.StringVar()

        username_entry = ttk.Entry(self, font=('Arial', 14, 'bold'),
                                cursor= 'xterm',
                                   textvariable=username_entry_var,
                                takefocus=True)
        username_entry.focus()
        username_entry.place(x=260, y=120)

        password_entry = ttk.Entry(self,font=('Arial', 14, 'bold'),
                                   cursor='xterm', show='*',
                                   textvariable= password_entry_var,
                                )
        password_entry.place(x=260, y=190)

        # Buttons
        login_button = ttk.Button(self, text='Login', style= 'login.TButton')
        login_button.place(x= 450, y= 260)

        forgot_password = ttk.Button(self, text='Forgot Password',
                                     style='forgot_pass.TButton', )
        forgot_password.place(x=100, y=260)

        close_button = ttk.Button(self, text='close',
                                 style='close.TButton',
                                 command=self.destroy,
                                 )
        close_button.place(x=540, y=2)

        def confirm_signin(event):
            try:
                print(username_entry_var.get(), password_entry_var.get())
                if username_entry_var.get() == 'Admin':
                    print('Admin is correct', username_entry_var.get())
                    notification_message.configure(text='Username is correct!',
                                                   foreground= 'green')
                    username_text.configure(foreground='green')
                    if password_entry_var.get() == 'admin':
                        print('Password is correct', password_entry_var.get())
                        notification_message.configure(text='Login Successful!',
                                                       foreground='green'
                                                       )
                        password_text.configure(foreground='green')
                        switch = True
                        self.dramatic_ending()

                    elif password_entry_var.get() == '':
                        print('Password is empty', password_entry_var.get())
                        notification_message.configure(text='Password cannot be Empty',
                                                       foreground='orange'
                                                       )
                        password_text.configure(foreground='orange')
                    else:
                        print('Password is wrong', password_entry_var.get())
                        notification_message.configure(text='Wrong Password',
                                                       foreground='red'
                                                       )
                        password_text.configure(foreground='red')

                elif username_entry_var.get() == '':
                    print('Username is empty', username_entry_var.get())
                    notification_message.configure(text='Please enter Username',
                                                   foreground='orange'
                                                   )
                    username_text.configure(foreground='orange')
                else:
                    print('Admin is Wrong', username_entry_var.get())
                    notification_message.configure(text='Invalid Username',
                                                   foreground='red'
                                                   )
                    username_text.configure(foreground='red')

            finally:
                print('\nNew Instance due to Error\n')
                # notification_message.destroy()

        self.bind('<Return>', confirm_signin)
        login_button.bind('<Return>', confirm_signin)

    def destruction(self):
        self.destroy()

    def dramatic_ending(self):
        sleep(0.5)
        timer = 50
        contrast = 0.5
        while timer != 0:
            self.attributes('-alpha', contrast)
            contrast = contrast - 0.01
            timer-=1
            sleep(0.03)
        else:
            self.destroy()



def launch_login():
    splash.destroy()
    Login().mainloop()


switch = False

def launch_maingui():
    # Login.destruction()
    if switch is True:
        import mainGUI
        mainGUI.app.mainloop()
    else:
        Login()


try:
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    splash = SplashScreen()
    # splash.after(3000, launch_login)
    splash.mainloop()
