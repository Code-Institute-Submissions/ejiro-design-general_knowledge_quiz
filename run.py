class questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
"""
creating an array of question prompt for the user
"""

questions_prompt = [
    "What is the capital of Finland? \n (a) Tampere\n (b) Turku\n (c) Espoo\n (d) Helsinki\n",
    "How many elements are there in the periodic table?:\n (a) 120 elements\n (b) 130 elements\n (c) 112 elements\n (d) 118 elements\n",
    "What is the largest country in the world?:\n (a) United Kingdom\n (b) Russia\n (c) Canada\n (d) United State\n",
    "Where was the mojito cocktail created?:\n (a) Brazil\n (b) Cuba\n (c) Coasta Rico\n (d) Poland\n" 

"""
I created a 4 question prompt to store the correct answers to the question
"""

question = [
    questions(questions_prompt[0], "d"),
    questions(questions_prompt[1], "d"),
    questions(questions_prompt[2], "b"),
    questions(questions_prompt[3], "b"),
]

def question_list(questions):
"""
create a function that contains a for loop 
that loops through the questions list and accepts a list as a parameter.
"""
    for question in questions:
        answer = input(question.prompt)

def __validate_answer__():
        valid_choice = ("a", "b", "c", "d")

def Check_answer(answer):
    score += 0
    if __validate_answer__ == answer:
        score += 1
        print("correct answer")
    else: 
        print("incorrect answer")
    print("You got" + str(score) + "correct out of" + str(len(questions)))

question_list(question)