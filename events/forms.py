from django import forms
from .models import Category, Event

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('organizer',)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('organizer',)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
