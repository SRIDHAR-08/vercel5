from django.forms import ModelForm
from .models import *

class class_form(ModelForm):
    class Meta:
        model = class_model
        fields = ['name', 'age']