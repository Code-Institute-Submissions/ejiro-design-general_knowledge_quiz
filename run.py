from question import questions

"""
creating an array of question prompt for the user
"""

questions_prompt = [
    "What is the capital of Finland? \n (a) Tampere\n (b) Turku\n (c) Espoo\n (d) Helsinki\n",
    "How many elements are there in the periodic table?:\n (a) 120 elements\n (b) 130 elements\n (c) 112 elements\n (d) 118 elements\n",
    "What is the largest country in the world?:\n (a) United Kingdom\n (b) Russia\n (c) Canada\n (d) United State\n",
    "Where was the mojito cocktail created?:\n (a) Brazil\n (b) Cuba\n (c) Coasta Rico\n (d) Poland\n" 
]

question_data = [
    questions(questions_prompt[0], "d"),
    questions(questions_prompt[1], "d"),
    questions(questions_prompt[2], "b"),
    questions(questions_prompt[3], "b"),
]


def ask_question(questions_1):
    """
    this function is to ask the user the questions and when the user gets \n
    the correct answer the score will increase by 1
    """
    score = 0
    for question in questions_1:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got" " " + str(score) + "/" + str(len(questions_1)) + " " "correct")


ask_question(question_data)
