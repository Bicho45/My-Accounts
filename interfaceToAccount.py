from tkinter import *
import webbrowser

root = Tk()
root.geometry('1300x550+6-150')         #Solving problem of size + problem of site
root.title('All in one')

#1
def chrome():
    webbrowser.open('https://www.google.com')
btn_c = Button(root,text='Chrome', fg='white', bg='gray', width=10, height=2, command=chrome)
btn_c.place(x=100, y=100)

def facebook():
    webbrowser.open('https://www.facebook.com/')
btn_f = Button(root,text='Facebook', fg='white', bg='gray', width=10, height=2, command=facebook)
btn_f.place(x=400, y=100)

def messenger():
    webbrowser.open('https://www.messenger.com/')
btn_m = Button(root,text='Messenger', fg='white', bg='gray', width=10, height=2, command=messenger)
btn_m.place(x=700, y=100)

def youtube():
    webbrowser.open('https://www.youtube.com/')
btn_y = Button(root,text='Youtube', fg='white', bg='gray', width=10, height=2, command=youtube)
btn_y.place(x=1000, y=100)

#2  
def zoom():    # -> retry
    webbrowser.open('https://zoom.us/signin')
btn_z = Button(root,text='Zoom', fg='white', bg='gray', width=10, height=2, command=zoom)
btn_z.place(x=100, y=300)

def teams():
    webbrowser.open('https://www.microsoft.com/ar-ww/microsoft-teams/log-in')
btn_t = Button(root,text='Teams', fg='white', bg='gray', width=10, height=2, command=teams)
btn_t.place(x=400, y=300)

def github():
    webbrowser.open('https://github.com/')
btn_g = Button(root,text='Github', fg='white', bg='gray', width=10, height=2, command=github)
btn_g.place(x=700, y=300)

def telegram():
    webbrowser.open('https://web.telegram.org/z/')
btn_te = Button(root,text='Telegram', fg='white', bg='gray', width=10, height=2, command=telegram)
btn_te.place(x=1000, y=300)

#3
def edclub():
    webbrowser.open('https://www.typingclub.com/sportal/')
btn_e = Button(root,text='Edclub', fg='white', bg='gray', width=10, height=2, command=edclub)
btn_e.place(x=100, y=480)

def gmail():
    webbrowser.open('https://mail.google.com/mail/u/0/')
btn_gm = Button(root,text='Gmail', fg='white', bg='gray', width=10, height=2, command=gmail)
btn_gm.place(x=400, y=480)

def google_drive():
    webbrowser.open('https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fmy-drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
btn_gd = Button(root,text='Google Drive', fg='white', bg='gray', width=10, height=2, command=google_drive)
btn_gd.place(x=700, y=480)

def udacity():
    webbrowser.open('https://www.udacity.com/online-learning-for-individuals?utm_source=gsem_brand&utm_medium=ads_r&utm_campaign=12949811881_c_individuals&utm_term=123473112164&utm_keyword=udacity_e&gclid=EAIaIQobChMIuJjwu_WV9wIVTgKLCh3OqQTKEAAYASAAEgKOiPD_BwE')
btn_g = Button(root,text='Udacity', fg='white', bg='gray', width=10, height=2, command=udacity)
btn_g.place(x=1000, y=480)

root.mainloop()