class User:
    def access_dashboard(self):
        print("Accessing user dashboard")

class Student(User):
    def access_dashboard(self):
        print("Accessing student dashboard")

class Instructor(User):
    def access_dashboard(self):
        print("Accessing instructor dashboard")

class TeachingAssistant(Student, Instructor):
    pass

teaching_assistant = TeachingAssistant()
teaching_assistant.access_dashboard() 
print(TeachingAssistant.__mro__)  
