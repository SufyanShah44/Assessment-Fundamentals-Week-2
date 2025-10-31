'''Here the Trainee and Assessment Class are initialised'''
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
    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self):
        return self.score * 0.7

class TechnicalAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)

    def calculate_score(self):
        return self.score

class PresentationAssessment(Assessment):
    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        return (self.score * 0.6)


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
