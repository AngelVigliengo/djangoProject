from django import forms
from django.forms.models import ModelForm

from .models import Student, Presence


class StudentForm(ModelForm):
    class Meta:
        model = Student

        fields = (
            "first_name",
            "birth_date",
            "email",
            "phone",
            "comments",
            "cursus",
            "last_name",
        )


class PresenceForm(ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.order_by('last_name'))

    class Meta:
        model = Presence

        fields = (
            'dateOfCall',
            "reason",
            "isMissing",
            'student',
        )
