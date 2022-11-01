from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random

question_bank = []


def populate_question_bank(data, num_questions=10):
    """
    Adds num_questions (default to 10) of questions to question_bank
    :param data: list of dict
    :param num_questions: int
    :return:
    """
    for i in range(num_questions):
        question = random.choice(data)
        q = Question(question["question"], question["correct_answer"], question["difficulty"])
        question_bank.append(q)


def quiz():
    populate_question_bank(question_data)
    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print("")
    print("You've finished the quiz!")
    print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")
    return


quiz()
