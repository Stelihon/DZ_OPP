class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for list_grades in self.grades.values():
                count += sum(list_grades) / len(list_grades)
            return round(count / len(self.grades), 1)
        else:
            return 'Оценоки отсутствуют'

    def __str__(self):
       return f'Имя: {self.name}\nФамилия: {self.surname} ' \
              f'\nСредняя оценка за домашнее задания: {self.average_grade()}' \
              f'\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {",".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Выбери студента'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.average_grade() < other.average_grade()
        return 'Оценок нет'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Выбери студента'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.average_grade() == other.average_grade()
        return 'Оценок нет'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_list.append(self)

    def average_grade(self):
        if len(self.grades) > 0:
            count = 0
            for list_grades in self.grades.values():
                count += sum(list_grades) / len(list_grades)
            return round(count / len(self.grades), 1)
        else:
            return 'Оценоки отсутствуют'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Выбери лектора'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.average_grade() < other.average_grade()
        return 'Оценок нет'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Выбери лектора'
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self.average_grade() == other.average_grade()
        return 'Оценок нет'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


students_list = []
lecturer_list = []


# Создаем студентов и учителей

harry = Student('Harry', 'Potter', 'male')
harry.finished_courses.append('Java')
harry.courses_in_progress.append('C++')
harry.courses_in_progress.append('Python')

hermione = Student('Hermione', 'Granger', 'female')
hermione.finished_courses.append('Python')
hermione.courses_in_progress.append('C++')
hermione.courses_in_progress.append('Java')

java_lecturer = Lecturer('Severus', 'Snape')
java_lecturer.courses_attached.append('Java')

python_c_lecturer = Lecturer('Minerva ', 'McGonagall')
python_c_lecturer.courses_attached.append('Python')
python_c_lecturer.courses_attached.append('C++')

python_c_reviewer = Reviewer('Dolores', 'Umbridge')
python_c_reviewer.courses_attached.append('Python')
python_c_reviewer.courses_attached.append('C++')

java_reviewer = Reviewer('Remus', 'Lupin')
java_reviewer.courses_attached.append('Java')


# Проверяющий(Java) ставит оценки Harry, но не чего не проставит т.к Java окончен, а дрругие он проставлять не может.
java_reviewer.rate_hw(harry, 'Java', 7)
java_reviewer.rate_hw(harry, 'C++', 5)
java_reviewer.rate_hw(harry, 'Python', 8)
java_reviewer.rate_hw(harry, 'Python', 8)
print(harry.grades)
print(harry, end='\n\n')

# Проверяющий(Python и C++) ставит оценки Harry.
python_c_reviewer.rate_hw(harry, 'C++', 7)
python_c_reviewer.rate_hw(harry, 'C++', 5)
python_c_reviewer.rate_hw(harry, 'Python', 8)
python_c_reviewer.rate_hw(harry, 'Python', 8)
print(harry.grades)
print(harry, end='\n\n')

# Проверяющий(Java) ставит оценки Hermione присвоит оценки только Java т.к другие ставить не может.
java_reviewer.rate_hw(hermione, 'Java', 8)
java_reviewer.rate_hw(hermione, 'Java', 9)
java_reviewer.rate_hw(hermione, 'C++', 7)
java_reviewer.rate_hw(hermione, 'Python', 5)
print(hermione.grades)
print(hermione, end='\n\n')

# Проверяющий(Python и C++) ставит оценки Hermione, но присвоит он оценки только за курсс C++  т.к Python окончен.
python_c_reviewer.rate_hw(hermione, 'C++', 8)
python_c_reviewer.rate_hw(hermione, 'C++', 7)
python_c_reviewer.rate_hw(hermione, 'Python', 9)
python_c_reviewer.rate_hw(hermione, 'Python', 3)
print(hermione.grades)
print(hermione, end='\n\n')

# Сравниваем Harry и Hermione
print('Harry учится хуже Hermione?', harry < hermione)
print('Hermione учится хуже Harry?', harry > hermione)
print('Hermione и Harry учатся одинаково?', harry > hermione, end='\n')

# Harry ставит ойценки лектору по Java, он не может ее поставить т.к. он закончил этот курс.
harry.rate_lecturer(java_lecturer, 'Java', 8)
print(java_lecturer, end='\n\n')

# Hermione ставит ойценки лектору по Java
hermione.rate_lecturer(java_lecturer, 'Java', 9)
hermione.rate_lecturer(java_lecturer, 'Java', 7)
hermione.rate_lecturer(java_lecturer, 'Java', 7)
print(java_lecturer, end='\n\n')

# Harry ставит ойценки лектору по Python.
harry.rate_lecturer(python_c_lecturer, 'Python', 7)
harry.rate_lecturer(python_c_lecturer, 'Python', 9)
harry.rate_lecturer(python_c_lecturer, 'Python', 9)
print(python_c_lecturer, end='\n\n')

# Hermione ставит ойценки лектору по Python, он не может ее поставить т.к. она закончила этот курс.
hermione.rate_lecturer(python_c_lecturer, 'Python', 8)
print(python_c_lecturer, end='\n\n')

# Harry ставит ойценки лектору по C++.
harry.rate_lecturer(python_c_lecturer, 'C++', 9)
harry.rate_lecturer(python_c_lecturer, 'C++', 6)
harry.rate_lecturer(python_c_lecturer, 'C++', 8)
print(python_c_lecturer, end='\n\n')

# Hermione ставит ойценки лектору по C++.
hermione.rate_lecturer(python_c_lecturer, 'C++', 9)
hermione.rate_lecturer(python_c_lecturer, 'C++', 7)
hermione.rate_lecturer(python_c_lecturer, 'C++', 9)
print(python_c_lecturer, end='\n\n')

# Сравниваем Лекторов
print('Java преподоют хуже чем C++ и Python', java_lecturer < python_c_lecturer)
print('Java преподоют так же как C++ и Python', java_lecturer == python_c_lecturer, end='\n\n')

# Функии по подсчету среднего бала на курсе
def average_lecturer_grade(lecturers, course_name):
    res = [i for i in lecturers if course_name in i.grades.keys()]
    count = 0
    for item in res:
        count += sum(item.grades[course_name]) / len(item.grades[course_name])
    print(f'Средняя оценка лектора по курсу {course_name}: {round(count / len(res), 1)}')

average_lecturer_grade(lecturer_list, 'C++')

def average_student_grade(students, course_name):
    res = [i for i in students if course_name in i.grades.keys()]
    count = 0
    for item in res:
        count += sum(item.grades[course_name]) / len(item.grades[course_name])
    print(f'Средняя оценка студента по курсу {course_name}: {round(count / len(res), 1)}')

average_student_grade(students_list, 'C++')