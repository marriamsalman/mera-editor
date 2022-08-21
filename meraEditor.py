# -*- coding: utf-8 -*-
"""
@author: Marriam Salman 
Text Editor/Mera Editor
"""

import tkinter as tk
from tkinter import * 
from tkinter import filedialog, messagebox, LabelFrame
from datetime import datetime
import os
import webbrowser
import re
win = tk.Tk()
 
# Add a title
win.title('New File - Mera Editor') 
# Add a icon    
win.iconbitmap('icons\icon.ico')
win.geometry("700x500")


labelframe = LabelFrame(win, text="", bd=5, relief = tk.GROOVE )
labelframe.pack(fill="both", expand="yes")
# text area
text_area = tk.Text(labelframe)
text_area.config(wrap = "word", relief = tk.FLAT, bg='#0C2D48' , fg = '#FCF6F5', undo = True  , exportselection = True)
                 
scrollbar = tk.Scrollbar(labelframe)
text_area.focus_set()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.pack(fill = tk.BOTH, expand = tk.TRUE)
scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set )

# MENU BAR
menubar = tk.Menu()
win.config(menu = menubar)

new_icon = tk.PhotoImage(file="icons\masla_new.png")
open_icon = tk.PhotoImage(file="icons\open.png")
save_icon = tk.PhotoImage(file="icons\save.png")
save_as_icon = tk.PhotoImage(file="icons\save_as2.png")
close_icon = tk.PhotoImage(file="icons\close.png")

word_count_icon = tk.PhotoImage(file="icons\word_counter.png")
char_count_icon = tk.PhotoImage(file="icons\character_counter.png")
copy_icon = tk.PhotoImage(file="icons\copy.png")
cut_icon = tk.PhotoImage(file="icons\cut.png")
paste_icon = tk.PhotoImage(file="icons\paste2.png")
clear_all_icon = tk.PhotoImage(file="icons\masla_clear_all.png")
select_all_icon = tk.PhotoImage(file="icons\select_all.png")
deselect_all_icon = tk.PhotoImage(file="icons\deselect_all.png")
undo_icon = tk.PhotoImage(file="icons\masla_undo.png")
redo_icon = tk.PhotoImage(file="icons\masla_redo.png")

Oldy_icon =tk.PhotoImage(file="icons\oldy.png")
Lime_Punch_icon =tk.PhotoImage(file="icons\Lime_Punch.png")
Green_Scene_icon =tk.PhotoImage(file="icons\Green_Scene.png")
Cherry_Ash_icon =tk.PhotoImage(file="icons\Cherry_Ash.png")
Blazing_Purple_icon =tk.PhotoImage(file="icons\Blazing_Purple.png")
Sapphire_icon =tk.PhotoImage(file="icons\Sapphire.png")

help_icon = tk.PhotoImage(file="icons\help.png")
about_icon = tk.PhotoImage(file="icons\info.png")


# file menu
# Set variable for open file name
global open_status_name
open_status_name = False

global current_location 
current_location = os.getcwd()

global filename
filename = " "
    
# Create New File Function
def new_file(event=None):
    text_area.delete("1.0", tk.END)
    win.title('New File - Mera Editor')

    global open_status_name
    open_status_name = False

# Open Files
def open_file(event=None):
    text_area.delete("1.0", tk.END)
    text_file = filedialog.askopenfilename(initialdir=current_location, title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = True
        
        global filename
        filename = text_file
        
    name = text_file
#    name = name.replace(str(current_location), "")
    win.title(f'{name} - Mera Editor')

    text_file = open(text_file, 'r')
    data = text_file.read()
    text_area.insert(tk.END, data)
    text_file.close()

# Save As File
def save_as_file(event=None):
    text_file = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=current_location, title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file      
#        name = name.replace(str(current_location), "")
        win.title(f'{name} - Mera Editor')

        text_file = open(text_file, 'w')
        text_file.write(text_area.get(1.0, tk.END))
        text_file.close()

# Save File
def save_file(event=None):
    global open_status_name
    if open_status_name:
        text_file = open(filename, 'w')
        text_file.write(text_area.get(1.0, tk.END))
        text_file.close()
        name = filename
#        name = name.replace(str(current_location), "")
        win.title(f'{name} - Mera Editor')
    else:
        save_as_file()

def close(event=None):
    win.destroy()


filemenu = tk.Menu(menubar, tearoff=0, activeborderwidth=2, activebackground="gray55")

filemenu.add_command(label = "New File", command = new_file, accelerator = "Ctrl+n", image = new_icon, compound = tk.LEFT)
filemenu.add_command(label = "Open...", command = open_file, accelerator = "Ctrl+o", image = open_icon, compound = tk.LEFT)
filemenu.add_command(label = "Save", command = save_file, accelerator = "Ctrl+s", image = save_icon, compound = tk.LEFT)
filemenu.add_command(label = "Save As...", command = save_as_file, accelerator = "Ctrl+r", image = save_as_icon, compound = tk.LEFT)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = close, accelerator = "Ctrl+e", image = close_icon, compound = tk.LEFT)
win.bind_all("<Control-n>", new_file)
win.bind_all("<Control-o>", open_file)
win.bind_all("<Control-s>", save_file)
win.bind_all("<Control-r>", save_as_file)
win.bind_all("<Control-e>", close)

# tool menu
def word_count():
    string = text_area.get(1.0,tk.END)
    if string == "":
        no_of_words=0
    else:    
        list_of_words = re.split(r'[;,\s\n]\s*', string)
        while( "" in list_of_words):
            list_of_words.remove("")       
        no_of_words = len(list_of_words)
    message = "Total number of words: " + str(no_of_words)
    messagebox.showinfo("Word Counter",message)
    
def char_count():
    string = text_area.get(1.0,tk.END)  
    if string == "":
        no_of_char = 0
    else:
        no_of_char = len(string)-1
    message = "Total number of characters: " + str(no_of_char)
    messagebox.showinfo("Character Counter",message)
    

toolmenu = tk.Menu(menubar, tearoff=0, activeborderwidth=2, activebackground="gray55")


toolmenu.add_command(label = "Word Counter", command = word_count, image = word_count_icon, compound = tk.LEFT)
toolmenu.add_command(label = "Character Counter", command = char_count, image = char_count_icon, compound = tk.LEFT)
toolmenu.add_separator()
toolmenu.add_command(label = "Copy", image = copy_icon, accelerator="Ctrl+c", compound = tk.LEFT, command=lambda: text_area.event_generate("<Control c>"))
toolmenu.add_command(label = "Cut", image = cut_icon, accelerator="Ctrl+x", compound = tk.LEFT, command=lambda: text_area.event_generate("<Control x>")) 
toolmenu.add_command(label = "Paste", image = paste_icon, accelerator="Ctrl+v", compound = tk.LEFT, command=lambda: text_area.event_generate("<Control v>"))
toolmenu.add_separator()
toolmenu.add_command(label = "Clear All", image = clear_all_icon, compound = tk.LEFT, command=lambda: text_area.delete('1.0', tk.END))
toolmenu.add_command(label = "Select All", image = select_all_icon, compound = tk.LEFT, command=lambda: text_area.tag_add("sel",'1.0',tk.END))
toolmenu.add_command(label = "Deselect All", image = deselect_all_icon, compound = tk.LEFT, command=lambda: text_area.tag_remove("sel",'1.0','end'))
toolmenu.add_separator()
toolmenu.add_command(label = "Undo", image = undo_icon, accelerator="Ctrl+z", compound = tk.LEFT, command=lambda: text_area.event_generate("<<Undo>>"))
toolmenu.add_command(label = "Redo", image = redo_icon, accelerator="Ctrl+y", compound = tk.LEFT, command=lambda: text_area.event_generate("<<Redo>>")) 



# view menu
def theme():
    get_theme = str(theme_select.get()) 
    if get_theme == 'Oldy':
        text_area.config(bg="#c0c0c0", fg = '#303030')
        status_text = "Current date and time: " + dt_str + "\tCurrent Theme: " + get_theme + "  " 
        status_bar.config(text=status_text, image=Oldy_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
    elif get_theme == 'Lime Punch':
        text_area.config(bg='#303030', fg = '#cfee59')
        status_text = "Current date and time: " + dt_str + "\tCurrent Theme: " + get_theme + "  "
        status_bar.config(text=status_text, image=Lime_Punch_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
    elif get_theme == 'Green Scene':
        text_area.config(bg='#037d64', fg = "#cbffcb")
        status_text = "Current date and time: " + dt_str + "\tCurrent Theme: " + get_theme + "  " 
        status_bar.config(text=status_text, image=Green_Scene_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
    elif get_theme == 'Cherry Ash':
        status_text = "Current date and time: " + dt_str + "\tCurrent Theme: " + get_theme + "  " 
        status_bar.config(text=status_text, image=Cherry_Ash_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
        text_area.config(bg='#696969', fg = '#E08152')
    elif get_theme == 'Blazing Purple':
        text_area.config(bg='#101820', fg = '#ff1aff')
        status_text = "Current date and time: " + dt_str + "\tCurrent Theme: " + get_theme + "  "
        status_bar.config(text=status_text, image=Blazing_Purple_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
    elif get_theme == 'Sapphire':
        status_text = "Current date and time: " + dt_str + "\tCurrent Theme: " + get_theme + "  "
        status_bar.config(text=status_text, image=Sapphire_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
        text_area.config(bg='#0C2D48', fg = '#FCF6F5')
    else:
        text_area.config(bg='#0C2D48', fg ='#FCF6F5' )
        status_bar.config(text=status_text, image=Oldy_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)
                   

viewmenu = tk.Menu(menubar, tearoff=0, activeborderwidth=2, activebackground="gray55")

theme_select = tk.StringVar()
theme_select.set("Sapphire")

themeicons = (Oldy_icon, Lime_Punch_icon, Green_Scene_icon, Cherry_Ash_icon, Blazing_Purple_icon, Sapphire_icon)
# values
theme_value_dict  = { 
'Oldy' : ('#c0c0c0' , '#FFFFFF'),
'Lime Punch' : ('#303030' , '#cfee59'),
'Green Scene' : ("#037d64", "#cbffcb"),
'Cherry Ash' : ('#696969' , "#E08152"),
'Blazing Purple' : ("#101820" , '#ff1aff'),
'Sapphire' : ('#0C2D48' , '#FCF6F5'),
} 
    
# fix variable
fix=0
for x in theme_value_dict:
    viewmenu.add_radiobutton(label = x, image = themeicons[fix], compound = tk.LEFT, variable=theme_select, command=theme)
    fix += 1

    
# help menu
def help_window(event=None):
      webbrowser.open_new(r"https://docs.python.org/3/index.html")

def about(event=None):
    message = 'Developer: Marriam Salman\
        \nMera Editor is a text editor that is scripted in PYTHON 3.7. \
        \n\n©2020 MarriamSalman All Rights Reserved.'
    messagebox.showinfo("About Mera Editor",message)
    

helpmenu = tk.Menu(menubar, tearoff=0, activeborderwidth=2, activebackground="gray55")

helpmenu.add_command(label = "View Python 3 Documentation", command = help_window, accelerator="F1", image = help_icon, compound = tk.LEFT)
helpmenu.add_command(label = "About Mera Editor", command = about, accelerator="Ctrl+F1", image = about_icon, compound = tk.LEFT)


win.bind_all("<F1>", help_window)
win.bind_all("<Control-F1>", about)

menubar.add_cascade(label = "File", menu = filemenu)
menubar.add_cascade(label = "Tools", menu = toolmenu)
menubar.add_cascade(label = "View", menu = viewmenu)
menubar.add_cascade(label = "Help", menu = helpmenu) 

#status bar
datetime = datetime.now()
dt_str = datetime.strftime("%d/%m/%Y %H:%M:%S")
status_text = "Current date and time: " + dt_str+ "\tCurrent Theme: " + "Sapphire "
status_bar = tk.Label(labelframe, text=status_text, image=Sapphire_icon, anchor=tk.CENTER, relief = tk.FLAT, compound=tk.RIGHT, pady=3)                             
status_bar.pack(fill="both", side=tk.BOTTOM)
    
win.mainloop() 