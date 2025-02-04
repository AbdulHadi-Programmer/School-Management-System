# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, SchoolClass, Attendance, Enrollment, Teacher, Parent
from .forms import StudentForm, TeacherForm, EnrollmentForm, AttendanceForm, SchoolClassForm, ParentForm, SubjectForm


# Create 
# def add_student(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST)      # take the student form in this variable by post method 
#         if form.is_valid():       # check form is valid or not 
#             form.save()           # save the form   
#             return redirect('student_list')       # now if form is successful then redirect to the list page

#     else:
#         form = StudentForm()
#     return render(request, 'add_student.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
# ********************************************************************************************************************
def manage_teacher(request, id=None):
    teacher = None
    if id:
        teacher = get_object_or_404(Teacher, id= id)  # Fetch the teacher for editing

    if request.method == 'POST':
        teachers = Teacher.objects.prefetch_related('subjects')
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')  # Redirect to the teacher list
    else:
        form = TeacherForm(instance=teacher)  # Pass the teacher instance for editing or None for adding

    return render(request, 'manage_teacher.html', {
        'form': form,
        'teacher': teacher,  # Pass teacher to distinguish between add/edit
        # 'teachers': teachers, 
    })

def manage_student(request, id=None):
    student = None 
    if id:
        student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'manage_student.html', {'form': form, 'student': student})


# Delete

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')  # Redirect to a student list page or some other page

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ===================================================================================================================================================================
# Teacher CRUD :
# ===================================================================================================================================================================
from django.shortcuts import render
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()  # Query all teachers from the database
    teachers = Teacher.objects.prefetch_related('subjects')
    return render(request, 'teachers.html', {'teachers': teachers}) #, 'teachers1': teachers1})

# Create and Update Teacher:
def manage_teacher(request, id=None):
    teacher = None
    if id:
        teacher = get_object_or_404(Teacher, id= id)  # Fetch the teacher for editing

    if request.method == 'POST':
        teachers = Teacher.objects.prefetch_related('subjects')
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')  # Redirect to the teacher list
    else:
        form = TeacherForm(instance=teacher)  # Pass the teacher instance for editing or None for adding

    return render(request, 'manage_teacher.html', {
        'form': form,
        'teacher': teacher,  # Pass teacher to distinguish between add/edit
        # 'teachers': teachers, 
    })


def delete_teacher(request, id):
    if request.method == "GET":
        teacher = get_object_or_404(Teacher, id= id)
        teacher.delete()
        return redirect('teachers')  # Redirect to the teacher list or desired page
    else:
        return redirect('teachers')  # Or return some other response


# ===================================================================================================================================================================


#------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import SchoolClassForm

# def manage_class(request, id=None):
#     # Fetch the existing object if 'id' is provided, else create a new one.
#     claas = get_object_or_404(Student, id=id) if id else None

#     if request.method == "POST":
#         # If the form is submitted, bind data to the form (with or without an instance).
#         form = SchoolClassForm(request.POST, instance=claas)
#         if form.is_valid():
#             form.save()
#             return redirect('class_list')  # Adjust the redirect URL as needed.
#     else:
#         # Render a form bound to the instance if it exists, or an empty form otherwise.
#         form = SchoolClassForm(instance=claas)

#     return render(request, 'manage_class.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import SchoolClass
from .forms import SchoolClassForm

def manage_class(request, id=None):
    claas = get_object_or_404(SchoolClass, id=id) if id else None

    if request.method == "POST":
        form = SchoolClassForm(request.POST, instance=claas)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = SchoolClassForm(instance=claas)

    return render(request, 'manage_class.html', {
        'form': form,
        'action': 'Edit' if claas else 'Add',
    })


def class_list(request):
    classes = SchoolClass.objects.all()
    return render(request, 'all_class.html', context = {'classes': classes})

def students_by_grade(request, grade_name):
    students = Student.objects.filter(grade=grade_name)  # Ensure grade_name is passed correctly
    return render(request, 'students_by_grade.html', {'grade_name': grade_name, 'students': students})


def delete_class(request, id):
    classs= get_object_or_404(SchoolClass, id=id)
    classs.delete()
    return render(request, 'all_class.html' )
    


# ==========================================================================================================================================================
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment
from .forms import EnrollmentForm
##########################################################################################################################################################
# Create and Update in one view
def enrollment_form_view(request, enrollment_id=None):
    if enrollment_id:  # If ID is provided, fetch the instance (EDIT mode)
        enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
    else:  # If no ID, create a new instance (ADD mode)
        enrollment = None

    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'add_enrollment.html', {'form': form, 'enrollment': enrollment})

## Understand this concepts: 
from django.shortcuts import render, get_object_or_404
from .models import Enrollment, Student

def student_enrollment_detail(request, student_id):
    # subject = Subject.objects.get(id=id)
    student = Student.objects.get(id=student_id)
    enrollments = Enrollment.objects.filter(student=student)

    # Collect subjects as a comma-separated string for each enrollment
    enrollment_details = [
        {
            "student": enrollment.student.name,
            "subjects": ", ".join(subject.name for subject in enrollment.subjects.all()) or "-",
            "date_enrolled": enrollment.date_enrolled.strftime("%b. %d, %Y"),
        }
        for enrollment in enrollments
    ]

    context = {
        'student': student,
        'enrollment_details': enrollment_details,
    }

    return render(request, 'student_enrollment_detail.html', context)


# List Enrollment View (shows all enrollments)

def enrollment_list(request):
    # Fetch all enrollments
    enrollments = Enrollment.objects.all()
    context = {
        'enrollments': enrollments
    }
    return render(request, 'enrollment_list.html', context)


def delete_enrollment(request, id):
    enr = Enrollment.objects.get(id=id)
    enr.delete()
    return redirect('enrollment_list')
# -------------------------------------------------------------------------------------------------------------
# Parent CRUD : 
# Create and Update Parent:
from django.shortcuts import render, redirect, get_object_or_404
from .models import Parent
from .forms import ParentForm

# View to list all parents
def list_parents(request):
    parents = Parent.objects.all()
    return render(request, 'parents.html', {'parents': parents})


# View to handle adding and editing parents
def manage_parent(request, parent_id=None):
    parent = None
    if parent_id:
        parent = get_object_or_404(Parent, id=parent_id)  # Get the parent if editing

    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('parents')  # Redirect to the list page
    else:
        form = ParentForm(instance=parent)

    return render(request, 'manage_parent.html', {'form': form, 'parent': parent})

def delete_parent(request, id):
    parent = Parent.objects.get(id=id)
    parent.delete()
    return redirect('parents')

def school(request):
    return render(request, "school.html")

# -------------------------------------------------------------------------------------------------------------------------------

def subject_lst(request):
    subject = Subject.objects.all()
    return render(request, "subjects.html", {'subject': subject})

def delete_subject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    return redirect('subject')



from .models import Subject

def manage_subject(request, id=None):
    if id:
        subject = get_object_or_404(Subject, pk=id)
        form = SubjectForm(request.POST or None, instance=subject)
    else:
        form = SubjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('subject')  # Replace with the appropriate redirect.

    return render(request, 'manage_subject.html', {'form': form, 'subject': subject if id else None})


# -------------------------------------------------------------------------------------------------------------------------------
# Attendence Crud: 
def attendance_lst(request):
    attendence = Attendance.objects.all()
    return render(request, {'attendence': attendence})

def manage_attendence(request, id):
    attendence = None
    if id:
        attendence = get_object_or_404(Attendance, id=id)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendence)
        if form.is_valid():
            form.save()
            return redirect('attendence')
        else:
            form = AttendanceForm(instance=attendence)
    return render(request, 'attendence_lst.html')

# ---------------------------------------------------------------------------------------------------------------------------------
