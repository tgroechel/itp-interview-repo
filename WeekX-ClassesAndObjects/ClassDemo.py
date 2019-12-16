class Card:
    def __init__(self, suit_in, value_in):
        self.suit = suit_in
        self.value = value_in

    def get_val(self):
        if self.value == "JACK":
            return 11
        elif self.value == "QUEEN":
            return 12
        elif self.value == "KING":
            return 13
        elif self.value == "ACE":
            return 14
        return int(self.value)

    def get_suit_color(self):
        if self.suit == "SPADES" or self.suit == "CLUBS":
            return "BLACK"
        else:
            return "RED"

    def __gt__(self, other):
        return self.get_val() > other.get_val()

    def __str__(self):
        return self.suit + " " + self.value


class Student:

    def __init__(self, name_in=None, grade_in=None):
        if name_in is None:
            name_in = ""
        if grade_in is None:
            grade_in = 0
        self.name = name_in
        self.grade = grade_in

    @classmethod
    def with_name(cls, name_in):
        return cls(name_in=name_in)

    @classmethod
    def with_grade(cls, grade_in):
        return cls(grade_in=grade_in)

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
potato = Student()
potato = Student.with_grade(80)

print(potato < brian)
print(brian <= angela)

brian.change_student_grade_by_percent(-10)

people = [brian, colleen, angela]
people.sort()

for student in people:
    print(student)
mixedList = ["tom", 4]
print(mixedList)
