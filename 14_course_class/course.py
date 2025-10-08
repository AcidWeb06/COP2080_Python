class Course:
    def __init__(self, courseName, studentList):
        self.__courseName = courseName
        self.__studentList = studentList
    
    def addStudent(self, student):
        if student not in self.__studentList:
            self.__studentList.append(student)
        else:
            print("That student is already present.")

    def getCourseName(self):
        return self.__courseName
    
    def getStudents(self):
        return self.__studentList
    
    def getNumberOfStudents(self):
        return len(self.__studentList)

    def dropStudent(self, student):
        if student in self.__studentList:
            self.__studentList.remove(student)
        else:
            print("That student is not enrolled in this course")

    def __str__(self):
        return f"Course Name: {self.getCourseName()}, List of Students: {self.__studentList}"

students = ["Andrew", "John", "Maggie", "Max"]
pythonCourse = Course("Computation Solving in Python", students)
pythonCourse.addStudent("Evan")
pythonCourse.addStudent("John")
print(pythonCourse)
        
     

class InPersonCourse(Course):
    def __init__(self, courseName, studentList, roomNumber, schedule, max_seats):
        super().__init__(courseName, studentList)
        self.__roomNumber = roomNumber
        self.__schedule = schedule
        self.__max_seats = max_seats

    def addStudent(self, student):
        if len(self.__studentList) < self.__max_seats:
            return super().addStudent(student)
        else:
            print("The class is full")

    def __str__(self):
        return super().__str__() + f", Room Number: {self.__roomNumber}, Schedule: {self.__schedule}, Max Seats: {self.__max_seats}"
    
chemistry = InPersonCourse("Chemistry 1", students, "IST-1067", "MWF 12 P.M. - 12:50 P.M.", "27")
print(chemistry)