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














window.mainloop()
