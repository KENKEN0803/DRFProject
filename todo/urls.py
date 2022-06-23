from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    # api_view 데코레이터 방식
    # path("list/", views.todo_list)

    # 클래스 기반 apiView 방식
    # path("list/", views.ListTodoView.as_view()),

    path("list/", views.APIViewTodo.as_view()),
    # path("<int:pk>/", views.SeeTodoView.as_view()),
]
