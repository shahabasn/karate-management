from django import forms

from .models import (
    Student,
    Batch
)


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = '__all__'


class BatchForm(forms.ModelForm):

    class Meta:

        model = Batch

        fields = '__all__'