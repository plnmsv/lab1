#coding:utf-8
groupmates = [
    {
    "name": u"Петр",
    "group": u"БВТ1702",
    "age": 20,
    "marks": [4, 5, 5, 4]
    },
{
    "name": u"Леонид",
    "group": u"БВТ1702",
    "age": 23,
    "marks": [4, 4, 3, 4]
    },
{
    "name": u"Ольга",
    "group": u"БВТ1701",
    "age": 19,
    "marks": [5, 5, 5, 5]
    },
{
    "name": u"Алексей",
    "group": u"БВТ1702",
    "age": 20,
    "marks": [3, 3, 4, 3]
    }
]
def print_students(students):
 print u"Имя студента".ljust(15), \
       u"Группа".ljust(8), \
       u"Возраст".ljust(8), \
       u"Оценки".ljust(20)
 for student in students:
    print \
        student["name"].ljust(15), \
        student["group"].ljust(8), \
        str(student["age"]).ljust(8), \
        str(student["marks"]).ljust(20)
    print "\n"
print_students(groupmates)

def print_students_v2(students):
 print u"Имя студента", \
       u"Группа", \
       u"Возраст" \
       u"Оценки"
 for student in students:
    print \
        student["name"], \
        student["group"], \
        str(student["age"]), \
        str(student["marks"])
    print "\n"
print_students_v2(groupmates)

print(u"Введите средний балл для сортировки:")
mid_mark=input()
good_students=[]
def mid_mark_sort(students, n):
    for students in students:
        if (sum(students["marks"]) / len(students["marks"])) > n:
            good_students.append(students)
mid_mark_sort(groupmates,mid_mark)
print_students(good_students)
