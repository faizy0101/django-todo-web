from django.urls import path

from todo_app import views

urlpatterns = [
    path('',views.landing,name='landing'),
    path('todo_list',views.todo_list,name='todo_list'),
    path('add/',views.add_todo,name='add_todo'),
    path('update/<int:id>',views.update_todo,name='update_todo'),
    path('delete/<int:id>',views.delete_todo,name='delete_todo'),
]