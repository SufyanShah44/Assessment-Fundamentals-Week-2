from datetime import date

class Trainee():
    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments
        assessments = []
    
    def get_age(self) -> int:
        if date.now().month > self.date_of_birth.month():
            return (date.now().year() - self.date_of_birth.year()) + 1
        return date.now().year() - self.date_of_birth.year()
    
class Assessment:
    def __init__(self):
        pass
    








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
