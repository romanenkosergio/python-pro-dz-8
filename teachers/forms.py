import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, DateInput

from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        # Validate first_name length
        if len(first_name) < 2:
            raise ValidationError("First name should be at least 2 characters long.")
        # Validate first_name contains only letters
        if not re.match(r'^[a-zA-Z]*$', first_name):
            raise ValidationError("First name should only contain letters.")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        # Validate last_name length
        if len(last_name) < 2:
            raise ValidationError("Last name should be at least 2 characters long.")
        # Validate last_name contains only letters
        if not re.match(r'^[a-zA-Z]*$', last_name):
            raise ValidationError("Last name should only contain letters.")

        return last_name
