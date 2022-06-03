def qanda_quiz():
     """
     defining the game variables, and using 
     for loop to iterate over the questions and answers  
     """
     correct_answer = 0
     wrong_answer = []
     question_no = 1

     for key in questions_data:
          print(key)

          for option in options:
               print(option[0])
# ___________________________________

def checkanswer():
     pass

def showscore():
     pass

def playagain():
     pass


questions_data = {
     "What is the capital of Finland?:" "Helsinki \n",
     "How many elements are there in the periodic table?:" "118 elements \n",
     "What is the largest country in the world?:" "Russia \n",
     "Where was the mojito cocktail created?:" "Cuba \n"}

options = [
     ["A. Tampere", "B. Turku", "C. Espoo", "D. Helsinki "],
     ["A. 120 elements", "B. 130 elements", "C. 118 elements", "D.12 elements"],
     ["A. United Kingdom", "B. Russia", "C. Canada", "D. United State "],
     ["A. Brazil \n", "B. Cuba \n", "C. Coasta Rico \n", "D.Poland"] 
     ]

qanda_quiz()