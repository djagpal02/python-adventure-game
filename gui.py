import tkinter as tk
from PIL import ImageTk, Image
import time
from grid_point import grid_element

class App():
    def __init__(self, root):
        self.frame1 = tk.Frame(root,width=625, height = 625, borderwidth=2 )
        self.frame1.pack_propagate(0)
        self.frame2 = tk.Frame(root,width=625, height=175,borderwidth=2)
        self.frame1.pack()
        self.frame2.pack()
        self.label1 = tk.Label(self.frame2, text=""""Welcome to my adventure game\nWould you like to start a new game or load a previous one? (load/new)""")
        self.label1.pack(padx=20,pady=20)
        self.all = []
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
        self.contin = False
        self.gametype = tk.IntVar()
        self.load = tk.Radiobutton(self.frame2, text="Load",padx = 20, variable = self.gametype, value=1)
        self.load.pack(side=tk.LEFT)
        self.new = tk.Radiobutton(self.frame2, text="New", padx = 20,variable = self.gametype, value=0)
        self.new.pack(side=tk.LEFT)
        self.entryIntro = tk.Entry(self.frame2)
        self.entryIntro.pack()
        self.enter = tk.Button(self.frame2,text = "enter", command = self.intro)
        self.enter.pack(side=tk.RIGHT)
        self.num = tk.IntVar()


        
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
    

        for i in range(22):
            self.frame1.columnconfigure(i,pad=1)
            self.frame1.rowconfigure(i,pad=1)

    def intro(self):
        self.username = self.entryIntro.get()
        self.entryIntro.destroy()
        self.enter.destroy()
        self.new.destroy()
        self.load.destroy()
        self.num.set(1)

        
    def change_image(self,label,img):
        label.configure(image=img)
        label.image = img
    
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
            




                    
            

    def new_msg(self,message):
            self.label1.configure(text=message)
            self.contin = False
    
    def contin_switch(self):
        self.label1.configure(text='')
        self.contin = True








win = tk.Tk()                           # Create a window
win.title("Grid layout")    
win.geometry("625x800")   
win.resizable(False, False)  # Set window title
global myApp  
myApp = App(win)

def printer(message,app=myApp):
    app.new_msg(message)

