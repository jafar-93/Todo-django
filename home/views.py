from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreated,TodoUpdatedForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todo':todos})

def hello(request):
    return render(request, 'hello.html', context={'name':'shahin'} )

def details(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    return render (request, 'details.html', {'todo' : todo })

def delete(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    messages.success(request, 'TOdo deleted successfully' , 'danger')
    return redirect('home') 

def update(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = TodoUpdatedForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'todo update succesfully' , 'success')
            return redirect('details', todo_id)
    else:
        form = TodoUpdatedForm(instance = todo)
    return render (request, 'update.html', {'form' : form})

def create(request):
    if request.method == 'POST':
        form = TodoCreated(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title = cd['title'], content = cd['content'], date = cd['date'] )
            messages.success(request, 'todo create succesfully' , 'success')
            return redirect('home')
    else:
        form = TodoCreated
    return render (request, 'create.html', {'form' : form})