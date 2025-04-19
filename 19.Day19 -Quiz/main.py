from question_model import Question
from data import question_data
from quiz_brain import Question_Brain


qb = []
for i in question_data:
    question_text = i ["text"]
    question_ans = i ["answer"]
    new_question = Question(question_text,question_ans)
    qb.append(new_question)
    


q = Question_Brain(qb)
while q.still_has_question():
    
    q.next_question()

if q.question_number == len(q.question_list):
    print(f"you have completed the quiz".center(90,"-").title())
    print(f"Fianl score {q.score}".center(90,"-").title())

    