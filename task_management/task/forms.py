
##### all the imports here
from django import forms
from .models import AddTask

##### create your form here
class AddTaskForm(forms.ModelForm):
    class Meta:
        models = AddTask
        fields = '__all__'