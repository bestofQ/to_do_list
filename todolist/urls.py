from django.urls import path
from . import views


app_name = 'todolist'
urlpatterns = [
	path('home/', views.home, name='todolist_home'),
	path('about/', views.about, name='todolist_about'),
	path('edit/', views.edit, name='todolist_edit'),
]
