class Workout:
    
    def fillInfo(exercise,sets,reps,exerciseMatrix):
        exerciseInfo = []
        exerciseInfo.append(exercise)
        exerciseInfo.append(sets)
        for i in range(0,sets):
            exerciseInfo.append(reps[i])
        exerciseMatrix.append(exerciseInfo)
        print(exerciseInfo)
    def ask():
        exerciseMatrix = []
        numExercise = int(input("How many different exercises did you do in your workout?Please enter numbers only"))
        for i in range(0,numExercise):
            exercise = input("What exercise did you do?")
            sets = int(input("How many sets of " + exercise + " did you do?"))
            reps = []
            for i in range(0,sets):
                reps.append(int(input("How many reps of " + exercise + " did you do in set number " + str(i) + "?")))
            Workout.fillInfo(exercise,sets,reps,exerciseMatrix)





