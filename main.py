from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []


def populate_question_bank(data):
    for question in data:
        q = Question(question["text"], question["answer"])
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
