from sqlite3 import paramstyle
import pandas as pd
import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook
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
    def __init__(self, parent, controller):
        def combinedFunc(*funcs):
            def inner_combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return inner_combined_func
        def destroyWidgets():
            exercise_label.destroy()
            sets_label.destroy()
            exercise_entry.destroy()
            sets_entry.destroy()
            sub_btn.destroy()
        def getInput():
            exercise = exercise_entry.get()
            sets = int(sets_entry.get())
            global params
            params = [exercise, sets]       
        def askInfo():
            def getInput1():
                global reps, weight
                reps = []
                weight = []
                reps.append(int(reps_entry.get()))
                weight.append(int(weight_entry.get()))
                params.append(reps, weight)
            reps = []
            weight = []
            sub_btn=tk.Button(self,text = 'Submit', command = combinedFunc(getInput1))
            sub_btn.grid(row = 20, column = 2)           
            if(params[1] > 0):
                for i in range(0,params[1]):
                    reps_label = tk.Label(root, text = "How many reps did you do in set " + str(i) +"?")
                    reps_label.grid(row = i)
                    reps_entry = tk.Entry(self)
                    reps_entry.grid(row = i+2, column  =1) 
                    reps.append(int(reps_label.get()))
                    weight_label = tk.Label(root, text = "How much weight did you use in set " + str(i) +"?")
                    weight_label.grid(row = i+1)
                    weight_entry = tk.Entry(self)
                    weight_entry.grid(row = i+3, column  =1) 
                    weight.append(int(weight_label.get()))
                        
        self.frame = tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NewWorkout Page")
        label.grid(row = 0)
        Main_button=ttk.Button(self, text = "Main", command = lambda : controller.show_frame(Main))
        Main_button.grid(row = 1, column = 0, padx = 5, pady = 5)
        exercise_label = tk.Label(self, text = "What exercise did you do?")
        exercise_label.grid(row = 2)                 
        exercise_entry = tk.Entry(self)
        exercise_entry.grid(row = 2, column  =1)        
        sets_label = tk.Label(self, text = "How many sets did you do?")
        sets_label.grid(row = 3)
        sets_entry = tk.Entry(self)
        sets_entry.grid(row = 3, column = 1)
        sub_btn=tk.Button(self,text = 'Submit', command = combinedFunc(getInput,destroyWidgets, askInfo))
        sub_btn.grid(row = 4, column = 2)
        
    

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
        self.minsize(500,200)
        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

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
    root = MainApplication()
    root.mainloop()