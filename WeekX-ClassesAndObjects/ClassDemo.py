class Student:
    def __init__(self, name_in, grade_in):
        self.name = name_in
        self.grade = grade_in

    def change_student_grade_by_percent(self, percent_change):
        potential_grade = self.grade + percent_change
        if potential_grade < 0 or potential_grade > 100:
            print("Grade out of range, did not change")
        else:
            self.grade = potential_grade

    def __str__(self):
        return str(self.name)\
               + "\thas grade: " \
               + str(self.grade)


brian = Student("Brian", 80)
angela = Student("Angela", 90)

brian.change_student_grade_by_percent(-10)



people = [brian, angela]
people.sort(key = lambda x : x.name)

for student in people:
    print(student)