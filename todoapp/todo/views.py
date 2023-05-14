from django.shortcuts import redirect, render
from todo.forms import TodoForm


from todo.models import Todo

# Create your views here.

# 완료되지 않은 todo를 필터링하여 todos변수에 담아 템플릿으로 전달한다
def todo_list(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})


def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect('todo_list')


def todo_done_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, 'todo/todo_done_list.html', {'dones': dones})