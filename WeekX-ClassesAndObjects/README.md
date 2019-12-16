# WeekX: Classes and Objects
![](https://intellipaat.com/mediaFiles/2019/03/python10.png)

## Why do we need these?
```python
names = ["Gerald", "Denise", "Kai", "Lou"]
grades = [80, 90, 75, 90]

```
- What happens when I want to sort by name?

```python
names.sort()
```

## What is a class?
- **Wikipedia:** In object-oriented programming, a class is an extensible program-code-template for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods)
- **My translation:** A blueprint/template to create objects


## What is an object?
- **Wikipedia:** In Object-oriented programming, an object is an instance of a Class. Objects are an abstraction. They hold both data, and ways to manipulate the data
- **My translation:** The actual data structure made using the blueprint


## Live example (See `ClassDemo.py`)
- motivation
- build class
- make instance
- `__init__(self)` method
- `change_student_grade_by_percent(self, percentage)` method
- `__str(self)__` method

## Class Special Methods
### [Contructors](https://www.geeksforgeeks.org/constructors-in-python/)
```python
class Student:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

denise = Student("Denise", 90) 

# denise :
#	name = "Denise"
#	grade = 90
```


### [Make class "pretty-print"](https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print)
```python
class Student:
	def __init__(self, name_in, grade_in):
		self.name = name_in
		self.grade = grade_in

	def __str__(self):
		return str(self.name)\
               + " has grade: " \
               + str(self.grade)

denise = Student("Denise", 90) 
print(denise)

# Output:
# Denise has grade 90
```

### [Operator Overloading](https://www.geeksforgeeks.org/operator-overloading-in-python/)
```python
class Student:
	def __init__(self, name_in, grade_in):
		self.name = name_in
		self.grade = grade_in

	def __gt__(self, rhs_student):
		return self.grade > rhs_student.grade

denise = Student("Denise", 90)
gerald = Student("Gerald", 80)

print(denise > gerald)

# Output:
# True
```

## Try Yourself
`Card.py` has an outline of a card class. Implement each method below the each comment block. You can check this against the completed `class Card` from the `CODE FINISHED` commit.


## Extra References
- [W3 Schools](https://www.w3schools.com/python/python_classes.asp)
- [Youtube Intro to Classes and Objects Conceptually](https://www.youtube.com/watch?v=8yjkWGRlUmY)
- [Youtube Classes and Objects Python Intro](https://www.youtube.com/watch?v=wfcWRAxRVBA)
- [What is `self`?](https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/)
- [Sorting lists](https://www.afternerd.com/blog/python-sort-list/#sort-objects)
