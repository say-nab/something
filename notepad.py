import tkinter as tk
window = tk.Tk()
window.title('notepad')
window.geometry('600x600')

content_text = tk.Text(window)
content_text.place(x=0,y=0, relwidth=1, relheight=1)

main_menu = tk.Menu(window)
window.configure(menu= main_menu)

















window.mainloop()
