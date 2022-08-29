"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score <= other.average_score

    def __gt__(self, other):
        return self.average_score >= other.average_score

    def __le__(self, other):
        return self.average_score < other.average_score

    def __ge__(self, other):
        return self.average_score > other.average_score

    def sort_by_score(self, students_list: list):
        if self.average_score > 5:
            return sorted(students_list)


student1 = Student("Targaryen", "Daenerys", 27, 8.8),
student2 = Student("Snow", "Jon", 27, 3.7),
student3 = Student("Stark", "Arya", 27, 5.1),
student4 = Student("Stark", "Sansa", 27, 6.2),
student5 = Student("Clegane", "Sandor", 27, 2.2)

students = list()
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)
