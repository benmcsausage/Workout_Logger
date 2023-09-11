import tkinter
import pandas as pd
from tkinter import *
from openpyxl import load_workbook

class Workout:

    def makeGui(exerciseMatrix):
        def submit():
            exercise = e
        root = Tk()
        root.title("Workout Logger 1.0")
        root.minsize(200,200)
        root.maxsize(500,500)
        Label(root, text = "What exercise did you do?").grid(row = 0)
        exercise_entry = Entry(root, width=22)
        exercise_entry.grid(column=1, row = 0)
        Label(root, text = "How many sets did you do?").grid(row = 1)
        sets_entry = Entry(root, width = 22)
        sets.grid(row = 1, column = 1)
        sets  = 0
        sub_btn=tkinter.Button(root,text = 'Submit', command = submit)
        sub_btn.grid(row = 2, column = 2)

        """
        sets = Spinbox(root, from_ = 0, to = 10)
        sets.grid(row = 1, column = 1)
        """
        reps = []
        weight = []
        if(int(sets) > 0):
            for i in range(0,int(sets)):
                Label(root, text = "How many reps did you do in set " + str(i) +"?").grid(row = 2)
                reps_entry = (Entry(root, width = 22))
                Label(root, text = "How much weight did you use in set " + str(i) +"?").grid(row = 3)
                weight_entry =(Entry(root, width =22))      
        mainloop()
        Workout.fillInfo(exercise, sets,reps, weight,exerciseMatrix)
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
        Workout.makeSheet(exerciseMatrix)
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





