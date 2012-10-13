from problem3gui import App
from Tkinter import *
import numpy
class App3(App):
    """docstring for App3"""
    def __init__(self, master):
        self.master = master
        
        # we initialize our previous problem
        prob3 = self.prob3 = App(master)
        
        # add the two entry widgets
        self.vEntry2 = Entry(prob3.top, width=10)
        self.vEntry2.pack(side=RIGHT, expand=False)
        self.vEntry1 = Entry(prob3.top, width=10)
        self.vEntry1.pack(side=RIGHT, expand=False)
        
        # add the button
        self.pathButton = Button(prob3.top, text='Animate', command=self.animate)
        self.pathButton.pack(side=RIGHT, expand=False)
        
        # assign a new title
        self.master.title('Problem 4')
        
        self.edges = []
        
    def animate(self):
        """animation main loop"""
        self.matrix = numpy.copy(self.prob3.conMat)
        self.genEdges()
        self.genPaths()
        print self.edges
        print self.paths
        self.drawLines()
    
    def genEdges(self):
        """generates a list of edges"""
        self.edges = []
        self.n = n = len(self.matrix)
        for i in range(n):
            for j in range(i,n):
                if self.matrix[i][j] == 1:
                    self.edges.append((i,j))
    
    def genPaths(self):
        """generates our list of paths"""
        import networkx as nx
        G = nx.Graph()
        G.add_edges_from(self.edges)
        paths = nx.all_simple_paths(G, source=int(self.vEntry1.get()), target=int(self.vEntry2.get()), cutoff=self.n)
        self.paths = list(paths)
    
    def drawLines(self):
        self.prob3.canvas.delete('animate')
        vert = self.prob3.vert
        print vert
        scale = self.prob3.scale
        size = self.prob3.size
        for item in self.paths:
            for x in range(len(item)-1):
                start = x
                stop = x+1
                startX = int(vert[start][0]*scale + size/2)
                startY = int(vert[start][1]*scale + size/2)
                endX = int(vert[stop][0]*scale + size/2)
                endY = int(vert[stop][1]*scale + size/2)
                self.prob3.canvas.create_line(startX,startY,endX,endY,fill='orange',tag='animate')

if __name__ == '__main__':
    root = Tk()
    app = App3(root)
    root.mainloop()