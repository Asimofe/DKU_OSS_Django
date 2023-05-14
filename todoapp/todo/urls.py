from django.urls import path
from . import views


# todo앱에서 목록 화면에 대한 url을 설정해준다.


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name='todo_post'),
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('done/', views.todo_done_list, name='todo_done_list'),
    path('done/<int:pk>', views.todo_done, name='todo_done'),
]