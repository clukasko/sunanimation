from tkinter import *
from time import *

class myFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas (width= 600 , height= 600, bg= "light blue")
        self.myCanvas.grid()
        
 #red arc
        self.myCanvas.create_arc(150, 150,440, 440, style="arc", start=0, extent=180, fill= "red",
                                 outline= "red", width= 20)

#orange arc
        self.myCanvas.create_arc(170, 170, 420, 420, style="arc", start=0, extent=180,
                                 fill= "orange", outline= "orange", width= 20)


#yellow arc
        self.myCanvas.create_arc(190, 190, 400, 400, style="arc", start=0, extent=180, fill= "yellow",
                                 outline= "yellow", width= 20)

#green arc
        self.myCanvas.create_arc(210, 210, 380, 380, style="arc", start=0, extent=180, fill= "indigo",
                                 outline= "indigo", width= 20)

#blue arc
        self.myCanvas.create_arc(230, 230, 360, 360, style="arc", start=0, extent=180, fill= "blue",
                                 outline= "blue", width= 20)

#green grass
        self.myCanvas.create_rectangle(0, 295, 600, 600, fill= "green", outline = "green")
        
#create sun
        
        my_sun_id= self.myCanvas.create_oval(0, 200, 40, 240, fill = "orange", outline = "orange")

#create animation for the sun (loop)
        for count in range(28):
            increment= 10*count
            self.myCanvas.coords(my_sun_id, 0 + increment, 200 - increment,
                                 40 + increment, 240 - increment)
            self.myCanvas.update()
            sleep(0.25)

        self.myCanvas.create_rectange(10, 10, 50, 50, fill="blue")
        self.myCanvas.update()
        
frame01=myFrame()
frame01.mainloop()
