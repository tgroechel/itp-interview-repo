class Student:
    name = ""
    age = ""

    def __str__(self):
        return str(self.name)\
               + "\thas grade: " \
               + str(self.age)


brian = Student()
brian.name = "tim"
brian.age = 80

angela = Student()
angela.name = "angela"
angela.age = 90

people = [brian, angela]
people.sort(key = lambda x : x.name)

for student in people:
    print(student)