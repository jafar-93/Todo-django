from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hello', views.hello),
    path('details/<todo_id>', views.details, name='details'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('create', views.create , name= 'create'),
    path('update/<todo_id>', views.update , name= 'update'),
]