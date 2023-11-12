from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from random import randint
import sqlite3

root = Tk()
root.title("Fun Vocabulary Game")
# full screen
root.geometry("{}x{}+0+0". format(root.winfo_screenwidth(), root.winfo_screenheight()))

# upload image
bg = ImageTk.PhotoImage(file="image/bg.jpg")
home_icon = ImageTk.PhotoImage(file="image/home_icon.png")
vocab_icon = ImageTk.PhotoImage(file="image/vocab_icon.png")

# keep track on coordinate
def position(event):
    global position_x, position_y
    position_x = event.x_root
    position_y = event.y_root
        
root.bind("<Button 1>",position)

# create canvas
canvas = Canvas(root)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, image=bg, anchor="nw")

# create intro page 1
def intropage1():
    canvas.create_text(750,350, text="   Hello!! welcome to\nFun Vocabulary Game", font=("Arial Black", 50), fill="#003297", tag="label1")
    button1 = Button(root, text="Next", font=("Arial Black", 25), bg="#003297", fg="white", width=10, command=next)
    canvas.create_window(640,480, anchor="nw", window=button1, tag="button1")
    
# crate intro page 2
def intropage2():
    canvas.create_text(750,350, text="  Let's create your\nown vocabulary set", font=("Arial Black", 50), fill="#003297", tag="label2")
    button2 = Button(root, text="Let's go", font=("Arial Black", 25), bg="#003297", fg="white", width=10, command=go)
    canvas.create_window(640,480, anchor="nw", window=button2, tag="button2")

# create next function
def next():
    canvas.delete("label1")
    canvas.delete("button1")
    intropage2()

# create go function
def go():
    canvas.destroy()
    create_menu()
    create_frame()


# ******************************************************** #
# create menu
def create_menu ():
    global mymenu
    mymenu = Menu(root)
    root.config(menu=mymenu)

    # create home menu
    home_menu = Menu(root)
    home_menu.add_command(label="Home", font=("", 15), command=home)
    home_menu.add_separator()
    home_menu.add_command(label="Find some vocabulary set", font=("", 15), command=findvocab)
    home_menu.add_command(label="Create your own vocabulary set", font=("", 15), command=createvocab)
    home_menu.add_separator()
    home_menu.add_command(label="Exit", font=("", 15), command=root.quit)
    
    # create vocab menu
    vocab_menu = Menu(root)
    vocab_menu.add_command(label="Your own vocabulary set", font=("", 15), command=newtab2)
    
    # create menu item
    mymenu.add_cascade(label="Home", menu=home_menu)
    mymenu.add_cascade(label="Vocabulary", menu=vocab_menu)

# ******************************************************** #
# create tab and frame
def create_frame():
    s = ttk.Style()
    s.configure('TNotebook.Tab', font=("Arial Black", 15))
    
    global Tab,frame1,frame2
    Tab = ttk.Notebook(root)
    frame1 = ttk.Frame(Tab)
    frame2 = ttk.Frame(Tab)
    
    # add tab
    Tab.add(frame1, text=" Home  ", image=home_icon, compound="right")
    Tab.add(frame2, text=" Vocabulary ", image=vocab_icon, compound="right")
    Tab.pack(fill="both", expand=1)
    
    # crate frame1
    global canvas1
    canvas1 = Canvas(frame1)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0,0, image=bg, anchor="nw")
    
    #create frame2
    global canvas2
    canvas2 = Canvas(frame2)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0,0, image=bg, anchor="nw")
    
    homepage()
    
    
# ******************************************************** #
# create home page
def homepage():
    global find_button
    find_button = Button(frame1, text="Find some\nvocabulary set", font=("Arial Black", 30), bg="#003297", fg="white", command=findvocab)
    canvas1.create_window(300,280, window=find_button, anchor="nw")
    
    global create_button
    create_button = Button(frame1, text="Create your own\nvocabulary set", font=("Arial Black", 30), bg="#003297", fg="white", command=createvocab)
    canvas1.create_window(770,280, window=create_button, anchor="nw")

# create home function
def home():
    canvas1.delete("all")
    canvas1.create_image(0,0, image=bg, anchor="nw")
    homepage()
    
# create new tab function
def newtab2(): Tab.select(frame2)
def newtab1(): Tab.select(frame1)

# create find vocab page
def findvocab():
    
    canvas1.delete("all")
    canvas1.create_image(0,0, image=bg, anchor="nw")
    find_label = Label(frame1, text=" Find some vocabulary set ", font=("Arial Black", 35), bg="#003297", fg="white", width=28, height=1)
    canvas1.create_window(280,200, window=find_label, anchor="w")
    
    
    global find_button1, find_button2, find_button3, find_button4
    find_button1 = Button(frame1, text="Financing", font=("Arial Black", 30), bg="#003297", fg="white", width=15, height=1, command=vocab_financing)
    find_button2 = Button(frame1, text="Travelling", font=("Arial Black", 30), bg="#003297", fg="white", width=15, height=1, command=vocab_travelling)
    find_button3 = Button(frame1, text="Management", font=("Arial Black", 30), bg="#003297", fg="white", width=15, height=1, command=vocab_management)
    find_button4 = Button(frame1, text="Purchasing", font=("Arial Black", 30), bg="#003297", fg="white", width=15, height=1, command=vocab_purchasing)
    
    canvas1.create_window(280,280, window=find_button1, anchor="nw")
    canvas1.create_window(750,280, window=find_button2, anchor="nw")
    canvas1.create_window(280,420, window=find_button3, anchor="nw")
    canvas1.create_window(750,420, window=find_button4, anchor="nw")
    
# create your own vocab page  
def createvocab():
    
    canvas1.delete("all")
    canvas1.create_image(0,0, image=bg, anchor="nw")
    
    global create_label, title_entrybox, createnext_button
    create_label = Label(frame1, text=" Create your own vocabulary set", font=("Arial Black", 25), bg="#003297", fg="white", width=31)
    title_entrybox = Entry(frame1, font=("Arial Black", 25), width=32)
    createnext_button = Button(frame1, text="Next", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=create_next)
    
    canvas1.create_window(450,270, window=create_label, anchor="w")
    canvas1.create_window(450,350, window=title_entrybox, anchor="w")
    canvas1.create_text(350,350, text="Title : ", font=("Arial Black", 30), fill="#003297")
    canvas1.create_window(700,420, window=createnext_button, anchor="nw")


# ******************************************************** #
# create database
def create_next():
    
    canvas1.delete("all")
    canvas1.create_image(0,0, image=bg, anchor="nw")
    
    global name1,connection1, cursor1
    name1 = title_entrybox.get()
    connection1 = sqlite3.connect("database/" + str(name1) + ".db")
    cursor1 = connection1.cursor()
    cursor1.execute("CREATE TABLE vocab (คำศัพท์ text, ความหมาย text)")
    
    global entrybox1, entrybox2
    canvas1.create_text(280,250, text="คำศัพท์ : ", font=("Arial Black", 30), fill="#003297", anchor="w")
    canvas1.create_text(280,350, text="ความหมาย : ", font=("Arial Black", 30), fill="#003297", anchor="w")
    entrybox1 = Entry(frame1, font=("Arial Black", 25), width=25)
    entrybox2 = Entry(frame1, font=("Arial Black", 25), width=25)
    canvas1.create_window(550,250, window=entrybox1, anchor="w")
    canvas1.create_window(550,350, window=entrybox2, anchor="w")
    
    add_button = Button(frame1, text="Add", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=add_data)
    finish_button = Button(frame1, text="Finish", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=finish)
    canvas1.create_window(630,450, window=add_button, anchor="w")
    canvas1.create_window(850,450, window=finish_button, anchor="w")
    
# add data to database
def add_data():
    
    data_vocab = entrybox1.get()
    data_meaning = entrybox2.get()
    
    name1 = title_entrybox.get()
    connection1 = sqlite3.connect("database/" + str(name1) + ".db")
    cursor1 = connection1.cursor()
    cursor1.execute("INSERT INTO vocab(คำศัพท์, ความหมาย) VALUES (?, ?)", (str(data_vocab), str(data_meaning)))
    connection1.commit()
    
    entrybox1.delete(0,END)
    entrybox2.delete(0,END)
    
# finish add data function
yourown_count = 0
name_list = []

def finish():
    name1 = title_entrybox.get()
    connect_db(str(name1))
    play_button = Button(frame1, text="play", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=play_yourown)
    canvas1.create_window(750,510, window=play_button, anchor="w")
    
    global yourown_count
    yourown_count = yourown_count + 1
    yourown()
    
    global name_list
    name_list.append(str(name1))

# upload your vocabulary set 
def yourown():
    name1 = title_entrybox.get()
    y_odd = (yourown_count-1)/2
    y_even = (yourown_count/2)-1
    yourown_label = Label(frame2, text="Your own vocabulary set", font=("Arial Black", 35), bg="#003297", fg="white", width=28, height=1)
    canvas2.create_window(280,200, window=yourown_label, anchor="w")
    
    yourown_button = Button(frame2, text=str(name1), font=("Arial Black", 30), bg="#003297", fg="white", width=15, height=1, command=vocab_yourown)
    if (yourown_count % 2) != 0 :
        canvas2.create_window(280,280+(140*y_odd), window=yourown_button, anchor="nw")
    else :
        canvas2.create_window(750,280+(140*y_even), window=yourown_button, anchor="nw")



# ******************************************************** #
# create funtion to link database
def vocab_financing(): 
    connect_db('financing')
    play_button_financing = Button(frame1, text="play", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=play_financing)
    back_button_financing = Button(frame1, text="back", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=findvocab)
    canvas1.create_window(650,510, window=play_button_financing, anchor="w")
    canvas1.create_window(850,510, window=back_button_financing, anchor="w")

def vocab_travelling(): 
    connect_db('travelling')
    play_button_travelling = Button(frame1, text="play", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=play_travelling)
    back_button_travelling = Button(frame1, text="back", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=findvocab)
    canvas1.create_window(650,510, window=play_button_travelling, anchor="w")
    canvas1.create_window(850,510, window=back_button_travelling, anchor="w")
    
def vocab_management(): 
    connect_db('management')
    play_button_management = Button(frame1, text="play", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=play_management)
    back_button_management = Button(frame1, text="back", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=findvocab)
    canvas1.create_window(650,510, window=play_button_management, anchor="w")
    canvas1.create_window(850,510, window=back_button_management, anchor="w")
    
def vocab_purchasing():
    connect_db('purchasing')
    play_button_purchasing = Button(frame1, text="play", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=play_purchasing)
    back_button_purchasing = Button(frame1, text="back", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=findvocab)
    canvas1.create_window(650,510, window=play_button_purchasing, anchor="w")
    canvas1.create_window(850,510, window=back_button_purchasing, anchor="w")
    
global position_x, position_y
def vocab_yourown():
    
    global name_count, name2
    if position_x >= 280 and position_x < 750 :
        name_count = int((position_y - 400)/140)
        name2 = name_count*2
        connect_db(str(name_list[name2]))
    else :
        name_count = int((position_y - 400)/140)
        name2 = ((name_count+1)*2)-1
        connect_db(str(name_list[name2]))
    
    newtab1()
    play_button_purchasing = Button(frame1, text="play", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=play_yourown2)
    back_button_purchasing = Button(frame1, text="back", font=("Arial Black", 15), bg="#003297", fg="white", width=10, command=newtab2)
    canvas1.create_window(650,510, window=play_button_purchasing, anchor="w")
    canvas1.create_window(850,510, window=back_button_purchasing, anchor="w")
    
    
    
# ******************************************************** #
# connect to database
def connect_db(name):
    
    canvas1.delete("all")
    canvas1.create_image(0,0, image=bg, anchor="nw")

    connection = sqlite3.connect("database/" + str(name) + ".db")
    cursor = connection.cursor()
    
    sql = "SELECT * FROM vocab"
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    name_label = Label(frame1, text="Vocab Set : " + str(name), font=("Arial Black", 25), bg="#003297", fg="white", width=23)
    canvas1.create_window(550,190, window=name_label, anchor="w")

    treeview = ttk.Treeview(frame1, column=(1,2), show="headings", height=5)
    canvas1.create_window(550,230, window=treeview, anchor="nw") 
    
    scroll = ttk.Scrollbar(frame1, orient="vertical", command=treeview.yview)
    canvas1.create_window(1100,230, window=scroll, anchor="nw", height=230) 
    treeview.configure(yscrollcommand=scroll.set)
    
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", "18"))
    style.configure("Treeview.Heading", font=("Arial Black", "18"))
    style.configure("Treeview", rowheight=40)
    
    treeview.column(1, stretch=NO, width=230)
    treeview.column(2, stretch=NO, width=300)
    treeview.heading(1, text="คำศัพท์")
    treeview.heading(2, text="ความหมาย")
    
    for i in rows :
        treeview.insert('', 'end', values=i)

        
# ******************************************************** #
def play_financing(): play('financing')
def play_travelling(): play('travelling')
def play_management(): play('management')
def play_purchasing(): play('purchasing')

def play_yourown():
    name1 = title_entrybox.get()
    play(str(name1))
    
def play_yourown2():
    play(str(name_list[name2]))


# create play function
def play(name):
    canvas1.delete("all")
    canvas1.create_image(0,0, image=bg, anchor="nw")
    
    connection = sqlite3.connect("database/" + str(name) + ".db")
    cursor = connection.cursor()
    sql = "SELECT * FROM vocab"
    
    global words, history, count
    words = list(cursor.execute(sql))
    count = len(words)
    history = []
    
    random()
    pass_button = Button(frame1, text="Pass", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=pass_function)
    next_button = Button(frame1, text="Next", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=go_next)
    answer_button = Button(frame1, text="Answer", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=answer)
    canvas1.create_window(600,500, window=next_button, anchor="w")
    canvas1.create_window(370,500, window=pass_button, anchor="w")
    canvas1.create_window(830,500, window=answer_button, anchor="w")
    
    global ans_entrybox
    ans_entrybox = Entry(frame1, font=("Arial Black", 25), width=29)
    canvas1.create_window(370,400, window=ans_entrybox, anchor="w")
    
    
# create random function   
def random():
    canvas1.delete("meaning")
    total = len(words)
    incorrect_count = total-(score + pass_count)
    
    correct_percent = (score/total)*100
    incorrect_percent = (incorrect_count/total)*100
    pass_percent = (pass_count/total)*100
    
    if len(words) < len(history)+1 :
        canvas1.delete("all")
        canvas1.create_image(0,0, image=bg, anchor="nw")
        canvas1.create_text(400,220, text="complete! คุณทำแบบทดสอบครบแล้ว", font=("Arial Black", 25), fill="red", anchor="w")
        canvas1.create_text(400,270, text=f"คะแนนรวมทั้งหมด {score} จาก {total} คะแนน", font=("Arial Black", 25), fill="red", anchor="w")
        canvas1.create_text(400,320, text=f"จำนวนคำศัพท์ที่ตอบถูก {score} คำ คิดเป็น {'%.2f' %(correct_percent)} %", font=("Arial Black", 25), fill="#003297", anchor="w")
        canvas1.create_text(400,370, text=f"จำนวนคำศัพท์ที่ตอบผิด {incorrect_count} คำ คิดเป็น {'%.2f' %(incorrect_percent)} %", font=("Arial Black", 25), fill="#003297", anchor="w")
        canvas1.create_text(400,420, text=f"จำนวนคำศัพท์ที่ข้าม {pass_count} คำ คิดเป็น {'%.2f' %(pass_percent)} %", font=("Arial Black", 25), fill="#003297", anchor="w")
        
        backhome_button = Button(frame1, text="Back to Home", font=("Arial Black", 18), bg="#003297", fg="white", width=15, command=backtohome)
        exit_button = Button(frame1, text="Exit", font=("Arial Black", 18), bg="#003297", fg="white", width=10, command=root.quit)
        canvas1.create_window(500,500, window=backhome_button, anchor="w")
        canvas1.create_window(800,500, window=exit_button, anchor="w")
        
    while(True) :
        global random_number
        random_number = randint(0, count-1)
        if not random_number in history:
            history.append(random_number)
            break
        if len(words) <= len(history):
            history.append(1000)
            break
     
    if len(history) <= len(words) : 
        canvas1.create_text(370,230, text="ความหมาย : ", font=("Arial Black", 30), fill="#003297", anchor="w", tag="meaning") 
        canvas1.create_text(630,230, text=str(words[random_number][1]), font=("Arial Black", 30), fill="#003297", anchor="w", tag="meaning")

global pass_count
pass_count = 0
  
# create pass function
def pass_function():
    global pass_count
    pass_count = pass_count + 1
    random()

global score
score = 0

# create answer function
def answer():
    global score
    answer_label = ans_entrybox.get()
    if answer_label.lower() == words[random_number][0] :
        canvas1.create_text(370,310, text="Correct! " + str(words[random_number][1]) + " คือ " + str(words[random_number][0]), font=("Arial Black", 30), fill="green", anchor="w", tag="answer")
        score = score+1
    else :
        canvas1.create_text(370,310, text="Incorrect! " + str(words[random_number][1]) + " คือ " + str(words[random_number][0]), font=("Arial Black", 30), fill="red", anchor="w", tag="answer")  
    
# create next function
def go_next():
    ans_entrybox.delete(0,END)
    canvas1.delete("answer")
    random()
    
# create back home function
def backtohome():
    global score,pass_count
    score = 0
    pass_count = 0
    home()
    

# ******************************************************** #

intropage1()
root.mainloop()
