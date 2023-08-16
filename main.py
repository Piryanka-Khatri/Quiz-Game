from QuestionModel import Question
from Questions import question_data
from QuizLogic import QuizLogic
from Design import Interface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizLogic(question_bank)
quiz_design = Interface(quiz)
