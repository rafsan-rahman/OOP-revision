class Student:
    def __init__(self, name, gender, age, grade):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade

    def get_info(self):
        return self.name, self.gender, self.age

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, c_name, c_code, max_stu_enrolled):
        self.c_name = c_name
        self.c_code = c_code
        self.max_stu_enrolled = max_stu_enrolled
        self.stud_list = []
    
    def get_courseInfo(self):
        return self.c_name,self.c_code,self.max_stu_enrolled
    
    def add_student(self, student):
        if len(self.stud_list)<self.max_stu_enrolled:
            self.stud_list.append(student)
            
        return "max student limit reached"

    def get_avg_mark(self):
        tot_mark = 0 
        for stu in self.stud_list:
            tot_mark += stu.grade 
        return tot_mark/len(self.stud_list)


s1 = Student('Tim', 'M', 22, 88)
s2 = Student('Bill', 'M', 21, 74)
s3 = Student('Kiyara', 'F', 22, 60)

c1 = Course("Soft Computing", "CSE4203", 3)

c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

print(f"Average grage of the course {c1.c_code} is {c1.get_avg_mark()}" )

