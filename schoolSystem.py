class Person:
    def __init__(self, name, tel_no):
        self.name = name
        self.tel_no = tel_no

    def show_info(self):
        print(f"Name: {self.name},  TelNo: {self.tel_no}")
        
class Student(Person): 
    def __init__(self, name, tel_no, reg_no, course):
        super().__init__(name, tel_no)
        self.reg_no = reg_no
        self.course = course
        self.registered = False
        self.tution_paid = 0.0
        
    def register(self):
        if not self.registered:
            self.registered = True
            print(f"{self.name} has been registered for {self.course}")
        else:
            print(f"{self.name} is already registered") 
            
    def pay_tution(self,ammount):
        if self.registered:
            self.tution_paid +=ammount
            print(f"{self.name} has paid ugx {ammount}. Total paid ugx: {self.tution_paid}") 
        else:
            print(f"{self.name} must register before paying tution")     
                     
    def show_info(self):
        status = "Registered" if self.registered else "Not Registered"
        print(f"Name: {self.name},regNo: {self.reg_no}, course: {self.course}")
        print(f"status:{status},tution paid ugx {self.tution_paid}")
        
        
class Lecturer(Person):
    def __init__(self, name, tel_no,staff_id,department):
        super().__init__(name, tel_no) 
        self.staff_id = staff_id
        self.department = department
        
    def attend_class(self,course):
               print(f"Lecturer {self.name} is attending and teaching the {course} class.")
    def show_info(self):
            print(f"Lecturer: {self.name}, Staff ID: {self.staff_id}, Department: {self.department}, TelNo: {self.tel_no}")
        
        
student1 = Student("Alice", "0756952", "S1001", "Computer Science")
lecturer1 = Lecturer("Dr. John", "0777633", "L2001", "Engineering")


print("\n-- student info--")
student1.show_info()
student1.pay_tution(50000)
student1.register()
student1.pay_tution(50000)
student1.show_info()

print("\n-- lecturer info--")
lecturer1.show_info()
lecturer1.attend_class("BIST")