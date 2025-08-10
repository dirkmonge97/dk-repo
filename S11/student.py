class Student:
    def __init__(self, name, section, spanish_grade, english_grade, social_grade, science_grade, grade_average):
        self.name=name
        self.section=section
        self.spanish_grade=spanish_grade
        self.english_grade=english_grade
        self.social_grade=social_grade
        self.science_grade=science_grade
        self.grade_average=grade_average
    def __str__(self):
        return (f"{self.name} | Section: {self.section} | Spanish: {self.spanish_grade} | English: {self.english_grade} | Social Studies: {self.social_grade} | Science: {self.science_grade} | Average: {self.grade_average:.2f}")
    def to_dict(self):
        return {
            "Name": self.name,
            "Section":self.section,
            "Spanish": self.spanish_grade,
            "English": self.english_grade,
            "Social Studies": self.social_grade,
            "Science":self.science_grade,
            "Average":self.grade_average
        }