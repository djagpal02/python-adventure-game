import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import time
from grid_point import grid_element

class App():
    def __init__(self, root):
        # Set frames
        self.frame1 = tk.Frame(root,highlightbackground="green", highlightcolor="green", highlightthickness=1,width=625, height = 625, borderwidth=2 )
        self.frame1.pack_propagate(0)
        self.frame2 = tk.Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1,width=625, height=325,borderwidth=2)
        self.frame3 = tk.Frame(root, highlightbackground="blue", highlightcolor="blue", highlightthickness=1,width=625, height=200,borderwidth=2)
        self.frame4 = tk.Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1,width=625, height=200,borderwidth=2)
        self.frame5 = tk.Frame(root, highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1,width=625, height=50,borderwidth=2)
        self.frame6 = tk.Frame(root, highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1,width=625, height=50,borderwidth=2)
        self.frame1.pack_propagate(0)
        self.frame1.pack(side= tk.LEFT)
        self.frame4.pack_propagate(0)
        self.frame4.pack(side = tk.TOP)
        self.frame6.pack_propagate(0)
        self.frame6.pack()
        self.frame5.pack_propagate(0)
        self.frame5.pack()
        self.frame2.pack_propagate(0)
        self.frame2.pack()
        self.frame3.pack_propagate(0)
        self.frame3.pack(side = tk.BOTTOM)

        # Images - 25x25 pixel squares
        self.img1 = ImageTk.PhotoImage(Image.open('images/black.png'))
        self.img2 = ImageTk.PhotoImage(Image.open('images/brown.png'))
        self.img3 = ImageTk.PhotoImage(Image.open('images/red.png'))
        self.img4 = ImageTk.PhotoImage(Image.open('images/green.png'))
        self.img5 = ImageTk.PhotoImage(Image.open('images/door.png'))
        self.img6 = ImageTk.PhotoImage(Image.open('images/blue.png'))
        self.img7 = ImageTk.PhotoImage(Image.open('images/yellow.png'))
        self.img8 = ImageTk.PhotoImage(Image.open('images/white.png'))
        self.img9 = ImageTk.PhotoImage(Image.open('images/orange.png'))
        self.img10 = ImageTk.PhotoImage(Image.open('images/grey.png'))
        self.img11 = ImageTk.PhotoImage(Image.open('images/white.png'))

        # Intro Label
        self.label1 = tk.Label(self.frame2, text=""""Welcome to my adventure game\nWould you like to start a new game or load a previous one? (load/new)""")
        self.label1.grid(row=1,padx=20,pady=20)
        self.all = []

        # Intro Radio Buttons
        self.gametype = tk.IntVar()
        self.load = tk.Radiobutton(self.frame2, text="Load",padx = 20, variable = self.gametype, value=1)
        self.load.grid(row=3)
        self.new = tk.Radiobutton(self.frame2, text="New", padx = 20,variable = self.gametype, value=0)
        self.new.grid(row=4)

        # Intro Name input
        self.entryIntro = tk.Entry(self.frame2)
        self.entryIntro.grid(row=5)
        self.enter = tk.Button(self.frame2,text = "enter", command = self.intro)
        self.enter.grid(row=6)

        # Fight info Label
        self.fightinfo = tk.Label(self.frame5, text = "")
        self.fightinfo.pack()
        self.fightinfo_row1 = tk.Label(self.frame5, text = "")
        self.fightinfo_row1.pack()

        # To pause after messages
        self.contin = False

        # Var to check for when waiting on input
        self.num = tk.IntVar()
        self.num2 = tk.IntVar()
        # Var to hold inputs
        self.inp = ""
        # Button and Entry Box for inputs
        self.entry = tk.Entry(self.frame2)
        self.enter_two = tk.Button(self.frame2,text = "enter", command = self.pull)
        self.enter_three = tk.Button(self.frame2,text = "enter2", command = self.pull2())

        # Create grid_element objects
        for i in range(22):
            for j in range(22):
                if i > 6 and i < 17 and j > 5 and j < 16:
                    tens = (i-7,j-6)
                else:
                    tens = (99,99)
                if i > 7 and i < 15 and j > 6 and j < 14:
                    sevens = (i-8,j-7)
                else:
                    sevens = (99,99)

                temp = tk.Label(self.frame1,image=self.img1)

                y = grid_element(i,j,temp,tens,sevens)
                y.label.grid(row=y.row,column = y.col)
                self.all.append(y)

        # Add padding to all rows and columns
        for i in range(22):
            self.frame1.columnconfigure(i,pad=1)
            self.frame1.rowconfigure(i,pad=1)


        self.stats = tk.Label(self.frame3, text = "")
        self.stats.grid(row=1, column=0)

        self.items = tk.Label(self.frame3, text = "")
        self.items.grid(row=1, column=1)


        # User instructions
        self.instructions = tk.Label(self.frame3, text = "Keys \nW - Up \nS - Down \nA - Left \nD - Right \nReturn - Continue")
        self.instructions.grid(row=1, column=2)

        # Location Label 
        self.big_loc = tk.Label(self.frame4, text = "")
        self.big_loc.grid()
        self.big_loc.config(width = 50)

        # Health bars
        #playerHP_blocks = []
        #oppHP_blocks = []
        #for i in range(20):
        #    strng = "playerHP" + str(i)
        #    self.strng = tk.Label(self.frame6,image=self.img1)
        #    self.strng.grid(row=0,column=i)
        #    playerHP_blocks.append(self.strng)
        #    strng2 = "opponentHP" + str(i)
        #    self.strng2 = tk.Label(self.frame6,image= self.img1)
        #    self.strng2.grid(row=1,column=i)
        #    oppHP_blocks.append(self.strng2)

    #############################################################################################################################################

    def intro(self):
        self.username = self.entryIntro.get()
        self.entryIntro.destroy()
        self.enter.destroy()
        self.new.destroy()
        self.load.destroy()
        self.num.set(1)
        
    def pull(self):
        self.num.set(1)
        
    def pull2(self):
        self.contin = True
        self.num2.set(1)

    def change_image(self,label,img):
        label.configure(image=img)
        label.image = img
    
    def new_msg(self,message):
        self.label1.configure(text=message)
        self.contin = False
    
    def new_msg_f5(self,message,row_num):
        if row_num == 0:
            self.fightinfo.configure(text=message)
        if row_num == 1:
            self.fightinfo_row1.configure(text=message)

    def new_warning(self,msg):
        messagebox.showinfo(title="Info", message=msg)
    
    def contin_switch(self):
        self.label1.configure(text='')
        self.contin = True
    

    ########################################################################################################################################
    

    def battle(self,game):
        if game.user.in_battle:
            for g in self.all:
                self.change_image(g.label,self.img1)





    ########################################################################################################################################

    
    def map_keys(self,label,plc):
        if plc == '-WALL':
            self.change_image(label,self.img2)
        elif plc == '#####':
            self.change_image(label,self.img4)
        elif plc == 'RIVER':
            self.change_image(label,self.img6)
        elif plc == 'WORLD':
            self.change_image(label,self.img3)
        elif plc in ['HOMEB', 'HTLB2', 'HTLB3', 'HTLB4']:
            self.change_image(label,self.img9)
        elif plc in ['SHOP1','SHOP2','SHOP3','SHOP4', 'SHOPM']:
            self.change_image(label,self.img10)
        elif plc in ['JOHN-','PARNT', 'CHIEF', 'RBKKA', 'EARL-', 'MNIMN', 'BENNN', 'MAYOR', 'GUARD', 'QUEEN', 'WOLFS', 'SIONN', 'SRPQN', 'FROST', 'DRKTH']:
            self.change_image(label,self.img7)
        elif plc in ['4TOWN', 'MNTN-', 'TOWER', '2TOWN', '3TOWN', 'HTOWN', '2CAVE', '1CAVE', 'HOUSE','LHOM1',  '2SHOP', '2HOTL', 'LHOM2',  '3SHOP', '3HOTL', 'LHOM3',  '4SHOP', '4HOTL', 'LHOM4', '1CVL1', '2CVL1', '2CVL2', '2CVL3', '1TWR1', '1TWR2', 'MNUP1', 'MNUP2', 'MNUP3']:
            self.change_image(label,self.img5)



    # Prints map, organization varies based on size of current map
    def show_map2(self,game):
        size = len(game.user.current_location.map.matrix)
        x = game.user.current_location.row
        y = game.user.current_location.col
        
        for g in self.all:
            if size == 22:
                for i in range(22):
                    for j in range(22):
                            plc = game.user.current_location.map.matrix[i][j][1]
                            if g.row == i and g.col == j:
                                self.map_keys(g.label,plc)
                                if g.row == x and g.col == y:
                                    self.change_image(g.label,self.img8)
            
            elif size == 10:
                for i in range(10):
                    for j in range(10):
                        plc = game.user.current_location.map.matrix[i][j][1]
                        if g.tens_mapping[0] == i and g.tens_mapping[1] == j:
                            self.map_keys(g.label,plc)
                            if g.tens_mapping[0] == x and g.tens_mapping[1] == y:
                                self.change_image(g.label,self.img8)

                        elif g.tens_mapping == (99,99):
                            self.change_image(g.label,self.img1)

            elif size == 7:
                for i in range(7):
                    for j in range(7):
                        plc = game.user.current_location.map.matrix[i][j][1]
                        if g.sevens_mapping[0] == i and g.sevens_mapping[1] == j:
                            self.map_keys(g.label,plc)
                            if g.sevens_mapping[0] == x and g.sevens_mapping[1] == y:
                                self.change_image(g.label,self.img8)

                        elif g.sevens_mapping == (99,99):
                            self.change_image(g.label,self.img1)

        self.show_stats(game)
        

    def show_stats(self,game):
        self.stats.configure(text = f"Name:  {game.user.name}\nLevel:  {game.user.level} \nAD: {game.user.AD} \nHP:  {game.user.HP}\nMAX HP:  {game.user.max_HP} \nEXP:  {game.user.EXP} \nEXP FOR NEXT LEVEL:  {game.user.exp_needed} \nGOLD:  {game.user.gold}")
        strng = "In your bag:"
        for item in game.user.items.keys():
            strng += f"\n{item.name} x {game.user.items[item]}"
        self.items.configure(text = strng)

        self.big_loc.configure(text = game.user.current_location.map.name)




win = tk.Tk()                           # Create a window
win.title("Pixel Adventure")    
win.geometry("1250x625")   
win.resizable(False, False)  # Set window title
global myApp  
myApp = App(win)

def printer(message,app=myApp,inp=False):
    app.new_msg(message)
    if inp == True:
        app.entry.grid(row = 5)
        app.enter_two.grid(row = 6)
        app.enter_two.wait_variable(app.num)
        app.inp = app.entry.get()
        app.entry.grid_forget()
        app.enter_two.grid_forget()

        return myApp.inp

def warning(message,app=myApp):
    app.new_warning(message)

def printer_frame5(message,row_num, app=myApp,):
    app.new_msg_f5(message,row_num)