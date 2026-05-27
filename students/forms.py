from django import forms

from .models import (
    Student,
    Batch,
    FeePackage
)


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = '__all__'

        widgets = {

            'admission_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'fee_start_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

        }


class BatchForm(forms.ModelForm):

    class Meta:

        model = Batch

        fields = '__all__'


class FeePackageForm(forms.ModelForm):

    class Meta:

        model = FeePackage

        fields = '__all__'