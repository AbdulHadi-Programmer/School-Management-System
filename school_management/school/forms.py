from django import forms
from .models import Student, Attendance, SchoolClass, Enrollment, Teacher, Subject, Parent

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name', 'age', 'grade', 'parent', 'subjects']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'age': forms.NumberInput(attrs={'class': 'age'}),
            'grade': forms.TextInput(attrs={'class': 'grade'}),
            'parent': forms.Select(attrs={'class': 'parent'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': 'subjects'}),
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'days_present'] 
        widgets = {
            'student': forms.Select(attrs={'class': 'student'}),
            'days_present': forms.NumberInput(attrs={'class': 'days'})
        }


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'subjects', 'date_enrolled']
        widgets = {
            'student': forms.Select(attrs={'class': 'student_name_r'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': 'subject_r'}),
            'date_enrolled': forms.DateInput(attrs={'class': 'date', 'type': 'date'}), 
        }

# **************************************************************************************************************************************
class SchoolClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ['name', 'teacher']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),  
            'teacher': forms.Select(attrs={'class': 'teacher'}), 
        }

    
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subjects', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent 
        fields = ['name', 'phone', 'email']
        widgets= {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model =  Subject
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    # subjects = forms.ModelMultipleChoiceField(
    #     queryset=Student.objects.all(),
    #     widgets= forms.CheckboxSelectMultiple, 
    #     required=False 
    # )
    # class Meta:
    #     model = Subject 
    #     fields = ['name']
