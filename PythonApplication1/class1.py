import pandas as pd
from tkinter import *
from openpyxl import load_workbook
class Navbar(Frame):
    x = 0
class Toolbar(Frame):
    x = 0
class Statusbar(Frame):
    x = 0
class Main(Frame):
    x = 0
class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)
        self.parent =parent
        """
        root = Tk()
        root.title("Workout Logger 1.0")
        root.minsize(200,200)
        root.maxsize(500,500)
        text = StringVar()
        text1 = IntVar()
        exercise = ""
        sets = 3
        Label(root, text = "What exercise did you do?").grid(row = 0)                 
        exercise_entry = Entry(root, text = exercise,width=22).grid(row = 0, column = 1)  
        Label(root, text = "How many sets did you do?").grid(row = 1)
        sets_entry = Entry(root, text1 = sets, width = 22).grid(row = 1, column = 1)
        sub_btn=Button(root,text = 'Submit')
        sub_btn.grid(row = 2, column = 2)    
        sets = Spinbox(root, from_ = 0, to = 10)
        sets.grid(row = 1, column = 1)
        reps = []
        weight = []
        if(sets > 0):
            for i in range(0,sets):
                Label(root, text = "How many reps did you do in set " + str(i) +"?").grid(row = i+2)
                reps.append(int(Entry(root, width = 22)))
                Label(root, text = "How much weight did you use in set " + str(i) +"?").grid(row = i+3)
                weight.append(int(Entry(root, width =22)))      
        mainloop()
        Workout.fillInfo(exercise, sets,reps, weight,exerciseMatrix)
        """

class Info:    
    def makeSheet(exerciseMatrix):
        df = pd.DataFrame(exerciseMatrix)
        df.to_csv('exerciseMatrix.csv')
    def fillInfo(exercise,sets,reps,weight,exerciseMatrix):
        exerciseInfo = []
        exerciseInfo.append(exercise)
        exerciseInfo.append(sets)
        for i in range(0,sets):
            exerciseInfo.append(reps[i])
            exerciseInfo.append(weight[i])
        exerciseMatrix.append(exerciseInfo)
        Info.makeSheet(exerciseMatrix)
    """
    def ask():
        numberOfUses = 0
        exerciseMatrix = []
        numExercise = int(input("How many different exercises did you do in your workout?Please enter numbers only\n"))
        for i in range(0,numExercise):
            exercise = input("What exercise did you do?\n")
            sets = int(input("How many sets of " + exercise + " did you do?\n"))
            reps, weight = [],[]
            for i in range(0,sets):
                reps.append(int(input("How many reps of " + exercise + " did you do in set number " + str(i) + "?\n")))
                weight.append(int(input("How much weight did you use for set number "+ str(i)+ " of " + exercise)))
            Workout.fillInfo(exercise,sets,reps,weight,exerciseMatrix)
        print(exerciseMatrix)
    """
if __name__ == "__main__":
    root = Tk()
    MainApplication(root).pack(side = "top", fill ="both", expand =True)
    root.mainloop()




