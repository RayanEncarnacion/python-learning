from quizz_questions import questions 

class QuizzGame:
    score = 0;
    questions: list[dict] = [];
    
    def __init__(self, questions: list[dict]) -> None:
        self.questions = questions
        
    def print_questions_separator(self, index: int) -> None:
        print("\n" * (2 if index > 0 else 1))
        
    def get_answer(self, index: int, question: str) -> bool:
        return input(f"Q.{index} - {question}").strip().lower() == 'true'
    
    def process_aswer(self, answer: bool, correct_answer: bool) -> None: 
        if answer == correct_answer:
            self.score += 1 
            print("You got it right!")
        else:
            print("That's wrong.")
            
        print(f"The correct answer was: {correct_answer}")
        
    def print_score(self, answered_question: int) -> None:
        num_of_questions = len(self.questions)
        
        if answered_question < num_of_questions:
            print(f"Your current score is: {self.score}/{answered_question}.")
        else: 
            print(f"\nGame completed! Your final score is: {self.score}/{num_of_questions}")
    
    def start(self) -> None:
        for idx, question in enumerate(self.questions):
            self.print_questions_separator(idx)
            answer = self.get_answer(idx + 1, question["text"])
            self.process_aswer(answer, question["correct_answer"])
            self.print_score(idx + 1)
            
game = QuizzGame(questions)
game.start()