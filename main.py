'''from tkinter import *  
from tkinter import messagebox  
  
  
def clicked():  
    messagebox.showinfo('Заголовок', 'Текст')  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
btn = Button(window, text='Клик', command=clicked)  
btn.grid(column=0, row=0)  
window.mainloop()'''

from tkinter import *  
from tkinter import ttk  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab3 = ttk.Frame(tab_control) 
tab4 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='Первая')  
tab_control.add(tab2, text='Вторая')  
tab_control.add(tab3, text='Третья') 
tab_control.add(tab4, text='Четвертая') 
lbl1 = Label(tab1, text='Вкладка 1')  
lbl1.grid(column=0, row=0)  
lbl2 = Label(tab2, text='Вкладка 2')  
lbl2.grid(column=0, row=0)  
lbl2 = Label(tab3, text='Вкладка 3')  
lbl2.grid(column=0, row=0)  
lbl2 = Label(tab4, text='Вкладка 4')  
lbl2.grid(column=0, row=0)  
tab_control.pack(expand=1, fill='both')  
window.mainloop()