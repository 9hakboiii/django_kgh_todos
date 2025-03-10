from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.

# dev_1


def home(request):
    # return HttpResponse('<h1>안녕하세요</h1>')
    return render(request, "home.html")


def todo_list(request):
    # select * from todos where complete = 0
    # objects = models.py의 Todo 클래스의 객체
    # objects > QuerySet 자료형으로 리턴
    # filter = where절
    todos = Todo.objects.filter(complete=0)
    return render(request, "todo/todo_list.html", {"todos": todos})  # context 객체


# dev_3
def todo_post(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo/todo_post.html", {"form": form})
