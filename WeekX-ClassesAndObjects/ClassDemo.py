class Student:

    def __init__(self, name_in=None, grade_in=None):
        if name_in is None:
            name_in = ""
        if grade_in is None:
            grade_in = 0
        self.name = name_in
        self.grade = grade_in

    def change_student_grade_by_percent(self, percent_change):
        potential_grade = self.grade + percent_change
        if potential_grade < 0 or potential_grade > 100:
            print("Grade out of range, did not change")
        else:
            self.grade = potential_grade

    def __gt__(self, another_student):
        return self.grade > another_student.grade

    def __eq__(self, another_student):
        return self.grade == another_student.grade

    def __ge__(self, another_student):
        return self.__gt__(another_student) \
               or self.__eq__(another_student)

    def __str__(self):
        return str(self.name) \
               + "\thas grade: " \
               + str(self.grade)


brian = Student("Brian", 80)
angela = Student("Angela", 90)
colleen = Student("Colleen", 65)

print(brian <= angela)
brian.change_student_grade_by_percent(-10)
people = [brian, colleen, angela]
people.sort()

for student in people:
    print(student)

