from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    finished = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',  # Sử dụng HTML5 datetime-local
            'class': 'form-control'
        }),
        required=True  # Bắt buộc nhập
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'finished']


