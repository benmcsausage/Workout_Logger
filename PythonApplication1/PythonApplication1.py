
from multiprocessing.util import ForkAwareLocal
from sqlite3 import paramstyle
import pandas as pd
import tkinter as tk
import _sqlite3
from tkinter import ttk
from openpyxl import load_workbook
global exerciseMatrix

exerciseMatrix = []
class PreviousWorkouts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PreviousWorkouts Page")
        label.grid(row = 0)
        Main_button=ttk.Button(self, text = "Main", command = lambda : controller.show_frame(Main))
        Main_button.grid(row = 1, column = 0, padx = 5, pady = 5)
        # We use the switch_window_button in order to call the show_frame() method as a lambda function
class Progress(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Progress Page")
        label.grid(row = 0)
        Main_button=ttk.Button(self, text = "Main", command = lambda : controller.show_frame(Main))
        Main_button.grid(row = 1, column = 0, padx = 5, pady = 5)
        # We use the switch_window_button in order to call the show_frame() method as a lambda function
class NewWorkout(tk.Frame):
    global params
    params = []
    def __init__(self, parent, controller):
        self.x = 0
        self.frame = tk.Frame.__init__(self, parent)
        def combinedFunc(*funcs):
            def inner_combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return inner_combined_func
        
        """
        def destroyWidgets():
            exercise_label.destroy()
            sets_label.destroy()
            exercise_entry.destroy()
            sets_entry.destroy()
            sub_btn.destroy()
        """
        def destroyWidgets(exnum_label, exnum_entry, sub_btn):
            exnum_entry.destroy()
            exnum_label.destroy()
            sub_btn.destroy()
            print("hello")
        def getInput(exnum_entry):
            ex_num = int(exnum_entry.get())          
            params.append(ex_num)
            print(params)
        """
        def getInput():
            exercise = exercise_entry.get()
            sets = int(sets_entry.get())
            global params
            params = [exercise, sets]
        """        
        def destroyWidgets1(entries,labels,sub_btn):
            sub_btn.destroy()
            for i in range(0,len(entries)):
                entries[i].destroy()
            for i in range(0,len(labels)):
                labels[i].destroy()
            recreateWidgets()
        def destroyWidgets2(entries,labels,sub_btn):
            sub_btn.destroy()
            for i in range(0,len(entries)):
                entries[i].destroy()
            for i in range(0,len(labels)):
                labels[i].destroy()
            recreateWidgets1()
        
        def getInput1(exercises, sets, entries, labels, sub_btn):
            for i in range(0,(params[0])*2-1, 2):
                exercises.append(entries[i].get())
                sets.append(int(entries[i+1].get()))
            params.append(exercises)
            params.append(sets)
            destroyWidgets1(entries,labels,sub_btn)
        def getInput2(reps, weight, entries, labels, sub_btn):
            for i in range(0,(params[0])*2-1, 2):
                reps.append(entries[i].get())
                weight.append(int(entries[i+1].get()))
            params.append(reps)
            params.append(weight)
            destroyWidgets2(entries,labels,sub_btn)
        def askInfo():
            print("hello")
            labels = []
            entries = []
            exercises = []
            sets = []
            if(params[0] > 0):
                for i in range(0,params[0]*2-1):
                    labels.append(tk.Label(self, text = "What is the name of exercise " + str(i+1) + "?"))
                    labels[i].grid(row = i+3, column = 0)                   
                    labels.append(tk.Label(self, text = "How many sets did you do for exercise " +str(i+1) + "?"))
                    labels[i+1].grid(row = i+4, column = 0)
            if(params[0]> 0):        
                for i in range(0,params[0]*2-1):
                    entries.append(tk.Entry(self))
                    entries[i].grid(row = i+3, column  =1)
                    entries.append(tk.Entry(self))
                    entries[i+1].grid(row = i+4, column  =1)
            sub_btn=tk.Button(self,text = 'Submit', command = lambda: [getInput1(exercises,sets,entries,labels,sub_btn)])
            sub_btn.grid(row = params[0]*2+4, column = 1)
        def recreateWidgets():
            labels = []
            entries = []
            reps = []
            weight = []
            y = 0
            w= 0
            z = 0
            u = 0
            for x in range(0, params[0]):
                labels.append(tk.Label(self, text = params[1][x]))
                labels[x+y].grid(row = x+y+3, column = 0)
                if x == 0:
                    for i in range(0,params[2][x]):
                        labels.append(tk.Label(self, text = "How many reps did you do in set " +str(i+1) + "?"))                       
                        labels[x+i*2+1].grid(row = x+w+4, column = 0)
                        labels.append(tk.Label(self, text = "How much weight did you use in set " + str(i+1) + "?"))
                        labels[x+i*2+2].grid(row = x+w+5, column = 0)
                        if params[2][x] != 1:
                            w+=2
                    for i in range(0,params[2][x]):
                        entries.append(tk.Entry(self))
                        entries[x-z+i*2].grid(row = x+u+4, column  =1)
                        entries.append(tk.Entry(self))
                        entries[x-z+1+i*2].grid(row = x+u+5, column  =1)
                        if params[2][x] != 1:
                            u+=2
                else:
                    for i in range(0,params[2][x]):
                        labels.append(tk.Label(self, text = "How many reps did you do in set " +str(i+1) + "?"))                       
                        labels[x+w+1].grid(row = x+w+4, column = 0)                   
                        labels.append(tk.Label(self, text = "How much weight did you use in set " + str(i+1) + "?"))
                        labels[x+w+2].grid(row = x+w+5, column = 0)
                        if params[2][x] != 1:
                            w+=2
                    for i in range(0,params[2][x]):
                        entries.append(tk.Entry(self))
                        entries[x-z+u].grid(row = x+u+4, column  =1)
                        entries.append(tk.Entry(self))
                        entries[x-z+1+u].grid(row = x+u+5, column  =1)
                        if params[2][x] != 1:
                            u+=2
                y+=params[2][x]*2
                z+=1
                print(labels)
                print(entries)
            sub_btn=tk.Button(self,text = 'Submit', command = lambda: [getInput2(reps, weight,entries,labels,sub_btn)])
            sub_btn.grid(row = params[0]*2+5+y, column = 1)
        def recreateWidgets1():
            label = tk.Label(self, text="NewWorkout Page")
            label.grid(row = 0)
            Main_button=ttk.Button(self, text = "Main", command = lambda : controller.show_frame(Main))
            Main_button.grid(row = 1, column = 0, padx = 5, pady = 5)
            exnum_label = tk.Label(self, text = "How many different exercises did you do?")
            exnum_label.grid(row = 2)
            exnum_entry = tk.Entry(self)
            exnum_entry.grid(row = 2, column = 1)
            sub_btn=tk.Button(self,text = 'Submit', command = lambda : [getInput(exnum_entry), destroyWidgets(exnum_label, exnum_entry, sub_btn), askInfo()])
            sub_btn.grid(row = 2, column = 2)
        recreateWidgets1()
        """
        def askInfo():           
            reps = []
            weight = []
            labels = []
            entries = []                             
            if(params[1] > 0):
                for i in range(0,params[1]*2-1):
                    labels.append(tk.Label(self, text = "How many reps did you do in set " + str(i+1) +"?"))
                    labels[i].grid(row = i+3, column = 0)                   
                    labels.append(tk.Label(self, text = "How much weight did you use in set " + str(i+1) +"?"))
                    labels[i+1].grid(row = i+4, column = 0)
            if(params[1]> 0):        
                for i in range(0,params[1]*2-1):
                    entries.append(tk.Entry(self))
                    entries[i].grid(row = i+3, column  =1)
                    entries.append(tk.Entry(self))
                    entries[i+1].grid(row = i+4, column  =1)
            sub_btn=tk.Button(self,text = 'Submit', command = lambda: [getInput1(reps,weight,entries,labels, sub_btn)])
            sub_btn.grid(row = 0, column = 3)
                   
        def recreateWidgets():
            def destroyWidgets2():
                exercise_label.destroy()
                sets_label.destroy()
                exercise_entry.destroy()
                sets_entry.destroy()
                sub_btn.destroy()
            def getInput1():
                params.append(exercise_entry.get())
                params.append(int(sets_entry.get()))
            Main_button=ttk.Button(self, text = "Main", command = lambda : controller.show_frame(Main))
            Main_button.grid(row = 1, column = 0, padx = 5, pady = 5)           
            exercise_label = tk.Label(self, text = "What's the next exercise you did after " + str(params))
            self.x += 4
            exercise_label.grid(row = 2)                 
            exercise_entry = tk.Entry(self)
            exercise_entry.grid(row = 2, column  =1)        
            sets_label = tk.Label(self, text = "How many sets did you do?")
            sets_label.grid(row = 3)
            sets_entry = tk.Entry(self)
            sets_entry.grid(row = 3, column = 1)
            sub_btn=tk.Button(self,text = 'Submit', command = combinedFunc(getInput1, destroyWidgets2, askInfo))
            sub_btn.grid(row = 4, column = 2)
        """
        
        
        
        """
        exercise_label = tk.Label(self, text = "What exercise did you do?")
        exercise_label.grid(row = 2)                 
        exercise_entry = tk.Entry(self)
        exercise_entry.grid(row = 2, column  =1)        
        sets_label = tk.Label(self, text = "How many sets did you do?")
        sets_label.grid(row = 3)
        sets_entry = tk.Entry(self)
        sets_entry.grid(row = 3, column = 1)
        
        """
        
    

class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.grid(row = 0)
        NewWorkout_button=ttk.Button(self, text = "New Workout", command = lambda : controller.show_frame(NewWorkout))
        NewWorkout_button.grid(row = 1, column = 0, padx = 0, pady = 5)
        PreviousWorkouts_button=ttk.Button(self, text = "Previous Workouts", command = lambda : controller.show_frame(PreviousWorkouts))
        PreviousWorkouts_button.grid(row = 1, column = 1, padx = 0, pady = 5)        
        Progress_button=ttk.Button(self, text = "Progress", command = lambda : controller.show_frame(Progress))
        Progress_button.grid(row = 1, column = 2, padx = 0, pady = 5)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Workout Logger 1.0")
        self.minsize(800,600)
        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.grid(row = 0)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (Main, PreviousWorkouts, NewWorkout, Progress):
            frame = F(container, self)

            # the MainApplication class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

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
if __name__ == "__main__":
    root = MainApplication()
    root.mainloop()