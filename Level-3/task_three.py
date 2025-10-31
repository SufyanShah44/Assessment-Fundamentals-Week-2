'''Here the Trainee, Assessment, Quiz, Marking and Question Classes are initialised'''
from datetime import date

class Trainee():
    '''Trainee Class'''
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        '''Returns the age of the trainee in years'''
        if date.today().month > self.date_of_birth.month:
            return date.today().year - self.date_of_birth.year + 1
        return date.today().year - self.date_of_birth.year

    def add_assessment(self, assessment: Assessment) -> None:
        '''Adds the assessment to our assessment list'''
        if not isinstance(assessment, Assessment):
            raise TypeError("Please enter a valid assessment class!")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment:
        ''' Returns assessments class if found in list'''
        for assessments in self.assessments:
            if assessments.name == name:
                return assessments

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        '''Returns if assessments based on provided type of assessment'''
        assessments_list = []
        for assessments in self.assessments:
            if type == assessments.type:
                assessments_list.append(assessments)
        return assessments_list


class Assessment:
    '''Assessment Class'''
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score

        type_options = ["multiple-choice", "technical",  "presentation"]
        if type not in type_options:
            raise ValueError("That isn't a valid assessment type!")
        if score > 100:
            raise ValueError("Score needs to be 100 or less!")
        if score < 0:
            raise ValueError("Score needs to be less than zero!")


class MultipleChoiceAssessment(Assessment):
    '''Creates Multiple Choice class that inherits assessment'''
    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self):
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    '''Creates Techinial class that inherits assessment'''
    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self):
        return self.score


class PresentationAssessment(Assessment):
    '''Creates Presentation class that inherits assessment'''
    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        return self.score * 0.6


class Question:
    '''Question class for creating questions and answers'''
    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    '''Quiz class for generating quiz'''
    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    '''Marking Class handles the marking'''
    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        '''Mark method used to check if answers are correct and gives scores'''
        total_score = 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                total_score += 1

        calculated_percentage = (total_score/len(self._quiz.questions)) * 100
        return int(calculated_percentage)


    def generate_assessment(self) -> Assessment:
        '''Returns instance of assessment'''
        score = self.mark()

        if self._quiz.type.lower() == "multiple-choice":
            return MultipleChoiceAssessment(self._quiz.name, score)
        elif self._quiz.type.lower() == "technical":
            return TechnicalAssessment(self._quiz.name, score)
        else:
            return Assessment(self._quiz.name, score)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
