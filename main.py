class UniversityManagementSystem:
    
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = {
                "name": name,
                "courses": []
            }
            print(f"Student {name} added successfully.")
    
    def add_course(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        
        if course_id in self.courses:
            print("Course ID already exists.")
        else:
            self.courses[course_id] = course_name
            print(f"Course {course_name} added successfully.")
    
    def enroll_student(self):
        student_id = input("Enter student ID to enroll: ")
        
        if student_id not in self.students:
            print("Student ID does not exist.")
            return
        course_id = input("Enter course ID to enroll in: ") 
                 
        if course_id not in self.courses:
            print("Course ID does not exist.")
            return
                
        if course_id not in self.students[student_id]['courses']:
            self.students[student_id]['courses'].append(course_id)
            print(f"Student enrolled in {self.courses[course_id]}.")
        else:
            print("Student already enrolled in this course.")
    
    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student_id, student_info in self.students.items():
                courses = ', '.join(self.courses[course_id] for course_id in student_info['courses'])
                print(f"ID: {student_id}, Name: {student_info['name']}, Courses: {courses}")
    
    def display_courses(self):
        if not self.courses:
            print("No courses available.")     
        else:
            for course_id, course_name in self.courses.items():
                print(f"ID: {course_id}, Name: {course_name}")
            
def main():
    ums = UniversityManagementSystem()
    while True:
        print("\nUniversity Management System")
        print("1. Add Student") 
        print("2. Add Course")
        print("3. Enroll Student")
        print("4. Display Students")
        print("5. Display Courses")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            ums.add_student()
        elif choice == "2":
            ums.add_course()
        elif choice == "3": 
            ums.enroll_student()
        elif choice == "4":
            ums.display_students()
        elif choice == "5":
            ums.display_courses()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
         