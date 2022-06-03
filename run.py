def qanda_quiz():
    """
    defining the game variables, and using for 
    loop to iterate over the questions and answers
    """
    right_answer = 0
    wrong_answer = []
    question_no = 1

    for key in questions_data:
        print(key)
        for option in options[question_no - 1]:
            print(option)

        answers = input("enter (A,B,C or D):")
        answers = answers.upper()
        wrong_answer.append(answers)

        check_answer(questions_data.get(key).answers)
        question_no += 1

# ___________________________________

def check_answer():
    pass


def showscore():
    pass


def playagain():
    pass


questions_data = {
    "What is the capital of Finland?: ": "Helsinki \n",
    "How many elements are there in the periodic table?: ": "118 elements \n",
    "What is the largest country in the world?: ": "Russia \n",
    "Where was the mojito cocktail created?: ": "Cuba \n"}

options = [
    ["A. Tampere", "B. Turku", "C. Espoo", "D. Helsinki \n"],
    ["A. 120 elements", "B. 130 elements", "C. 118 elements",
     "D. 112 elements\n"],
    ["A. United Kingdom", "B. Russia", "C. Canada", "D. United State\n "],
    ["A. Brazil", "B. Cuba", "C. Coasta Rico", "D. Poland\n"]
]

qanda_quiz()
