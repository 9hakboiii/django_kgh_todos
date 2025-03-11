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
    return render(
        request, "todo/todo_list.html", {"todos": todos}
    )  # context 객체 (key : value 형태로 넘김)


# dev_3
def todo_post(request):

    if request.method == "POST":
        form = TodoForm(request.POST)

        if (
            form.is_valid()
        ):  # 값 검증, 모든 필드가 올바르게 입력되었는지 확인하고, 유효하지 않으면 오류 메시지를 제공
            todo = form.save(
                commit=False
            )  # form 데이터를 사용하여 todo 객체 생성, commit=False는 db에 즉시저장 x
            todo.save()  # todo 객체를 db에 저장
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo/todo_post.html", {"form": form})


# http://120.0.0.1:8000/todo/{1}/ + GET, POST, PUT, DELETE, OPTION
# path("<int:pk>", views.todo_detail, name="todo_detail")
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)  # filter는 1개이상, get은 1개만 꺼냄
    return render(request, "todo/todo_detail.html", {"todo": todo})


# dev_5
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            # SQL 실행시킨 상태이지만 메모리에만 올려놓고 영구저장(commit)은 안 한 상태
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")
    else:
        # instance = 레코드, 튜플
        form = TodoForm(instance=todo)

    return render(request, "todo/todo_post.html", {"form": form})


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect("todo_list")


def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, "todo/todo_done.html", {"dones": dones})


# redirect 하고 forward의 차이이
