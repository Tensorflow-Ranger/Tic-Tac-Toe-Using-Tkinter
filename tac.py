from tkinter import *
from tkinter.ttk import *
import random
  
# creating tkinter window 
root = Tk()
l1 = Label(root, text = "Tic Tac Toe",font =('Verdana', 15))
l1.pack(fill = BOTH, expand= True,pady = 10)
l1.config(anchor=CENTER)

l2 = Label(root, text = "You are O and computer in X",font =('Verdana', 15))
l2.pack(fill = BOTH, expand= True,pady = 10)
l2.config(anchor=CENTER)

photo = PhotoImage(file = "O.png")
photo1 = PhotoImage(file = "X1.png")
photo2 = PhotoImage(file = "images.png")
  
# Resizing image to fit on button 
photoimage = photo.subsample(3, 3)
photoimage1 = photo1.subsample(9, 9)
photoimage2 = photo2.subsample(9, 9)

pane = Frame(root) 
pane.pack(fill = BOTH, expand = True)
    
# button widgets which can also expand and fill 
# in the parent widget entirely 
b1 = Button(pane,text=" ")
b2 = Button(pane,text=" ")
b3 = Button(pane,text=" ")
b4 = Button(pane,text=" ")
b5 = Button(pane,text=" ")
b6 = Button(pane,text=" ")
b7 = Button(pane,text=" ")
b8 = Button(pane,text=" ")
b9 = Button(pane,text=" ")
b10 = Button(pane,text="New Game")

global available
available = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

def win():
    try:
        if (b1['text']=="O" and b4['text']=="O" and b7['text']=="O"
        or b2['text']=="O" and b5['text']=="O" and b8['text']=="O"
        or b3['text']=="O" and b6['text']=="O" and b9['text']=="O"
        or b1['text']=="O" and b2['text']=="O" and b3['text']=="O"
        or b4['text']=="O" and b5['text']=="O" and b6['text']=="O"
        or b7['text']=="O" and b8['text']=="O" and b9['text']=="O"
        or b1['text']=="O" and b5['text']=="O" and b9['text']=="O"
        or b3['text']=="O" and b5['text']=="O" and b7['text']=="O"):
            print("You won")
            l2.config(text="You Won")
        elif (b1['text']=="X" and b4['text']=="X" and b7['text']=="X"
        or b2['text']=="X" and b5['text']=="X" and b8['text']=="X"
        or b3['text']=="X" and b6['text']=="X" and b9['text']=="X"
        or b1['text']=="X" and b2['text']=="X" and b3['text']=="X"
        or b4['text']=="X" and b5['text']=="X" and b6['text']=="X"
        or b7['text']=="X" and b8['text']=="X" and b9['text']=="X"
        or b1['text']=="X" and b5['text']=="X" and b9['text']=="X"
        or b3['text']=="X" and b5['text']=="X" and b7['text']=="X"):
            print("You lost")
            l2.config(text="You Lost")    

    except:
        print("Its a draw")
        l2.config(text="Its a draw")
        

def comp_move():
    try:
        leng = len(available)
        print(available,len(available))
        numb = random.randint(0,leng-1)
        print(numb)
        chose = available[numb]
        print(chose)
        available.remove(chose)
        chose.config(image=photoimage1,state=DISABLED,text="X")
    except:
        l2.config(text="Its a draw")
        
    
def Change(button):
    if button == "b1":
        print(available)
        available.remove(b1)
        b1.config(image=photoimage,state=DISABLED,text="O")
        comp_move()
        win()
    elif button =="b2":
        b2.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b2)
        comp_move()
        win()

    elif button =="b3":
        b3.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b3)
        comp_move()
        win()
    elif button =="b4":
        b4.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b4)
        comp_move()
        win()
    elif button =="b5":
        b5.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b5)
        comp_move()
        win()
    elif button =="b6":
        b6.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b6)
        comp_move()
        win()
    elif button =="b7":
        b7.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b7)
        comp_move()
        win()
    elif button =="b8":
        b8.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b8)
        comp_move()
        win()
    elif button =="b9":
        b9.config(image=photoimage,state=DISABLED,text="O")
        available.remove(b9)
        comp_move()
        win()

def New():
    b1.config(image=photoimage2,state="normal",text=" ")
    b2.config(image=photoimage2,state="normal",text=" ")
    b3.config(image=photoimage2,state="normal",text=" ")
    b4.config(image=photoimage2,state="normal",text=" ")
    b5.config(image=photoimage2,state="normal",text=" ")
    b6.config(image=photoimage2,state="normal",text=" ")
    b7.config(image=photoimage2,state="normal",text=" ")
    b8.config(image=photoimage2,state="normal",text=" ")
    b9.config(image=photoimage2,state="normal",text=" ")
    l2.config(text="You are O and computer in X")
    global available
    available = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    print(available)
    
    

b1.grid(row = 0, column = 0, sticky = W)
b2.grid(row = 0, column = 1, sticky = W)
b3.grid(row = 0, column = 2, sticky = W)
b4.grid(row = 1, column = 0, sticky = W)
b5.grid(row = 1, column = 1, sticky = W)
b6.grid(row = 1, column = 2, sticky = W)
b7.grid(row = 2, column = 0, sticky = W)
b8.grid(row = 2, column = 1, sticky = W)
b9.grid(row = 2, column = 2, sticky = W)
b10.grid(row = 3, column = 1, sticky = W)

b1.config(image=photoimage2,command=lambda: Change("b1"))
b2.config(image=photoimage2,command=lambda: Change("b2"))
b3.config(image=photoimage2,command=lambda: Change("b3"))
b4.config(image=photoimage2,command=lambda: Change("b4"))
b5.config(image=photoimage2,command=lambda: Change("b5"))
b6.config(image=photoimage2,command=lambda: Change("b6"))
b7.config(image=photoimage2,command=lambda: Change("b7"))
b8.config(image=photoimage2,command=lambda: Change("b8"))
b9.config(image=photoimage2,command=lambda: Change("b9"))
b10.config(command=lambda: New())


mainloop()
