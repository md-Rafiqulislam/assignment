
##### all the imports here
from django.shortcuts import render, redirect
from . import forms


##### Create your views here.
# home page
def home_page(request):
    return render(request, 'task/index.html')


# add task page
def add_task(request):
    if request.method == 'POST':
        task_form = forms.AddTaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('addTaskPage')
    else:
        task_form = forms.AddTaskForm(request.POST)
        return (request, 'task/index.html', {'form': task_form})