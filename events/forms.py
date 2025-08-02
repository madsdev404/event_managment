from django import forms
from .models import Category, Event, Participant

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'