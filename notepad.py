from ast import Delete
import tkinter as tk
window = tk.Tk()
window.title('notepad')
window.geometry('600x600')

content_text = tk.Text(window)
content_text.place(x=0,y=0, relwidth=1, relheight=1)


main_menu = tk.Menu(window)
window.configure(menu= main_menu)

new_file_icon = tk.PhotoImage(file= 'new_file.gif')
file_menu = tk.Menu(main_menu)
main_menu.add_cascade(label= "File", menu=file_menu)
file_menu.add_command(label= 'New File', image= new_file_icon, compound= "right")

save_file_icon = tk.PhotoImage(file= 'save_file.gif')
save_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Save", menu= save_menu)
save_menu.add_command(label= 'Save', image= save_file_icon, compound= 'right')

open_file_icon = tk.PhotoImage(file= 'open_file.gif')
open_file= tk.Menu(main_menu)
main_menu.add_cascade(label="Open", menu= open_file)
open_file.add_command(label= 'Open', image= open_file_icon, compound="right")

#with open("blank.txt", "w") as file:
 #   file.write("hello")
    
#with open("blank.txt", "w") as file:

def open_file():
    with open('blank.txt', 'r') as file:
       content_text.insert(1.0, file.read()) 
        
#save_as_file and new file function

def save_as():
    with open('text.txt', 'w') as save:
        save.write(content_text)

def new_file():
    content_text.delete('0.0', 'end')






window.mainloop()
