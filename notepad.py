from ast import Delete
import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm


window = tk.Tk()
window.title('notepad')
window.geometry('600x600')

content_text = tk.Text(window)
content_text.place(x=0,y=0, relwidth=1, relheight=1)


main_menu = tk.Menu(window)
window.configure(menu= main_menu)
file_name= ''
file_Label= tk.Label(window, text= f'File {file_name}', font= ("Bookman Old Style", 20))
file_Label.place(relx=0, rely=1, anchor= 'sw')

def file_open():
    content_text.delete(1.0 , "end")
    global file_name
    file_name= tfd.askopenfilename()
    with open(file_name) as file:
       content_text.insert(1.0, file.read()) 


def save_as():
    global file_name
    file_name= tfd.asksaveasfilename()
    content = content_text.get(1.0, 'end')
    with open(file_name, 'w') as save:
        save.write(content)
        

def new_file():
    global file_name
    if tkm.askokcancel("Creating a new file", 'Are you sure? Unsaved text will be deleted'):
        file_name=''
        content_text.delete(1.0, 'end')



new_file_icon = tk.PhotoImage(file= 'new_file.gif')
file_menu = tk.Menu(main_menu)
main_menu.add_cascade(label= "File", menu=file_menu)
file_menu.add_command(label= 'New File', image= new_file_icon, compound= "right", command=new_file)

save_file_icon = tk.PhotoImage(file= 'save_file.gif')
save_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Save", menu= save_menu)
save_menu.add_command(label= 'Save as', image= save_file_icon, compound= 'right', command= save_as)

open_file_icon = tk.PhotoImage(file= 'open_file.gif')
open_file = tk.Menu(main_menu)
main_menu.add_cascade(label="Open", menu= open_file)
open_file.add_command(label= 'Open', image= open_file_icon, compound="right", command= file_open)


#with open("blank.txt", "w") as file:
 #   file.write("hello")
    
#with open("blank.txt", "w") as file:


#save_as_file and new file function









window.mainloop()