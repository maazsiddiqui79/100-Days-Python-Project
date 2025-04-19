class Question_Brain:
    score = 0
    
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        
    def still_has_question(self):
        return self.question_number < len(self.question_list )
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_ans = input(f"\nQ.{self.question_number} {current_question.text} (True/False):")
        
        self.check_ans(user_ans,current_question.ans)
        
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score +=1
            print("You Got It Right!")
            print(f"the correct answer was:".title(),correct_ans)
            if self.question_number != len(self.question_list):
                print(f"Your Current Score is: {self.score}/{self.question_number}")
            
           
        else:
            print("Close, but not correct!")
            print(f"the correct answer was:".title(),correct_ans)
            
            if self.question_number != len(self.question_list):
                print(f"Your Current Score is: {self.score}/{self.question_number}")
            
           