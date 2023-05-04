import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        # Validate name length
        if len(name) < 2:
            raise ValidationError("Group name should be at least 2 characters long.")
        # Validate name contains only letters
        if not re.match(r'^[a-zA-Z]*$', name):
            raise ValidationError("Group name should only contain letters.")

        return name
