class Questions:
    """ 
    this is a class that accept two parameters to prompt
    and answer each question, the question the valid choices and the answer
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# this list the question prompt for the user


questions_prompt = [
    ("What is the capital of Finland? \n (a) Tampere\n (b) Turku\n (c) Espoo\n (d) Helsinki\n"),
    ("How many elements are there in the periodic table?:\n (a) 120 elements\n (b) 130 elements\n (c) 112 elements\n (d) 118 elements\n"),
    ("What is the largest country in the world?:\n (a) United Kingdom\n (b) Russia\n (c) Canada\n (d) United State\n"),
    ("Where was the mojito cocktail created?:\n (a) Brazil\n (b) Cuba\n (c) Coasta Rico\n (d) Poland\n")  
]

# This question prompt stores the correct answers to the question


QUESTION_DATA = [
    Questions(questions_prompt[0], "d"),
    Questions(questions_prompt[1], "d"),
    Questions(questions_prompt[2], "b"),
    Questions(questions_prompt[3], "b"),
]


def user_question(questions_no):
    """
    this function is to ask the user the questions and when the user gets \n
    the correct answer the score will increase by 1 or decrease, it also \n
    gives you an option to quit the game and skip a question
    """
    while True:
        try:
            name = input("Please enter your name:")
            if not name.isdigit():
                print("Hello", name, "welcome to the quiz:\n")
                print("You have 4 questions to answer")
                break   
        except NameError():
            print("invalid, please enter your name")

    score = 0
    for question in questions_no:
        skip_quiz = input("would you like to skip this question? (yes/no):")
        if not skip_quiz == "no":
            continue
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct answer, 1 point")
            score += 1
            print("Your current score is:", score)
        else: 
            print("Wrong answer, you lost 1 point")
            score -= 1
            print("Your current score is:", score)
        quit_quizs = input("do you want to quit (yes/no):")
        if not quit_quizs == "no":
            break
    print("You got" " " + str(score) + "/" + str(len(questions_no)) + " " "correct")


def main():
    """
    display all call function
    """
    user_question(QUESTION_DATA)


main()
