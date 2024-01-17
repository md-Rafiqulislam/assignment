
##### all the imports here
from django.shortcuts import render, redirect
from . import forms

##### Create your views here.
# add category page
def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid:
            category_form.save()
            return redirect('addCategory')
    else:
        category_form = forms.CategoryForm()
        return render(request, 'category/index.html', {'form': category_form})