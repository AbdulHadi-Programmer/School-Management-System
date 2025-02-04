from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Parent, Teacher, Subject, Student, Attendance, SchoolClass, Enrollment

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_list')  # List the name and the subjects
    
    # Custom method to display many-to-many related data (subjects in this case)
    def subject_list(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    subject_list.short_description = 'Subjects'

admin.site.register(Teacher, TeacherAdmin)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade', 'parent')
    filter_horizontal = ('subjects',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'days_present')

@admin.register(SchoolClass)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')

# @admin.register(Enrollment)
# class EnrollmentAdmin(admin.ModelAdmin):
#     list_display = ('student', 'subjects', 'date_enrolled')
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'subjects_list', 'date_enrolled')

    def subjects_list(self, obj):
        # Displaying a comma-separated list of subjects for each enrollment
        return ", ".join([subject.name for subject in obj.subjects.all()])
    subjects_list.short_description = 'Subjects'

admin.site.register(Enrollment, EnrollmentAdmin)
