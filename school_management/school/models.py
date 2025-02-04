from django.db import models

# Create your models here.

# The Parent: Every student had a parent who cared for them. Each Parent had a name, phone number, and email 
# address to communicate with the school whenever needed.
class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

## Teacher Model:
#- 1-Many : Schools has  many Teachers
#- 


# # Subject Model:
# The Subject: A Subject was any topic taught in the school, like Math, Science, History, etc. Each subject had
# a name, and teachers could be assigned to multiple subjects, teaching the same subject to different groups of 
# students.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# The Teacher: The school had many Teachers who taught different Subjects. Each teacher had a name and an email  
# to contact them. They were also responsible for the subjects they taught, and some teachers taught more than  
# one subject.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
    email = models.EmailField()
    def __str__(self):
        return self.name


# # Student Model  -------------------
# The Student: The heart of the school were the Students. Each student had a name, age, and grade. They also had a Parent linked to them (for communication purposes), and they were enrolled in multiple subjects. Each student could have many subjects, and these subjects helped them learn.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

# Attendance Model (One-to-One Relationship)
# Attendance: To keep track of how often each student attended school, the school kept a record of Attendance. 
# For each student, there was a one-to-one relationship between the student and their attendance record. The 
# number of days a student was present was recorded here.
class Attendance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    days_present = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.name} - Days Present: {self.days_present}"


# Class Model (One-to-Many Relationship)
# Classes: Each Class represented a group of students taught by a specific teacher. Each class had a Teacher, and 
# many students could be enrolled in that class. The teacher taught them the subjects, and the class helped 
# organize their learning experience.
class SchoolClass(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


# Enrollment Model (Many-to-Many Relationship)
# Enrollment: Students didn’t just learn randomly; they were Enrolled in subjects. Each Enrollment captured which 
# student was enrolled in which subject, and the date they began their enrollment. This many-to-many relationship 
# helped track all the subjects each student was involved with and when they started.
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)  # Many-to-many relationship for multiple subjects
    date_enrolled = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {', '.join([subject.name for subject in self.subjects.all()])}"


# How It All Works Together
# The Parents are associated with Students, providing necessary contact information.
# Teachers teach Subjects and manage their respective Classes. A teacher could teach multiple subjects.
# Students have a grade, and they are enrolled in multiple subjects. Their attendance is tracked individually.
# The Attendance model ensures that each student's presence is accurately recorded.
# The Enrollment model tracks when a student first enrolled in a subject, creating a relationship between the student and their academic journey.

