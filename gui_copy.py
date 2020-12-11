import tkinter as tk
from PIL import ImageTk, Image
import time
from full_map_gui import map_create
from world_map_gui import world_config


class App():
    def __init__(self, root):
        self.frame1 = tk.Frame(root,width=625, height = 625, borderwidth=2 )
        self.frame1.pack_propagate(0)
        self.frame2 = tk.Frame(root,width=625, height=175,borderwidth=2)
        self.frame1.pack()
        self.frame2.pack()
        self.label1 = tk.Label(self.frame2, text="")
        self.label1.pack(padx=20,pady=20)
        self.all = []
        self.grid = []
        self.tens_grid = []
        self.tens_grid_background = []
        self.sevens_grid = []
        self.sevens_grid_background = []
        self.map_creater()
        self.prev_rows = 0
        self.img1 = ImageTk.PhotoImage(Image.open('images/black.png'))
        self.img2 = ImageTk.PhotoImage(Image.open('images/brown.png'))
        self.img3 = ImageTk.PhotoImage(Image.open('images/red.png'))
        self.img4 = ImageTk.PhotoImage(Image.open('images/green.png'))
        
        for tup in self.all:
            temp = tk.Label(self.frame1,image=self.img1)
            temp.grid(row=tup[1],column=tup[2])
            self.grid.append(temp)
            if tup[1] > 6 and tup[1] < 17 and tup[2] > 5 and tup[2] < 16:
                self.tens_grid.append(temp)
            else:
                self.tens_grid_background.append(temp)
            if tup[1] > 7 and tup[1] < 15 and tup[2] > 6 and tup[2] < 14:
                self.sevens_grid.append(temp)
            else:
                self.sevens_grid_background.append(temp)

        for i in range(22):
            self.frame1.columnconfigure(i,pad=1)
            self.frame1.rowconfigure(i,pad=1)


    def map_creater(self):
        for i in range(22):
            for j in range(22):
                x = 'img' + str(i)+ str(j)
                y = (x,i,j)
                self.all.append(y)
    
    def change_image(self,label,img):
        label.configure(image=img)
        label.image = img

                        
    def show_map2(self,game):
        overall_matrix = []
        rows = 0
        for i in game.user.current_location.map.matrix:
            inner_lists = []
            rows += 1
            for j in i:
                inner_lists.append(j[1])
            overall_matrix.append(inner_lists)
        if self.prev_rows != rows:
            if rows == 22:
                for lab in self.grid:
                    self.change_image(lab,self.img2)
            elif rows == 10:
                for lab in self.tens_grid_background:
                    self.change_image(lab,self.img1)
                for lab in self.tens_grid:
                    self.change_image(lab,self.img2)
            elif rows == 7:
                for lab in self.sevens_grid_background:
                    self.change_image(lab,self.img1)
                for lab in self.sevens_grid:
                    self.change_image(lab,self.img2)

        x = game.user.current_location.row
        y = game.user.current_location.col
        for tup in self.all:
            if tup[1] = x+1 and tup[2] = y+1:
                pass
        temp[y][x] = "PLYER" 0
        self.prev_rows = rows


            

    def new_msg(self,message):
        self.label1.configure(text=message)








win = tk.Tk()                           # Create a window
win.title("Grid layout")    
win.geometry("625x800")   
win.resizable(False, False)  # Set window title
global myApp  
myApp = App(win)

def printer(message,app=myApp):
    app.new_msg(message)

