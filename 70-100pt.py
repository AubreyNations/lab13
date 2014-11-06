#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.


import random
from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='#C2FCFF')
player = drawpad.create_oval(390,580,410,600, fill="#CA85FF", outline="#CA85FF")
enemy1 = drawpad.create_rectangle(random.randint(10,250),100,125,125, fill="#FF9D1C", outline="#FF9D1C")
enemy2 = drawpad.create_rectangle(random.randint(10,250),250,125,275, fill="#FF9D1C", outline="#FF9D1C")
enemy3 = drawpad.create_rectangle(random.randint(10,250),400,125,425, fill="#FF9D1C", outline="#FF9D1C")
direction = 1
# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "#8AD6FF")
       	    self.up.grid(row=0,column=1)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.left = Button(self.myContainer1)
	    self.left.configure(text="Left", background= "#8AD6FF")
	    self.left.grid(row=1,column=0)
	    self.left.bind("<Button-1>", self.leftClicked)
		
	    self.right = Button(self.myContainer1)
	    self.right.configure(text="Right", background= "#8AD6FF")
	    self.right.grid(row=1,column=2)											
	    self.right.bind("<Button-1>", self.rightClicked)
            
            self.down = Button(self.myContainer1)
	    self.down.configure(text="Down", background= "#8AD6FF")
	    self.down.grid(row=2,column=1)											
	    self.down.bind("<Button-1>", self.downClicked) 
	         	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-30)

        def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-30,0)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,30,0)		
		
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,30)
	   # Create our animation function
	   
#Staying stationary. HELP!
def animate1(): 
    global direction
    global enemy1
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    if x2 > drawpad.winfo_width():
        direction = - 825
    elif x1 < -5:
        direction = 5
    #Move our oval object by the value of direction
    drawpad.move(enemy1,direction,0)
    drawpad.after(1, animate1)

#Staying stationary. HELP!    
def animate2():
    global direction 
    global enemy2 
    x1, y1, x2, y2 = drawpad.coords(enemy2)
    if x2 > drawpad.winfo_width():
        direction = - 825
    elif x1 < -5:
        direction = 5
    drawpad.move(enemy2,direction,0)
    drawpad.after(1, animate2)

#This is the only moving enemy at the moment.    
def animate3():
    global direction 
    global enemy3  
    x1, y1, x2, y2 = drawpad.coords(enemy3)
    if x2 > drawpad.winfo_width():
        direction = - 825
    elif x1 < -5:
        direction = 5
    drawpad.move(enemy3,direction,0)
    drawpad.after(1, animate3)

animate1()
animate2()
animate3()		
app = MyApp(root)
root.mainloop()