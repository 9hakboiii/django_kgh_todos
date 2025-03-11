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
