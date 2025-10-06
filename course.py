class Course:
    """
        course_name (private)
        list of students (private)
        
        addStudent(self, student) shouldn't enroll the same student twice
        
        getCourseName
        
        getStudents
        
        getNumberOfStudents
        
        dropStudent(self, student) Should provide a message with a dropped student name
        Should check does the student enroll in the couse (print message)
        
        __str__ info about the course and list of students
        
    """
    pass

class InPersonCourse(Course):
    """
        private (room_number)
        schedule(MWF 11 A.M. - 11:50 A.M)
        private max_seats
        
        Override addStudent method(check are there available seats) print appropriate message

        Override __str__

    """