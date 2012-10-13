from Tkinter import *
from problem3 import *
class App(Frame):
    """Main application window"""
    def __init__(self, master):
        self.master = master
        Frame.__init__(self,master)
        self.scale = 250
        self.size = 600
        self.rad = 5
        
        #draw two frames
        self.top = Frame(master) #buttons and stuff go here
        self.top.pack(side=TOP, expand = False, fill=X)
        self.bottom = Frame(master) #canvas goes here
        self.bottom.pack(side=BOTTOM, expand=True, fill=BOTH)
        
        self.master.title("Problem 3")
        master.wm_state("zoomed")
        
        self.canvas = Canvas(self.bottom,width=self.size,height=self.size)
        self.canvas.pack(fill=BOTH,expand=YES)
        self.canvas.config(background='black', borderwidth = 0)
        
        self.nEntry = Entry(self.top, width=30)
        self.nEntry.pack(side=LEFT, expand=False)
        self.nEntry.insert(0,'n vertices')
        
        self.go = Button(self.top,text='Generate', command = self.mainLogic)
        self.go.pack(side=LEFT, expand=False)
    
    
    def mainLogic(self):
        """Main execution loop when button is pressed"""
        self.canvas.delete('all')
        n = int(self.nEntry.get())
        
        self.vert = vert = genVertList(n)
        self.drawPoints(vert)
        
        self.conMat = conMat = ranSymMatrix(n)
        self.calcConn(conMat)
    
    
    def drawPoints(self,vert):
        #print self.width
        rad = self.rad
        count = 0
        for p in vert:
            x = int(p[0]*self.scale + self.size/2)
            y = int(p[1]*self.scale + self.size/2)
            self.canvas.create_oval(x-rad,y-rad,x+rad,y+rad,width=1,outline='red',fill='red',tag=count)
            count = count+1
    
    
    def calcConn(self,conMat):
        for i in range(len(conMat)):
            for j in range(i,len(conMat)):
                if conMat[i,j]==1:
                    self.drawLine(i,j)
    
    
    def drawLine(self,start,stop):
        """docstring for drawLines"""
        startX = int(self.vert[start][0]*self.scale + self.size/2)
        startY = int(self.vert[start][1]*self.scale + self.size/2)
        endX = int(self.vert[stop][0]*self.scale + self.size/2)
        endY = int(self.vert[stop][1]*self.scale + self.size/2)
        
        self.canvas.create_line(startX,startY,endX,endY,fill='white')
    
    

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
        