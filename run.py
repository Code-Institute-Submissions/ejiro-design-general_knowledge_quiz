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

        choose_answer = input("enter (A,B,C or D):")
        choose_answer = choose_answer.upper()
        wrong_answer.append(choose_answer)

        check_answer(questions_data.get(key), choose_answer)
        question_no += 1

# ___________________________________

def check_answer(answer, choose_answer):

    """
    checking for correct or wrong answer and return a point or score
    """

    if answer == choose_answer:
        print("correct answer:")
        return 1
    else:
        print("wrong answer:")
        return 0

# ___________________________________
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
check_answer()
