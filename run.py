class questions:
    """
    this is a class that accept two parameters to prompt
     and answer each question
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

"""
this list the question prompt for the user
"""


questions_prompt = [
    "What is the capital of Finland? \n (a) Tampere\n (b) Turku\n (c) Espoo\n (d) Helsinki\n",
    "How many elements are there in the periodic table?:\n (a) 120 elements\n (b) 130 elements\n (c) 112 elements\n (d) 118 elements\n",
    "What is the largest country in the world?:\n (a) United Kingdom\n (b) Russia\n (c) Canada\n (d) United State\n",
    "Where was the mojito cocktail created?:\n (a) Brazil\n (b) Cuba\n (c) Coasta Rico\n (d) Poland\n" 
]
"""
This question prompt stores the correct answers to the question
"""

question = [
    questions(questions_prompt[0], "d"),
    questions(questions_prompt[1], "d"),
    questions(questions_prompt[2], "b"),
    questions(questions_prompt[3], "b"),
]


def question_list(questiones):
    score = 0
    """
    this function loops through the questions list and accepts a list as a parameter.
    """
    for question in questiones:
        answer = input(question.prompt)
        if answer == questions:
            check = check_ans(question, answer, score)
            if check:
                score += 1
            return True
        else:
            return False
            continue


def check_ans(question, answer, score):
    if answer == questions:
        score += 1
        print("correct")
        return True
    else:
        print("incorect")
        return False

    print("You got" + " " + str(score) + " " + "correct out of" + " " + str(len(questiones)))

def main():
    """
    run all program function
    """
    question_list(question)
    check_ans(question, answer, score)

main()