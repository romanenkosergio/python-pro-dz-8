import re

import phonenumbers
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Student


class StudentForm(ModelForm):
    """Student form."""

    class Meta:
        model = Student
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

    def clean_phone(self):
        country_code = self.cleaned_data.get('country_code')
        phone = self.cleaned_data['phone']
        # Validate phone number
        try:
            parsed_number = phonenumbers.parse(phone, country_code)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError("Invalid phone number.")
        except phonenumbers.NumberParseException:
            raise ValidationError("Invalid phone number.")

        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
