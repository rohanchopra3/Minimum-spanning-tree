
#This file contains all the fucntions to implement GUI and use the algorithms.
#Created By Rohan Chopra

import tkinter as tk
import tkinter.messagebox
import PrimsAlgo as PA
import DataStructures as DS
import KruskalAlgo as KA


from tkinter.filedialog import askopenfilename

#FIRST VIEW CLASS
class ViewSpace(object):
    def __init__(self,window):
        self.window = window
        self.text = "Minimum Spanning Tree"
        self.title_frame = tk.Frame(window, width=600, height=200)
        self.button_frame = tk.Frame(window, width=500,height=100)


        self.titleLabl = tk.Label(self.title_frame, text=self.text, height = 3,font = ('arial', 18, 'bold'))
        self.FooterLabl = tk.Label(window, text="Created by Rohan Chopra", height=3, font=('arial', 12))
        self.button1 = tk.Button(self.button_frame, text="Prims" ,fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",cursor = "hand1",command=self.primsButtonClick)
        self.button2 = tk.Button(self.button_frame, text="Kruskal",fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",cursor = "hand1",command=self.KruskalButtonClick)
        self.button3 = tk.Button(self.button_frame, text="Dont know?",fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",cursor = "hand1",command=self.donwKnowButton)


    def setUpInitalView(self):
        self.title_frame.pack(side="top")
        self.button_frame.pack()
        self.FooterLabl.pack(side="bottom")
        self.titleLabl.pack()
        self.button1.grid(row = 4, column = 0, padx = 1, pady = 1)
        self.button2.grid(row=4, column=1, padx = 1, pady = 1)
        self.button3.grid(row=4, column=2, padx = 1, pady = 1)


    def primsButtonClick(self):
        self.title_frame.destroy()
        self.button_frame.destroy()
        Prim = AlgoView(self.window,"Prims Algorithm")
        Prim.ViewSetup()
        Prim.typeOfAlgo = 1

    def KruskalButtonClick(self):
        self.title_frame.destroy()
        self.button_frame.destroy()
        Prim = AlgoView(self.window,"Kruskal Algorithm")
        Prim.ViewSetup()
        Prim.typeOfAlgo = 2

    def donwKnowButton(self):

        self.title_frame.destroy()
        self.button_frame.destroy()
        DontKnow = dontKnowButtonAlgo(self.window,"Compare")
        DontKnow.setupView()


#ALGORITHM VIEW CLASS
class AlgoView(object):


    def __init__(self,window,text):
        self.filePath = ""
        self.Graph = []
        self.numberOfVertices = 0
        self.window = window
        self.typeOfAlgo = 0 # 1 for prims and 2 for Kruskal
        self.MST = []
        self.time = ""
        self.primsButtonClickPageTitle = tk.Frame(window, width=600, height=100)
        self.primsButtonClickPageBody = tk.Frame(window, width=600, height=100)
        self.primsButtonClickPageBody2 = tk.Frame(window, width=600, height=175)
        self.titleLabel = tk.Label(self.primsButtonClickPageTitle, text=text, height=3,
             font=('arial', 18, 'bold'))
        self.SelectButton = tk.Button(self.primsButtonClickPageBody, text="Select File ", fg="black", width=10, height=1,
                             bd=0, bg="#fff", cursor="hand1", command=self.selectFile)
        self.textLabel = tk.Label(self.primsButtonClickPageBody, text="Please select a text file with graph data:", height=3)
        self.fileSelectionLabel = tk.Label(self.primsButtonClickPageBody2, text="No file selected", height=1)
        self.GoButton = tk.Button(self.primsButtonClickPageBody2, text="GO", fg="black", width=10, height=1, bd=0, bg="#fff",
                         cursor="hand1", command=self.goButtonMethod)
        self.orLabel = tk.Label(self.primsButtonClickPageBody2, text="Or", height=1)
        self.backButton = tk.Button(self.primsButtonClickPageBody2, text="Back", fg="black", width=10, height=1, bd=0,
                           bg="#fff", cursor="hand1", command=self.backButtonMethod)

    def ViewSetup(self):

        self.primsButtonClickPageTitle.pack(side="top")
        self.primsButtonClickPageBody.pack()
        self.primsButtonClickPageBody2.pack()
        self.titleLabel.pack()
        self.textLabel.grid(row=1, column=0, padx=0, pady=0)
        self.SelectButton.grid(row=1, column=1, padx=0, pady=0)
        self.fileSelectionLabel.pack()
        self.GoButton.pack()
        self.orLabel.pack()
        self.backButton.pack()

    def backButtonMethod(self):
        self.primsButtonClickPageTitle.destroy()
        self.primsButtonClickPageBody.destroy()
        self.primsButtonClickPageBody2.destroy()
        self.typeOfAlgo = 0
        g = ViewSpace(self.window)
        g.setUpInitalView()
        g.FooterLabl.destroy()

    def selectFile(self):
        self.filePath = askopenfilename()
        if len(self.filePath) != 0:
            with open(self.filePath, 'r') as f:
                 self.Graph = [[int(num) for num in line.split(',')] for line in f]

            self.numberOfVertices = DS.CountVertices(self.Graph)
            if self.numberOfVertices != 0:
                 self.fileSelectionLabel.configure(text="Graph extracted with {} vertices".format(self.numberOfVertices))
            else:
                self.fileSelectionLabel.configure(text="Input Not accepted")

    # THIS FUNCTIONS CHECK WHICH TYPE OF ALGO SHOULD BE USED
    def goButtonMethod(self):

        if self.numberOfVertices != 0 :
            if self.typeOfAlgo == 1 :
                 self.performsPrims()
            else:
                 self.performsKruskal()


    def performsPrims(self):
        print()
        g = DS.createGraphUsingAdjMatrix(self.numberOfVertices)
        g.addGraphToAdjMAtrix(self.Graph)
        p = PA.prims(self.numberOfVertices)
        p.runPrimsAlgoFor(g.adjMatrix)
        self.MST = p.minSpanningTree
        print("prims")
        print(p.minSpanningTree)
        self.time = p.time
        self.ShowAlertWithResult()


    def performsKruskal(self):
        K = KA.kruskalAlgo(self.numberOfVertices)
        K.DS.addRecursively(self.Graph)
        K.FindMST()
        self.MST = K.MST
        print("Kruskal")
        print(K.MST)
        self.time = K.time
        self.ShowAlertWithResult()

    def ShowAlertWithResult(self):

        if len(self.MST) < 30 :
            textValue = "[V1,V2,Weight] "
            for i in self.MST:
                 textValue = textValue + "\n" + str(i)

            textValue = textValue +"\n" + self.time
            tk.messagebox.showinfo("Minimum Spanning Tree is- ", textValue )
        else:
            textValue = "[V1,V2,Weight] {} ".format(self.MST)
            textValue = textValue + "\n" + self.time
            tk.messagebox.showinfo("Minimum Spanning Tree is- ", textValue)



#DONT KNOW VIEW CLASS
class dontKnowButtonAlgo(object):

    def __init__(self, window, text):
        self.window = window
        self.vertices = 0
        self.edges = 0
        self.dontKnowButtonTitle = tk.Frame(window, width=600, height=100)
        self.dontKnowButtonPageBody = tk.Frame(window, width=600, height=100)
        self.dontKnowButtonBody2 = tk.Frame(window, width=600, height=175)

        self.titleLabel = tk.Label(self.dontKnowButtonTitle, text=text, height=2,font=('arial', 18, 'bold'))

        self.textLabel = tk.Label(self.dontKnowButtonPageBody, text="Enter number of vertices:",
                              height=1)
        self.textLabel2 = tk.Label(self.dontKnowButtonPageBody, text="Enter number of Edges:",
                                  height=1)

        self.prims = tk.Label(self.dontKnowButtonPageBody, text="Prims= O(|V*V|)",
                                  height=3)
        self.kruskal = tk.Label(self.dontKnowButtonPageBody, text="Kruskal= O(|E*LogV|)",
                                   height=3)
        self.input1 = tk.Entry(self.dontKnowButtonPageBody,width=4)
        self.input2 = tk.Entry(self.dontKnowButtonPageBody, width=4)
        self.go = tk.Button(self.dontKnowButtonBody2, text="Go", fg="black", width=10, height=1, bd=0,
                           bg="#fff", cursor="hand1",command=self.goButton)
        self.back = tk.Button(self.dontKnowButtonBody2, text="Back", fg="black", width=10, height=1, bd=0,
                            bg="#fff", cursor="hand1", command=self.backButton)


    def setupView(self):
        self.dontKnowButtonTitle.pack(side="top")
        self.dontKnowButtonPageBody.pack()
        self.dontKnowButtonBody2.pack()

        self.titleLabel.pack(side="top")
        self.textLabel.grid(row=0,column=0)
        self.input1.grid(row=0,column=1)

        self.textLabel2.grid(row=1,column=0)
        self.input2.grid(row=1, column=1)

        self.kruskal.grid(row=2,column=0)
        self.prims.grid(row=2, column=1)
        self.go.pack()
        self.back.pack()


    def goButton(self):
        msh = self.CheckForResult()
        if len(msh) != 0:
            tk.messagebox.showinfo("You should use ", msh)

    def CheckForResult(self):

        if len(self.input1.get()) != 0 and len(self.input2.get()) != 0:

            v = int(self.input1.get())
            e = int(self.input2.get())
            d = (2 * e) / (v * (v - 1))
            if d > 0.5:
                return "You should use Prims. Since graph is dense."
            else:
                return "You should use Kruskal. Since graph is sparse."

    def backButton(self):

        self.dontKnowButtonTitle.destroy()
        self.dontKnowButtonPageBody.destroy()
        self.dontKnowButtonBody2.destroy()
        g = ViewSpace(self.window)
        g.setUpInitalView()
        g.FooterLabl.destroy()



