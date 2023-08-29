from django.forms import ChoiceField, IntegerField, ModelForm
from Programs.models import *

class ProgramForm(ModelForm):

    class Meta:
        model = Program
        fields = ['name','desc','duration','agegroup']