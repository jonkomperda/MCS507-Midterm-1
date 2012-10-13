from problem3gui import App
from Tkinter import *
import numpy
import tkMessageBox
class App3(App):
    """Extension from problem 3 to problem 4"""
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
        #localize the matrix
        try:
            self.matrix = numpy.copy(self.prob3.conMat)
        except:
            tkMessageBox.showerror('Usage Error','You must first generate a gragh BEFORE animating it!')
        #generate the edges from the matrix
        self.genEdges()
        
        #check if the user points exist
        edgeExist = self.checkIfEdgeExist()
        
        #then do our stuff if they exist, othewise tell user they messed up
        if edgeExist:
            self.genPaths()
            self.drawLines()
        else:
            tkMessageBox.showerror('Value Error','You did not select a valid point, it does not have connections. Please select a different point!')
    
    
    def genEdges(self):
        """generates a list of edges between the points"""
        self.edges = []
        self.n = n = len(self.matrix)
        for i in range(n):
            for j in range(i,n):
                if self.matrix[i,j] == 1:
                    self.edges.append((i,j))
    
    
    def checkIfEdgeExist(self):
        """
        We check if the edges specified by the user exist
        If we don't do this, then networkx will spit out a nasty error and crash
        """
        #get the points users wants fromt the gui
        point1 = self.vEntry1.get()
        point2 = self.vEntry2.get()
        
        #flatten the edge list and remove duplicates
        flatList = list(set([item for sublist in self.edges for item in sublist]))
        
        if point1 in flatList:
            if point2 in flatList:
                return True
            else:
                return False
        else:
            return False
    
    
    def genPaths(self):
        """
        Generates our list of possible paths between two nodes in the network.
        This routine takes advantage of the all_simple_paths feature of networkx.
        I attempted to use the Floyd Warshall algorithm to reconstruct the paths,
        but was unsucessful. Luckily, open source scientific software that solves
        the problem at hand exists
        """
        # check whether the user has network x
        try:
            import networkx as nx
        # tell them how to get it if they don't have it
        except:
            tkMessageBox.showerror('Missing Package','In order to use this feature you must install NetworkX from http://networkx.lanl.gov\nUse \'sudo easy_install networkx\' to install the package')
        
        # make G our graph
        G = nx.Graph()
        
        # add our edges to the graph
        G.add_edges_from(self.edges)
        
        # generate our paths using all_simple_paths
        # http://networkx.lanl.gov/reference/generated/networkx.algorithms.simple_paths.all_simple_paths.html
        paths = nx.all_simple_paths(G, source=int(self.vEntry1.get()), target=int(self.vEntry2.get()), cutoff=self.n)
        # bring it back to list format so it can be used
        self.paths = list(paths)
    
    
    def drawLines(self):
        """
        Draws the actual lines that we are looking for
        """
        self.prob3.canvas.delete('animate')
        vert = self.prob3.vert
        print vert
        scale = self.prob3.scale
        size = self.prob3.size
        for item in self.paths:
            for x in range(len(item)-1):
                start = item[x]
                stop = item[x+1]
                startX = int(vert[start][0]*scale + size/2)
                startY = int(vert[start][1]*scale + size/2)
                endX = int(vert[stop][0]*scale + size/2)
                endY = int(vert[stop][1]*scale + size/2)
                self.prob3.canvas.create_line(startX,startY,endX,endY,fill='orange',tag='animate')

if __name__ == '__main__':
    root = Tk()
    app = App3(root)
    root.mainloop()