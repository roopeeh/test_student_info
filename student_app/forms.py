from django import forms
from django.forms import fields
from .models import StudentInfo, StudentAcademics


class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = ['Name', 'Class', 'School', 'mobile', 'Address']


class UpdateAccadamicsForm(forms.ModelForm):

    class Meta:
        model = StudentAcademics
        fields = ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
