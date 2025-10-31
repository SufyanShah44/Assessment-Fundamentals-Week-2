from datetime import date

class Trainee():
    '''Trainee Class that '''
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
    
    
class Assessment:
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score

    


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
