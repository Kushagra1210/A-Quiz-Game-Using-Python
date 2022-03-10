print("Welcome to the python quiz!")
print("RULE NO. 1: +1 for correct answer")
print("RULE NO. 2: PASSING MARKS(50% OR 5 CORRECT QUESTIONS)")
name = input("What is your name? ")
playing = input( name  + " do you want to play the quiz?(yes/no) ")
score = 0



if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play")

answer = input("Who developed python programming language? ")
if answer.lower() == "Guido van Rossum":
    print("Correct!")
    score += 1 
    
else:
    print("Incorrect!")
    

answer = input("What is the correct extension for python file? ")
if answer.lower() == ".py":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    

answer = input("Which keyword is used for function in python language? ")
if answer == "def":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
  
    
answer = input("Which character is used to give single-line comments in python? ")
if answer == "#":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("Which command is used to check the installed version of Python in the command line? ")
if answer == "python -version":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("What does pip stand for? ")
if answer.lower() == "preferred installer program":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What is truncation division operator in python? ")
if answer == "//":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What is used to define a block of code in python? ")
if answer.lower() == "indentation":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("In which year was the python language developed? ")
if answer == "1991":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("Python supports the creation of anonymous functions at runtime, using which construct? ")
if answer.lower() == "lambda":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")


    







print("Thank you for taking the quiz!")

if (score>=5):
    print("Congratulations! You have successfully passed the quiz.")
else:
    print("Better luck next time.")

print(name + " you got " + str(score) + "/10 questions correct." )
print("Accuracy: " + str((score/10) * 100) + " %")