from django.shortcuts import render, redirect

from todo_app import models
from todo_app.form import todo_form
from todo_app.models import todo_model


# Create
def add_todo(request):
    form = todo_form()
    if request.method == 'POST':
        form=todo_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    # else:
    #     form=todo_form()

    return render(request, 'add_todo.html', {'form':form})


#Read
def todo_list(request):
    todos=models.todo_model.objects.all()
    return render(request, 'todo_list.html', {'todos':todos})

#Update
def update_todo(request, id):
    todos=todo_model.objects.get(id=id)
    if request.method == 'POST':
        form=todo_form(request.POST, instance=todos)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form=todo_form(instance=todos)
    return render(request, 'update_todo.html', {'form':form})

#delete
def delete_todo(request, id):
    todos=todo_model.objects.get(id=id)
    if request.method == 'POST':
        todos.delete()
        return redirect('todo_list')
    return render(request, 'delete_todo.html', {'todos':todos})


def landing(request):
    return render(request, 'landing.html')