from django.db.models import fields
from django.forms import ModelForm
from .models import Diary

class DiaryForm(ModelForm):
    class Meta:
        model=Diary
        fields='__all__'