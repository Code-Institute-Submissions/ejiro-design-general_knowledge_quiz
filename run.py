from question import questions

"""
creating an array of question prompt for the user
"""

questions_prompt = [
    "What is the capital of Finland?:\n  A. Tampere, B. Turku, C. Espoo, D. Helsinki \n",
    "How many elements are there in the periodic table?:\n A. 120 elements\n, B. 130 elements \n C. 112 elements\n, D. 118 elements",
    "What is the largest country in the world?:\n  A. United Kingdom \n, B. Russia \n, C. Canada \n, D. United State\n",
    "Where was the mojito cocktail created?:\n A. Brazil, B. Cuba, C. Coasta Rico, D. Poland\n" 
]

question_data = [
    questions(questions_prompt[3], "D"),
    questions(questions_prompt[3], "D"),
    questions(questions_prompt[1], "B"),
    questions(questions_prompt[1], "B"),
]