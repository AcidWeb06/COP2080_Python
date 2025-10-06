class Student:
    def __init__(self, name, student_id, major):
        self.__name = name
        self.__student_id = student_id
        self.__major = major

    def getName(self):
        return self.__name
    
    def getStudentID(self):
        return self.__student_id
    
    def getMajor(self):
        return self.__major

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__student_id}, Major: {self.__major}"
    
class underGraduateStudent(Student):
    def __init__(self, name, student_id, major, year):
        super().__init__(name, student_id, major)
        self.__year = year

    def __str__(self):
        return super().__str__() + f", Year: {self.__year}"
    
    def getName(self):
        return super().getName()
    
    def getStudentID(self):
        return super().getStudentID()
    
    def getMajor(self):
        return super().getMajor()
    
    def getYear(self):
        return self.__year
    
if __name__ == "__main__":
    student = Student("Alice", "U0120", "Computer Science")
    print(student)
    
    underGrad = underGraduateStudent("Michael", "U1222", "Physics", "Freshman")
    print(underGrad)
    print(student.getStudentID)

