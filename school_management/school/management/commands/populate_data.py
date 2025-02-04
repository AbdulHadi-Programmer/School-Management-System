import random
from faker import Faker
from django.core.management.base import BaseCommand
from school.models import Parent, Teacher, Subject, Student, Attendance, SchoolClass, Enrollment

fake = Faker()

class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        self.populate_parents(20)
        subjects = self.populate_subjects(10)
        teachers = self.populate_teachers(10, subjects)
        students = self.populate_students(50)
        self.populate_attendance(students)
        self.populate_school_classes(5, teachers, students)
        self.populate_enrollments(students, subjects)

    def populate_parents(self, count):
        print(f"Creating {count} parents...")
        for _ in range(count):
            Parent.objects.create(
                name=fake.name(),
                phone=fake.phone_number(),
                email=fake.email()
            )

    def populate_subjects(self, count):
        print(f"Creating {count} subjects...")
        subjects = []
        for _ in range(count):
            subjects.append(
                Subject.objects.create(name=fake.word().capitalize())
            )
        return subjects

    def populate_teachers(self, count, subjects):
        print(f"Creating {count} teachers...")
        teachers = []
        for _ in range(count):
            teacher = Teacher.objects.create(
                name=fake.name(),
                email=fake.email()
            )
            teacher.subjects.set(random.sample(subjects, k=random.randint(1, 3)))
            teachers.append(teacher)
        return teachers

    def populate_students(self, count):
        print(f"Creating {count} students...")
        parents = list(Parent.objects.all())
        students = []
        for _ in range(count):
            student = Student.objects.create(
                name=fake.name(),
                age=random.randint(5, 18),
                grade=f"Grade {random.randint(1, 12)}",
                parent=random.choice(parents),
            )
            student.subjects.set(Subject.objects.order_by("?")[:random.randint(2, 5)])
            students.append(student)
        return students

    def populate_attendance(self, students):
        print(f"Creating attendance for {len(students)} students...")
        for student in students:
            Attendance.objects.create(
                student=student,
                days_present=random.randint(50, 200)
            )

    def populate_school_classes(self, count, teachers, students):
        print(f"Creating {count} school classes...")
        for _ in range(count):
            teacher = random.choice(teachers)
            school_class = SchoolClass.objects.create(
                name=fake.word().capitalize(),
                teacher=teacher
            )
            class_students = random.sample(students, k=random.randint(10, 20))
            for student in class_students:
                student.subjects.add(*teacher.subjects.all())

    def populate_enrollments(self, students, subjects):
        print("Creating enrollments...")
        for student in students:
            enrollment = Enrollment.objects.create(
                student=student,
                date_enrolled=fake.date_between(start_date='-2y', end_date='today')
            )
            enrollment.subjects.set(random.sample(subjects, k=random.randint(1, 3)))
