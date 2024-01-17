
##### all the imports here
from django import forms
from .models import Category

##### create your forms here
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'