class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code
        
    def get_address(self):
        return f"Address: {self.street}, {self.city}, {self.zip_code}"

class Course:
    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration
        self.fee = fee
        
    def get_course_details(self):
        return f"Course: {self.name}, Duration: {self.duration}, Fee: {self.fee}"

class Employee(Person):
    def __init__(self, name, age, email, employee_id):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        
class Trainer(Employee):
    def assign_course(self, course):
        return f"{self.name} is assigned to teach {course.name}"

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        
    def enroll_student(self):
        return f"{self.student.name} enrolled in {self.course.name}"

# Usage Example
person1 = Person("Alice", 30, "alice@example.com")
address1 = Address("123 Street", "City", "12345")
course1 = Course("Python Programming", "8 weeks", "$200")
employee1 = Employee("Bob", 35, "bob@example.com", "EMP001")
trainer1 = Trainer("Charlie", 25, "charlie@example.com", "TRN001")
enrollment1 = Enrollment(person1, course1)

print(person1.get_details())
print(address1.get_address())
print(course1.get_course_details())
print(trainer1.assign_course(course1))
print(enrollment1.enroll_student()
