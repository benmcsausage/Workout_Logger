class Workout:
    def __init__(self, exercise,sets,reps):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
    def newfunc(self):
        print("hello my exercise is " + self.exercise)
    def ask():
        self.exercise = input("What exercise did you do?")
        self.sets = input("How many sets of " + self.exercise + " did you do?")
        for i in range(0,self.sets):
            self.sets = input("How many reps of " + self.exercise + " did you do in set number " + i + "?")






