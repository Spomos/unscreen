import tkinter as tk
import tkinter.font as font
root = tk.Tk()


root.geometry('650x650')
root.configure(bg="turquoise")
root.title("Unscreen")
root.iconbitmap(r'C:\pythonproject\unscreenbutt1.ico')

#def raise_markers(x, y):
    #whenever button is clicked, add one more block to stack


labelFont = font.Font(family='Tahoma', size=10, weight='bold')

label1 = tk.Label(root, text = "Movement\n Goal:", font=labelFont, bg = "turquoise")
label2 = tk.Label(root, text = "Nature\n Goal:", font=labelFont, bg = "turquoise")
label3 = tk.Label(root, text = "Learning\n Goal:", font=labelFont, bg = "turquoise")
label4 = tk.Label(root, text = "Project\n Goal:", font=labelFont, bg = "turquoise")
label5 = tk.Label(root, text = "Art & Beauty\n Goal:", font=labelFont, bg = "turquoise")


entry1 = tk.Entry(root, width = 3)
entry2 = tk.Entry(root, width = 3)
entry3 = tk.Entry(root, width = 3)
entry4 = tk.Entry(root, width = 3)
entry5 = tk.Entry(root, width = 3)

movement_goal = entry1.get()
nature_goal = entry2.get()
learning_goal = entry3.get()
projects_goal = entry4.get()
art_goal = entry5.get()

movement_total = 0
nature_total = 0
learning_total = 0
projects_total = 0
art_total = 0

def message_choice(goal_name, click_total):
   click_total += 1
   if goal_name == click_total:
      label_done = tk.Label(root, text = "You met your daily goal!", font=labelFont, bg = "turquoise")
      label_done.pack()
      return(click_total)
   else:
       label_continue = tk.Label(root, text = "Keep working towards your goal!", font=labelFont, bg = "turquoise")
       label_continue.pack()
      


buttonFont = font.Font(family='Tahoma', size=12, weight='bold')
   
btn1 = tk.Button(root, text = "Movement", font=buttonFont, bg = "red4", command=message_choice(movement_goal, movement_total), activebackground = "firebrick", fg = "gold", height = 4, width = 11)
btn2 = tk.Button(root, text = "Nature", font=buttonFont, bg = "OrangeRed2", activebackground = "coral", fg = "gold", height = 4, width = 11)
btn3 = tk.Button(root, text = "Self-Directed\n Learning", font=buttonFont, bg = "dark goldenrod", activebackground = "goldenrod", fg = "gold", height = 4, width = 11)
btn4 = tk.Button(root, text = "Hands-On\n Projects", font=buttonFont, bg = "dark slate gray", activebackground = "medium slate blue", fg = "gold", height = 4, width = 11)
btn5 = tk.Button(root, text = "Art &\n Beauty", font=buttonFont, bg = "VioletRed4", activebackground = "medium violet red", fg = "gold", height = 4, width = 11)


label1.pack()
label1.place(x=25, y=15)
label2.pack()
label2.place(x=148, y=15)
label3.pack()
label3.place(x=271, y=15)
label4.pack()
label4.place(x=394, y=15)
label5.pack()
label5.place(x=517, y=15)

entry1.pack()
entry1.place(x=95, y=35)
entry2.pack()
entry2.place(x=218, y=35)
entry3.pack()
entry3.place(x=341, y=35)
entry4.pack()
entry4.place(x=464, y=35)
entry5.pack()
entry5.place(x=587, y=35)

btn1.pack()
btn1.place(x=25, y=550)
btn2.pack()
btn2.place(x=148, y=550)
btn3.pack()
btn3.place(x=271, y=550)
btn4.pack()
btn4.place(x=394, y=550)
btn5.pack()
btn5.place(x=517, y=550)
root.mainloop()
