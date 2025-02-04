from django.urls import path 
from school import views

urlpatterns = [
    path('', views.school, name="school"),   # School Home Page
    
    path('students/', views.student_list, name='student_list'),   # Student List 
    path('students/add/', views.manage_student, name='add_student'),   # Add Student 
    path('students/update/<int:id>/', views.manage_student, name='update_student'),  # Update Student 
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),  # Delete Student 

    path('teachers/', views.teacher_list, name='teachers' ),   # Teachers List 
    path('teachers/manage/', views.manage_teacher, name='add_teacher'),  # Add teacher
    path('teachers/manage/<int:id>/', views.manage_teacher, name='edit_teacher'),  # Edit teacher
    path('teachers/delete/<int:id>/', views.delete_teacher, name='delete_teacher'),   # Delete teacher
    
    path('enrollments/', views.enrollment_list, name='enrollment_list'),  # Enrollment List
    path('enrollments/new/', views.enrollment_form_view, name='create_enrollment'),  # Create Enrollment 
    path('enrollments/edit/<int:enrollment_id>/', views.enrollment_form_view, name='edit_enrollment'),  # Edit Enrollment 
    path('student/<int:student_id>/enrollments/', views.student_enrollment_detail, name='student_enrollment_detail'), # Enrollment Detail 
    path('enrollment/delete/<int:id>/', views.delete_enrollment, name='delete_enrollment'),   # Delete Enrollment 

    path('add_class/', views.manage_class, name='manage_class'),  # Add Class
    path('edit_class/<int:id>', views.manage_class, name='edit_class'),  # Edit Class 
    path('class-list/', views.class_list, name='class_list'),  # Class List 
    path('delete-class/<int:id>', views.delete_class , name='delete_class'),  # Delete Class  

    path('students/grade/<str:grade_name>/', views.students_by_grade, name='view_students_by_grade'),  # Get students of specific class

    path('parents/', views.list_parents, name='parents'),  # List all Parents
    path('parents/add/', views.manage_parent, name='add_parent'),  # Add Parent
    path('parents/edit/<int:parent_id>/', views.manage_parent, name='edit_parent'),  # Edit Parent
    path('parents/delete/<int:id>/', views.delete_parent, name="delete_parent"),  # Delete Parent 
    path('school/', views.school, name="school"),   # School Home Page

    path('subjects/', views.subject_lst, name="subject"),   # subjects list 
    path('subjects/add-subjects/', views.manage_subject, name="add_subject"),   # Add Subject 
    path('subjects/update-subjects/<int:id>', views.manage_subject, name="update_subject"),  # Edit Subject
    path('subjects/delete-subject/<int:id>', views.delete_subject, name='delete_subject' ),  # Delete Subject
]

